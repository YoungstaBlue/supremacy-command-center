#!/usr/bin/env bash
# clip_bwc_exhibits.sh — cut Exhibits F1–F4 from raw body-worn-camera footage
# for State of Missouri v. Tyler Ross Garner (Marion County, Case Nos.
# 2026-001376 / 2026-0032-01 / 2026-155).
#
# Every clip is produced with ffmpeg DIRECT STREAM COPY (-c copy). The video
# and audio packets are copied byte-for-byte out of the source container; no
# frame is decoded, re-encoded, scaled or filtered. That keeps the clips
# forensically faithful to the original BWC file and avoids any argument that
# the defense "altered" the footage.
#
# USAGE
#   scripts/clip_bwc_exhibits.sh <raw_bwc_file> <BWC_START> [output_dir]
#
#   raw_bwc_file  The untouched BWC file in 04_BWC_RAW_FOOTAGE/.
#   BWC_START     Wall-clock time (HH:MM:SS, 24-hour) shown at the very first
#                 frame of the raw file. Take it from the on-screen overlay or
#                 the vendor audit trail. All exhibit windows below are
#                 wall-clock times and are converted to file offsets with it.
#   output_dir    Defaults to 05_EXHIBIT_VIDEO_CLIPS/ beside this script.
#
#   Environment overrides:
#     EXHIBITS="F1 F3"   produce only the listed exhibits (default: all four)
#     DRY_RUN=1          print the ffmpeg commands without running them
#
# EXAMPLE
#   scripts/clip_bwc_exhibits.sh 04_BWC_RAW_FOOTAGE/AXON_Jobe_2026-01-27.mp4 15:02:11
#
# OUTPUT (in output_dir)
#   EXHIBIT_F<n>_<slug>_<start>-<end>.<ext>   the four clips
#   checksums_sha256_exhibits.txt             SHA-256 of source + every clip
#   ffprobe_EXHIBIT_F<n>.txt                  stream metadata per clip
#   clip_run_<UTC timestamp>.txt              full run log for the foundation witness
#
# KEYFRAME CAVEAT
#   A stream-copy cut can only begin on a keyframe. ffmpeg therefore starts each
#   clip at the last keyframe AT OR BEFORE the requested time, so a clip may
#   open up to a few seconds early. It never opens late and never omits frames
#   inside the requested window. The run log records the requested and the
#   actual start so the witness can explain the difference if asked.

set -euo pipefail

