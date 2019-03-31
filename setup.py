import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "win32GUI"

setup(name="ChargeFileValidation",
      version="0.1",
      description="Validate charge files against BL_RATED table",
      executables=[Executable("ChargeFileValidation.py", base=base)])
