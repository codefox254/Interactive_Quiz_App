#!/usr/bin/env python3


import subprocess

def install_package(package):
    try:
        # Using subprocess.run for better control of output and errors
        result = subprocess.run(["pip", "install", package], check=True, capture_output=True, text=True)
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}. Error: {e.stderr}")

def install_packages_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            packages = f.readlines()
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return

    for package in packages:
        package = package.strip()  # Clean up any whitespace
        if package:  # Ensure it's not an empty line
            install_package(package)

# Specify the requirements.txt file location
install_packages_from_file("requirements.txt")
