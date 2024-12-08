import torch

def validate_cuda():
    if torch.cuda.is_available():
        device_name = torch.cuda.get_device_name(0)
        print(f"CUDA está disponible. Usando dispositivo: {device_name}")
        return True
    else:
        print("CUDA no está disponible.")
        return False