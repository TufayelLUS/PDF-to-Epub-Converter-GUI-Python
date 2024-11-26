import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"  # Use this option to create a GUI executable on Windows
# set the name of the python script below
executables = [Executable("Epub Maker.py", base=base)]
# if you want to show the console, use the line below instead and comment out the line above
# executables = [Executable("python_file_name.py", base="Console")]

options = {
    "build_exe": {
        "optimize": 2, # set level of optimization 0-2
        "packages": [],  # List of packages to include
        "include_files": [],  # List of additional files to include
    },
}

setup(
    name="Epub Maker", # name of the process
    version="1.0",
    description="Epub Maker", # description of the process
    options=options,
    executables=executables
)