from pathlib import Path
import sys
parent_dir = str(Path(__file__).resolve().parents[0])
sys.path.append(parent_dir)

from typing import Any
import pytorch_lightning as pl
import torch
from abc import ABC, abstractmethod
import numpy as np
from dataclasses import asdict
from dataclasses import dataclass
from collections import Counter, OrderedDict
from torchtext.vocab import vocab
import torchtext
from torchdata.datapipes.iter import IterableWrapper
from torch.utils.data import DataLoader, random_split
from nltk import ngrams
from pytorch_lightning.utilities.types import STEP_OUTPUT
import matplotlib.pyplot as plt



@dataclass
class ConfigInformation:
    # Path
    path_data_dir                   : str = parent_dir + '/DataFolder'
    path_data_file                  : str = path_data_dir + "/TinyShakespeare.txt"
    dir_checkpoint                  : str = path_data_dir + "/Checkpoints/"


if __name__ == '__main__':
    config = ConfigInformation()
    print(config.path_data_dir)