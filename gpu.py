import torch as torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(torch.__version__)
gpu_index = torch.cuda.current_device()
print("Using GPU"+str(gpu_index))
print(device)