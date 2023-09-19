from pathlib import Path
import sys
parent_dir = str(Path(__file__).resolve().parents[0])
sys.path.append(parent_dir)
from ConfigClass import *



# Dataset: 
    # 1. Create vocabulary
    # 2. Create n-grams data
    # 3. Convert text to numerical

class MyDataset(torch._utils.data.Dataset):
    def __init__(self, Information):
        super().__init__()
        self.Information = Information

        # 1. Create vocabulary
        