# pyTABS - ETABS .NET API python wrapper
# Custom Enumerations
# Enumerations not included within ETABS API

# import enum types
from enum import IntEnum


class eGeometryNonlinearityTypes(IntEnum):
    NONE = 0
    P_DELTA = 1
    P_DELTA_LARGE_DELTA = 2