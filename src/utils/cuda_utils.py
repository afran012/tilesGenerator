import torch

def initialize_cuda():
    if torch.cuda.is_available():
        device = torch.device('cuda')
        print(f"Usando dispositivo CUDA: {torch.cuda.get_device_name(device)}")
    else:
        print("CUDA no está disponible. Usando CPU.")