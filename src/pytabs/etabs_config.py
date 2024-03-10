# PyTABS - ETABS .NET API python wrapper
# ETABS Configuration - ETABS API DLL handler

# general library imports
import pytabs.pytabs_config as config
import sys
import warnings
import clr

# Mock for pdoc pipeline where dependency is not available
# reference: https://blog.rtwilson.com/how-to-make-your-sphinx-documentation-compile-with-readthedocs-when-youre-using-numpy-and-scipy/
MOCK_MODULES = ['ETABSv1']


class Mock(object):
    __qualname__ = 'mock'

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            # return type(name, (), {})
            return None
        else:
            return Mock()


# read pytabs config file
pytabs_config = config.read_config()
etabs_api_path = pytabs_config['ETABS']['API_DLL_PATH']

# pythonnet clr-loader import of Marshal - ETABS API requirement
clr.AddReference("System.Runtime.InteropServices")

# pythonnet clr-loader try import of ETABS API DLL (ETABSv1.dll) else load Mock
warnings.filterwarnings('default')
try:
    clr.AddReference(etabs_api_path)
    import ETABSv1 as etabs
except:
    for mod_name in MOCK_MODULES:
        sys.modules[mod_name] = Mock()
    import ETABSv1 as etabs
    warnings.warn("ETABS API DLL file (ETABSv1.dll) not found in configured location, check pytabs_config.ini",
                  ImportWarning)
