# pyTABS - ETABS .NET API python wrapper
# ETABS Configuration - ETABS API DLL handler


# general library imports
import pytabs.pytabs_config as config
import warnings

# import pythonnet clr-loader
import clr

# pythonnet clr-loader import of Marshal - ETABS API requirement
clr.AddReference("System.Runtime.InteropServices")
from System.Runtime.InteropServices import Marshal


# read pytabs config file
pytabs_config = config.read_config()

# try import of ETABS API DLL path from config file
etabs_api_path = pytabs_config['ETABS']['API_DLL_PATH']

# pythonnet clr-loader try import of ETABS API DLL (ETABSv1.dll)
try:
    clr.AddReference(etabs_api_path)
    from ETABSv1 import *
except:
    warnings.warn("ETABS API DLL file (ETABSv1.dll) not found in configured location, check pytabs_config.ini", ImportWarning)