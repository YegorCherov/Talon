#!/usr/bin/env python3
"""
Creates the folder structure for the "Talon" project,
mirroring the layout used in the Apex repo:

3d print/
cad/
  v1/
  v2/
  v3-final/
images/
"""

import os

# Root folder name - change if you want it nested somewhere else
ROOT = "Talon"

FOLDERS = [
    "3d print",
    os.path.join("cad", "v1"),
    os.path.join("cad", "v2"),
    os.path.join("cad", "v3-final"),
    "images",
]

def create_structure(root: str = ROOT):
    for folder in FOLDERS:
        path = os.path.join(root, folder)
        os.makedirs(path, exist_ok=True)
        # Add a .gitkeep so empty folders survive a git commit
        gitkeep = os.path.join(path, ".gitkeep")
        if not os.path.exists(gitkeep):
            open(gitkeep, "w").close()
        print(f"Created: {path}")

    # Placeholder top-level files, matching Apex's repo root
    for filename in ["README.md", "CHANGELOG.md", "LICENSE"]:
        filepath = os.path.join(root, filename)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                if filename == "README.md":
                    f.write("# Talon\n\n")
            print(f"Created: {filepath}")

if __name__ == "__main__":
    create_structure()
    print(f"\nDone. '{ROOT}/' now mirrors the Apex repo structure.")
