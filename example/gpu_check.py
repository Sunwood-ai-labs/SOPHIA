import torch

print("PyTorch version:", torch.__version__)
# PyTorch version: 1.7.1

print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("Number of GPUs:", torch.cuda.device_count())
    print("Current GPU index:", torch.cuda.current_device())
    print("Current GPU name:", torch.cuda.get_device_name())
    # Current GPU name: GeForce GTX 1080 Ti
    print("Current GPU capability:", torch.cuda.get_device_capability())
    # Current GPU capability: (6, 1)
else:
    print("No CUDA-capable GPU detected.")
    
# root@SOPHIA-Container:/app# python3 example/gpu_check.py 
# PyTorch version: 2.3.1+cu118
# CUDA available: True
# Number of GPUs: 2
# Current GPU index: 0
# Current GPU name: NVIDIA GeForce RTX 4090
# Current GPU capability: (8, 9)
# root@SOPHIA-Container:/app# 