# LocalScribe: Tasks

Status key: [x] done, [ ] to do.

## Phase 1: Core app
- [x] Single-file UI with capture, transcript, result and saved-notes sections
- [x] Microphone recording and audio upload
- [x] On-device transcription with Whisper-tiny.en (FR-3)
- [x] On-device summary, decisions, actions and risks with Qwen2.5-0.5B (FR-4)
- [x] Local note storage, open and delete (FR-5)
- [x] Markdown export (FR-6)
- [x] Device panel and privacy indicator (FR-7, FR-8)
- [x] Sample-text button (FR-9)
- [x] Accessibility basics: focus styles, ARIA status, dark mode, reduced motion (NFR-5)

## Phase 2: Verify on the target hardware
- [ ] Open `index.html` in Edge on the Snapdragon HP PC
- [ ] Confirm WebGPU is detected and the device panel shows the right backend
- [ ] Complete first-run model download, then turn Wi-Fi off and repeat the flow (FR-10)
- [ ] Test with a 2-minute recording and a 10-minute file
- [ ] Record timings: transcription time per audio minute, summary time, first-load time
- [ ] Note any failures and fix them (microphone permission, decode errors, memory)
- [ ] Check keyboard-only use and 200% zoom

## Phase 3: Snapdragon NPU path (FR-11)
- [ ] Set up Python on Windows Arm64 with `qai_hub_models` and ONNX Runtime with the QNN execution provider
- [ ] Export Whisper from Qualcomm AI Hub for the Snapdragon X target
- [ ] Export or select a small LLM from Qualcomm AI Hub for the summary step
- [ ] Write a small local wrapper (Python or Electron) that serves the same UI and calls the NPU models
- [ ] Compare GPU (browser) and NPU timings and battery impact; add results to README

## Phase 4: Quality improvements
- [ ] Improve summary prompt with two or three example transcripts
- [ ] Add a copy-to-clipboard button for action items
- [ ] Add a language option (multilingual Whisper) if time allows (FR-12)
- [ ] Handle recordings longer than 30 minutes by summarising in sections

## Phase 5: Presentation and documentation
- [ ] Add screenshots to README
- [ ] Add a measured-performance table to README
- [ ] Write a one-page project description for the intake form
- [ ] Record a 2-minute demo video with Wi-Fi off: record, transcribe, summarise, export
- [ ] Prepare 3 to 5 slides: problem, solution, architecture, results, roadmap

## Phase 6: Final submission checklist
- [ ] Confirm the work is solely yours
- [ ] Confirm this is your only submission
- [ ] Check every intake-form field (no edits after submitting)
- [ ] Verify links, files and demo video open correctly
- [ ] Submit before the deadline

## Suggested order
1. Phase 2 (find real problems early)
2. Phase 5 (secure a complete submission)
3. Phase 3 (NPU path, the biggest win for the Snapdragon criterion)
4. Phase 4 (polish with remaining time)
