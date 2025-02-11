from pathlib import Path

def get_data_path():
    return Path(__file__).resolve().parent.parent.parent / "data"

print(f"Path.cwd(): {Path.cwd()}")
print(f"Path(__file__).resolve(): {Path(__file__).resolve()}")
print(
    f"Path(__file__).resolve().parent: {Path(__file__).resolve().parent}"
)
print(f"Path_data_path: {get_data_path()}")

# # Need to complie the code from the project directory
# with open("data/boston.csv") as file:
#     first_line = file.readline()
#     print(first_line.strip())

# # Using Pathlib to get the cwd path to the data directory
# data_path = Path.cwd() / "data"  # Go up one level from src to find data
# with open(data_path / "boston.csv") as file:
#     first_line = file.readline()
#     print(first_line.strip())

# # Using Pathlib to get the relative path to the data directory
# data_path = Path(__file__).resolve().parent.parent.parent / "data"
# with open(data_path / "boston.csv") as file:
#     first_line = file.readline()
#     print(first_line.strip())
