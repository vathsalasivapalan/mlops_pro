import os
from pathlib import Path

package_name = "mongodb_connect"

# List of required files
list_of_files = [
    ".github/workflows/ci.yaml",  # Fixed the filename from .ymal to .yaml
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/int.py",
    "init_setup.sh",
    "requirements.txt",  # Production
    "requirements_dev.txt",  # Development
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)  # Correct variable usage
    filedir, filename = os.path.split(filepath)  # Get parent directory

    # Create the parent directory if it does not exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)  # Use os.makedirs()

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
       with open(filepath, 'w') as f:
          pass  # Create an empty file
