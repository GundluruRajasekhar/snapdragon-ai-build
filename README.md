# LocalScribe: private meeting notes on Snapdragon-powered HP PCs

Record or upload a meeting. LocalScribe transcribes it and produces a summary, decisions, action items and risks. All AI runs on the device. No audio or text is uploaded, and after the first model download it works offline.

## Problem
Meeting tools send audio to the cloud. That is a blocker for legal, health, HR and finance teams, and for anyone with poor connectivity. Snapdragon X laptops (HP OmniBook / EliteBook) have an NPU and long battery life, which makes always-on local transcription practical.

## AI models (open source)
| Task | Model | Source |
|---|---|---|
| Speech to text | Whisper-tiny.en (ONNX) | Open source, also on Qualcomm AI Hub |
| Summary and actions | Qwen2.5-0.5B-Instruct (q4, ONNX) | Open source |

Runtime: Transformers.js on ONNX Runtime Web, with WebGPU (Adreno GPU) when available and WASM fallback.

## Run it
1. On the HP PC, open `index.html` in Microsoft Edge (Arm64 build). Or serve the folder: `python -m http.server 8080` and open http://localhost:8080.
2. First use downloads about 250 MB of models, then caches them.
3. Turn Wi-Fi off to confirm it still works.

## Criteria map
**Technical implementation**: two-model pipeline (ASR then LLM), 16 kHz audio decoding, 30 s chunking with stride for long recordings, structured-output prompt with a tolerant parser, backend auto-selection (WebGPU or WASM), and a network monitor that flags any outbound request.

**Use case and innovation**: privacy-first meeting assistant that produces action items with owners and due dates, plus Markdown export. Data never leaves the device.

**Deployment and accessibility**: one HTML file, no installer, no server, no account. Keyboard focus styles, ARIA live status, light/dark themes, reduced-motion support, responsive layout, editable transcript for correcting errors.

**Presentation and documentation**: this README, an in-app device panel and privacy check for demos, and a sample-text button so judges can see the full flow in seconds.

## NPU roadmap (Snapdragon X Elite / Plus)
Export the same models from Qualcomm AI Hub (`qai_hub_models`), compile for the Snapdragon X target, and run through ONNX Runtime with the QNN Execution Provider. Swap the backend in a small Python or Electron wrapper. The UI and prompts stay unchanged.

## Known limits
- Browser builds use the GPU, not the NPU. The QNN path above is the NPU route.
- 0.5B summariser can miss details on long meetings; the transcript stays editable.
- English only in this version (whisper-tiny.en).

## Submission checklist
- [ ] Test on the HP Snapdragon PC and note real timings (transcribe minutes per audio minute)
- [ ] Record a 2-minute demo with Wi-Fi off
- [ ] Fill every intake-form field, since submissions cannot be edited after sending
- [ ] Confirm the work is solely yours; one submission per participant
