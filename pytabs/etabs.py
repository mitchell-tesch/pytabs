# pyTABS - ETABS .NET API python wrapper
# ETABSv1 namespace reference


# import default settings
from pathlib import Path
from pytabs.settings import ETABS_DIR, ETABS_API_DLL, ETABS_EXE
default_etabs_api_path = Path(ETABS_DIR) / ETABS_API_DLL
default_etabs_exe_path = Path(ETABS_DIR) / ETABS_EXE

# import pythonnet clr-loader
import clr

# pythonnet clr-loader import of Marshal - ETABS API requirement
clr.AddReference("System.Runtime.InteropServices")
from System.Runtime.InteropServices import Marshal

# pythonnet clr-loader import of ETABS API .dll
# clr.AddReference(str(default_etabs_api_path))
clr.AddReference('ETABSv1')
from ETABSv1 import *
