import subprocess
import torch

def get_cuda_info():
    print("NVIDIA Graphics Card Driver: ", subprocess.getoutput("nvidia-smi")[:980])
    print("CUDA version: ", subprocess.getoutput("nvcc --version"), "\n")

def get_torch_info():
    print(subprocess.getoutput("pip show torch"), "\n")

def get_device(show_info = True):
    if torch.cuda.is_available():    
        device = torch.device("cuda")

        if show_info:
            print('There are %d GPU(s) available.' % torch.cuda.device_count())
            print('We will use the GPU:', torch.cuda.get_device_name(0))

    else:
        device = torch.device("cpu")

        if show_info:
            print('No GPU available, using the CPU instead.')

    return device