import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup(rank, world_size):
    # Initialize the process group
    dist.init_process_group("nccl", rank=rank, world_size=world_size)
    # Ensure each process has its own GPU
    torch.cuda.set_device(rank)

def cleanup():
    dist.destroy_process_group()
