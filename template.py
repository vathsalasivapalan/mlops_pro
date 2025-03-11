import os
from pathlib import Path
import logging  # Added logging import

# Fixed variable name ("list_of_files" instead of "list of files")
list_of_files = [
    "github/workflows/.gitkeep",  # Corrected file name from ",gitkeep" to ".gitkeep"
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",            # Changed "pipline" to "pipeline" if that was the intent
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",               # Added the ".py" extension for consistency
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",          # Added the ".py" extension assuming it's a Python file
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cgf",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, filename = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        # Fixed f-string formatting
        logging.info(f"Creating Directory: {file_dir} for file: {filename}")

    # Create the file if it does not exist or is empty
    if (not file_path.exists()) or (file_path.stat().st_size == 0):
        with open(file_path, 'w') as f:
            pass  # create an empty file
