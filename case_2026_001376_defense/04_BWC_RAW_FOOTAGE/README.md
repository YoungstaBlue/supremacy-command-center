# 04 — BWC Raw Footage

**Never edit, rename, re-encode or open-and-save anything in this folder.** It holds the body-worn-camera files exactly as produced by the State / vendor (Axon, WatchGuard, etc.), plus their audit trails.

Required for each raw file:

1. The original file, bit-for-bit, in the vendor's container.
2. The vendor audit trail / chain-of-custody export (upload time, retention category, deactivation events, who viewed or exported).
3. A SHA-256 hash recorded at the moment of receipt: `sha256sum <file> > <file>.sha256`.
4. A note of the **wall-clock time at which the recording begins** (from the on-screen overlay or vendor metadata). `scripts/clip_bwc_exhibits.sh` needs it as `BWC_START` to turn clock times such as `15:16:18` into offsets within the file.

Known gap to document: BWC deactivation at approximately 15:18 (Exhibit F2) and the unrecorded Griffin statement at 15:42 (Exhibit D).
