# pyTABS - ETABS .NET API python wrapper
# Custom Enumerations
# Enumerations not included within ETABS API

# import enum types
from enum import Enum, IntEnum


class eGeometryNonlinearityType(IntEnum):
    NONE = 0
    P_DELTA = 1
    P_DELTA_LARGE_DELTA = 2


class eLoadApplicationControlType(IntEnum):
    FULL_LOAD = 0
    DISPLACEMENT_CONTROL = 1
    QUASI_STATIC = 2


class eDisplacementControlType(IntEnum):
    CONJUGATE = 0
    MONITORED = 1


class eDisplacementMonitorType(IntEnum):
    DOF_JOINT = 0
    GENERALIZED = 1


class eMonitoredDisplacementDoF(IntEnum):
    U1 = 0
    U2 = 1
    U3 = 2
    R1 = 3
    R2 = 4
    R3 = 5


class eLinearStaticCaseLoadType(str, Enum):
    LOAD = 'Load'
    ACCELERATION = 'Accel'


class eNonlinearStaticCaseLoadType(str, Enum):
    LOAD = 'Load'
    ACCELERATION = 'Accel'
    MODE = 'Mode'


class eStageOperationType(IntEnum):
    ADD_STRUCTURE = 1
    REMOVE_STRUCTURE = 2
    LOAD_NEW = 3
    LOAD_ALL = 4
    CHANGE_PROPERTY = 5
    CHANGE_PROPERTY_MODIFIERS = 6
    CHANGE_RELEASES = 7
    CHANGE_PROPERTY_AGE = 11


class eStageObjectType(str, Enum):
    GROUP = 'Group'
    FRAME = 'Frame'
    CABLE = 'Cable'
    TENDON = 'Tendon'
    AREA = 'Area'
    SOLID = 'Solid'
    LINK = 'Link'
    POINT = 'Point'


class eStageMyType(str, Enum):
    LOAD = 'Load'
    ACCELERATION = 'Accel'
    FRAME = 'Frame'
    CABLE = 'Cable'
    TENDON = 'Tendon'
    AREA = 'Area'
    SOLID = 'Solid'
    LINK = 'Link'