# LocalScribe: Requirements

## 1. Purpose
LocalScribe turns meeting audio into structured notes (summary, decisions, action items, risks) using AI models that run entirely on a Snapdragon-powered HP PC. No audio or text leaves the device.

## 2. Challenge compliance
| Rule | How LocalScribe meets it |
|---|---|
| Designed or optimized for Snapdragon-powered HP PCs | Targets Windows on Arm (Edge Arm64), uses the Adreno GPU via WebGPU, with a documented NPU path through Qualcomm AI Hub and the QNN execution provider |
| Uses AI models from Qualcomm AI Hub or open-source platforms | Whisper-tiny.en (speech to text) and Qwen2.5-0.5B-Instruct (summarising), both open source |
| Solely owned work or idea | Original work by the participant; confirm before submitting |
| One submission per participant | Submit once only |
| No edits after submission | Complete the final checklist in `tasks.md` before submitting |

## 3. Users
- Professionals who handle confidential meetings (legal, health, HR, finance).
- Students and teams with limited or unreliable internet.
- Anyone who wants meeting notes without creating an account.

## 4. Functional requirements
| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Record audio from the microphone | Must |
| FR-2 | Upload an audio or video file for transcription | Must |
| FR-3 | Transcribe speech on the device and show an editable transcript | Must |
| FR-4 | Generate a summary, decisions, action items (owner, task, due date) and risks | Must |
| FR-5 | Save notes locally and reopen or delete them | Must |
| FR-6 | Export a note as Markdown | Must |
| FR-7 | Show device details (threads, memory, GPU, AI backend) | Should |
| FR-8 | Show a privacy indicator that flags any outbound request carrying user data | Should |
| FR-9 | Provide a sample-text button for instant demos | Should |
| FR-10 | Work offline after the first model download | Must |
| FR-11 | Run the same models through the QNN provider on the Snapdragon NPU | Could |
| FR-12 | Support languages other than English | Could |

## 5. Non-functional requirements
| ID | Requirement | Target |
|---|---|---|
| NFR-1 Privacy | No user audio or text sent over the network | 0 bytes; visible in the app |
| NFR-2 Deployment | One HTML file, no installer, server or account | Opens directly in Edge |
| NFR-3 Performance | Transcription faster than real time on a Snapdragon HP PC | To be measured and recorded in README |
| NFR-4 Footprint | First-run model download | About 250 MB, cached afterwards |
| NFR-5 Accessibility | Keyboard focus, ARIA live status, light and dark themes, reduced motion, responsive layout | Met in current build |
| NFR-6 Reliability | Clear error messages for blocked microphone, failed decode, full storage | Met in current build |
| NFR-7 Compatibility | Edge or Chrome with WebGPU preferred; WASM fallback elsewhere | Met in current build |

## 6. Constraints and assumptions
- The first run needs internet to download models from the model host; later runs do not.
- The browser build uses the GPU, not the NPU. NPU use requires the QNN wrapper (FR-11).
- The 0.5B summariser can miss details on long meetings, so the transcript stays editable.
- The current models are English only.
- Notes are kept in browser local storage (up to 30 notes).

## 7. Out of scope
- Live captions during a call, speaker identification, cloud sync, multi-user sharing, calendar integration.

## 8. Evaluation criteria mapping
| Criterion | Evidence |
|---|---|
| Technical Implementation | FR-3, FR-4, FR-8, FR-10, NFR-1, NFR-3 |
| Application Use Case and Innovation | Private meeting assistant with action items; FR-4, NFR-1 |
| Deployment and Accessibility | NFR-2, NFR-5, NFR-7 |
| Presentation and Documentation | README, this file, `tasks.md`, FR-7, FR-9, demo video |

## 9. Acceptance criteria
1. With Wi-Fi off (after first download), a recorded 2-minute clip produces a transcript and structured notes.
2. The privacy indicator shows "0 bytes of your data sent" during the full flow.
3. A note can be saved, reopened, exported as Markdown and deleted.
4. The app is fully usable with the keyboard only.
5. README records real timings measured on a Snapdragon HP PC.
