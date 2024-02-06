# End to End Machine Learing Project

# MLOps Project Setup Guide

This guide outlines the setup process for our MLOps project, including environment setup, project structure, and common functionalities.

## Environment Setup

1. **Creating a New Environment:**
   - Create a new repository on GitHub and name it appropriately.
   - Locally, create a new project folder.
   - Open the project folder using an IDE like Visual Studio Code.
   - Create a virtual environment with Python 3.8: `conda create -p venv python==3.8 -y`.
   - Activate the virtual environment: `conda activate`.
   - Synchronize the remote GitHub repository with your IDE project:
     - Initialize Git, create a README.md locally, add files to staging, commit, create branches, and push changes to GitHub.
     - On GitHub, create a `.gitignore` file.
     - Pull changes to your IDE using Git.

2. **Setup.py:**
   - A Python script ensuring correct installation of the program as a package, enabling its distribution via PyPI.
   - After `setup.py`, ensure the `src` folder is created and recognized as a package.

3. **Requirements.txt:** List all project dependencies here.

## Project Structure

1. **Src Folder:** Development hub of the project, identified as a package by `__init__.py` files.

2. **Components Folder:** Contains modules like data ingestion, data transformation, and model training, including functionality to push the trained model file to the cloud. It's made importable by including an `__init__.py` file.

3. **Pipeline Folder:** Houses training and prediction pipelines.

4. **Logger File:** For logging all execution information, helping track errors or exceptions.

5. **Exception File:** Handles exceptions, utilizing the sys library to interact with the Python runtime environment.

6. **Utils File:** Contains common functions used throughout the project, such as reading data from clouds or pushing `.pkl` files to the cloud.

Remember to replace placeholders with your specific details, and adjust the structure as necessary for your project.
