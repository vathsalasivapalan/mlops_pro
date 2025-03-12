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

# Create directories and files
for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir = file_path.parent  # Get parent directory

    # Create the directory if it doesn't exist
    if file_dir and not file_dir.exists():
        file_dir.mkdir(parents=True, exist_ok=True)

    # Create the file if it does not exist or is empty
    if not file_path.exists() or file_path.stat().st_size == 0:
        file_path.touch()