# ---------------------------------------------------------------------------
# Exhibit table: ID | start clock | end clock | file slug | description
# ---------------------------------------------------------------------------
EXHIBIT_TABLE=$(cat <<'TABLE'
F1|15:16:18|15:17:55|witness-coaching-flail-buzzword|Witness Coaching & 'Flail' Buzzword
F2|15:18:00|15:21:00|bwc-deactivation-cough-masking-shadow-signals|BWC Deactivation, Chest Cough Masking & Ground Shadow Hand/Foot Signals
F3|15:05:45|15:07:15|physical-takedown-left-knee-kick|Physical Takedown & Left Knee Kick
F4|15:10:40|16:07:29|cad-ems-request-ankle-pain-wheelchair|CAD 15:10:40 EMS Request for Severe Ankle Pain & Wheelchair at PD/Hospital
TABLE
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
die() { printf 'clip_bwc_exhibits: %s\n' "$*" >&2; exit 1; }

# HH:MM:SS -> integer seconds since midnight
clock_to_secs() {
  local t=$1
  [[ $t =~ ^([0-9]{1,2}):([0-5][0-9]):([0-5][0-9])$ ]] || die "bad clock time '$t' (want HH:MM:SS)"
  echo $(( 10#${BASH_REMATCH[1]} * 3600 + 10#${BASH_REMATCH[2]} * 60 + 10#${BASH_REMATCH[3]} ))
}

# seconds -> HH:MM:SS
secs_to_clock() {
  printf '%02d:%02d:%02d' $(( $1 / 3600 )) $(( ($1 % 3600) / 60 )) $(( $1 % 60 ))
}

sha256_of() {
  if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | awk '{print $1}'
  elif command -v shasum >/dev/null 2>&1; then shasum -a 256 "$1" | awk '{print $1}'
  else die "need sha256sum or shasum"; fi
}

# ---------------------------------------------------------------------------
# Arguments and environment
# ---------------------------------------------------------------------------
[[ $# -ge 2 ]] || { sed -n '2,40p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }

SRC=$1
BWC_START=$2
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
OUT_DIR=${3:-"$SCRIPT_DIR/../05_EXHIBIT_VIDEO_CLIPS"}
EXHIBITS=${EXHIBITS:-"F1 F2 F3 F4"}
DRY_RUN=${DRY_RUN:-0}

[[ -f $SRC ]] || die "source file not found: $SRC"
command -v ffmpeg  >/dev/null 2>&1 || die "ffmpeg not installed"
command -v ffprobe >/dev/null 2>&1 || die "ffprobe not installed"

mkdir -p "$OUT_DIR"
OUT_DIR=$(cd "$OUT_DIR" && pwd)
SRC_ABS=$(cd "$(dirname "$SRC")" && pwd)/$(basename "$SRC")
SRC_EXT=${SRC##*.}
[[ $SRC_EXT == "$SRC" ]] && SRC_EXT=mp4

START_SECS=$(clock_to_secs "$BWC_START")
RUN_STAMP=$(date -u +%Y%m%dT%H%M%SZ)
LOG="$OUT_DIR/clip_run_$RUN_STAMP.txt"
CHECKSUMS="$OUT_DIR/checksums_sha256_exhibits.txt"

# Source duration so we can refuse windows that fall outside the file.
SRC_DURATION=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$SRC_ABS" || echo 0)
SRC_DURATION=${SRC_DURATION%.*}
[[ -n $SRC_DURATION && $SRC_DURATION != "N/A" ]] || SRC_DURATION=0

log() { printf '%s\n' "$*" | tee -a "$LOG"; }

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
{
  echo "BWC EXHIBIT CLIP RUN — State v. Tyler Ross Garner (2026-001376 / 2026-0032-01 / 2026-155)"
  echo "Run (UTC):        $RUN_STAMP"
  echo "Operator:         ${USER:-unknown}@$(hostname)"
  echo "ffmpeg:           $(ffmpeg -version | head -n1)"
  echo "Source file:      $SRC_ABS"
  echo "Source size:      $(wc -c < "$SRC_ABS") bytes"
  echo "Source duration:  ${SRC_DURATION}s ($(secs_to_clock "$SRC_DURATION"))"
  echo "BWC start clock:  $BWC_START (offset 0 of file)"
  echo "Method:           ffmpeg -ss <offset> -i <src> -t <len> -map 0 -c copy (no re-encode)"
  echo
} > "$LOG"
cat "$LOG"

if [[ $DRY_RUN != 1 ]]; then
  log "Hashing source (SHA-256)..."
  SRC_SHA=$(sha256_of "$SRC_ABS")
  log "Source SHA-256:   $SRC_SHA"
  printf '# SHA-256 checksums — State v. Garner BWC exhibits — generated %s\n' "$RUN_STAMP" > "$CHECKSUMS"
  printf '# Verify with: sha256sum -c %s\n' "$(basename "$CHECKSUMS")" >> "$CHECKSUMS"
  printf '# SOURCE (04_BWC_RAW_FOOTAGE): %s\n' "$SRC_ABS" >> "$CHECKSUMS"
  printf '%s  %s\n' "$SRC_SHA" "$SRC_ABS" >> "$CHECKSUMS"
  log
fi

# ---------------------------------------------------------------------------
# Cut each exhibit
# ---------------------------------------------------------------------------
FAILED=0
while IFS='|' read -r ID C_START C_END SLUG DESC; do
  [[ -z $ID ]] && continue
  [[ " $EXHIBITS " == *" $ID "* ]] || continue

  s=$(clock_to_secs "$C_START"); e=$(clock_to_secs "$C_END")
  (( e > s )) || die "$ID: end $C_END is not after start $C_START"
  off=$(( s - START_SECS )); len=$(( e - s ))
  tag_start=${C_START//:/}; tag_end=${C_END//:/}
  OUT="$OUT_DIR/EXHIBIT_${ID}_${SLUG}_${tag_start}-${tag_end}.${SRC_EXT}"

  log "== EXHIBIT $ID: $DESC"
  log "   window (clock): $C_START -> $C_END  ($len s)"
  if (( off >= 0 )); then
    log "   file offset:    $(secs_to_clock "$off") (+${off}s)  length ${len}s"
  else
    log "   file offset:    ${off}s (before the recording starts)  length ${len}s"
  fi
  log "   output:         $(basename "$OUT")"

  if (( off < 0 )); then
    log "   SKIPPED: window starts ${off#-}s before the recording begins (BWC_START=$BWC_START). Wrong source file or wrong BWC_START?"
    FAILED=1; log; continue
  fi
  if (( SRC_DURATION > 0 && off >= SRC_DURATION )); then
    log "   SKIPPED: window starts after the recording ends (${SRC_DURATION}s). Wrong source file or wrong BWC_START?"
    FAILED=1; log; continue
  fi
  if (( SRC_DURATION > 0 && off + len > SRC_DURATION )); then
    log "   WARNING: window runs past end of recording; clip will end at EOF ($(secs_to_clock "$SRC_DURATION"))."
  fi

  CMD=(ffmpeg -hide_banner -nostdin -y -loglevel error
       -ss "$off" -i "$SRC_ABS" -t "$len"
       -map 0 -c copy -avoid_negative_ts make_zero
       -movflags +faststart
       -metadata "title=EXHIBIT $ID — $DESC"
       -metadata "comment=State v. Garner 2026-001376; stream copy of $(basename "$SRC_ABS") clock $C_START-$C_END; no re-encode"
       "$OUT")
  log "   cmd: $(printf '%q ' "${CMD[@]}")"

  if [[ $DRY_RUN == 1 ]]; then log "   (dry run)"; log; continue; fi

  if "${CMD[@]}"; then
    # Actual first-packet timestamp and duration of what we produced.
    ACT_DUR=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$OUT")
    FIRST_KF=$(ffprobe -v error -select_streams v:0 -read_intervals "${off}%+#1" -show_entries packet=pts_time -of default=nw=1:nk=1 "$SRC_ABS" 2>/dev/null | head -n1 || true)
    CLIP_SHA=$(sha256_of "$OUT")
    log "   produced:       $(wc -c < "$OUT") bytes, duration ${ACT_DUR}s"
    [[ -n $FIRST_KF ]] && log "   cut begins at source offset ${FIRST_KF}s (requested ${off}s; if earlier, that is the keyframe snap)"
    log "   SHA-256:        $CLIP_SHA"
    printf '# EXHIBIT %s: %s (clock %s-%s)\n' "$ID" "$DESC" "$C_START" "$C_END" >> "$CHECKSUMS"
    printf '%s  %s\n' "$CLIP_SHA" "$(basename "$OUT")" >> "$CHECKSUMS"
    ffprobe -hide_banner -show_format -show_streams "$OUT" > "$OUT_DIR/ffprobe_EXHIBIT_${ID}.txt" 2>&1 || true
  else
    log "   FAILED: ffmpeg returned an error"
    FAILED=1
  fi
  log
done <<< "$EXHIBIT_TABLE"

# ---------------------------------------------------------------------------
# Verify and summarise
# ---------------------------------------------------------------------------
if [[ $DRY_RUN != 1 ]]; then
  log "Verifying checksums..."
  if (cd "$OUT_DIR" && sha256sum -c --quiet "$(basename "$CHECKSUMS")" 2>&1 | tee -a "$LOG" | grep -q FAILED); then
    log "CHECKSUM VERIFICATION FAILED"; FAILED=1
  else
    log "All clip checksums verified."
  fi
  log
  log "Checksums file:   $CHECKSUMS"
fi
log "Run log:          $LOG"
log "Output directory: $OUT_DIR"

(( FAILED == 0 )) || die "one or more exhibits were not produced — see run log"
log "Done."
