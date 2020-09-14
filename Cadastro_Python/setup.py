#setup.py
import sys
from cx_Freeze import setup, Executable
import cx_Freeze
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
setup(
    name = "cadastro",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["os","sys","ctypes"],
        'include_files': [],
        'include_msvcr': True,
    }},
    executables = [Executable("cadastro_tela.py",base=base)]
    )