#!/usr/bin/env node
// Pull the data arrays out of a self-contained artifact page whose content is
// rendered client-side from inline JavaScript (`const DATA = [...]`, an IIFE
// holding `var DICTIONARY = [...]`, and so on).
//
// The page's largest inline script is run inside a Node `vm` sandbox with a
// stubbed DOM. Any IIFE wrapper is removed and top-level const/let are turned
// into var so the data lands on the sandbox global, which is then dumped as
// JSON. Rendering code throws harmlessly against the stub DOM; the data has
// already been declared by then.
//
// usage: node extract_js.mjs <index.html> <out.json>
import fs from 'node:fs';
import vm from 'node:vm';

const [, , file, out] = process.argv;
if (!file || !out) {
  console.error('usage: node extract_js.mjs <index.html> <out.json>');
  process.exit(2);
}

const html = fs.readFileSync(file, 'utf8');
const scripts = [...html.matchAll(/<script(?![^>]*type="application\/json")[^>]*>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
if (!scripts.length) {
  console.error(`${file}: no inline script`);
  process.exit(1);
}
let src = scripts.sort((a, b) => b.length - a.length)[0];

if (/^\s*\(function\s*\(\)\s*\{/.test(src)) {
  src = src
    .replace(/^\s*\(function\s*\(\)\s*\{\s*("use strict";)?/, '')
    .replace(/\}\)\s*\(\)\s*;?\s*$/, '');
}
src = src.replace(/^(\s*)(const|let)\s+([A-Za-z_$][\w$]*)\s*=/gm, '$1var $3 =');

// A permissive stand-in for every DOM object the script might touch.
const proxy = new Proxy(function () {}, {
  get: (t, k) => {
    if (typeof k === 'symbol') return k === Symbol.toPrimitive ? () => '' : undefined;
    if (k === 'length') return 0;
    if (k === 'then') return undefined;
    return proxy;
  },
  apply: () => proxy,
  construct: () => proxy,
  set: () => true,
});

const BUILTINS = ['console', 'Intl', 'Date', 'JSON', 'Math', 'location'];
const sandbox = {
  document: proxy, window: proxy, localStorage: proxy, navigator: proxy,
  location: { hash: '' },
  console, Intl, Date, JSON, Math, RegExp, Array, Object, String, Number, Map, Set, Promise,
  encodeURIComponent, decodeURIComponent,
  setTimeout() {}, requestAnimationFrame() {},
  fetch: () => Promise.resolve(proxy),
  URL: proxy,
};
sandbox.globalThis = sandbox;
sandbox.self = sandbox;
vm.createContext(sandbox);
try {
  vm.runInContext(src, sandbox, { timeout: 20000 });
} catch (e) {
  console.error(`script threw after declaring data (expected): ${String(e).slice(0, 160)}`);
}

const data = {};
for (const [k, v] of Object.entries(sandbox)) {
  if (v === proxy || v === sandbox || typeof v === 'function') continue;
  if (['globalThis', 'self', ...BUILTINS].includes(k)) continue;
  if (Array.isArray(v) && v.length) data[k] = v;
  else if (v && typeof v === 'object' && !(v instanceof Promise) && Object.keys(v).length) data[k] = v;
}
const clean = JSON.parse(JSON.stringify(data, (k, v) => (typeof v === 'function' ? undefined : v)));
fs.writeFileSync(out, JSON.stringify(clean, null, 1));
console.log(
  `${file}: ${Object.entries(clean).map(([k, v]) => `${k}=${Array.isArray(v) ? v.length : Object.keys(v).length}`).join(' ')}`,
);
