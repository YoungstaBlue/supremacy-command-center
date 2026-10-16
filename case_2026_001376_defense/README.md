# Defense Case File — State v. Tyler Ross Garner

Circuit Court of Marion County, Missouri · Case Nos. 2026-001376 / 2026-0032-01 / 2026-155

**Start with `MASTER_EVIDENCE_INDEX.md`.** It lists every exhibit (A–E, F1–F4), where it lives, why it matters, and what is still open.

```
case_2026_001376_defense/
├── MASTER_EVIDENCE_INDEX.md        exhibit list, detail, timeline, custody log, open items
├── 01_PLEADINGS_AND_MOTIONS/       charging docs, defense motions, orders
├── 02_POLICE_REPORTS_AND_CAD/      Exhibits A, B, C + CAD logs and BWC audit trails
├── 03_WITNESS_STATEMENTS/          Exhibit D + any other statements
├── 04_BWC_RAW_FOOTAGE/             untouched BWC originals (never edit)
├── 05_EXHIBIT_VIDEO_CLIPS/         Exhibits F1–F4 + checksums + run logs (script output)
├── 06_TRANSCRIPTS_AND_STILLS/      clip transcripts and frame stills
├── 07_CHILD_VISITATION_RECORDS/    Exhibit E
└── scripts/
    └── clip_bwc_exhibits.sh        ffmpeg -c copy clipper for F1–F4 with SHA-256 manifest
```

## Cutting the BWC exhibits

```
# 1. drop the raw BWC file into 04_BWC_RAW_FOOTAGE/ and note the clock time of its first frame
# 2. run (BWC_START = that clock time, HH:MM:SS, 24-hour):
case_2026_001376_defense/scripts/clip_bwc_exhibits.sh \
  case_2026_001376_defense/04_BWC_RAW_FOOTAGE/<raw file> 15:02:11

# preview the commands first:
DRY_RUN=1 case_2026_001376_defense/scripts/clip_bwc_exhibits.sh <raw file> <BWC_START>

# only some exhibits:
EXHIBITS="F3 F4" case_2026_001376_defense/scripts/clip_bwc_exhibits.sh <raw file> <BWC_START>
```

Requires `ffmpeg`, `ffprobe` and `sha256sum` (or `shasum`). Clips are direct stream copies; nothing is re-encoded. Output, checksums and the run log land in `05_EXHIBIT_VIDEO_CLIPS/`.

## Confidentiality

Only the scaffold, scripts, READMEs and the index are tracked in git. `case_2026_001376_defense/.gitignore` excludes video, PDFs, images, office documents and generated checksum/log files so evidence is never pushed to the remote. Keep the evidence itself on encrypted local storage and in the defense's own backup.
