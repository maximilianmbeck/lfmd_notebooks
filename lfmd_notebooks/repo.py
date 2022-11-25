from pathlib import Path
from ml_utilities.output_loader.repo import Repo
from omegaconf import OmegaConf


REPO = Repo(dir=Path('../../erank'), hydra_defaults=OmegaConf.load('../configs/defaults.yaml'))