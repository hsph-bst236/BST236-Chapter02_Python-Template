import sys
from pathlib import Path

#sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.path_demo import get_data_path

print(get_data_path())
