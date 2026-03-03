# FFmpeg Frame Export Setup (Windows) — Template
Location: templates/tools/FFmpeg_Frame_Export_Setup.md

[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_23__templates__ffmpeg-frame-export
title: FFmpeg Frame Export Setup (Windows) — Template
date: 2026-02-23
status: active
topic: templates
type: template
tags: ffmpeg, video, frames, ingest
sensitivity: low
visibility: shared
source: doc
domain: tools
authority: propose_only
[CAPSULE_HEADER_END]

module: TPL.FFMPEG.M01 | name="Purpose"
Find: ffmpeg frame export subtitles ingest video
Goal:
- Export 1 image every ~5 seconds from a lecture clip with timestamped filenames.
- Use the frames + subtitles/transcript to ingest a video like a document batch.

Constraints:
- Keep uploads under your platform ZIP limit (e.g., 512MB).
- Prefer downscaled resolution for frame exports (e.g., 1280x720) when acceptable.

/module

module: TPL.FFMPEG.M02 | name="Prereqs"
Find: prereqs ffmpeg windows subtitle edit
Prereqs:
- FFmpeg installed and available on PATH (Windows).
- Optional: Subtitle Edit (or any tool that can export SRT/VTT).
- A source clip (mp4/mkv) and transcript/subtitles if possible.

/module

module: TPL.FFMPEG.M03 | name="Command Patterns"
Find: commands fps every 5 seconds timestamps
Approach A (fps method): export one frame every 5 seconds
- 1 frame / 5 seconds = 0.2 fps

Example:
ffmpeg -i "input.mp4" -vf fps=0.2 -q:v 2 "frames/%06d.png"

Approach B (select by time): (alternative if you need exact stepping)
ffmpeg -i "input.mp4" -vf "select='not(mod(t,5))',setpts=N/FRAME_RATE/TB" -vsync vfr -q:v 2 "frames/%06d.png"

Notes:
- Use -s 1280x720 or -vf scale=1280:-2 to reduce size.
- Use JPEG for smaller output: "frames/%06d.jpg"

/module

module: TPL.FFMPEG.M04 | name="Timestamped filenames"
Find: timestamp filenames frame pts
If you want timestamps embedded, use drawtext (requires fonts) or post-process rename.
Practical variant:
- Export frames to %06d and store a sidecar CSV mapping frame index → timestamp.
- If you have SRT, you can align by time window (e.g., 00:10:00–00:15:00).

/module

module: TPL.FFMPEG.M05 | name="Packaging for ingestion"
Find: zip slices 5 minute chunks
Packaging recommendation:
- Chunk exports into 5–10 minute slices (folders or separate zips).
- For each slice, include:
  - frames zip
  - subtitles/transcript for that time range (or full transcript)
  - a short manifest line: title + time window + mode (skim/deep)

/module

module: TPL.FFMPEG.M06 | name="Video PASS item label"
Find: item label time slice
Use this label format when sending a slice:
Item N/Total — <video title> — HH:MM:SS–HH:MM:SS — skim|deep — focus(optional)

/module
