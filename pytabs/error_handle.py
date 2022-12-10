# pyTABS - ETABS .NET API python wrapper
# ErrorHandling - for pyTABS exceptions
__all__ = ['handle']

class Error(Exception):
    """Error base class for non-exit exceptions"""
    pass

class EtabsError(Error):
    """General ETABS API Error Class"""
    def __init__(self, ret : int, msg : str = 'EtabsError: Unknown API error.'):
        self.ret : int = ret
        self.msg : str = msg


def handle(ret : int) -> None:
    """handles ETABS API return errors

    Args:
        ret (int): return integer from ETABS API function

    Raises:
        EtabsError: General ETABS API error if return int is != 0 
    """
    if ret != 0:
        raise EtabsError(ret=ret)