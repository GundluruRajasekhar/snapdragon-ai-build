"""Download LocalScribe models into ./models so the app runs fully offline.

Usage (run inside the LocalScribe folder):
    pip install huggingface_hub
    python get_models.py

If huggingface.co is blocked on your network, use the mirror:
    Windows PowerShell:  $env:HF_ENDPOINT="https://hf-mirror.com"; python get_models.py
    Command Prompt:      set HF_ENDPOINT=https://hf-mirror.com && python get_models.py
"""
from huggingface_hub import snapshot_download

MODELS = [
    "onnx-community/whisper-tiny.en",
    "onnx-community/Qwen2.5-0.5B-Instruct",
]
PATTERNS = [
    "*.json", "*.txt",
    "onnx/encoder_model.onnx",
    "onnx/decoder_model_merged.onnx",
    "onnx/decoder_model_merged_q4.onnx",
    "onnx/decoder_model_merged_quantized.onnx",
    "onnx/encoder_model_quantized.onnx",
    "onnx/model_q4f16.onnx",
    "onnx/model_quantized.onnx",
]

for repo in MODELS:
    print("Downloading", repo)
    snapshot_download(repo_id=repo, local_dir=f"models/{repo}", allow_patterns=PATTERNS)
print("Done. Serve this folder: python -m http.server 8080  then open http://localhost:8080")
