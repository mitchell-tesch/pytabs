# encoding: utf-8
# module ETABSv1
# from ETABSv1, Version=1.0.0.0, Culture=neutral, PublicKeyToken=453d728ef24c6f5e
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class cAnalysisResults:
    # no doc
    def AreaForceShell(self, Name, ItemTypeElm, NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum, F11, F22, F12, FMax, FMin, FAngle, FVM, M11, M22, M12, MMax, MMin, MAngle, V13, V23, VMax, VAngle):
        """ AreaForceShell(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], F11: Array[float], F22: Array[float], F12: Array[float], FMax: Array[float], FMin: Array[float], FAngle: Array[float], FVM: Array[float], M11: Array[float], M22: Array[float], M12: Array[float], MMax: Array[float], MMin: Array[float], MAngle: Array[float], V13: Array[float], V23: Array[float], VMax: Array[float], VAngle: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def AreaJointForceShell(self, Name, ItemTypeElm, NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum, F1, F2, F3, M1, M2, M3):
        """ AreaJointForceShell(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], F1: Array[float], F2: Array[float], F3: Array[float], M1: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def AreaStrainShell(self, Name, ItemTypeElm, NumberResults, obj, elm, PointElm, LoadCase, StepType, StepNum, e11top, e22top, g12top, emaxtop, emintop, eangletop, evmtop, e11bot, e22bot, g12bot, emaxbot, eminbot, eanglebot, evmbot, g13avg, g23avg, gmaxavg, gangleavg):
        """ AreaStrainShell(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, obj: Array[str], elm: Array[str], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], e11top: Array[float], e22top: Array[float], g12top: Array[float], emaxtop: Array[float], emintop: Array[float], eangletop: Array[float], evmtop: Array[float], e11bot: Array[float], e22bot: Array[float], g12bot: Array[float], emaxbot: Array[float], eminbot: Array[float], eanglebot: Array[float], evmbot: Array[float], g13avg: Array[float], g23avg: Array[float], gmaxavg: Array[float], gangleavg: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def AreaStrainShellLayered(self, Name, ItemTypeElm, NumberResults, obj, elm, Layer, IntPtNum, IntPtLoc, PointElm, LoadCase, StepType, StepNum, E11, E22, G12, EMax, EMin, EAngle, EVM, G13avg, G23avg, GMaxavg, GAngleavg):
        """ AreaStrainShellLayered(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, obj: Array[str], elm: Array[str], Layer: Array[str], IntPtNum: Array[int], IntPtLoc: Array[float], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], E11: Array[float], E22: Array[float], G12: Array[float], EMax: Array[float], EMin: Array[float], EAngle: Array[float], EVM: Array[float], G13avg: Array[float], G23avg: Array[float], GMaxavg: Array[float], GAngleavg: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[int], Array[float], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def AreaStressShell(self, Name, ItemTypeElm, NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum, S11Top, S22Top, S12Top, SMaxTop, SMinTop, SAngleTop, SVMTop, S11Bot, S22Bot, S12Bot, SMaxBot, SMinBot, SAngleBot, SVMBot, S13Avg, S23Avg, SMaxAvg, SAngleAvg):
        """ AreaStressShell(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], S11Top: Array[float], S22Top: Array[float], S12Top: Array[float], SMaxTop: Array[float], SMinTop: Array[float], SAngleTop: Array[float], SVMTop: Array[float], S11Bot: Array[float], S22Bot: Array[float], S12Bot: Array[float], SMaxBot: Array[float], SMinBot: Array[float], SAngleBot: Array[float], SVMBot: Array[float], S13Avg: Array[float], S23Avg: Array[float], SMaxAvg: Array[float], SAngleAvg: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def AreaStressShellLayered(self, Name, ItemTypeElm, NumberResults, Obj, Elm, Layer, IntPtNum, IntPtLoc, PointElm, LoadCase, StepType, StepNum, S11, S22, S12, SMax, SMin, SAngle, SVM, S13Avg, S23Avg, SMaxAvg, SAngleAvg):
        """ AreaStressShellLayered(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], Layer: Array[str], IntPtNum: Array[int], IntPtLoc: Array[float], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], S11: Array[float], S22: Array[float], S12: Array[float], SMax: Array[float], SMin: Array[float], SAngle: Array[float], SVM: Array[float], S13Avg: Array[float], S23Avg: Array[float], SMaxAvg: Array[float], SAngleAvg: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[int], Array[float], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def AssembledJointMass(self, Name, ItemTypeElm, NumberResults, PointElm, U1, U2, U3, R1, R2, R3):
        """ AssembledJointMass(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, PointElm: Array[str], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def BaseReact(self, NumberResults, LoadCase, StepType, StepNum, FX, FY, FZ, MX, ParamMy, MZ, GX, GY, GZ):
        """ BaseReact(self: cAnalysisResults, NumberResults: int, LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], FX: Array[float], FY: Array[float], FZ: Array[float], MX: Array[float], ParamMy: Array[float], MZ: Array[float], GX: float, GY: float, GZ: float) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], float, float, float) """
        pass

    def BaseReactWithCentroid(self, NumberResults, LoadCase, StepType, StepNum, FX, FY, FZ, MX, ParamMy, MZ, GX, GY, GZ, XCentroidForFX, YCentroidForFX, ZCentroidForFX, XCentroidForFY, YCentroidForFY, ZCentroidForFY, XCentroidForFZ, YCentroidForFZ, ZCentroidForFZ):
        """ BaseReactWithCentroid(self: cAnalysisResults, NumberResults: int, LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], FX: Array[float], FY: Array[float], FZ: Array[float], MX: Array[float], ParamMy: Array[float], MZ: Array[float], GX: float, GY: float, GZ: float, XCentroidForFX: Array[float], YCentroidForFX: Array[float], ZCentroidForFX: Array[float], XCentroidForFY: Array[float], YCentroidForFY: Array[float], ZCentroidForFY: Array[float], XCentroidForFZ: Array[float], YCentroidForFZ: Array[float], ZCentroidForFZ: Array[float]) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], float, float, float, Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def BucklingFactor(self, NumberResults, LoadCase, StepType, StepNum, Factor):
        """ BucklingFactor(self: cAnalysisResults, NumberResults: int, LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], Factor: Array[float]) -> (int, int, Array[str], Array[str], Array[float], Array[float]) """
        pass

    def FrameForce(self, Name, ItemTypeElm, NumberResults, Obj, ObjSta, Elm, ElmSta, LoadCase, StepType, StepNum, P, V2, V3, T, M2, M3):
        """ FrameForce(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], ObjSta: Array[float], Elm: Array[str], ElmSta: Array[float], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[float], Array[str], Array[float], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FrameJointForce(self, Name, ItemTypeElm, NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum, F1, F2, F3, M1, M2, M3):
        """ FrameJointForce(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], F1: Array[float], F2: Array[float], F3: Array[float], M1: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GeneralizedDispl(self, Name, NumberResults, GD, LoadCase, StepType, StepNum, DType, Value):
        """ GeneralizedDispl(self: cAnalysisResults, Name: str, NumberResults: int, GD: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], DType: Array[str], Value: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[str], Array[float]) """
        pass

    def JointAcc(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ JointAcc(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def JointAccAbs(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ JointAccAbs(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def JointDispl(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ JointDispl(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def JointDisplAbs(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ JointDisplAbs(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def JointDrifts(self, NumberResults, Story, Label, Name, LoadCase, StepType, StepNum, DisplacementX, DisplacementY, DriftX, DriftY):
        """ JointDrifts(self: cAnalysisResults, NumberResults: int, Story: Array[str], Label: Array[str], Name: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], DisplacementX: Array[float], DisplacementY: Array[float], DriftX: Array[float], DriftY: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def JointReact(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, F1, F2, F3, M1, M2, M3):
        """ JointReact(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], F1: Array[float], F2: Array[float], F3: Array[float], M1: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def JointVel(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ JointVel(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def JointVelAbs(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ JointVelAbs(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def LinkDeformation(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ LinkDeformation(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def LinkForce(self, Name, ItemTypeElm, NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum, P, V2, V3, T, M2, M3):
        """ LinkForce(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def LinkJointForce(self, Name, ItemTypeElm, NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum, F1, F2, F3, M1, M2, M3):
        """ LinkJointForce(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], F1: Array[float], F2: Array[float], F3: Array[float], M1: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def ModalLoadParticipationRatios(self, NumberResults, LoadCase, ItemType, Item, Stat, Dyn):
        """ ModalLoadParticipationRatios(self: cAnalysisResults, NumberResults: int, LoadCase: Array[str], ItemType: Array[str], Item: Array[str], Stat: Array[float], Dyn: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[float]) """
        pass

    def ModalParticipatingMassRatios(self, NumberResults, LoadCase, StepType, StepNum, Period, UX, UY, UZ, SumUX, SumUY, SumUZ, RX, RY, RZ, SumRX, SumRY, SumRZ):
        """ ModalParticipatingMassRatios(self: cAnalysisResults, NumberResults: int, LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], Period: Array[float], UX: Array[float], UY: Array[float], UZ: Array[float], SumUX: Array[float], SumUY: Array[float], SumUZ: Array[float], RX: Array[float], RY: Array[float], RZ: Array[float], SumRX: Array[float], SumRY: Array[float], SumRZ: Array[float]) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def ModalParticipationFactors(self, NumberResults, LoadCase, StepType, StepNum, Period, UX, UY, UZ, RX, RY, RZ, ModalMass, ModalStiff):
        """ ModalParticipationFactors(self: cAnalysisResults, NumberResults: int, LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], Period: Array[float], UX: Array[float], UY: Array[float], UZ: Array[float], RX: Array[float], RY: Array[float], RZ: Array[float], ModalMass: Array[float], ModalStiff: Array[float]) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def ModalPeriod(self, NumberResults, LoadCase, StepType, StepNum, Period, Frequency, CircFreq, EigenValue):
        """ ModalPeriod(self: cAnalysisResults, NumberResults: int, LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], Period: Array[float], Frequency: Array[float], CircFreq: Array[float], EigenValue: Array[float]) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def ModeShape(self, Name, ItemTypeElm, NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ ModeShape(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Obj: Array[str], Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def PanelZoneDeformation(self, Name, ItemTypeElm, NumberResults, Elm, LoadCase, StepType, StepNum, U1, U2, U3, R1, R2, R3):
        """ PanelZoneDeformation(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Elm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def PanelZoneForce(self, Name, ItemTypeElm, NumberResults, Elm, PointElm, LoadCase, StepType, StepNum, P, V2, V3, T, M2, M3):
        """ PanelZoneForce(self: cAnalysisResults, Name: str, ItemTypeElm: eItemTypeElm, NumberResults: int, Elm: Array[str], PointElm: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def PierForce(self, NumberResults, StoryName, PierName, LoadCase, Location, P, V2, V3, T, M2, M3):
        """ PierForce(self: cAnalysisResults, NumberResults: int, StoryName: Array[str], PierName: Array[str], LoadCase: Array[str], Location: Array[str], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SectionCutAnalysis(self, NumberResults, SCut, LoadCase, StepType, StepNum, F1, F2, F3, M1, M2, M3):
        """ SectionCutAnalysis(self: cAnalysisResults, NumberResults: int, SCut: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], F1: Array[float], F2: Array[float], F3: Array[float], M1: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SectionCutDesign(self, NumberResults, SCut, LoadCase, StepType, StepNum, P, V2, V3, T, M2, M3):
        """ SectionCutDesign(self: cAnalysisResults, NumberResults: int, SCut: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SpandrelForce(self, NumberResults, StoryName, SpandrelName, LoadCase, Location, P, V2, V3, T, M2, M3):
        """ SpandrelForce(self: cAnalysisResults, NumberResults: int, StoryName: Array[str], SpandrelName: Array[str], LoadCase: Array[str], Location: Array[str], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def StoryDrifts(self, NumberResults, Story, LoadCase, StepType, StepNum, Direction, Drift, Label, X, Y, Z):
        """ StoryDrifts(self: cAnalysisResults, NumberResults: int, Story: Array[str], LoadCase: Array[str], StepType: Array[str], StepNum: Array[float], Direction: Array[str], Drift: Array[float], Label: Array[str], X: Array[float], Y: Array[float], Z: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[str], Array[float], Array[str], Array[float], Array[float], Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Setup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Setup(self: cAnalysisResults) -> cAnalysisResultsSetup

"""



class cAnalysisResultsSetup:
    # no doc
    def DeselectAllCasesAndCombosForOutput(self):
        """ DeselectAllCasesAndCombosForOutput(self: cAnalysisResultsSetup) -> int """
        pass

    def GetCaseSelectedForOutput(self, Name, Selected):
        """ GetCaseSelectedForOutput(self: cAnalysisResultsSetup, Name: str, Selected: bool) -> (int, bool) """
        pass

    def GetComboSelectedForOutput(self, Name, Selected):
        """ GetComboSelectedForOutput(self: cAnalysisResultsSetup, Name: str, Selected: bool) -> (int, bool) """
        pass

    def GetOptionBaseReactLoc(self, GX, GY, GZ):
        """ GetOptionBaseReactLoc(self: cAnalysisResultsSetup, GX: float, GY: float, GZ: float) -> (int, float, float, float) """
        pass

    def GetOptionBucklingMode(self, BuckModeStart, BuckModeEnd, BuckModeAll):
        """ GetOptionBucklingMode(self: cAnalysisResultsSetup, BuckModeStart: int, BuckModeEnd: int, BuckModeAll: bool) -> (int, int, int, bool) """
        pass

    def GetOptionDirectHist(self, Value):
        """ GetOptionDirectHist(self: cAnalysisResultsSetup, Value: int) -> (int, int) """
        pass

    def GetOptionModalHist(self, Value):
        """ GetOptionModalHist(self: cAnalysisResultsSetup, Value: int) -> (int, int) """
        pass

    def GetOptionModeShape(self, ModeShapeStart, ModeShapeEnd, ModeShapesAll):
        """ GetOptionModeShape(self: cAnalysisResultsSetup, ModeShapeStart: int, ModeShapeEnd: int, ModeShapesAll: bool) -> (int, int, int, bool) """
        pass

    def GetOptionMultiStepStatic(self, Value):
        """ GetOptionMultiStepStatic(self: cAnalysisResultsSetup, Value: int) -> (int, int) """
        pass

    def GetOptionMultiValuedCombo(self, Value):
        """ GetOptionMultiValuedCombo(self: cAnalysisResultsSetup, Value: int) -> (int, int) """
        pass

    def GetOptionNLStatic(self, Value):
        """ GetOptionNLStatic(self: cAnalysisResultsSetup, Value: int) -> (int, int) """
        pass

    def SetCaseSelectedForOutput(self, Name, Selected):
        """ SetCaseSelectedForOutput(self: cAnalysisResultsSetup, Name: str, Selected: bool) -> int """
        pass

    def SetComboSelectedForOutput(self, Name, Selected):
        """ SetComboSelectedForOutput(self: cAnalysisResultsSetup, Name: str, Selected: bool) -> int """
        pass

    def SetOptionBaseReactLoc(self, GX, GY, GZ):
        """ SetOptionBaseReactLoc(self: cAnalysisResultsSetup, GX: float, GY: float, GZ: float) -> int """
        pass

    def SetOptionBucklingMode(self, BuckModeStart, BuckModeEnd, BuckModeAll):
        """ SetOptionBucklingMode(self: cAnalysisResultsSetup, BuckModeStart: int, BuckModeEnd: int, BuckModeAll: bool) -> int """
        pass

    def SetOptionDirectHist(self, Value):
        """ SetOptionDirectHist(self: cAnalysisResultsSetup, Value: int) -> int """
        pass

    def SetOptionModalHist(self, Value):
        """ SetOptionModalHist(self: cAnalysisResultsSetup, Value: int) -> int """
        pass

    def SetOptionModeShape(self, ModeShapeStart, ModeShapeEnd, ModeShapesAll):
        """ SetOptionModeShape(self: cAnalysisResultsSetup, ModeShapeStart: int, ModeShapeEnd: int, ModeShapesAll: bool) -> int """
        pass

    def SetOptionMultiStepStatic(self, Value):
        """ SetOptionMultiStepStatic(self: cAnalysisResultsSetup, Value: int) -> int """
        pass

    def SetOptionMultiValuedCombo(self, Value):
        """ SetOptionMultiValuedCombo(self: cAnalysisResultsSetup, Value: int) -> int """
        pass

    def SetOptionNLStatic(self, Value):
        """ SetOptionNLStatic(self: cAnalysisResultsSetup, Value: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cAnalyze:
    # no doc
    def CreateAnalysisModel(self):
        """ CreateAnalysisModel(self: cAnalyze) -> int """
        pass

    def DeleteResults(self, Name, All):
        """ DeleteResults(self: cAnalyze, Name: str, All: bool) -> int """
        pass

    def GetActiveDOF(self, DOF):
        """ GetActiveDOF(self: cAnalyze, DOF: Array[bool]) -> (int, Array[bool]) """
        pass

    def GetCaseStatus(self, NumberItems, CaseName, Status):
        """ GetCaseStatus(self: cAnalyze, NumberItems: int, CaseName: Array[str], Status: Array[int]) -> (int, int, Array[str], Array[int]) """
        pass

    def GetDesignResponseOption(self, NumberDesignThreads, NumberResponseRecoveryThreads, UseMemoryMappedFilesForResponseRecovery, ModelDifferencesOKWhenMergingResults):
        """ GetDesignResponseOption(self: cAnalyze, NumberDesignThreads: int, NumberResponseRecoveryThreads: int, UseMemoryMappedFilesForResponseRecovery: int, ModelDifferencesOKWhenMergingResults: bool) -> (int, int, int, int, bool) """
        pass

    def GetRunCaseFlag(self, NumberItems, CaseName, Run):
        """ GetRunCaseFlag(self: cAnalyze, NumberItems: int, CaseName: Array[str], Run: Array[bool]) -> (int, int, Array[str], Array[bool]) """
        pass

    def GetSolverOption(self, SolverType, Force32BitSolver, StiffCase):
        """ GetSolverOption(self: cAnalyze, SolverType: int, Force32BitSolver: bool, StiffCase: str) -> (int, int, bool, str) """
        pass

    def GetSolverOption_1(self, SolverType, SolverProcessType, Force32BitSolver, StiffCase):
        """ GetSolverOption_1(self: cAnalyze, SolverType: int, SolverProcessType: int, Force32BitSolver: bool, StiffCase: str) -> (int, int, int, bool, str) """
        pass

    def GetSolverOption_2(self, SolverType, SolverProcessType, NumberParallelRuns, StiffCase):
        """ GetSolverOption_2(self: cAnalyze, SolverType: int, SolverProcessType: int, NumberParallelRuns: int, StiffCase: str) -> (int, int, int, int, str) """
        pass

    def GetSolverOption_3(self, SolverType, SolverProcessType, NumberParallelRuns, ResponseFileSizeMaxMB, NumberAnalysisThreads, StiffCase):
        """ GetSolverOption_3(self: cAnalyze, SolverType: int, SolverProcessType: int, NumberParallelRuns: int, ResponseFileSizeMaxMB: int, NumberAnalysisThreads: int, StiffCase: str) -> (int, int, int, int, int, int, str) """
        pass

    def MergeAnalysisResults(self, SourceFileName):
        """ MergeAnalysisResults(self: cAnalyze, SourceFileName: str) -> int """
        pass

    def ModifyUndeformedGeometry(self, CaseName, SF, Stage, Original):
        """ ModifyUndeformedGeometry(self: cAnalyze, CaseName: str, SF: float, Stage: int, Original: bool) -> int """
        pass

    def ModifyUndeformedGeometryModeShape(self, CaseName, Mode, MaxDispl, Direction, Original):
        """ ModifyUndeformedGeometryModeShape(self: cAnalyze, CaseName: str, Mode: int, MaxDispl: float, Direction: int, Original: bool) -> int """
        pass

    def RunAnalysis(self):
        """ RunAnalysis(self: cAnalyze) -> int """
        pass

    def SetActiveDOF(self, DOF):
        """ SetActiveDOF(self: cAnalyze, DOF: Array[bool]) -> (int, Array[bool]) """
        pass

    def SetDesignResponseOption(self, NumberDesignThreads, NumberResponseRecoveryThreads, UseMemoryMappedFilesForResponseRecovery, ModelDifferencesOKWhenMergingResults):
        """ SetDesignResponseOption(self: cAnalyze, NumberDesignThreads: int, NumberResponseRecoveryThreads: int, UseMemoryMappedFilesForResponseRecovery: int, ModelDifferencesOKWhenMergingResults: bool) -> int """
        pass

    def SetRunCaseFlag(self, Name, Run, All):
        """ SetRunCaseFlag(self: cAnalyze, Name: str, Run: bool, All: bool) -> int """
        pass

    def SetSolverOption(self, SolverType, Force32BitSolver, StiffCase):
        """ SetSolverOption(self: cAnalyze, SolverType: int, Force32BitSolver: bool, StiffCase: str) -> int """
        pass

    def SetSolverOption_1(self, SolverType, SolverProcessType, Force32BitSolver, StiffCase):
        """ SetSolverOption_1(self: cAnalyze, SolverType: int, SolverProcessType: int, Force32BitSolver: bool, StiffCase: str) -> int """
        pass

    def SetSolverOption_2(self, SolverType, SolverProcessType, NumberParallelRuns, StiffCase):
        """ SetSolverOption_2(self: cAnalyze, SolverType: int, SolverProcessType: int, NumberParallelRuns: int, StiffCase: str) -> int """
        pass

    def SetSolverOption_3(self, SolverType, SolverProcessType, NumberParallelRuns, ResponseFileSizeMaxMB, NumberAnalysisThreads, StiffCase):
        """ SetSolverOption_3(self: cAnalyze, SolverType: int, SolverProcessType: int, NumberParallelRuns: int, ResponseFileSizeMaxMB: int, NumberAnalysisThreads: int, StiffCase: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cAreaElm:
    # no doc
    def Count(self):
        """ Count(self: cAreaElm) -> int """
        pass

    def GetLoadTemperature(self, Name, NumberItems, AreaName, LoadPat, MyType, Value, PatternName, ItemTypeElm):
        """ GetLoadTemperature(self: cAreaElm, Name: str, NumberItems: int, AreaName: Array[str], LoadPat: Array[str], MyType: Array[int], Value: Array[float], PatternName: Array[str], ItemTypeElm: eItemTypeElm) -> (int, int, Array[str], Array[str], Array[int], Array[float], Array[str]) """
        pass

    def GetLoadUniform(self, Name, NumberItems, AreaName, LoadPat, CSys, Dir, Value, ItemTypeElm):
        """ GetLoadUniform(self: cAreaElm, Name: str, NumberItems: int, AreaName: Array[str], LoadPat: Array[str], CSys: Array[str], Dir: Array[int], Value: Array[float], ItemTypeElm: eItemTypeElm) -> (int, int, Array[str], Array[str], Array[str], Array[int], Array[float]) """
        pass

    def GetLocalAxes(self, Name, Ang):
        """ GetLocalAxes(self: cAreaElm, Name: str, Ang: float) -> (int, float) """
        pass

    def GetMaterialOverwrite(self, Name, PropName):
        """ GetMaterialOverwrite(self: cAreaElm, Name: str, PropName: str) -> (int, str) """
        pass

    def GetModifiers(self, Name, Value):
        """ GetModifiers(self: cAreaElm, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cAreaElm, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetObj(self, Name, Obj):
        """ GetObj(self: cAreaElm, Name: str, Obj: str) -> (int, str) """
        pass

    def GetOffsets(self, Name, OffsetType, OffsetPattern, OffsetPatternSF, Offset):
        """ GetOffsets(self: cAreaElm, Name: str, OffsetType: int, OffsetPattern: str, OffsetPatternSF: float, Offset: Array[float]) -> (int, int, str, float, Array[float]) """
        pass

    def GetPoints(self, Name, NumberPoints, Point):
        """ GetPoints(self: cAreaElm, Name: str, NumberPoints: int, Point: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetProperty(self, Name, PropName):
        """ GetProperty(self: cAreaElm, Name: str, PropName: str) -> (int, str) """
        pass

    def GetThickness(self, Name, ThicknessType, ThicknessPattern, ThicknessPatternSF, Thickness):
        """ GetThickness(self: cAreaElm, Name: str, ThicknessType: int, ThicknessPattern: str, ThicknessPatternSF: float, Thickness: Array[float]) -> (int, int, str, float, Array[float]) """
        pass

    def GetTransformationMatrix(self, Name, Value):
        """ GetTransformationMatrix(self: cAreaElm, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cAreaObj:
    # no doc
    def AddByCoord(self, NumberPoints, X, Y, Z, Name, PropName, UserName, CSys):
        """ AddByCoord(self: cAreaObj, NumberPoints: int, X: Array[float], Y: Array[float], Z: Array[float], Name: str, PropName: str, UserName: str, CSys: str) -> (int, Array[float], Array[float], Array[float], str) """
        pass

    def AddByPoint(self, NumberPoints, Point, Name, PropName, UserName):
        """ AddByPoint(self: cAreaObj, NumberPoints: int, Point: Array[str], Name: str, PropName: str, UserName: str) -> (int, Array[str], str) """
        pass

    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cAreaObj, Name: str, NewName: str) -> int """
        pass

    def Count(self):
        """ Count(self: cAreaObj) -> int """
        pass

    def Delete(self, Name, ItemType):
        """ Delete(self: cAreaObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteLoadTemperature(self, Name, LoadPat, ItemType):
        """ DeleteLoadTemperature(self: cAreaObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteLoadUniform(self, Name, LoadPat, ItemType):
        """ DeleteLoadUniform(self: cAreaObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteLoadUniformToFrame(self, Name, LoadPat, ItemType):
        """ DeleteLoadUniformToFrame(self: cAreaObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteLoadWindPressure(self, Name, LoadPat, ItemType):
        """ DeleteLoadWindPressure(self: cAreaObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteMass(self, Name, ItemType):
        """ DeleteMass(self: cAreaObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteModifiers(self, Name, ItemType):
        """ DeleteModifiers(self: cAreaObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteSpring(self, Name, ItemType):
        """ DeleteSpring(self: cAreaObj, Name: str, ItemType: eItemType) -> int """
        pass

    def GetAllAreas(self, NumberNames, MyName, DesignOrientation, NumberBoundaryPts, PointDelimiter, PointNames, PointX, PointY, PointZ):
        """ GetAllAreas(self: cAreaObj, NumberNames: int, MyName: Array[str], DesignOrientation: Array[eAreaDesignOrientation], NumberBoundaryPts: int, PointDelimiter: Array[int], PointNames: Array[str], PointX: Array[float], PointY: Array[float], PointZ: Array[float]) -> (int, int, Array[str], Array[eAreaDesignOrientation], int, Array[int], Array[str], Array[float], Array[float], Array[float]) """
        pass

    def GetCurvedEdges(self, Name, NumEdges, CurveType, Tension, NumPoints, gx, gy, gz):
        """ GetCurvedEdges(self: cAreaObj, Name: str, NumEdges: int, CurveType: Array[int], Tension: Array[float], NumPoints: Array[int], gx: Array[float], gy: Array[float], gz: Array[float]) -> (int, int, Array[int], Array[float], Array[int], Array[float], Array[float], Array[float]) """
        pass

    def GetDesignOrientation(self, Name, DesignOrientation):
        """ GetDesignOrientation(self: cAreaObj, Name: str, DesignOrientation: eAreaDesignOrientation) -> (int, eAreaDesignOrientation) """
        pass

    def GetDiaphragm(self, Name, DiaphragmName):
        """ GetDiaphragm(self: cAreaObj, Name: str, DiaphragmName: str) -> (int, str) """
        pass

    def GetEdgeConstraint(self, Name, ConstraintExists):
        """ GetEdgeConstraint(self: cAreaObj, Name: str, ConstraintExists: bool) -> (int, bool) """
        pass

    def GetElm(self, Name, NElm, Elm):
        """ GetElm(self: cAreaObj, Name: str, NElm: int, Elm: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetGroupAssign(self, Name, NumberGroups, Groups):
        """ GetGroupAssign(self: cAreaObj, Name: str, NumberGroups: int, Groups: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetGUID(self, Name, GUID):
        """ GetGUID(self: cAreaObj, Name: str, GUID: str) -> (int, str) """
        pass

    def GetLabelFromName(self, Name, Label, Story):
        """ GetLabelFromName(self: cAreaObj, Name: str, Label: str, Story: str) -> (int, str, str) """
        pass

    def GetLabelNameList(self, NumberNames, MyName, MyLabel, MyStory):
        """ GetLabelNameList(self: cAreaObj, NumberNames: int, MyName: Array[str], MyLabel: Array[str], MyStory: Array[str]) -> (int, int, Array[str], Array[str], Array[str]) """
        pass

    def GetLoadTemperature(self, Name, NumberItems, AreaName, LoadPat, MyType, Value, PatternName, ItemType):
        """ GetLoadTemperature(self: cAreaObj, Name: str, NumberItems: int, AreaName: Array[str], LoadPat: Array[str], MyType: Array[int], Value: Array[float], PatternName: Array[str], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[int], Array[float], Array[str]) """
        pass

    def GetLoadUniform(self, Name, NumberItems, AreaName, LoadPat, CSys, Dir, Value, ItemType):
        """ GetLoadUniform(self: cAreaObj, Name: str, NumberItems: int, AreaName: Array[str], LoadPat: Array[str], CSys: Array[str], Dir: Array[int], Value: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[str], Array[int], Array[float]) """
        pass

    def GetLoadUniformToFrame(self, Name, NumberItems, AreaName, LoadPat, CSys, Dir, Value, DistType, ItemType):
        """ GetLoadUniformToFrame(self: cAreaObj, Name: str, NumberItems: int, AreaName: Array[str], LoadPat: Array[str], CSys: Array[str], Dir: Array[int], Value: Array[float], DistType: Array[int], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[str], Array[int], Array[float], Array[int]) """
        pass

    def GetLoadWindPressure(self, Name, NumberItems, AreaName, LoadPat, MyType, Cp, ItemType):
        """ GetLoadWindPressure(self: cAreaObj, Name: str, NumberItems: int, AreaName: Array[str], LoadPat: Array[str], MyType: Array[int], Cp: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[int], Array[float]) """
        pass

    def GetLocalAxes(self, Name, Ang, Advanced):
        """ GetLocalAxes(self: cAreaObj, Name: str, Ang: float, Advanced: bool) -> (int, float, bool) """
        pass

    def GetMass(self, Name, MassOverL2):
        """ GetMass(self: cAreaObj, Name: str, MassOverL2: float) -> (int, float) """
        pass

    def GetMaterialOverwrite(self, Name, PropName):
        """ GetMaterialOverwrite(self: cAreaObj, Name: str, PropName: str) -> (int, str) """
        pass

    def GetModifiers(self, Name, Value):
        """ GetModifiers(self: cAreaObj, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def GetNameFromLabel(self, Label, Story, Name):
        """ GetNameFromLabel(self: cAreaObj, Label: str, Story: str, Name: str) -> (int, str) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cAreaObj, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetNameListOnStory(self, StoryName, NumberNames, MyName):
        """ GetNameListOnStory(self: cAreaObj, StoryName: str, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetOffsets3(self, Name, NumberPoints, Offsets):
        """ GetOffsets3(self: cAreaObj, Name: str, NumberPoints: int, Offsets: Array[float]) -> (int, int, Array[float]) """
        pass

    def GetOpening(self, Name, IsOpening):
        """ GetOpening(self: cAreaObj, Name: str, IsOpening: bool) -> (int, bool) """
        pass

    def GetPier(self, Name, PierName):
        """ GetPier(self: cAreaObj, Name: str, PierName: str) -> (int, str) """
        pass

    def GetPoints(self, Name, NumberPoints, Point):
        """ GetPoints(self: cAreaObj, Name: str, NumberPoints: int, Point: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetProperty(self, Name, PropName):
        """ GetProperty(self: cAreaObj, Name: str, PropName: str) -> (int, str) """
        pass

    def GetRebarDataPier(self, Name, NumberRebarLayers, LayerID, LayerType, ClearCover, BarSizeName, BarArea, BarSpacing, NumberBars, Confined, EndZoneLength, EndZoneThickness, EndZoneOffset):
        """ GetRebarDataPier(self: cAreaObj, Name: str, NumberRebarLayers: int, LayerID: Array[str], LayerType: Array[eWallPierRebarLayerType], ClearCover: Array[float], BarSizeName: Array[str], BarArea: Array[float], BarSpacing: Array[float], NumberBars: Array[int], Confined: Array[bool], EndZoneLength: Array[float], EndZoneThickness: Array[float], EndZoneOffset: Array[float]) -> (int, int, Array[str], Array[eWallPierRebarLayerType], Array[float], Array[str], Array[float], Array[float], Array[int], Array[bool], Array[float], Array[float], Array[float]) """
        pass

    def GetRebarDataSpandrel(self, Name, NumberRebarLayers, LayerID, LayerType, ClearCover, BarSizeIndex, BarArea, BarSpacing, NumberBars, Confined):
        """ GetRebarDataSpandrel(self: cAreaObj, Name: str, NumberRebarLayers: int, LayerID: Array[str], LayerType: Array[eWallSpandrelRebarLayerType], ClearCover: Array[float], BarSizeIndex: Array[int], BarArea: Array[float], BarSpacing: Array[float], NumberBars: Array[int], Confined: Array[bool]) -> (int, int, Array[str], Array[eWallSpandrelRebarLayerType], Array[float], Array[int], Array[float], Array[float], Array[int], Array[bool]) """
        pass

    def GetSelected(self, Name, Selected):
        """ GetSelected(self: cAreaObj, Name: str, Selected: bool) -> (int, bool) """
        pass

    def GetSelectedEdge(self, Name, NumberEdges, Selected):
        """ GetSelectedEdge(self: cAreaObj, Name: str, NumberEdges: int, Selected: Array[bool]) -> (int, int, Array[bool]) """
        pass

    def GetSpandrel(self, Name, SpandrelName):
        """ GetSpandrel(self: cAreaObj, Name: str, SpandrelName: str) -> (int, str) """
        pass

    def GetSpringAssignment(self, Name, SpringProp):
        """ GetSpringAssignment(self: cAreaObj, Name: str, SpringProp: str) -> (int, str) """
        pass

    def GetTransformationMatrix(self, Name, Value, IsGlobal):
        """ GetTransformationMatrix(self: cAreaObj, Name: str, Value: Array[float], IsGlobal: bool) -> (int, Array[float]) """
        pass

    def SetDiaphragm(self, Name, DiaphragmName):
        """ SetDiaphragm(self: cAreaObj, Name: str, DiaphragmName: str) -> int """
        pass

    def SetEdgeConstraint(self, Name, ConstraintExists, ItemType):
        """ SetEdgeConstraint(self: cAreaObj, Name: str, ConstraintExists: bool, ItemType: eItemType) -> int """
        pass

    def SetGroupAssign(self, Name, GroupName, Remove, ItemType):
        """ SetGroupAssign(self: cAreaObj, Name: str, GroupName: str, Remove: bool, ItemType: eItemType) -> int """
        pass

    def SetGUID(self, Name, GUID):
        """ SetGUID(self: cAreaObj, Name: str, GUID: str) -> int """
        pass

    def SetLoadTemperature(self, Name, LoadPat, MyType, Value, PatternName, Replace, ItemType):
        """ SetLoadTemperature(self: cAreaObj, Name: str, LoadPat: str, MyType: int, Value: float, PatternName: str, Replace: bool, ItemType: eItemType) -> int """
        pass

    def SetLoadUniform(self, Name, LoadPat, Value, Dir, Replace, CSys, ItemType):
        """ SetLoadUniform(self: cAreaObj, Name: str, LoadPat: str, Value: float, Dir: int, Replace: bool, CSys: str, ItemType: eItemType) -> int """
        pass

    def SetLoadUniformToFrame(self, Name, LoadPat, Value, Dir, DistType, Replace, CSys, ItemType):
        """ SetLoadUniformToFrame(self: cAreaObj, Name: str, LoadPat: str, Value: float, Dir: int, DistType: int, Replace: bool, CSys: str, ItemType: eItemType) -> int """
        pass

    def SetLoadWindPressure(self, Name, LoadPat, MyType, Cp, ItemType):
        """ SetLoadWindPressure(self: cAreaObj, Name: str, LoadPat: str, MyType: int, Cp: float, ItemType: eItemType) -> int """
        pass

    def SetLocalAxes(self, Name, Ang, ItemType):
        """ SetLocalAxes(self: cAreaObj, Name: str, Ang: float, ItemType: eItemType) -> int """
        pass

    def SetMass(self, Name, MassOverL2, Replace, ItemType):
        """ SetMass(self: cAreaObj, Name: str, MassOverL2: float, Replace: bool, ItemType: eItemType) -> int """
        pass

    def SetMaterialOverwrite(self, Name, PropName, ItemType):
        """ SetMaterialOverwrite(self: cAreaObj, Name: str, PropName: str, ItemType: eItemType) -> int """
        pass

    def SetModifiers(self, Name, Value, ItemType):
        """ SetModifiers(self: cAreaObj, Name: str, Value: Array[float], ItemType: eItemType) -> (int, Array[float]) """
        pass

    def SetOpening(self, Name, IsOpening, ItemType):
        """ SetOpening(self: cAreaObj, Name: str, IsOpening: bool, ItemType: eItemType) -> int """
        pass

    def SetPier(self, Name, PierName, ItemType):
        """ SetPier(self: cAreaObj, Name: str, PierName: str, ItemType: eItemType) -> int """
        pass

    def SetProperty(self, Name, PropName, ItemType):
        """ SetProperty(self: cAreaObj, Name: str, PropName: str, ItemType: eItemType) -> int """
        pass

    def SetSelected(self, Name, Selected, ItemType):
        """ SetSelected(self: cAreaObj, Name: str, Selected: bool, ItemType: eItemType) -> int """
        pass

    def SetSelectedEdge(self, Name, EdgeNum, Selected):
        """ SetSelectedEdge(self: cAreaObj, Name: str, EdgeNum: int, Selected: bool) -> int """
        pass

    def SetSpandrel(self, Name, SpandrelName, ItemType):
        """ SetSpandrel(self: cAreaObj, Name: str, SpandrelName: str, ItemType: eItemType) -> int """
        pass

    def SetSpringAssignment(self, Name, SpringProp, ItemType):
        """ SetSpringAssignment(self: cAreaObj, Name: str, SpringProp: str, ItemType: eItemType) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cAutoSeismic:
    # no doc
    def GetIBC2006(self, Name, DirFlag, Eccen, PeriodFlag, CtType, UserT, UserZ, TopZ, BottomZ, R, Omega, Cd, I, IBC2006Option, Latitude, Longitude, ZipCode, Ss, S1, Tl, SiteClass, Fa, Fv):
        """ GetIBC2006(self: cAutoSeismic, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CtType: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, R: float, Omega: float, Cd: float, I: float, IBC2006Option: int, Latitude: float, Longitude: float, ZipCode: str, Ss: float, S1: float, Tl: float, SiteClass: int, Fa: float, Fv: float) -> (int, int, float, int, int, float, bool, float, float, float, float, float, float, int, float, float, str, float, float, float, int, float, float) """
        pass

    def SetIBC2006(self, Name, DirFlag, Eccen, PeriodFlag, CtType, UserT, UserZ, TopZ, BottomZ, R, Omega, Cd, I, IBC2006Option, Latitude, Longitude, ZipCode, Ss, S1, Tl, SiteClass, Fa, Fv):
        """ SetIBC2006(self: cAutoSeismic, Name: str, DirFlag: int, Eccen: float, PeriodFlag: int, CtType: int, UserT: float, UserZ: bool, TopZ: float, BottomZ: float, R: float, Omega: float, Cd: float, I: float, IBC2006Option: int, Latitude: float, Longitude: float, ZipCode: str, Ss: float, S1: float, Tl: float, SiteClass: int, Fa: float, Fv: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cAutoWind:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cAutoWindBridge:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseBuckling:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseDirectHistoryLinear:
    # no doc
    def GetLoads(self, Name, NumberLoads, LoadType, LoadName, Func, SF, Tf, At, CSys, Ang):
        """ GetLoads(self: cCaseDirectHistoryLinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], Func: Array[str], SF: Array[float], Tf: Array[float], At: Array[float], CSys: Array[str], Ang: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[str], Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseDirectHistoryNonlinear:
    # no doc
    def GetLoads(self, Name, NumberLoads, LoadType, LoadName, Func, SF, Tf, At, CSys, Ang):
        """ GetLoads(self: cCaseDirectHistoryNonlinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], Func: Array[str], SF: Array[float], Tf: Array[float], At: Array[float], CSys: Array[str], Ang: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[str], Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseHyperStatic:
    # no doc
    def GetBaseCase(self, Name, HyperStaticCase):
        """ GetBaseCase(self: cCaseHyperStatic, Name: str, HyperStaticCase: str) -> (int, str) """
        pass

    def SetBaseCase(self, Name, HyperStaticCase):
        """ SetBaseCase(self: cCaseHyperStatic, Name: str, HyperStaticCase: str) -> int """
        pass

    def SetCase(self, Name):
        """ SetCase(self: cCaseHyperStatic, Name: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseModalEigen:
    # no doc
    def GetInitialCase(self, Name, InitialCase):
        """ GetInitialCase(self: cCaseModalEigen, Name: str, InitialCase: str) -> (int, str) """
        pass

    def GetLoads(self, Name, NumberLoads, LoadType, LoadName, TargetPar, StaticCorrect):
        """ GetLoads(self: cCaseModalEigen, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], TargetPar: Array[float], StaticCorrect: Array[bool]) -> (int, int, Array[str], Array[str], Array[float], Array[bool]) """
        pass

    def GetNumberModes(self, Name, MaxModes, MinModes):
        """ GetNumberModes(self: cCaseModalEigen, Name: str, MaxModes: int, MinModes: int) -> (int, int, int) """
        pass

    def GetParameters(self, Name, EigenShiftFreq, EigenCutOff, EigenTol, AllowAutoFreqShift):
        """ GetParameters(self: cCaseModalEigen, Name: str, EigenShiftFreq: float, EigenCutOff: float, EigenTol: float, AllowAutoFreqShift: int) -> (int, float, float, float, int) """
        pass

    def SetCase(self, Name):
        """ SetCase(self: cCaseModalEigen, Name: str) -> int """
        pass

    def SetInitialCase(self, Name, InitialCase):
        """ SetInitialCase(self: cCaseModalEigen, Name: str, InitialCase: str) -> int """
        pass

    def SetLoads(self, Name, NumberLoads, LoadType, LoadName, TargetPar, StaticCorrect):
        """ SetLoads(self: cCaseModalEigen, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], TargetPar: Array[float], StaticCorrect: Array[bool]) -> (int, Array[str], Array[str], Array[float], Array[bool]) """
        pass

    def SetNumberModes(self, Name, MaxModes, MinModes):
        """ SetNumberModes(self: cCaseModalEigen, Name: str, MaxModes: int, MinModes: int) -> int """
        pass

    def SetParameters(self, Name, EigenShiftFreq, EigenCutOff, EigenTol, AllowAutoFreqShift):
        """ SetParameters(self: cCaseModalEigen, Name: str, EigenShiftFreq: float, EigenCutOff: float, EigenTol: float, AllowAutoFreqShift: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseModalHistoryLinear:
    # no doc
    def GetLoads(self, Name, NumberLoads, LoadType, LoadName, Func, SF, Tf, At, CSys, Ang):
        """ GetLoads(self: cCaseModalHistoryLinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], Func: Array[str], SF: Array[float], Tf: Array[float], At: Array[float], CSys: Array[str], Ang: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[str], Array[float]) """
        pass

    def SetCase(self, Name):
        """ SetCase(self: cCaseModalHistoryLinear, Name: str) -> int """
        pass

    def SetLoads(self, Name, NumberLoads, LoadType, LoadName, Func, SF, Tf, At, CSys, Ang):
        """ SetLoads(self: cCaseModalHistoryLinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], Func: Array[str], SF: Array[float], Tf: Array[float], At: Array[float], CSys: Array[str], Ang: Array[float]) -> (int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[str], Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseModalHistoryNonlinear:
    # no doc
    def GetLoads(self, Name, NumberLoads, LoadType, LoadName, Func, SF, Tf, At, CSys, Ang):
        """ GetLoads(self: cCaseModalHistoryNonlinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], Func: Array[str], SF: Array[float], Tf: Array[float], At: Array[float], CSys: Array[str], Ang: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[str], Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseModalRitz:
    # no doc
    def GetInitialCase(self, Name, InitialCase):
        """ GetInitialCase(self: cCaseModalRitz, Name: str, InitialCase: str) -> (int, str) """
        pass

    def GetLoads(self, Name, NumberLoads, LoadType, LoadName, RitzMaxCyc, TargetPar):
        """ GetLoads(self: cCaseModalRitz, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], RitzMaxCyc: Array[int], TargetPar: Array[float]) -> (int, int, Array[str], Array[str], Array[int], Array[float]) """
        pass

    def GetNumberModes(self, Name, MaxModes, MinModes):
        """ GetNumberModes(self: cCaseModalRitz, Name: str, MaxModes: int, MinModes: int) -> (int, int, int) """
        pass

    def SetCase(self, Name):
        """ SetCase(self: cCaseModalRitz, Name: str) -> int """
        pass

    def SetInitialCase(self, Name, InitialCase):
        """ SetInitialCase(self: cCaseModalRitz, Name: str, InitialCase: str) -> int """
        pass

    def SetLoads(self, Name, NumberLoads, LoadType, LoadName, RitzMaxCyc, TargetPar):
        """ SetLoads(self: cCaseModalRitz, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], RitzMaxCyc: Array[int], TargetPar: Array[float]) -> (int, Array[str], Array[str], Array[int], Array[float]) """
        pass

    def SetNumberModes(self, Name, MaxModes, MinModes):
        """ SetNumberModes(self: cCaseModalRitz, Name: str, MaxModes: int, MinModes: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseResponseSpectrum:
    # no doc
    def GetDampConstant(self, Name, Damp):
        """ GetDampConstant(self: cCaseResponseSpectrum, Name: str, Damp: float) -> (int, float) """
        pass

    def GetDampInterpolated(self, Name, DampType, NumberItems, Time, Damp):
        """ GetDampInterpolated(self: cCaseResponseSpectrum, Name: str, DampType: int, NumberItems: int, Time: Array[float], Damp: Array[float]) -> (int, int, int, Array[float], Array[float]) """
        pass

    def GetDampOverrides(self, Name, NumberItems, Mode, Damp):
        """ GetDampOverrides(self: cCaseResponseSpectrum, Name: str, NumberItems: int, Mode: Array[int], Damp: Array[float]) -> (int, int, Array[int], Array[float]) """
        pass

    def GetDampProportional(self, Name, DampType, DampA, DampB, DampF1, DampF2, DampD1, DampD2):
        """ GetDampProportional(self: cCaseResponseSpectrum, Name: str, DampType: int, DampA: float, DampB: float, DampF1: float, DampF2: float, DampD1: float, DampD2: float) -> (int, int, float, float, float, float, float, float) """
        pass

    def GetDampType(self, Name, DampType):
        """ GetDampType(self: cCaseResponseSpectrum, Name: str, DampType: int) -> (int, int) """
        pass

    def GetDiaphragmEccentricityOverride(self, Name, Num, Diaph, Eccen):
        """ GetDiaphragmEccentricityOverride(self: cCaseResponseSpectrum, Name: str, Num: int, Diaph: Array[str], Eccen: Array[float]) -> (int, int, Array[str], Array[float]) """
        pass

    def GetDirComb(self, Name, MyType, SF):
        """ GetDirComb(self: cCaseResponseSpectrum, Name: str, MyType: int, SF: float) -> (int, int, float) """
        pass

    def GetEccentricity(self, Name, Eccen):
        """ GetEccentricity(self: cCaseResponseSpectrum, Name: str, Eccen: float) -> (int, float) """
        pass

    def GetLoads(self, Name, NumberLoads, LoadName, Func, SF, CSys, Ang):
        """ GetLoads(self: cCaseResponseSpectrum, Name: str, NumberLoads: int, LoadName: Array[str], Func: Array[str], SF: Array[float], CSys: Array[str], Ang: Array[float]) -> (int, int, Array[str], Array[str], Array[float], Array[str], Array[float]) """
        pass

    def GetModalCase(self, Name, ModalCase):
        """ GetModalCase(self: cCaseResponseSpectrum, Name: str, ModalCase: str) -> (int, str) """
        pass

    def GetModalComb(self, Name, MyType, F1, F2, Td):
        """ GetModalComb(self: cCaseResponseSpectrum, Name: str, MyType: int, F1: float, F2: float, Td: float) -> (int, int, float, float, float) """
        pass

    def GetModalComb_1(self, Name, MyType, F1, F2, PeriodicRigidCombType, Td):
        """ GetModalComb_1(self: cCaseResponseSpectrum, Name: str, MyType: int, F1: float, F2: float, PeriodicRigidCombType: int, Td: float) -> (int, int, float, float, int, float) """
        pass

    def SetCase(self, Name):
        """ SetCase(self: cCaseResponseSpectrum, Name: str) -> int """
        pass

    def SetEccentricity(self, Name, Eccen):
        """ SetEccentricity(self: cCaseResponseSpectrum, Name: str, Eccen: float) -> int """
        pass

    def SetLoads(self, Name, NumberLoads, LoadName, Func, SF, CSys, Ang):
        """ SetLoads(self: cCaseResponseSpectrum, Name: str, NumberLoads: int, LoadName: Array[str], Func: Array[str], SF: Array[float], CSys: Array[str], Ang: Array[float]) -> (int, Array[str], Array[str], Array[float], Array[str], Array[float]) """
        pass

    def SetModalCase(self, Name, ModalCase):
        """ SetModalCase(self: cCaseResponseSpectrum, Name: str, ModalCase: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseStaticLinear:
    # no doc
    def GetInitialCase(self, Name, InitialCase):
        """ GetInitialCase(self: cCaseStaticLinear, Name: str, InitialCase: str) -> (int, str) """
        pass

    def GetLoads(self, Name, NumberLoads, LoadType, LoadName, SF):
        """ GetLoads(self: cCaseStaticLinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], SF: Array[float]) -> (int, int, Array[str], Array[str], Array[float]) """
        pass

    def SetCase(self, Name):
        """ SetCase(self: cCaseStaticLinear, Name: str) -> int """
        pass

    def SetInitialCase(self, Name, InitialCase):
        """ SetInitialCase(self: cCaseStaticLinear, Name: str, InitialCase: str) -> int """
        pass

    def SetLoads(self, Name, NumberLoads, LoadType, LoadName, SF):
        """ SetLoads(self: cCaseStaticLinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], SF: Array[float]) -> (int, Array[str], Array[str], Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseStaticNonlinear:
    # no doc
    def GetGeometricNonlinearity(self, Name, NLGeomType):
        """ GetGeometricNonlinearity(self: cCaseStaticNonlinear, Name: str, NLGeomType: int) -> (int, int) """
        pass

    def GetHingeUnloading(self, Name, UnloadType):
        """ GetHingeUnloading(self: cCaseStaticNonlinear, Name: str, UnloadType: int) -> (int, int) """
        pass

    def GetInitialCase(self, Name, InitialCase):
        """ GetInitialCase(self: cCaseStaticNonlinear, Name: str, InitialCase: str) -> (int, str) """
        pass

    def GetLoadApplication(self, Name, LoadControl, DispType, Displ, Monitor, DOF, PointName, GDispl):
        """ GetLoadApplication(self: cCaseStaticNonlinear, Name: str, LoadControl: int, DispType: int, Displ: float, Monitor: int, DOF: int, PointName: str, GDispl: str) -> (int, int, int, float, int, int, str, str) """
        pass

    def GetLoads(self, Name, NumberLoads, LoadType, LoadName, SF):
        """ GetLoads(self: cCaseStaticNonlinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], SF: Array[float]) -> (int, int, Array[str], Array[str], Array[float]) """
        pass

    def GetMassSource(self, Name, mSource):
        """ GetMassSource(self: cCaseStaticNonlinear, Name: str, mSource: str) -> (int, str) """
        pass

    def GetModalCase(self, Name, ModalCase):
        """ GetModalCase(self: cCaseStaticNonlinear, Name: str, ModalCase: str) -> (int, str) """
        pass

    def GetResultsSaved(self, Name, SaveMultipleSteps, MinSavedStates, MaxSavedStates, PositiveOnly):
        """ GetResultsSaved(self: cCaseStaticNonlinear, Name: str, SaveMultipleSteps: bool, MinSavedStates: int, MaxSavedStates: int, PositiveOnly: bool) -> (int, bool, int, int, bool) """
        pass

    def GetSolControlParameters(self, Name, MaxTotalSteps, MaxFailedSubSteps, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact):
        """ GetSolControlParameters(self: cCaseStaticNonlinear, Name: str, MaxTotalSteps: int, MaxFailedSubSteps: int, MaxIterCS: int, MaxIterNR: int, TolConvD: float, UseEventStepping: bool, TolEventD: float, MaxLineSearchPerIter: int, TolLineSearch: float, LineSearchStepFact: float) -> (int, int, int, int, int, float, bool, float, int, float, float) """
        pass

    def GetTargetForceParameters(self, Name, TolConvF, MaxIter, AccelFact, NoStop):
        """ GetTargetForceParameters(self: cCaseStaticNonlinear, Name: str, TolConvF: float, MaxIter: int, AccelFact: float, NoStop: bool) -> (int, float, int, float, bool) """
        pass

    def SetCase(self, Name):
        """ SetCase(self: cCaseStaticNonlinear, Name: str) -> int """
        pass

    def SetGeometricNonlinearity(self, Name, NLGeomType):
        """ SetGeometricNonlinearity(self: cCaseStaticNonlinear, Name: str, NLGeomType: int) -> int """
        pass

    def SetHingeUnloading(self, Name, UnloadType):
        """ SetHingeUnloading(self: cCaseStaticNonlinear, Name: str, UnloadType: int) -> int """
        pass

    def SetInitialCase(self, Name, InitialCase):
        """ SetInitialCase(self: cCaseStaticNonlinear, Name: str, InitialCase: str) -> int """
        pass

    def SetLoadApplication(self, Name, LoadControl, DispType, Displ, Monitor, DOF, PointName, GDispl):
        """ SetLoadApplication(self: cCaseStaticNonlinear, Name: str, LoadControl: int, DispType: int, Displ: float, Monitor: int, DOF: int, PointName: str, GDispl: str) -> int """
        pass

    def SetLoads(self, Name, NumberLoads, LoadType, LoadName, SF):
        """ SetLoads(self: cCaseStaticNonlinear, Name: str, NumberLoads: int, LoadType: Array[str], LoadName: Array[str], SF: Array[float]) -> (int, Array[str], Array[str], Array[float]) """
        pass

    def SetMassSource(self, Name, mSource):
        """ SetMassSource(self: cCaseStaticNonlinear, Name: str, mSource: str) -> int """
        pass

    def SetModalCase(self, Name, ModalCase):
        """ SetModalCase(self: cCaseStaticNonlinear, Name: str, ModalCase: str) -> int """
        pass

    def SetResultsSaved(self, Name, SaveMultipleSteps, MinSavedStates, MaxSavedStates, PositiveOnly):
        """ SetResultsSaved(self: cCaseStaticNonlinear, Name: str, SaveMultipleSteps: bool, MinSavedStates: int, MaxSavedStates: int, PositiveOnly: bool) -> int """
        pass

    def SetSolControlParameters(self, Name, MaxTotalSteps, MaxFailedSubSteps, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact):
        """ SetSolControlParameters(self: cCaseStaticNonlinear, Name: str, MaxTotalSteps: int, MaxFailedSubSteps: int, MaxIterCS: int, MaxIterNR: int, TolConvD: float, UseEventStepping: bool, TolEventD: float, MaxLineSearchPerIter: int, TolLineSearch: float, LineSearchStepFact: float) -> int """
        pass

    def SetTargetForceParameters(self, Name, TolConvF, MaxIter, AccelFact, NoStop):
        """ SetTargetForceParameters(self: cCaseStaticNonlinear, Name: str, TolConvF: float, MaxIter: int, AccelFact: float, NoStop: bool) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCaseStaticNonlinearStaged:
    # no doc
    def GetGeometricNonlinearity(self, Name, NLGeomType):
        """ GetGeometricNonlinearity(self: cCaseStaticNonlinearStaged, Name: str, NLGeomType: int) -> (int, int) """
        pass

    def GetHingeUnloading(self, Name, UnloadType):
        """ GetHingeUnloading(self: cCaseStaticNonlinearStaged, Name: str, UnloadType: int) -> (int, int) """
        pass

    def GetInitialCase(self, Name, InitialCase):
        """ GetInitialCase(self: cCaseStaticNonlinearStaged, Name: str, InitialCase: str) -> (int, str) """
        pass

    def GetMassSource(self, Name, mSource):
        """ GetMassSource(self: cCaseStaticNonlinearStaged, Name: str, mSource: str) -> (int, str) """
        pass

    def GetMaterialNonlinearity(self, Name, TimeDepMatProp):
        """ GetMaterialNonlinearity(self: cCaseStaticNonlinearStaged, Name: str, TimeDepMatProp: bool) -> (int, bool) """
        pass

    def GetResultsSaved(self, Name, StagedSaveOption, StagedMinSteps, StagedMinStepsTD):
        """ GetResultsSaved(self: cCaseStaticNonlinearStaged, Name: str, StagedSaveOption: int, StagedMinSteps: int, StagedMinStepsTD: int) -> (int, int, int, int) """
        pass

    def GetSolControlParameters(self, Name, MaxTotalSteps, MaxFailedSubSteps, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact):
        """ GetSolControlParameters(self: cCaseStaticNonlinearStaged, Name: str, MaxTotalSteps: int, MaxFailedSubSteps: int, MaxIterCS: int, MaxIterNR: int, TolConvD: float, UseEventStepping: bool, TolEventD: float, MaxLineSearchPerIter: int, TolLineSearch: float, LineSearchStepFact: float) -> (int, int, int, int, int, float, bool, float, int, float, float) """
        pass

    def GetStageData(self, Name, Stage, NumberOperations, Operation, GroupName, Age, LoadType, LoadName, SF):
        """ GetStageData(self: cCaseStaticNonlinearStaged, Name: str, Stage: int, NumberOperations: int, Operation: Array[int], GroupName: Array[str], Age: Array[int], LoadType: Array[str], LoadName: Array[str], SF: Array[float]) -> (int, int, int, Array[int], Array[str], Array[int], Array[str], Array[str], Array[float]) """
        pass

    def GetStageData_1(self, Name, Stage, NumberOperations, Operation, ObjectType, ObjectName, Age, MyType, MyName, SF):
        """ GetStageData_1(self: cCaseStaticNonlinearStaged, Name: str, Stage: int, NumberOperations: int, Operation: Array[int], ObjectType: Array[str], ObjectName: Array[str], Age: Array[int], MyType: Array[str], MyName: Array[str], SF: Array[float]) -> (int, int, int, Array[int], Array[str], Array[str], Array[int], Array[str], Array[str], Array[float]) """
        pass

    def GetStageData_2(self, Name, Stage, NumberOperations, Operation, ObjectType, ObjectName, Age, MyType, MyName, SF):
        """ GetStageData_2(self: cCaseStaticNonlinearStaged, Name: str, Stage: int, NumberOperations: int, Operation: Array[int], ObjectType: Array[str], ObjectName: Array[str], Age: Array[float], MyType: Array[str], MyName: Array[str], SF: Array[float]) -> (int, int, int, Array[int], Array[str], Array[str], Array[float], Array[str], Array[str], Array[float]) """
        pass

    def GetStageDefinitions(self, Name, NumberStages, Duration, Comment):
        """ GetStageDefinitions(self: cCaseStaticNonlinearStaged, Name: str, NumberStages: int, Duration: Array[int], Comment: Array[str]) -> (int, int, Array[int], Array[str]) """
        pass

    def GetStageDefinitions_1(self, Name, NumberStages, Duration, Output, OutputName, Comment):
        """ GetStageDefinitions_1(self: cCaseStaticNonlinearStaged, Name: str, NumberStages: int, Duration: Array[int], Output: Array[bool], OutputName: Array[str], Comment: Array[str]) -> (int, int, Array[int], Array[bool], Array[str], Array[str]) """
        pass

    def GetStageDefinitions_2(self, Name, NumberStages, Duration, Output, OutputName, Comment):
        """ GetStageDefinitions_2(self: cCaseStaticNonlinearStaged, Name: str, NumberStages: int, Duration: Array[float], Output: Array[bool], OutputName: Array[str], Comment: Array[str]) -> (int, int, Array[float], Array[bool], Array[str], Array[str]) """
        pass

    def GetTargetForceParameters(self, Name, TolConvF, MaxIter, AccelFact, NoStop):
        """ GetTargetForceParameters(self: cCaseStaticNonlinearStaged, Name: str, TolConvF: float, MaxIter: int, AccelFact: float, NoStop: bool) -> (int, float, int, float, bool) """
        pass

    def SetCase(self, Name):
        """ SetCase(self: cCaseStaticNonlinearStaged, Name: str) -> int """
        pass

    def SetGeometricNonlinearity(self, Name, NLGeomType):
        """ SetGeometricNonlinearity(self: cCaseStaticNonlinearStaged, Name: str, NLGeomType: int) -> int """
        pass

    def SetHingeUnloading(self, Name, UnloadType):
        """ SetHingeUnloading(self: cCaseStaticNonlinearStaged, Name: str, UnloadType: int) -> int """
        pass

    def SetInitialCase(self, Name, InitialCase):
        """ SetInitialCase(self: cCaseStaticNonlinearStaged, Name: str, InitialCase: str) -> int """
        pass

    def SetMassSource(self, Name, mSource):
        """ SetMassSource(self: cCaseStaticNonlinearStaged, Name: str, mSource: str) -> int """
        pass

    def SetMaterialNonlinearity(self, Name, TimeDepMatProp):
        """ SetMaterialNonlinearity(self: cCaseStaticNonlinearStaged, Name: str, TimeDepMatProp: bool) -> int """
        pass

    def SetResultsSaved(self, Name, StagedSaveOption, StagedMinSteps, StagedMinStepsTD):
        """ SetResultsSaved(self: cCaseStaticNonlinearStaged, Name: str, StagedSaveOption: int, StagedMinSteps: int, StagedMinStepsTD: int) -> int """
        pass

    def SetSolControlParameters(self, Name, MaxTotalSteps, MaxFailedSubSteps, MaxIterCS, MaxIterNR, TolConvD, UseEventStepping, TolEventD, MaxLineSearchPerIter, TolLineSearch, LineSearchStepFact):
        """ SetSolControlParameters(self: cCaseStaticNonlinearStaged, Name: str, MaxTotalSteps: int, MaxFailedSubSteps: int, MaxIterCS: int, MaxIterNR: int, TolConvD: float, UseEventStepping: bool, TolEventD: float, MaxLineSearchPerIter: int, TolLineSearch: float, LineSearchStepFact: float) -> int """
        pass

    def SetStageData(self, Name, Stage, NumberOperations, Operation, GroupName, Age, LoadType, LoadName, SF):
        """ SetStageData(self: cCaseStaticNonlinearStaged, Name: str, Stage: int, NumberOperations: int, Operation: Array[int], GroupName: Array[str], Age: Array[int], LoadType: Array[str], LoadName: Array[str], SF: Array[float]) -> (int, Array[int], Array[str], Array[int], Array[str], Array[str], Array[float]) """
        pass

    def SetStageData_1(self, Name, Stage, NumberOperations, Operation, ObjectType, ObjectName, Age, MyType, MyName, SF):
        """ SetStageData_1(self: cCaseStaticNonlinearStaged, Name: str, Stage: int, NumberOperations: int, Operation: Array[int], ObjectType: Array[str], ObjectName: Array[str], Age: Array[int], MyType: Array[str], MyName: Array[str], SF: Array[float]) -> (int, Array[int], Array[str], Array[str], Array[int], Array[str], Array[str], Array[float]) """
        pass

    def SetStageData_2(self, Name, Stage, NumberOperations, Operation, ObjectType, ObjectName, Age, MyType, MyName, SF):
        """ SetStageData_2(self: cCaseStaticNonlinearStaged, Name: str, Stage: int, NumberOperations: int, Operation: Array[int], ObjectType: Array[str], ObjectName: Array[str], Age: Array[float], MyType: Array[str], MyName: Array[str], SF: Array[float]) -> (int, Array[int], Array[str], Array[str], Array[float], Array[str], Array[str], Array[float]) """
        pass

    def SetStageDefinitions(self, Name, NumberStages, Duration, Comment):
        """ SetStageDefinitions(self: cCaseStaticNonlinearStaged, Name: str, NumberStages: int, Duration: Array[int], Comment: Array[str]) -> (int, Array[int], Array[str]) """
        pass

    def SetStageDefinitions_1(self, Name, NumberStages, Duration, Output, OutputName, Comment):
        """ SetStageDefinitions_1(self: cCaseStaticNonlinearStaged, Name: str, NumberStages: int, Duration: Array[int], Output: Array[bool], OutputName: Array[str], Comment: Array[str]) -> (int, Array[int], Array[bool], Array[str], Array[str]) """
        pass

    def SetStageDefinitions_2(self, Name, NumberStages, Duration, Output, OutputName, Comment):
        """ SetStageDefinitions_2(self: cCaseStaticNonlinearStaged, Name: str, NumberStages: int, Duration: Array[float], Output: Array[bool], OutputName: Array[str], Comment: Array[str]) -> (int, Array[float], Array[bool], Array[str], Array[str]) """
        pass

    def SetTargetForceParameters(self, Name, TolConvF, MaxIter, AccelFact, NoStop):
        """ SetTargetForceParameters(self: cCaseStaticNonlinearStaged, Name: str, TolConvF: float, MaxIter: int, AccelFact: float, NoStop: bool) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cCombo:
    # no doc
    def Add(self, Name, ComboType):
        """ Add(self: cCombo, Name: str, ComboType: int) -> int """
        pass

    def AddDesignDefaultCombos(self, DesignSteel, DesignConcrete, DesignAluminum, DesignColdFormed):
        """ AddDesignDefaultCombos(self: cCombo, DesignSteel: bool, DesignConcrete: bool, DesignAluminum: bool, DesignColdFormed: bool) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cCombo, Name: str) -> int """
        pass

    def DeleteCase(self, Name, CNameType, CName):
        """ DeleteCase(self: cCombo, Name: str, CNameType: eCNameType, CName: str) -> int """
        pass

    def GetCaseList(self, Name, NumberItems, CNameType, CName, SF):
        """ GetCaseList(self: cCombo, Name: str, NumberItems: int, CNameType: Array[eCNameType], CName: Array[str], SF: Array[float]) -> (int, int, Array[eCNameType], Array[str], Array[float]) """
        pass

    def GetCaseList_1(self, Name, NumberItems, CNameType, CName, ModeNumber, SF):
        """ GetCaseList_1(self: cCombo, Name: str, NumberItems: int, CNameType: Array[eCNameType], CName: Array[str], ModeNumber: Array[int], SF: Array[float]) -> (int, int, Array[eCNameType], Array[str], Array[int], Array[float]) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cCombo, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetTypeCombo(self, Name, ComboType):
        """ GetTypeCombo(self: cCombo, Name: str, ComboType: int) -> (int, int) """
        pass

    def GetTypeOAPI(self, name, ComboType):
        """ GetTypeOAPI(self: cCombo, name: str, ComboType: int) -> (int, int) """
        pass

    def SetCaseList(self, Name, CNameType, CName, SF):
        """ SetCaseList(self: cCombo, Name: str, CNameType: eCNameType, CName: str, SF: float) -> (int, eCNameType) """
        pass

    def SetCaseList_1(self, Name, CNameType, CName, ModeNumber, SF):
        """ SetCaseList_1(self: cCombo, Name: str, CNameType: eCNameType, CName: str, ModeNumber: int, SF: float) -> (int, eCNameType) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cConstraint:
    # no doc
    def Delete(self, Name):
        """ Delete(self: cConstraint, Name: str) -> int """
        pass

    def GetDiaphragm(self, Name, Axis, CSys):
        """ GetDiaphragm(self: cConstraint, Name: str, Axis: eConstraintAxis, CSys: str) -> (int, eConstraintAxis, str) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cConstraint, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def SetDiaphragm(self, Name, Axis, CSys):
        """ SetDiaphragm(self: cConstraint, Name: str, Axis: eConstraintAxis, CSys: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDatabaseTables:
    # no doc
    def ApplyEditedTables(self, FillImportLog, NumFatalErrors, NumErrorMsgs, NumWarnMsgs, NumInfoMsgs, ImportLog):
        """ ApplyEditedTables(self: cDatabaseTables, FillImportLog: bool, NumFatalErrors: int, NumErrorMsgs: int, NumWarnMsgs: int, NumInfoMsgs: int, ImportLog: str) -> (int, int, int, int, int, str) """
        pass

    def CancelTableEditing(self):
        """ CancelTableEditing(self: cDatabaseTables) -> int """
        pass

    def GetAllFieldsInTable(self, TableKey, TableVersion, NumberFields, FieldKey, FieldName, Description, UnitsString, IsImportable):
        """ GetAllFieldsInTable(self: cDatabaseTables, TableKey: str, TableVersion: int, NumberFields: int, FieldKey: Array[str], FieldName: Array[str], Description: Array[str], UnitsString: Array[str], IsImportable: Array[bool]) -> (int, int, int, Array[str], Array[str], Array[str], Array[str], Array[bool]) """
        pass

    def GetAllTables(self, NumberTables, TableKey, TableName, ImportType, IsEmpty):
        """ GetAllTables(self: cDatabaseTables, NumberTables: int, TableKey: Array[str], TableName: Array[str], ImportType: Array[int], IsEmpty: Array[bool]) -> (int, int, Array[str], Array[str], Array[int], Array[bool]) """
        pass

    def GetAvailableTables(self, NumberTables, TableKey, TableName, ImportType):
        """ GetAvailableTables(self: cDatabaseTables, NumberTables: int, TableKey: Array[str], TableName: Array[str], ImportType: Array[int]) -> (int, int, Array[str], Array[str], Array[int]) """
        pass

    def GetLoadCasesSelectedForDisplay(self, NumberSelectedLoadCases, LoadCaseList):
        """ GetLoadCasesSelectedForDisplay(self: cDatabaseTables, NumberSelectedLoadCases: int, LoadCaseList: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetLoadCombinationsSelectedForDisplay(self, NumberSelectedLoadCombinations, LoadCombinationList):
        """ GetLoadCombinationsSelectedForDisplay(self: cDatabaseTables, NumberSelectedLoadCombinations: int, LoadCombinationList: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetLoadPatternsSelectedForDisplay(self, NumberSelectedLoadPatterns, LoadPatternList):
        """ GetLoadPatternsSelectedForDisplay(self: cDatabaseTables, NumberSelectedLoadPatterns: int, LoadPatternList: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetObsoleteTableKeyList(self, NumberTableKeys, TableKeyList, NotesList):
        """ GetObsoleteTableKeyList(self: cDatabaseTables, NumberTableKeys: int, TableKeyList: Array[str], NotesList: Array[str]) -> (int, int, Array[str], Array[str]) """
        pass

    def GetOutputOptionsForDisplay(self, IsUserBaseReactionLocation, UserBaseReactionX, UserBaseReactionY, UserBaseReactionZ, IsAllModes, StartMode, EndMode, IsAllBucklingModes, StartBucklingMode, EndBucklingMode, MultistepStatic, NonlinearStatic, ModalHistory, DirectHistory, Combo):
        """ GetOutputOptionsForDisplay(self: cDatabaseTables, IsUserBaseReactionLocation: bool, UserBaseReactionX: float, UserBaseReactionY: float, UserBaseReactionZ: float, IsAllModes: bool, StartMode: int, EndMode: int, IsAllBucklingModes: bool, StartBucklingMode: int, EndBucklingMode: int, MultistepStatic: int, NonlinearStatic: int, ModalHistory: int, DirectHistory: int, Combo: int) -> (int, bool, float, float, float, bool, int, int, bool, int, int, int, int, int, int, int) """
        pass

    def GetTableForDisplayArray(self, TableKey, FieldKeyList, GroupName, TableVersion, FieldsKeysIncluded, NumberRecords, TableData):
        """ GetTableForDisplayArray(self: cDatabaseTables, TableKey: str, FieldKeyList: Array[str], GroupName: str, TableVersion: int, FieldsKeysIncluded: Array[str], NumberRecords: int, TableData: Array[str]) -> (int, Array[str], int, Array[str], int, Array[str]) """
        pass

    def GetTableForDisplayCSVFile(self, TableKey, FieldKeyList, GroupName, TableVersion, csvFilePath, sepChar):
        """ GetTableForDisplayCSVFile(self: cDatabaseTables, TableKey: str, FieldKeyList: Array[str], GroupName: str, TableVersion: int, csvFilePath: str, sepChar: str) -> (int, Array[str], int) """
        pass

    def GetTableForDisplayCSVString(self, TableKey, FieldKeyList, GroupName, TableVersion, csvString, sepChar):
        """ GetTableForDisplayCSVString(self: cDatabaseTables, TableKey: str, FieldKeyList: Array[str], GroupName: str, TableVersion: int, csvString: str, sepChar: str) -> (int, Array[str], int, str) """
        pass

    def GetTableForDisplayXMLString(self, TableKey, FieldKeyList, GroupName, IncludeSchema, TableVersion, XMLTableData):
        """ GetTableForDisplayXMLString(self: cDatabaseTables, TableKey: str, FieldKeyList: Array[str], GroupName: str, IncludeSchema: bool, TableVersion: int, XMLTableData: str) -> (int, Array[str], int, str) """
        pass

    def GetTableForEditingArray(self, TableKey, GroupName, TableVersion, FieldsKeysIncluded, NumberRecords, TableData):
        """ GetTableForEditingArray(self: cDatabaseTables, TableKey: str, GroupName: str, TableVersion: int, FieldsKeysIncluded: Array[str], NumberRecords: int, TableData: Array[str]) -> (int, int, Array[str], int, Array[str]) """
        pass

    def GetTableForEditingCSVFile(self, TableKey, GroupName, TableVersion, csvFilePath, sepChar):
        """ GetTableForEditingCSVFile(self: cDatabaseTables, TableKey: str, GroupName: str, TableVersion: int, csvFilePath: str, sepChar: str) -> (int, int) """
        pass

    def GetTableForEditingCSVString(self, TableKey, GroupName, TableVersion, csvString, sepChar):
        """ GetTableForEditingCSVString(self: cDatabaseTables, TableKey: str, GroupName: str, TableVersion: int, csvString: str, sepChar: str) -> (int, int, str) """
        pass

    def SetLoadCasesSelectedForDisplay(self, LoadCaseList):
        """ SetLoadCasesSelectedForDisplay(self: cDatabaseTables, LoadCaseList: Array[str]) -> (int, Array[str]) """
        pass

    def SetLoadCombinationsSelectedForDisplay(self, LoadCombinationList):
        """ SetLoadCombinationsSelectedForDisplay(self: cDatabaseTables, LoadCombinationList: Array[str]) -> (int, Array[str]) """
        pass

    def SetLoadPatternsSelectedForDisplay(self, LoadPatternList):
        """ SetLoadPatternsSelectedForDisplay(self: cDatabaseTables, LoadPatternList: Array[str]) -> (int, Array[str]) """
        pass

    def SetOutputOptionsForDisplay(self, IsUserBaseReactionLocation, UserBaseReactionX, UserBaseReactionY, UserBaseReactionZ, IsAllModes, StartMode, EndMode, IsAllBucklingModes, StartBucklingMode, EndBucklingMode, MultistepStatic, NonlinearStatic, ModalHistory, DirectHistory, Combo):
        """ SetOutputOptionsForDisplay(self: cDatabaseTables, IsUserBaseReactionLocation: bool, UserBaseReactionX: float, UserBaseReactionY: float, UserBaseReactionZ: float, IsAllModes: bool, StartMode: int, EndMode: int, IsAllBucklingModes: bool, StartBucklingMode: int, EndBucklingMode: int, MultistepStatic: int, NonlinearStatic: int, ModalHistory: int, DirectHistory: int, Combo: int) -> int """
        pass

    def SetTableForEditingArray(self, TableKey, TableVersion, FieldsKeysIncluded, NumberRecords, TableData):
        """ SetTableForEditingArray(self: cDatabaseTables, TableKey: str, TableVersion: int, FieldsKeysIncluded: Array[str], NumberRecords: int, TableData: Array[str]) -> (int, int, Array[str], Array[str]) """
        pass

    def SetTableForEditingCSVFile(self, TableKey, TableVersion, csvFilePath, sepChar):
        """ SetTableForEditingCSVFile(self: cDatabaseTables, TableKey: str, TableVersion: int, csvFilePath: str, sepChar: str) -> (int, int) """
        pass

    def SetTableForEditingCSVString(self, TableKey, TableVersion, csvString, sepChar):
        """ SetTableForEditingCSVString(self: cDatabaseTables, TableKey: str, TableVersion: int, csvString: str, sepChar: str) -> (int, int, str) """
        pass

    def ShowTablesInExcel(self, TableKeyList, WindowHandle):
        """ ShowTablesInExcel(self: cDatabaseTables, TableKeyList: Array[str], WindowHandle: int) -> (int, Array[str]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoACI318_08_IBC2009:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoACI318_08_IBC2009, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoACI318_08_IBC2009, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoACI318_08_IBC2009, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoACI318_08_IBC2009, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoACI318_11:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoACI318_11, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoACI318_11, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoACI318_11, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoACI318_11, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoACI318_14:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoACI318_14, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoACI318_14, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoACI318_14, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoACI318_14, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoACI318_19:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoACI318_19, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoACI318_19, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoACI318_19, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoACI318_19, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoAS_3600_09:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoAS_3600_09, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoAS_3600_09, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoAS_3600_09, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoAS_3600_09, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoAS_3600_2018:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoAS_3600_2018, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoAS_3600_2018, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoAS_3600_2018, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoAS_3600_2018, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoBS8110_97:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoBS8110_97, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoBS8110_97, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoBS8110_97, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoBS8110_97, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoChinese_2010:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoChinese_2010, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoChinese_2010, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoChinese_2010, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoChinese_2010, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoEurocode_2_2004:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoEurocode_2_2004, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoEurocode_2_2004, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoEurocode_2_2004, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoEurocode_2_2004, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoHong_Kong_CP_2013:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoHong_Kong_CP_2013, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoHong_Kong_CP_2013, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoHong_Kong_CP_2013, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoHong_Kong_CP_2013, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoIndian_IS_456_2000:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoIndian_IS_456_2000, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoIndian_IS_456_2000, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoIndian_IS_456_2000, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoIndian_IS_456_2000, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoItalianNTC2008C:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoItalianNTC2008C, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoItalianNTC2008C, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoItalianNTC2008C, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoItalianNTC2008C, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoMexican_RCDF_2004:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoMexican_RCDF_2004, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoMexican_RCDF_2004, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoMexican_RCDF_2004, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoMexican_RCDF_2004, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoMexican_RCDF_2017:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoMexican_RCDF_2017, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoMexican_RCDF_2017, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoMexican_RCDF_2017, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoMexican_RCDF_2017, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDConcShellEurocode_2_2004:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDConcSlabACI318_14:
    # no doc
    def GetPreference(self, Item, textValue, numericValue):
        """ GetPreference(self: cDConcSlabACI318_14, Item: int, textValue: str, numericValue: float) -> (int, str, float) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDConcSlabACI318_19:
    # no doc
    def GetPreference(self, Item, textValue, numericValue):
        """ GetPreference(self: cDConcSlabACI318_19, Item: int, textValue: str, numericValue: float) -> (int, str, float) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoNZS_3101_2006:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoNZS_3101_2006, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoNZS_3101_2006, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoNZS_3101_2006, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoNZS_3101_2006, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoSP63133302011:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoSP63133302011, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoSP63133302011, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoSP63133302011, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoSP63133302011, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoTS_500_2000:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoTS_500_2000, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoTS_500_2000, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoTS_500_2000, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoTS_500_2000, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDCoTS_500_2000_R2018:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDCoTS_500_2000_R2018, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDCoTS_500_2000_R2018, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDCoTS_500_2000_R2018, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDCoTS_500_2000_R2018, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDesignCompositeBeam:
    # no doc
    def DeleteResults(self):
        """ DeleteResults(self: cDesignCompositeBeam) -> int """
        pass

    def GetCode(self, CodeName):
        """ GetCode(self: cDesignCompositeBeam, CodeName: str) -> (int, str) """
        pass

    def GetComboDeflection(self, NumberItems, MyName):
        """ GetComboDeflection(self: cDesignCompositeBeam, NumberItems: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetComboStrength(self, NumberItems, MyName):
        """ GetComboStrength(self: cDesignCompositeBeam, NumberItems: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetDesignSection(self, Name, PropName):
        """ GetDesignSection(self: cDesignCompositeBeam, Name: str, PropName: str) -> (int, str) """
        pass

    def GetGroup(self, NumberItems, MyName):
        """ GetGroup(self: cDesignCompositeBeam, NumberItems: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetResultsAvailable(self):
        """ GetResultsAvailable(self: cDesignCompositeBeam) -> bool """
        pass

    def GetSummaryResults(self, Name, NumberItems, DesignSect, BeamFy, StudDia, StudLayout, BeamShored, BeamCamber, PassFail, ReacLeft, ReacRt, MMaxNeg, MMaxPos, PCC, OverallRatio, StudRatio, StrPMRat, ConstPMRat, StrShrRat, ConShrRat, PCDLDfRat, SDLDfRat, LLDfRat, TotCamDfRat, FreqRat, MDampRat, ItemType):
        """ GetSummaryResults(self: cDesignCompositeBeam, Name: str, NumberItems: int, DesignSect: Array[str], BeamFy: Array[float], StudDia: Array[float], StudLayout: Array[str], BeamShored: Array[bool], BeamCamber: Array[float], PassFail: Array[str], ReacLeft: Array[float], ReacRt: Array[float], MMaxNeg: Array[float], MMaxPos: Array[float], PCC: Array[float], OverallRatio: Array[float], StudRatio: Array[float], StrPMRat: Array[float], ConstPMRat: Array[float], StrShrRat: Array[float], ConShrRat: Array[float], PCDLDfRat: Array[float], SDLDfRat: Array[float], LLDfRat: Array[float], TotCamDfRat: Array[float], FreqRat: Array[float], MDampRat: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[float], Array[float], Array[str], Array[bool], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetTargetDispl(self, NumberItems, LoadCase, Point, Displ, Active):
        """ GetTargetDispl(self: cDesignCompositeBeam, NumberItems: int, LoadCase: Array[str], Point: Array[str], Displ: Array[float], Active: bool) -> (int, int, Array[str], Array[str], Array[float], bool) """
        pass

    def GetTargetPeriod(self, NumberItems, ModalCase, Mode, Period, Active):
        """ GetTargetPeriod(self: cDesignCompositeBeam, NumberItems: int, ModalCase: str, Mode: Array[int], Period: Array[float], Active: bool) -> (int, int, str, Array[int], Array[float], bool) """
        pass

    def ResetOverwrites(self):
        """ ResetOverwrites(self: cDesignCompositeBeam) -> int """
        pass

    def SetAutoSelectNull(self, Name, ItemType):
        """ SetAutoSelectNull(self: cDesignCompositeBeam, Name: str, ItemType: eItemType) -> int """
        pass

    def SetCode(self, CodeName):
        """ SetCode(self: cDesignCompositeBeam, CodeName: str) -> int """
        pass

    def SetComboDeflection(self, Name, Selected):
        """ SetComboDeflection(self: cDesignCompositeBeam, Name: str, Selected: bool) -> int """
        pass

    def SetComboStrength(self, Name, Selected):
        """ SetComboStrength(self: cDesignCompositeBeam, Name: str, Selected: bool) -> int """
        pass

    def SetDesignSection(self, Name, PropName, LastAnalysis, ItemType):
        """ SetDesignSection(self: cDesignCompositeBeam, Name: str, PropName: str, LastAnalysis: bool, ItemType: eItemType) -> int """
        pass

    def SetGroup(self, Name, Selected):
        """ SetGroup(self: cDesignCompositeBeam, Name: str, Selected: bool) -> int """
        pass

    def SetTargetDispl(self, NumberItems, LoadCase, Point, Displ, Active):
        """ SetTargetDispl(self: cDesignCompositeBeam, NumberItems: int, LoadCase: Array[str], Point: Array[str], Displ: Array[float], Active: bool) -> (int, Array[str], Array[str], Array[float]) """
        pass

    def SetTargetPeriod(self, NumberItems, ModalCase, Mode, Period, Active):
        """ SetTargetPeriod(self: cDesignCompositeBeam, NumberItems: int, ModalCase: str, Mode: Array[int], Period: Array[float], Active: bool) -> (int, Array[int], Array[float]) """
        pass

    def StartDesign(self):
        """ StartDesign(self: cDesignCompositeBeam) -> int """
        pass

    def VerifyPassed(self, NumberItems, N1, N2, MyName):
        """ VerifyPassed(self: cDesignCompositeBeam, NumberItems: int, N1: int, N2: int, MyName: Array[str]) -> (int, int, int, int, Array[str]) """
        pass

    def VerifySections(self, NumberItems, MyName):
        """ VerifySections(self: cDesignCompositeBeam, NumberItems: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDesignConcrete:
    # no doc
    def GetCode(self, CodeName):
        """ GetCode(self: cDesignConcrete, CodeName: str) -> (int, str) """
        pass

    def GetDesignSection(self, Name, PropName):
        """ GetDesignSection(self: cDesignConcrete, Name: str, PropName: str) -> (int, str) """
        pass

    def GetRebarPrefsBeam(self, Item, Value):
        """ GetRebarPrefsBeam(self: cDesignConcrete, Item: int, Value: str) -> (int, str) """
        pass

    def GetRebarPrefsColumn(self, Item, Value):
        """ GetRebarPrefsColumn(self: cDesignConcrete, Item: int, Value: str) -> (int, str) """
        pass

    def GetResultsAvailable(self):
        """ GetResultsAvailable(self: cDesignConcrete) -> bool """
        pass

    def GetSeismicFramingType(self, Name, NumberItems, FrameName, FramingType, ItemType):
        """ GetSeismicFramingType(self: cDesignConcrete, Name: str, NumberItems: int, FrameName: Array[str], FramingType: Array[int], ItemType: eItemType) -> (int, int, Array[str], Array[int]) """
        pass

    def GetSummaryResultsBeam(self, Name, NumberItems, FrameName, Location, TopCombo, TopArea, BotCombo, BotArea, VMajorCombo, VMajorArea, TLCombo, TLArea, TTCombo, TTArea, ErrorSummary, WarningSummary, ItemType):
        """ GetSummaryResultsBeam(self: cDesignConcrete, Name: str, NumberItems: int, FrameName: Array[str], Location: Array[float], TopCombo: Array[str], TopArea: Array[float], BotCombo: Array[str], BotArea: Array[float], VMajorCombo: Array[str], VMajorArea: Array[float], TLCombo: Array[str], TLArea: Array[float], TTCombo: Array[str], TTArea: Array[float], ErrorSummary: Array[str], WarningSummary: Array[str], ItemType: eItemType) -> (int, int, Array[str], Array[float], Array[str], Array[float], Array[str], Array[float], Array[str], Array[float], Array[str], Array[float], Array[str], Array[float], Array[str], Array[str]) """
        pass

    def GetSummaryResultsBeam_2(self, Name, NumberItems, FrameName, Location, TopCombo, TopArea, TopAreaReq, TopAreaMin, TopAreaProvided, BotCombo, BotArea, BotAreaReq, BotAreaMin, BotAreaProvided, VmajorCombo, VmajorArea, VmajorAreaReq, VmajorAreaMin, VmajorAreaProvided, TLCombo, TLArea, TTCombo, TTArea, ErrorSummary, WarningSummary, ItemType):
        """ GetSummaryResultsBeam_2(self: cDesignConcrete, Name: str, NumberItems: int, FrameName: Array[str], Location: Array[float], TopCombo: Array[str], TopArea: Array[float], TopAreaReq: Array[float], TopAreaMin: Array[float], TopAreaProvided: Array[float], BotCombo: Array[str], BotArea: Array[float], BotAreaReq: Array[float], BotAreaMin: Array[float], BotAreaProvided: Array[float], VmajorCombo: Array[str], VmajorArea: Array[float], VmajorAreaReq: Array[float], VmajorAreaMin: Array[float], VmajorAreaProvided: Array[float], TLCombo: Array[str], TLArea: Array[float], TTCombo: Array[str], TTArea: Array[float], ErrorSummary: Array[str], WarningSummary: Array[str], ItemType: eItemType) -> (int, int, Array[str], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[str], Array[float], Array[str], Array[str]) """
        pass

    def GetSummaryResultsColumn(self, Name, NumberItems, FrameName, MyOption, Location, PMMCombo, PMMArea, PMMRatio, VMajorCombo, AVMajor, VMinorCombo, AVMinor, ErrorSummary, WarningSummary, ItemType):
        """ GetSummaryResultsColumn(self: cDesignConcrete, Name: str, NumberItems: int, FrameName: Array[str], MyOption: Array[int], Location: Array[float], PMMCombo: Array[str], PMMArea: Array[float], PMMRatio: Array[float], VMajorCombo: Array[str], AVMajor: Array[float], VMinorCombo: Array[str], AVMinor: Array[float], ErrorSummary: Array[str], WarningSummary: Array[str], ItemType: eItemType) -> (int, int, Array[str], Array[int], Array[float], Array[str], Array[float], Array[float], Array[str], Array[float], Array[str], Array[float], Array[str], Array[str]) """
        pass

    def GetSummaryResultsJoint(self, Name, NumberItems, FrameName, LCJSRatioMajor, JSRatioMajor, LCJSRatioMinor, JSRatioMinor, LCBCCRatioMajor, BCCRatioMajor, LCBCCRatioMinor, BCCRatioMinor, ErrorSummary, WarningSummary, ItemType):
        """ GetSummaryResultsJoint(self: cDesignConcrete, Name: str, NumberItems: int, FrameName: Array[str], LCJSRatioMajor: Array[str], JSRatioMajor: Array[float], LCJSRatioMinor: Array[str], JSRatioMinor: Array[float], LCBCCRatioMajor: Array[str], BCCRatioMajor: Array[float], LCBCCRatioMinor: Array[str], BCCRatioMinor: Array[float], ErrorSummary: Array[str], WarningSummary: Array[str], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[float], Array[str], Array[float], Array[str], Array[float], Array[str], Array[float], Array[str], Array[str]) """
        pass

    def SetCode(self, CodeName):
        """ SetCode(self: cDesignConcrete, CodeName: str) -> int """
        pass

    def SetDesignSection(self, Name, PropName, LastAnalysis, ItemType):
        """ SetDesignSection(self: cDesignConcrete, Name: str, PropName: str, LastAnalysis: bool, ItemType: eItemType) -> int """
        pass

    def StartDesign(self):
        """ StartDesign(self: cDesignConcrete) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ACI318_08_IBC2009 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ACI318_08_IBC2009(self: cDesignConcrete) -> cDCoACI318_08_IBC2009

"""

    ACI318_14 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ACI318_14(self: cDesignConcrete) -> cDCoACI318_14

"""

    ACI318_19 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ACI318_19(self: cDesignConcrete) -> cDCoACI318_19

"""

    AS_3600_09 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AS_3600_09(self: cDesignConcrete) -> cDCoAS_3600_09

"""

    AS_3600_2018 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AS_3600_2018(self: cDesignConcrete) -> cDCoAS_3600_2018

"""

    BS8110_97 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BS8110_97(self: cDesignConcrete) -> cDCoBS8110_97

"""

    Chinese_2010 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chinese_2010(self: cDesignConcrete) -> cDCoChinese_2010

"""

    Eurocode_2_2004 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Eurocode_2_2004(self: cDesignConcrete) -> cDCoEurocode_2_2004

"""

    Indian_IS_456_2000 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Indian_IS_456_2000(self: cDesignConcrete) -> cDCoIndian_IS_456_2000

"""

    Mexican_RCDF_2017 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mexican_RCDF_2017(self: cDesignConcrete) -> cDCoMexican_RCDF_2017

"""

    SP63_13330_2012 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SP63_13330_2012(self: cDesignConcrete) -> cDCoSP63133302011

"""

    TS_500_2000_R2018 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TS_500_2000_R2018(self: cDesignConcrete) -> cDCoTS_500_2000_R2018

"""



class cDesignConcreteShell:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDesignConcreteSlab:
    # no doc
    def GetFlexureAndShear(self, StoryName, DesignStripName, Station, ConcWidth, FTopCombo, FTopMoment, FTopArea, FTopAMin, FBotCombo, FBotMoment, FBotArea, FBotAMin, AxialForce, VCombo, VForce, VArea, Status, GlobalX, GlobalY, Layer):
        """ GetFlexureAndShear(self: cDesignConcreteSlab, StoryName: Array[str], DesignStripName: Array[str], Station: Array[float], ConcWidth: Array[float], FTopCombo: Array[str], FTopMoment: Array[float], FTopArea: Array[float], FTopAMin: Array[float], FBotCombo: Array[str], FBotMoment: Array[float], FBotArea: Array[float], FBotAMin: Array[float], AxialForce: Array[float], VCombo: Array[str], VForce: Array[float], VArea: Array[float], Status: Array[str], GlobalX: Array[float], GlobalY: Array[float], Layer: Array[str]) -> (int, Array[str], Array[str], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[str], Array[float], Array[float], Array[str]) """
        pass

    def GetSummaryResultsFlexureAndShear(self, StoryName, DesignStripName, SpanID, Location, FTopCombo, FTopMoment, FTopArea, FBotCombo, FBotMoment, FBotArea, VCombo, VForce, VArea, Status, Layer):
        """ GetSummaryResultsFlexureAndShear(self: cDesignConcreteSlab, StoryName: Array[str], DesignStripName: Array[str], SpanID: Array[str], Location: Array[str], FTopCombo: Array[str], FTopMoment: Array[float], FTopArea: Array[float], FBotCombo: Array[str], FBotMoment: Array[float], FBotArea: Array[float], VCombo: Array[str], VForce: Array[float], VArea: Array[float], Status: Array[str], Layer: Array[str]) -> (int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[str], Array[float], Array[float], Array[str], Array[float], Array[float], Array[str], Array[str]) """
        pass

    def GetSummaryResultsSpanDefinition(self, StoryName, DesignStripName, SpanID, SpanLength, StartDist, EndDist, GlobalX1, GlobalY1, GlobalX2, GlobalY2):
        """ GetSummaryResultsSpanDefinition(self: cDesignConcreteSlab, StoryName: Array[str], DesignStripName: Array[str], SpanID: Array[str], SpanLength: Array[float], StartDist: Array[float], EndDist: Array[float], GlobalX1: Array[float], GlobalY1: Array[float], GlobalX2: Array[float], GlobalY2: Array[float]) -> (int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def StartSlabDesign(self):
        """ StartSlabDesign(self: cDesignConcreteSlab) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ACI318_14 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ACI318_14(self: cDesignConcreteSlab) -> cDConcSlabACI318_14

"""

    DesignStrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignStrip(self: cDesignConcreteSlab) -> cDesignStrip

"""



class cDesignForces:
    # no doc
    def BeamDesignForces(self, Name, NumberResults, FrameName, ComboName, Station, P, V2, V3, T, M2, M3, ItemType):
        """ BeamDesignForces(self: cDesignForces, Name: str, NumberResults: int, FrameName: Array[str], ComboName: Array[str], Station: Array[float], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def BraceDesignForces(self, Name, NumberResults, FrameName, ComboName, Station, P, V2, V3, T, M2, M3, ItemType):
        """ BraceDesignForces(self: cDesignForces, Name: str, NumberResults: int, FrameName: Array[str], ComboName: Array[str], Station: Array[float], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def ColumnDesignForces(self, Name, NumberResults, FrameName, ComboName, Station, P, V2, V3, T, M2, M3, ItemType):
        """ ColumnDesignForces(self: cDesignForces, Name: str, NumberResults: int, FrameName: Array[str], ComboName: Array[str], Station: Array[float], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def PierDesignForces(self, InputPierLabel, InputStoryName, NumberResults, Story, PierLabel, ComboName, Location, P, V2, V3, T, M2, M3):
        """ PierDesignForces(self: cDesignForces, InputPierLabel: str, InputStoryName: str, NumberResults: int, Story: Array[str], PierLabel: Array[str], ComboName: Array[str], Location: Array[str], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SpandrelDesignForces(self, InputSpandrelLabel, InputStoryName, NumberResults, Story, SpandrelLabel, ComboName, Location, P, V2, V3, T, M2, M3):
        """ SpandrelDesignForces(self: cDesignForces, InputSpandrelLabel: str, InputStoryName: str, NumberResults: int, Story: Array[str], SpandrelLabel: Array[str], ComboName: Array[str], Location: Array[str], P: Array[float], V2: Array[float], V3: Array[float], T: Array[float], M2: Array[float], M3: Array[float]) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDesignResults:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DesignForces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignForces(self: cDesignResults) -> cDesignForces

"""



class cDesignShearWall:
    # no doc
    def GetPierSummaryResults(self, Story, PierLabel, Station, DesignType, PierSecType, EdgeBar, EndBar, BarSpacing, ReinfPercent, CurrPercent, DCRatio, PierLeg, LegX1, LegY1, LegX2, LegY2, EdgeLeft, EdgeRight, AsLeft, AsRight, ShearAv, StressCompLeft, StressCompRight, StressLimitLeft, StressLimitRight, CDepthLeft, CLimitLeft, CDepthRight, CLimitRight, InelasticRotDemand, InelasticRotCapacity, NormCompStress, NormCompStressLimit, CDepth, BZoneL, BZoneR, BZoneLength, WarnMsg, ErrMsg):
        """ GetPierSummaryResults(self: cDesignShearWall, Story: Array[str], PierLabel: Array[str], Station: Array[str], DesignType: Array[str], PierSecType: Array[str], EdgeBar: Array[str], EndBar: Array[str], BarSpacing: Array[float], ReinfPercent: Array[float], CurrPercent: Array[float], DCRatio: Array[float], PierLeg: Array[str], LegX1: Array[float], LegY1: Array[float], LegX2: Array[float], LegY2: Array[float], EdgeLeft: Array[float], EdgeRight: Array[float], AsLeft: Array[float], AsRight: Array[float], ShearAv: Array[float], StressCompLeft: Array[float], StressCompRight: Array[float], StressLimitLeft: Array[float], StressLimitRight: Array[float], CDepthLeft: Array[float], CLimitLeft: Array[float], CDepthRight: Array[float], CLimitRight: Array[float], InelasticRotDemand: Array[float], InelasticRotCapacity: Array[float], NormCompStress: Array[float], NormCompStressLimit: Array[float], CDepth: Array[float], BZoneL: Array[float], BZoneR: Array[float], BZoneLength: Array[float], WarnMsg: Array[str], ErrMsg: Array[str]) -> (int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[str], Array[str]) """
        pass

    def GetRebar(self, AreaObjName, StoryName, PierLabel, StationLocation, LegID, LeftX1, LeftY1, RightX2, RightY2, Length, Thickness, fc, fy, fys, Flexural, ShearAndConfinement):
        """ GetRebar(self: cDesignShearWall, AreaObjName: Array[str], StoryName: Array[str], PierLabel: Array[str], StationLocation: Array[str], LegID: Array[str], LeftX1: Array[float], LeftY1: Array[float], RightX2: Array[float], RightY2: Array[float], Length: Array[float], Thickness: Array[float], fc: Array[float], fy: Array[float], fys: Array[float], Flexural: Array[str], ShearAndConfinement: Array[str]) -> (int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[str], Array[str]) """
        pass

    def GetRebarPrefsPier(self, Item, Value):
        """ GetRebarPrefsPier(self: cDesignShearWall, Item: int, Value: str) -> (int, str) """
        pass

    def GetRebarPrefsSpandrel(self, Item, Value):
        """ GetRebarPrefsSpandrel(self: cDesignShearWall, Item: int, Value: str) -> (int, str) """
        pass

    def GetSpandrelSummaryResults(self, Story, Spandrel, Station, TopRebar, TopRebarRatio, TopRebarCombo, MuTop, BotRebar, BotRebarRatio, BotRebarCombo, MuBot, AVert, AHorz, ShearCombo, Vu, ADiag, ShearDiagCombo, VuDiag, WarnMsg, ErrMsg):
        """ GetSpandrelSummaryResults(self: cDesignShearWall, Story: Array[str], Spandrel: Array[str], Station: Array[str], TopRebar: Array[float], TopRebarRatio: Array[float], TopRebarCombo: Array[str], MuTop: Array[float], BotRebar: Array[float], BotRebarRatio: Array[float], BotRebarCombo: Array[str], MuBot: Array[float], AVert: Array[float], AHorz: Array[float], ShearCombo: Array[str], Vu: Array[float], ADiag: Array[float], ShearDiagCombo: Array[str], VuDiag: Array[float], WarnMsg: Array[str], ErrMsg: Array[str]) -> (int, Array[str], Array[str], Array[str], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[str], Array[float], Array[str], Array[str]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDesignSteel:
    # no doc
    def DeleteResults(self):
        """ DeleteResults(self: cDesignSteel) -> int """
        pass

    def GetCode(self, CodeName):
        """ GetCode(self: cDesignSteel, CodeName: str) -> (int, str) """
        pass

    def GetComboDeflection(self, NumberItems, MyName):
        """ GetComboDeflection(self: cDesignSteel, NumberItems: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetComboStrength(self, NumberItems, MyName):
        """ GetComboStrength(self: cDesignSteel, NumberItems: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetDesignSection(self, Name, PropName):
        """ GetDesignSection(self: cDesignSteel, Name: str, PropName: str) -> (int, str) """
        pass

    def GetGroup(self, NumberItems, MyName):
        """ GetGroup(self: cDesignSteel, NumberItems: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetResultsAvailable(self):
        """ GetResultsAvailable(self: cDesignSteel) -> bool """
        pass

    def GetSummaryResults(self, Name, NumberItems, FrameName, Ratio, RatioType, Location, ComboName, ErrorSummary, WarningSummary, ItemType):
        """ GetSummaryResults(self: cDesignSteel, Name: str, NumberItems: int, FrameName: Array[str], Ratio: Array[float], RatioType: Array[int], Location: Array[float], ComboName: Array[str], ErrorSummary: Array[str], WarningSummary: Array[str], ItemType: eItemType) -> (int, int, Array[str], Array[float], Array[int], Array[float], Array[str], Array[str], Array[str]) """
        pass

    def GetSummaryResults_2(self, Name, NumberItems, FrameType, DesignSect, Status, PMMCombo, PMMRatio, PRatio, MMajRatio, MMinRatio, VMajCombo, VMajRatio, VMinCombo, VMinRatio, ItemType):
        """ GetSummaryResults_2(self: cDesignSteel, Name: str, NumberItems: int, FrameType: Array[str], DesignSect: Array[str], Status: Array[str], PMMCombo: Array[str], PMMRatio: Array[float], PRatio: Array[float], MMajRatio: Array[float], MMinRatio: Array[float], VMajCombo: Array[str], VMajRatio: Array[float], VMinCombo: Array[str], VMinRatio: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[str], Array[float]) """
        pass

    def GetSummaryResults_3(self, Name, NumberItems, FrameName, FrameType, DesignSect, Status, PMMCombo, PMMRatio, PRatio, MMajRatio, MMinRatio, VMajCombo, VMajRatio, VMinCombo, VMinRatio, ItemType):
        """ GetSummaryResults_3(self: cDesignSteel, Name: str, NumberItems: int, FrameName: Array[str], FrameType: Array[eFrameDesignOrientation], DesignSect: Array[str], Status: Array[str], PMMCombo: Array[str], PMMRatio: Array[float], PRatio: Array[float], MMajRatio: Array[float], MMinRatio: Array[float], VMajCombo: Array[str], VMajRatio: Array[float], VMinCombo: Array[str], VMinRatio: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[eFrameDesignOrientation], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[str], Array[float]) """
        pass

    def GetTargetDispl(self, NumberItems, LoadCase, Point, Displ, Active):
        """ GetTargetDispl(self: cDesignSteel, NumberItems: int, LoadCase: Array[str], Point: Array[str], Displ: Array[float], Active: bool) -> (int, int, Array[str], Array[str], Array[float], bool) """
        pass

    def GetTargetPeriod(self, NumberItems, ModalCase, Mode, Period, Active):
        """ GetTargetPeriod(self: cDesignSteel, NumberItems: int, ModalCase: str, Mode: Array[int], Period: Array[float], Active: bool) -> (int, int, str, Array[int], Array[float], bool) """
        pass

    def ResetOverwrites(self):
        """ ResetOverwrites(self: cDesignSteel) -> int """
        pass

    def SetAutoSelectNull(self, Name, ItemType):
        """ SetAutoSelectNull(self: cDesignSteel, Name: str, ItemType: eItemType) -> int """
        pass

    def SetCode(self, CodeName):
        """ SetCode(self: cDesignSteel, CodeName: str) -> int """
        pass

    def SetComboDeflection(self, Name, Selected):
        """ SetComboDeflection(self: cDesignSteel, Name: str, Selected: bool) -> int """
        pass

    def SetComboStrength(self, Name, Selected):
        """ SetComboStrength(self: cDesignSteel, Name: str, Selected: bool) -> int """
        pass

    def SetDesignSection(self, Name, PropName, LastAnalysis, ItemType):
        """ SetDesignSection(self: cDesignSteel, Name: str, PropName: str, LastAnalysis: bool, ItemType: eItemType) -> int """
        pass

    def SetGroup(self, Name, Selected):
        """ SetGroup(self: cDesignSteel, Name: str, Selected: bool) -> int """
        pass

    def SetTargetDispl(self, NumberItems, LoadCase, Point, Displ, Active):
        """ SetTargetDispl(self: cDesignSteel, NumberItems: int, LoadCase: Array[str], Point: Array[str], Displ: Array[float], Active: bool) -> (int, Array[str], Array[str], Array[float]) """
        pass

    def SetTargetPeriod(self, NumberItems, ModalCase, Mode, Period, Active):
        """ SetTargetPeriod(self: cDesignSteel, NumberItems: int, ModalCase: str, Mode: Array[int], Period: Array[float], Active: bool) -> (int, Array[int], Array[float]) """
        pass

    def StartDesign(self):
        """ StartDesign(self: cDesignSteel) -> int """
        pass

    def VerifyPassed(self, NumberItems, N1, N2, MyName):
        """ VerifyPassed(self: cDesignSteel, NumberItems: int, N1: int, N2: int, MyName: Array[str]) -> (int, int, int, int, Array[str]) """
        pass

    def VerifySections(self, NumberItems, MyName):
        """ VerifySections(self: cDesignSteel, NumberItems: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AISC360_05_IBC2006 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AISC360_05_IBC2006(self: cDesignSteel) -> cDStAISC360_05_IBC2006

"""

    AISC_LRFD93 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AISC_LRFD93(self: cDesignSteel) -> cDStAISC_LRFD93

"""

    Australian_AS4100_98 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Australian_AS4100_98(self: cDesignSteel) -> cDStAustralian_AS4100_98

"""

    BS5950_2000 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BS5950_2000(self: cDesignSteel) -> cDStBS5950_2000

"""

    Canadian_S16_09 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Canadian_S16_09(self: cDesignSteel) -> cDStCanadian_S16_09

"""

    Canadian_S16_14 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Canadian_S16_14(self: cDesignSteel) -> cDStCanadian_S16_14

"""

    Canadian_S16_19 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Canadian_S16_19(self: cDesignSteel) -> cDStCanadian_S16_19

"""

    Chinese_2010 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chinese_2010(self: cDesignSteel) -> cDStChinese_2010

"""

    Chinese_2018 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chinese_2018(self: cDesignSteel) -> cDStChinese_2018

"""

    Eurocode_3_2005 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Eurocode_3_2005(self: cDesignSteel) -> cDStEurocode_3_2005

"""

    Indian_IS_800_2007 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Indian_IS_800_2007(self: cDesignSteel) -> cDStIndian_IS_800_2007

"""

    Italian_NTC_2008 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Italian_NTC_2008(self: cDesignSteel) -> cDStItalianNTC2008S

"""

    Italian_NTC_2018 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Italian_NTC_2018(self: cDesignSteel) -> cDStItalianNTC2018S

"""

    NewZealand_NZS3404_97 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewZealand_NZS3404_97(self: cDesignSteel) -> cDStNewZealand_NZS3404_97

"""

    SP16_13330_2011 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SP16_13330_2011(self: cDesignSteel) -> cDStSP16_13330_2011

"""



class cDesignStrip:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cDesignStrip, Name: str, NewName: str) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cDesignStrip, Name: str) -> int """
        pass

    def GetDesignStrip(self, Name, Point, GlobalX, GlobalY, GlobalZ, WBLeft, WBRight, WALeft, WARight, AutoWiden):
        """ GetDesignStrip(self: cDesignStrip, Name: str, Point: Array[str], GlobalX: Array[float], GlobalY: Array[float], GlobalZ: Array[float], WBLeft: Array[float], WBRight: Array[float], WALeft: Array[float], WARight: Array[float], AutoWiden: Array[bool]) -> (int, Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[bool]) """
        pass

    def GetDesignStrip_1(self, Name, DesignType, Point, GlobalX, GlobalY, GlobalZ, WBLeft, WBRight, WALeft, WARight, AutoWiden):
        """ GetDesignStrip_1(self: cDesignStrip, Name: str, DesignType: int, Point: Array[str], GlobalX: Array[float], GlobalY: Array[float], GlobalZ: Array[float], WBLeft: Array[float], WBRight: Array[float], WALeft: Array[float], WARight: Array[float], AutoWiden: Array[bool]) -> (int, int, Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[bool]) """
        pass

    def GetGUID(self, Name, GUID):
        """ GetGUID(self: cDesignStrip, Name: str, GUID: str) -> (int, str) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cDesignStrip, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def SetGUID(self, Name, GUID):
        """ SetGUID(self: cDesignStrip, Name: str, GUID: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDetailing:
    # no doc
    def ClearDetailing(self):
        """ ClearDetailing(self: cDetailing) -> int """
        pass

    def GetBeamLongRebarData(self, Name, NumberRebarSets, BarSizeName, BarArea, NumberBars, Location, ClearCover, StartCoord1, BarLength, BendingAngleStart, BendingAngleEnd, RebarSetGUID):
        """ GetBeamLongRebarData(self: cDetailing, Name: str, NumberRebarSets: int, BarSizeName: Array[str], BarArea: Array[float], NumberBars: Array[int], Location: Array[str], ClearCover: Array[float], StartCoord1: Array[float], BarLength: Array[float], BendingAngleStart: Array[float], BendingAngleEnd: Array[float], RebarSetGUID: Array[str]) -> (int, int, Array[str], Array[float], Array[int], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[str]) """
        pass

    def GetBeamTieRebarData(self, Name, NumberRebarSets, BarSizeName, BarArea, NumberLegs, Location, ClearCover, StartCoord1, Spacing, Lengths, RebarSetGUID):
        """ GetBeamTieRebarData(self: cDetailing, Name: str, NumberRebarSets: int, BarSizeName: Array[str], BarArea: Array[float], NumberLegs: Array[float], Location: Array[str], ClearCover: Array[float], StartCoord1: Array[float], Spacing: Array[float], Lengths: Array[float], RebarSetGUID: Array[str]) -> (int, int, Array[str], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str]) """
        pass

    def GetColumnLongRebarData(self, Name, NumberRebarSets, BarSizeName, BarArea, NumberCBars, NumberR3Bars, NumberR2Bars, Location, ClearCover, RebarSetGUID):
        """ GetColumnLongRebarData(self: cDetailing, Name: str, NumberRebarSets: int, BarSizeName: Array[str], BarArea: Array[float], NumberCBars: Array[int], NumberR3Bars: Array[int], NumberR2Bars: Array[int], Location: Array[str], ClearCover: Array[float], RebarSetGUID: Array[str]) -> (int, int, Array[str], Array[float], Array[int], Array[int], Array[int], Array[str], Array[float], Array[str]) """
        pass

    def GetColumnTieRebarData(self, Name, NumberRebarSets, BarSizeName, BarArea, Pattern, ConfineType, NumberLegs2Dir, NumberLegs3Dir, Location, ClearCover, StartCoord1, Spacing, Heights, RebarSetGUID):
        """ GetColumnTieRebarData(self: cDetailing, Name: str, NumberRebarSets: int, BarSizeName: Array[str], BarArea: Array[float], Pattern: Array[int], ConfineType: Array[int], NumberLegs2Dir: Array[int], NumberLegs3Dir: Array[int], Location: Array[str], ClearCover: Array[float], StartCoord1: Array[float], Spacing: Array[float], Heights: Array[float], RebarSetGUID: Array[str]) -> (int, int, Array[str], Array[float], Array[int], Array[int], Array[int], Array[int], Array[str], Array[float], Array[float], Array[float], Array[float], Array[str]) """
        pass

    def GetDetailedBeamLineData(self, BeamLineID, ObjectUniqueNames, NumberSpans, SpanLength, NumLongBars, LongBarDiameter, LongBarNotation, LongBarStartDist, LongBarStartBend, LongBarEndBend, LongBarLength, LongBarNumLayers, NumTieBars, NumTieVertLegs, TieBarDiameter, TieBarNotation, TieBarStartDist, TieBarSpacing, TieBarType):
        """ GetDetailedBeamLineData(self: cDetailing, BeamLineID: str, ObjectUniqueNames: Array[str], NumberSpans: int, SpanLength: Array[float], NumLongBars: Array[int], LongBarDiameter: Array[float], LongBarNotation: Array[str], LongBarStartDist: Array[float], LongBarStartBend: Array[int], LongBarEndBend: Array[int], LongBarLength: Array[float], LongBarNumLayers: Array[int], NumTieBars: Array[int], NumTieVertLegs: Array[int], TieBarDiameter: Array[float], TieBarNotation: Array[str], TieBarStartDist: Array[float], TieBarSpacing: Array[float], TieBarType: Array[int]) -> (int, Array[str], int, Array[float], Array[int], Array[float], Array[str], Array[float], Array[int], Array[int], Array[float], Array[int], Array[int], Array[int], Array[float], Array[str], Array[float], Array[float], Array[int]) """
        pass

    def GetDetailedBeamLineData_1(self, BeamLineID, ObjectUniqueNames, NumberSpans, SpanLength, NumLongBars, LongBarGUID, LongBarDiameter, LongBarNotation, LongBarStartDist, LongBarStartBend, LongBarEndBend, LongBarLength, LongBarNumLayers, NumTieBars, NumTieVertLegs, TieBarGUID, TieBarDiameter, TieBarNotation, TieBarStartDist, TieBarSpacing, TieBarType):
        """ GetDetailedBeamLineData_1(self: cDetailing, BeamLineID: str, ObjectUniqueNames: Array[str], NumberSpans: int, SpanLength: Array[float], NumLongBars: Array[int], LongBarGUID: Array[str], LongBarDiameter: Array[float], LongBarNotation: Array[str], LongBarStartDist: Array[float], LongBarStartBend: Array[int], LongBarEndBend: Array[int], LongBarLength: Array[float], LongBarNumLayers: Array[int], NumTieBars: Array[int], NumTieVertLegs: Array[int], TieBarGUID: Array[str], TieBarDiameter: Array[float], TieBarNotation: Array[str], TieBarStartDist: Array[float], TieBarSpacing: Array[float], TieBarType: Array[int]) -> (int, Array[str], int, Array[float], Array[int], Array[str], Array[float], Array[str], Array[float], Array[int], Array[int], Array[float], Array[int], Array[int], Array[int], Array[str], Array[float], Array[str], Array[float], Array[float], Array[int]) """
        pass

    def GetDetailedBeamLineGuidData(self, BeamLineID, SimilarFirstBeamUniqueID, LongitudinalABars, LongitudinalBBars, LongitudinalCBars, LongitudinalDBars, LongitudinalEBars, LongitudinalFBars, LongitudinalGBars, LongitudinalHBars, ZoneATies, ZoneBTies, ZoneCTies):
        """ GetDetailedBeamLineGuidData(self: cDetailing, BeamLineID: str, SimilarFirstBeamUniqueID: str, LongitudinalABars: Array[str], LongitudinalBBars: Array[str], LongitudinalCBars: Array[str], LongitudinalDBars: Array[str], LongitudinalEBars: Array[str], LongitudinalFBars: Array[str], LongitudinalGBars: Array[str], LongitudinalHBars: Array[str], ZoneATies: Array[str], ZoneBTies: Array[str], ZoneCTies: Array[str]) -> (int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[str], Array[str], Array[str], Array[str], Array[str], Array[str]) """
        pass

    def GetDetailedBeamLines(self, NumberItems, BeamLineIDs):
        """ GetDetailedBeamLines(self: cDetailing, NumberItems: int, BeamLineIDs: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetDetailedColumnStackData(self, ColumnStackID, ObjectUniqueNames, NumLongBarSets, NumLongBars, LongBarDiameter, LongBarNotation, LongBarStartDist, LongBarStartBend, LongBarEndBend, LongBarLength, LongBarNumLayers, NumTieZones, TieBarZones, NumTieBars, NumTieVertLegs, TieBarDiameter, TieBarNotation, TieBarStartDist, TieBarSpacing, TieBarType):
        """ GetDetailedColumnStackData(self: cDetailing, ColumnStackID: str, ObjectUniqueNames: Array[str], NumLongBarSets: int, NumLongBars: Array[int], LongBarDiameter: Array[float], LongBarNotation: Array[str], LongBarStartDist: Array[float], LongBarStartBend: Array[int], LongBarEndBend: Array[int], LongBarLength: Array[float], LongBarNumLayers: Array[int], NumTieZones: int, TieBarZones: Array[str], NumTieBars: Array[int], NumTieVertLegs: Array[int], TieBarDiameter: Array[float], TieBarNotation: Array[str], TieBarStartDist: Array[float], TieBarSpacing: Array[float], TieBarType: Array[int]) -> (int, Array[str], int, Array[int], Array[float], Array[str], Array[float], Array[int], Array[int], Array[float], Array[int], int, Array[str], Array[int], Array[int], Array[float], Array[str], Array[float], Array[float], Array[int]) """
        pass

    def GetDetailedColumnStackData_1(self, ColumnStackID, ObjectUniqueNames, NumLongBarSets, NumLongBars, LongBarGUID, LongBarDiameter, LongBarNotation, LongBarStartDist, LongBarStartBend, LongBarEndBend, LongBarLength, LongBarNumLayers, NumTieZones, TieBarZones, NumTieBars, NumTieHorLegs, NumTieVertLegs, TieBarGUID, TieBarDiameter, TieBarNotation, TieBarStartDist, TieBarSpacing, TieBarType):
        """ GetDetailedColumnStackData_1(self: cDetailing, ColumnStackID: str, ObjectUniqueNames: Array[str], NumLongBarSets: int, NumLongBars: Array[int], LongBarGUID: Array[str], LongBarDiameter: Array[float], LongBarNotation: Array[str], LongBarStartDist: Array[float], LongBarStartBend: Array[int], LongBarEndBend: Array[int], LongBarLength: Array[float], LongBarNumLayers: Array[int], NumTieZones: int, TieBarZones: Array[str], NumTieBars: Array[int], NumTieHorLegs: Array[int], NumTieVertLegs: Array[int], TieBarGUID: Array[str], TieBarDiameter: Array[float], TieBarNotation: Array[str], TieBarStartDist: Array[float], TieBarSpacing: Array[float], TieBarType: Array[int]) -> (int, Array[str], int, Array[int], Array[str], Array[float], Array[str], Array[float], Array[int], Array[int], Array[float], Array[int], int, Array[str], Array[int], Array[int], Array[int], Array[str], Array[float], Array[str], Array[float], Array[float], Array[int]) """
        pass

    def GetDetailedColumnStackData_2(self, ColumnStackID, ObjectUniqueNames, NumLongBarSets, NumLongBars, NumLongR2Bars, NumLongR3Bars, LongBarGUID, LongBarDiameter, LongBarNotation, LongBarStartDist, LongBarStartBend, LongBarEndBend, LongBarLength, LongBarNumLayers, NumTieZones, TieBarZone, NumTieBars, NumTieR2Legs, NumTieR3Legs, TieBarGUID, TieBarDiameter, TieBarNotation, TieBarStartDist, TieBarSpacing, TieBarType):
        """ GetDetailedColumnStackData_2(self: cDetailing, ColumnStackID: str, ObjectUniqueNames: Array[str], NumLongBarSets: int, NumLongBars: Array[int], NumLongR2Bars: Array[int], NumLongR3Bars: Array[int], LongBarGUID: Array[str], LongBarDiameter: Array[float], LongBarNotation: Array[str], LongBarStartDist: Array[float], LongBarStartBend: Array[int], LongBarEndBend: Array[int], LongBarLength: Array[float], LongBarNumLayers: Array[int], NumTieZones: int, TieBarZone: Array[str], NumTieBars: Array[int], NumTieR2Legs: Array[int], NumTieR3Legs: Array[int], TieBarGUID: Array[str], TieBarDiameter: Array[float], TieBarNotation: Array[str], TieBarStartDist: Array[float], TieBarSpacing: Array[float], TieBarType: Array[int]) -> (int, Array[str], int, Array[int], Array[int], Array[int], Array[str], Array[float], Array[str], Array[float], Array[int], Array[int], Array[float], Array[int], int, Array[str], Array[int], Array[int], Array[int], Array[str], Array[float], Array[str], Array[float], Array[float], Array[int]) """
        pass

    def GetDetailedColumnStackGuidData(self, ColumnStackID, SimilarFirstColumnUniqueID, LongitudinalBars, TiesA, TiesB, TiesC):
        """ GetDetailedColumnStackGuidData(self: cDetailing, ColumnStackID: str, SimilarFirstColumnUniqueID: str, LongitudinalBars: Array[str], TiesA: Array[str], TiesB: Array[str], TiesC: Array[str]) -> (int, Array[str], Array[str], Array[str], Array[str]) """
        pass

    def GetDetailedColumnStacks(self, NumberItems, ColumnStackIDs):
        """ GetDetailedColumnStacks(self: cDetailing, NumberItems: int, ColumnStackIDs: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetDetailedSlabBotBarData(self, SlabName, NumData, Names, NumBars, BarDiameter, BarNotation, BarMaterial, StartX, StartY, StartZ, EndX, EndY, EndZ, WidthLeft, WidthRight, OffsetFromTop, OffsetFromBot, StartBarBend, EndBarBend, GUIDs):
        """ GetDetailedSlabBotBarData(self: cDetailing, SlabName: str, NumData: int, Names: Array[str], NumBars: Array[int], BarDiameter: Array[float], BarNotation: Array[str], BarMaterial: Array[str], StartX: Array[float], StartY: Array[float], StartZ: Array[float], EndX: Array[float], EndY: Array[float], EndZ: Array[float], WidthLeft: Array[float], WidthRight: Array[float], OffsetFromTop: Array[float], OffsetFromBot: Array[float], StartBarBend: Array[int], EndBarBend: Array[int], GUIDs: Array[str]) -> (int, int, Array[str], Array[int], Array[float], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[int], Array[int], Array[str]) """
        pass

    def GetDetailedSlabBotBarData_1(self, SlabName, NumData, Names, NumBars, BarDiameter, BarNotation, BarMaterial, StartX, StartY, StartZ, EndX, EndY, EndZ, WidthLeft, WidthRight, OffsetFromTop, OffsetFromBot, StartBarBend, EndBarBend, GUIDs, StripNames, SpanNos):
        """ GetDetailedSlabBotBarData_1(self: cDetailing, SlabName: str, NumData: int, Names: Array[str], NumBars: Array[int], BarDiameter: Array[float], BarNotation: Array[str], BarMaterial: Array[str], StartX: Array[float], StartY: Array[float], StartZ: Array[float], EndX: Array[float], EndY: Array[float], EndZ: Array[float], WidthLeft: Array[float], WidthRight: Array[float], OffsetFromTop: Array[float], OffsetFromBot: Array[float], StartBarBend: Array[int], EndBarBend: Array[int], GUIDs: Array[str], StripNames: Array[str], SpanNos: Array[int]) -> (int, int, Array[str], Array[int], Array[float], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[int], Array[int], Array[str], Array[str], Array[int]) """
        pass

    def GetDetailedSlabs(self, NumberItems, Names, SlabElevations, GUIDs):
        """ GetDetailedSlabs(self: cDetailing, NumberItems: int, Names: Array[str], SlabElevations: Array[float], GUIDs: Array[str]) -> (int, int, Array[str], Array[float], Array[str]) """
        pass

    def GetDetailedSlabTopBarData(self, SlabName, NumData, Names, NumBars, BarDiameter, BarNotation, BarMaterial, StartX, StartY, StartZ, EndX, EndY, EndZ, WidthLeft, WidthRight, OffsetFromTop, OffsetFromBot, StartBarBend, EndBarBend, GUIDs):
        """ GetDetailedSlabTopBarData(self: cDetailing, SlabName: str, NumData: int, Names: Array[str], NumBars: Array[int], BarDiameter: Array[float], BarNotation: Array[str], BarMaterial: Array[str], StartX: Array[float], StartY: Array[float], StartZ: Array[float], EndX: Array[float], EndY: Array[float], EndZ: Array[float], WidthLeft: Array[float], WidthRight: Array[float], OffsetFromTop: Array[float], OffsetFromBot: Array[float], StartBarBend: Array[int], EndBarBend: Array[int], GUIDs: Array[str]) -> (int, int, Array[str], Array[int], Array[float], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[int], Array[int], Array[str]) """
        pass

    def GetDetailedSlabTopBarData_1(self, SlabName, NumData, Names, NumBars, BarDiameter, BarNotation, BarMaterial, StartX, StartY, StartZ, EndX, EndY, EndZ, WidthLeft, WidthRight, OffsetFromTop, OffsetFromBot, StartBarBend, EndBarBend, GUIDs, StripNames, SpanNos):
        """ GetDetailedSlabTopBarData_1(self: cDetailing, SlabName: str, NumData: int, Names: Array[str], NumBars: Array[int], BarDiameter: Array[float], BarNotation: Array[str], BarMaterial: Array[str], StartX: Array[float], StartY: Array[float], StartZ: Array[float], EndX: Array[float], EndY: Array[float], EndZ: Array[float], WidthLeft: Array[float], WidthRight: Array[float], OffsetFromTop: Array[float], OffsetFromBot: Array[float], StartBarBend: Array[int], EndBarBend: Array[int], GUIDs: Array[str], StripNames: Array[str], SpanNos: Array[int]) -> (int, int, Array[str], Array[int], Array[float], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[int], Array[int], Array[str], Array[str], Array[int]) """
        pass

    def GetDetailedSlab_OneDetailingOutputInfo(self, DetailingOutputIndex, Guid_ETABS, Floor, StoryNameETABS, LevelZ, NumberStrips):
        """ GetDetailedSlab_OneDetailingOutputInfo(self: cDetailing, DetailingOutputIndex: int, Guid_ETABS: str, Floor: str, StoryNameETABS: str, LevelZ: float, NumberStrips: int) -> (int, str, str, str, float, int) """
        pass

    def GetDetailedWall_OnePier_OneDesignLeg_OneTieBar_OneTiePline_OnePoint(self, WallStackIndex, PierIndex, DesignLegIndex, TieBarIndex, TiePLineIndex, TPLinePointIndex, X, Y, Z):
        """ GetDetailedWall_OnePier_OneDesignLeg_OneTieBar_OneTiePline_OnePoint(self: cDetailing, WallStackIndex: int, PierIndex: int, DesignLegIndex: int, TieBarIndex: int, TiePLineIndex: int, TPLinePointIndex: int, X: float, Y: float, Z: float) -> (int, float, float, float) """
        pass

    def GetDetailedWall_OneWallStack_OnePierOutputInfo(self, WallStackIndex, PierIndex, StoryID, ETABSStoryName, NumberDesignLegs):
        """ GetDetailedWall_OneWallStack_OnePierOutputInfo(self: cDetailing, WallStackIndex: int, PierIndex: int, StoryID: int, ETABSStoryName: str, NumberDesignLegs: int) -> (int, int, str, int) """
        pass

    def GetDetailedWall_OneWallStack_OnePier_OneDesignLegOutputInfo(self, WallStackIndex, PierIndex, DesignLegIndex, GUID, PierLabel, x1, y1, z1, x2, y2, z2, ZLevel, NumberVerticalBars, NumberHorizontalBars, TotalAreaObjects, AreaObjectNames):
        """ GetDetailedWall_OneWallStack_OnePier_OneDesignLegOutputInfo(self: cDetailing, WallStackIndex: int, PierIndex: int, DesignLegIndex: int, GUID: str, PierLabel: str, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, ZLevel: float, NumberVerticalBars: int, NumberHorizontalBars: int, TotalAreaObjects: int, AreaObjectNames: Array[str]) -> (int, str, str, float, float, float, float, float, float, float, int, int, int, Array[str]) """
        pass

    def GetDetailedWall_OneWallStack_OnePier_OneDesignLeg_OneTieBarInfo(self, WallStackIndex, PierIndex, DesignLegIndex, TieBarIndex, GUID, BarSize_Dia, BarSize_Area, BarSize_Fy, BarSize_Notation, Spacing, StartZ, EndZ, TieShape, NumberOfTiePlines):
        """ GetDetailedWall_OneWallStack_OnePier_OneDesignLeg_OneTieBarInfo(self: cDetailing, WallStackIndex: int, PierIndex: int, DesignLegIndex: int, TieBarIndex: int, GUID: str, BarSize_Dia: float, BarSize_Area: float, BarSize_Fy: float, BarSize_Notation: str, Spacing: float, StartZ: float, EndZ: float, TieShape: int, NumberOfTiePlines: int) -> (int, str, float, float, float, str, float, float, float, int, int) """
        pass

    def GetDetailedWall_OneWallStack_OnePier_OneDesignLeg_OneTieBar_OneTiePlineInfo(self, WallStackIndex, PierIndex, DesignLegIndex, TieBarIndex, TiePLineIndex, Dia, NumberPoints, ZoneLength, LocationCode):
        """ GetDetailedWall_OneWallStack_OnePier_OneDesignLeg_OneTieBar_OneTiePlineInfo(self: cDetailing, WallStackIndex: int, PierIndex: int, DesignLegIndex: int, TieBarIndex: int, TiePLineIndex: int, Dia: float, NumberPoints: int, ZoneLength: float, LocationCode: int) -> (int, float, int, float, int) """
        pass

    def GetDetailedWall_OneWallStack_OnePier_OneDesignLeg_OneVerticalBarInfo(self, WallStackIndex, PierIndex, DesignLegIndex, VerticalBarIndex, GUID, BarSizeFirst_Dia, BarSizeFirst_Area, BarSizeFirst_Fy, BarSizeFirst_Notation, BarSizeLast_Dia, BarSizeLast_Area, BarSizeLast_Fy, BarSizeLast_Notation, BarSizeOthers_Dia, BarSizeOthers_Area, BarSizeOthers_Fy, BarSizeOthers_Notation, Number, StartX, StartY, EndX, EndY, StartBarBend, EndBarBend, OffsetZ, BarLength, LocationCode):
        """ GetDetailedWall_OneWallStack_OnePier_OneDesignLeg_OneVerticalBarInfo(self: cDetailing, WallStackIndex: int, PierIndex: int, DesignLegIndex: int, VerticalBarIndex: int, GUID: str, BarSizeFirst_Dia: float, BarSizeFirst_Area: float, BarSizeFirst_Fy: float, BarSizeFirst_Notation: str, BarSizeLast_Dia: float, BarSizeLast_Area: float, BarSizeLast_Fy: float, BarSizeLast_Notation: str, BarSizeOthers_Dia: float, BarSizeOthers_Area: float, BarSizeOthers_Fy: float, BarSizeOthers_Notation: str, Number: int, StartX: float, StartY: float, EndX: float, EndY: float, StartBarBend: int, EndBarBend: int, OffsetZ: float, BarLength: float, LocationCode: int) -> (int, str, float, float, float, str, float, float, float, str, float, float, float, str, int, float, float, float, float, int, int, float, float, int) """
        pass

    def GetDetailedWall_OneWallStack_OneSpandrelOutputInfo(self, WallStackIndex, SpandrelIndex, GUID, Name, Height, Width, Thickness, CoverLongBar, CoverStirrups, x1, y1, z1, x2, y2, z2, NumberLongBars, NumberStirrups, TotalAreaObjects, AreaObjectNames):
        """ GetDetailedWall_OneWallStack_OneSpandrelOutputInfo(self: cDetailing, WallStackIndex: int, SpandrelIndex: int, GUID: str, Name: str, Height: float, Width: float, Thickness: float, CoverLongBar: float, CoverStirrups: float, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, NumberLongBars: int, NumberStirrups: int, TotalAreaObjects: int, AreaObjectNames: Array[str]) -> (int, str, str, float, float, float, float, float, float, float, float, float, float, float, int, int, int, Array[str]) """
        pass

    def GetDetailedWall_OneWallStack_OneSpandrel_OneLongBarInfo(self, WallStackIndex, SpandrelIndex, LongBarIndex, BarSize_Dia, BarSize_Area, BarSize_Fy, BarSize_Notation, NumberPoints, X, Y, Z, StartType, EndType):
        """ GetDetailedWall_OneWallStack_OneSpandrel_OneLongBarInfo(self: cDetailing, WallStackIndex: int, SpandrelIndex: int, LongBarIndex: int, BarSize_Dia: float, BarSize_Area: float, BarSize_Fy: float, BarSize_Notation: str, NumberPoints: int, X: Array[float], Y: Array[float], Z: Array[float], StartType: int, EndType: int) -> (int, float, float, float, str, int, Array[float], Array[float], Array[float], int, int) """
        pass

    def GetDetailedWall_OneWallStack_OneSpandrel_OneStirrupsInfo(self, WallStackIndex, SpandrelIndex, StirrupsIndex, BarSize_Dia, BarSize_Area, BarSize_Fy, BarSize_Notation, X1, X2, Spacing, NumberLegs):
        """ GetDetailedWall_OneWallStack_OneSpandrel_OneStirrupsInfo(self: cDetailing, WallStackIndex: int, SpandrelIndex: int, StirrupsIndex: int, BarSize_Dia: float, BarSize_Area: float, BarSize_Fy: float, BarSize_Notation: str, X1: float, X2: float, Spacing: float, NumberLegs: int) -> (int, float, float, float, str, float, float, float, int) """
        pass

    def GetDetailed_OneWallStack(self, WallStackIndex, GUID, TowerID, NumberPiers, NUmberSpandrels):
        """ GetDetailed_OneWallStack(self: cDetailing, WallStackIndex: int, GUID: str, TowerID: int, NumberPiers: int, NUmberSpandrels: int) -> (int, str, int, int, int) """
        pass

    def GetDetailingAvailable(self):
        """ GetDetailingAvailable(self: cDetailing) -> bool """
        pass

    def GetNumberDetailedSlabs(self, NumberDetailingOutput):
        """ GetNumberDetailedSlabs(self: cDetailing, NumberDetailingOutput: int) -> (int, int) """
        pass

    def GetNumberDetailedWallStacks(self, NumberWallStacks):
        """ GetNumberDetailedWallStacks(self: cDetailing, NumberWallStacks: int) -> (int, int) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegionInfo(self, DetailingOutputIndex, StripIndex, DetailingRegionIndex, X1, Y1, X2, Y2, NumberTopBars, NumberBottomBars):
        """ GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegionInfo(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, DetailingRegionIndex: int, X1: float, Y1: float, X2: float, Y2: float, NumberTopBars: int, NumberBottomBars: int) -> (int, float, float, float, float, int, int) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneBottomRebarInfo(self, DetailingOutputIndex, StripIndex, DetailingRegionIndex, BottomRebarIndex, X1, Y1, X2, Y2, WidthRight, WidthLeft, Z, ReqAst, ProvAst):
        """ GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneBottomRebarInfo(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, DetailingRegionIndex: int, BottomRebarIndex: int, X1: float, Y1: float, X2: float, Y2: float, WidthRight: float, WidthLeft: float, Z: float, ReqAst: float, ProvAst: float) -> (int, float, float, float, float, float, float, float, float, float) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneBottomRebar_Bar1Info(self, DetailingOutputIndex, StripIndex, DetailingRegionIndex, BottomRebarIndex, GUID, PlaceCode, Dia, Size, Number, StartDist, EndDist, StartBend, EndBend, Material):
        """ GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneBottomRebar_Bar1Info(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, DetailingRegionIndex: int, BottomRebarIndex: int, GUID: str, PlaceCode: str, Dia: float, Size: str, Number: int, StartDist: float, EndDist: float, StartBend: int, EndBend: int, Material: str) -> (int, str, str, float, str, int, float, float, int, int, str) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneBottomRebar_Bar2Info(self, DetailingOutputIndex, StripIndex, DetailingRegionIndex, BottomRebarIndex, GUID, PlaceCode, Dia, Size, Number, StartDist, EndDist, StartBend, EndBend, Material):
        """ GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneBottomRebar_Bar2Info(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, DetailingRegionIndex: int, BottomRebarIndex: int, GUID: str, PlaceCode: str, Dia: float, Size: str, Number: int, StartDist: float, EndDist: float, StartBend: int, EndBend: int, Material: str) -> (int, str, str, float, str, int, float, float, int, int, str) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneTopRebarInfo(self, DetailingOutputIndex, StripIndex, DetailingRegionIndex, TopRebarIndex, X1, Y1, X2, Y2, WidthRight, WidthLeft, Z, ReqAst, ProvAst):
        """ GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneTopRebarInfo(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, DetailingRegionIndex: int, TopRebarIndex: int, X1: float, Y1: float, X2: float, Y2: float, WidthRight: float, WidthLeft: float, Z: float, ReqAst: float, ProvAst: float) -> (int, float, float, float, float, float, float, float, float, float) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneTopRebar_Bar1Info(self, DetailingOutputIndex, StripIndex, DetailingRegionIndex, TopRebarIndex, GUID, PlaceCode, Dia, Size, Number, StartDist, EndDist, StartBend, EndBend, Material):
        """ GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneTopRebar_Bar1Info(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, DetailingRegionIndex: int, TopRebarIndex: int, GUID: str, PlaceCode: str, Dia: float, Size: str, Number: int, StartDist: float, EndDist: float, StartBend: int, EndBend: int, Material: str) -> (int, str, str, float, str, int, float, float, int, int, str) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneTopRebar_Bar2Info(self, DetailingOutputIndex, StripIndex, DetailingRegionIndex, TopRebarIndex, GUID, PlaceCode, Dia, Size, Number, StartDist, EndDist, StartBend, EndBend, Material):
        """ GetOneDetailedSlab_OneDetailingOutput_OneStrip_OneDetailingRegion_OneTopRebar_Bar2Info(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, DetailingRegionIndex: int, TopRebarIndex: int, GUID: str, PlaceCode: str, Dia: float, Size: str, Number: int, StartDist: float, EndDist: float, StartBend: int, EndBend: int, Material: str) -> (int, str, str, float, str, int, float, float, int, int, str) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_StripGUID(self, DetailingOutputIndex, StripIndex, GUID_ETABS):
        """ GetOneDetailedSlab_OneDetailingOutput_StripGUID(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, GUID_ETABS: str) -> (int, str) """
        pass

    def GetOneDetailedSlab_OneDetailingOutput_StripInfo(self, DetailingOutputIndex, StripIndex, Name, LayerName, StripType, NumberRegions):
        """ GetOneDetailedSlab_OneDetailingOutput_StripInfo(self: cDetailing, DetailingOutputIndex: int, StripIndex: int, Name: str, LayerName: str, StripType: str, NumberRegions: int) -> (int, str, str, str, int) """
        pass

    def GetSimilarBeamLines(self, BeamLineID, NumberSimilarBeams, NumberUniqueObjects, ObjectUniqueNames):
        """ GetSimilarBeamLines(self: cDetailing, BeamLineID: str, NumberSimilarBeams: int, NumberUniqueObjects: Array[int], ObjectUniqueNames: Array[str]) -> (int, int, Array[int], Array[str]) """
        pass

    def GetSimilarColumnStacks(self, ColumnStackID, NumberSimilarColumns, NumberUniqueObjects, ObjectUniqueNames):
        """ GetSimilarColumnStacks(self: cDetailing, ColumnStackID: str, NumberSimilarColumns: int, NumberUniqueObjects: Array[int], ObjectUniqueNames: Array[str]) -> (int, int, Array[int], Array[str]) """
        pass

    def GetSimilarSlabs(self, SlabName, NumberSimilarSlabs, Names):
        """ GetSimilarSlabs(self: cDetailing, SlabName: str, NumberSimilarSlabs: int, Names: Array[str]) -> (int, int, Array[str]) """
        pass

    def StartDetailing(self, OverwriteExisting):
        """ StartDetailing(self: cDetailing, OverwriteExisting: bool) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDiaphragm:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cDiaphragm, Name: str, NewName: str) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cDiaphragm, Name: str) -> int """
        pass

    def GetDiaphragm(self, Name, SemiRigid):
        """ GetDiaphragm(self: cDiaphragm, Name: str, SemiRigid: bool) -> (int, bool) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cDiaphragm, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def SetDiaphragm(self, Name, SemiRigid):
        """ SetDiaphragm(self: cDiaphragm, Name: str, SemiRigid: bool) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStAISC360_05_IBC2006:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStAISC360_05_IBC2006, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStAISC360_05_IBC2006, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStAISC360_05_IBC2006, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStAISC360_05_IBC2006, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStAISC360_10:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStAISC360_10, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStAISC360_10, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStAISC360_10, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStAISC360_10, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStAISC_ASD89:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStAISC_ASD89, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStAISC_ASD89, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStAISC_ASD89, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStAISC_ASD89, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStAISC_LRFD93:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStAISC_LRFD93, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStAISC_LRFD93, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStAISC_LRFD93, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStAISC_LRFD93, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStAustralian_AS4100_98:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStAustralian_AS4100_98, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStAustralian_AS4100_98, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStAustralian_AS4100_98, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStAustralian_AS4100_98, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStBS5950_2000:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStBS5950_2000, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStBS5950_2000, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStBS5950_2000, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStBS5950_2000, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStCanadian_S16_09:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStCanadian_S16_09, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStCanadian_S16_09, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStCanadian_S16_09, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStCanadian_S16_09, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStCanadian_S16_14:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStCanadian_S16_14, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStCanadian_S16_14, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStCanadian_S16_14, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStCanadian_S16_14, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStCanadian_S16_19:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStCanadian_S16_19, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStCanadian_S16_19, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStCanadian_S16_19, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStCanadian_S16_19, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStChinese_2010:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStChinese_2010, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStChinese_2010, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStChinese_2010, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStChinese_2010, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStChinese_2018:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStChinese_2018, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStChinese_2018, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStChinese_2018, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStChinese_2018, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStEurocode_3_2005:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStEurocode_3_2005, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStEurocode_3_2005, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStEurocode_3_2005, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStEurocode_3_2005, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStIndian_IS_800_2007:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStIndian_IS_800_2007, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStIndian_IS_800_2007, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStIndian_IS_800_2007, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStIndian_IS_800_2007, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStItalianNTC2008S:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStItalianNTC2008S, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStItalianNTC2008S, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStItalianNTC2008S, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStItalianNTC2008S, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStItalianNTC2018S:
    # no doc
    def GetOverwrite(self, Name, Item, textValue, numericValue, ProgDet):
        """ GetOverwrite(self: cDStItalianNTC2018S, Name: str, Item: int, textValue: str, numericValue: float, ProgDet: bool) -> (int, str, float, bool) """
        pass

    def GetPreference(self, Item, textValue, numericValue):
        """ GetPreference(self: cDStItalianNTC2018S, Item: int, textValue: str, numericValue: float) -> (int, str, float) """
        pass

    def SetOverwrite(self, Name, Item, textValue, numericValue, ItemType):
        """ SetOverwrite(self: cDStItalianNTC2018S, Name: str, Item: int, textValue: str, numericValue: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, textValue, numericValue):
        """ SetPreference(self: cDStItalianNTC2018S, Item: int, textValue: str, numericValue: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStNewZealand_NZS3404_97:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStNewZealand_NZS3404_97, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStNewZealand_NZS3404_97, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStNewZealand_NZS3404_97, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStNewZealand_NZS3404_97, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStSP16_13330_2011:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStSP16_13330_2011, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStSP16_13330_2011, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStSP16_13330_2011, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStSP16_13330_2011, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cDStSP16_13330_2017:
    # no doc
    def GetOverwrite(self, Name, Item, Value, ProgDet):
        """ GetOverwrite(self: cDStSP16_13330_2017, Name: str, Item: int, Value: float, ProgDet: bool) -> (int, float, bool) """
        pass

    def GetPreference(self, Item, Value):
        """ GetPreference(self: cDStSP16_13330_2017, Item: int, Value: float) -> (int, float) """
        pass

    def SetOverwrite(self, Name, Item, Value, ItemType):
        """ SetOverwrite(self: cDStSP16_13330_2017, Name: str, Item: int, Value: float, ItemType: eItemType) -> int """
        pass

    def SetPreference(self, Item, Value):
        """ SetPreference(self: cDStSP16_13330_2017, Item: int, Value: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cEditArea:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cEditFrame:
    # no doc
    def ChangeConnectivity(self, Name, Point1, Point2):
        """ ChangeConnectivity(self: cEditFrame, Name: str, Point1: str, Point2: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cEditGeneral:
    # no doc
    def Move(self, DX, DY, DZ):
        """ Move(self: cEditGeneral, DX: float, DY: float, DZ: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cEditPoint:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cFile:
    # no doc
    def GetFilePath(self, FilePath):
        """ GetFilePath(self: cFile, FilePath: str) -> (int, str) """
        pass

    def NewBlank(self):
        """ NewBlank(self: cFile) -> int """
        pass

    def NewGridOnly(self, NumberStorys, TypicalStoryHeight, BottomStoryHeight, NumberLinesX, NumberLinesY, SpacingX, SpacingY):
        """ NewGridOnly(self: cFile, NumberStorys: int, TypicalStoryHeight: float, BottomStoryHeight: float, NumberLinesX: int, NumberLinesY: int, SpacingX: float, SpacingY: float) -> int """
        pass

    def NewSteelDeck(self, NumberStorys, TypicalStoryHeight, BottomStoryHeight, NumberLinesX, NumberLinesY, SpacingX, SpacingY):
        """ NewSteelDeck(self: cFile, NumberStorys: int, TypicalStoryHeight: float, BottomStoryHeight: float, NumberLinesX: int, NumberLinesY: int, SpacingX: float, SpacingY: float) -> int """
        pass

    def OpenFile(self, FileName):
        """ OpenFile(self: cFile, FileName: str) -> int """
        pass

    def Save(self, FileName):
        """ Save(self: cFile, FileName: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cFrameObj:
    # no doc
    def AddByCoord(self, XI, YI, ZI, XJ, YJ, ZJ, Name, PropName, UserName, CSys):
        """ AddByCoord(self: cFrameObj, XI: float, YI: float, ZI: float, XJ: float, YJ: float, ZJ: float, Name: str, PropName: str, UserName: str, CSys: str) -> (int, str) """
        pass

    def AddByPoint(self, Point1, Point2, Name, PropName, UserName):
        """ AddByPoint(self: cFrameObj, Point1: str, Point2: str, Name: str, PropName: str, UserName: str) -> (int, str) """
        pass

    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cFrameObj, Name: str, NewName: str) -> int """
        pass

    def Count(self, MyType):
        """ Count(self: cFrameObj, MyType: str) -> int """
        pass

    def Delete(self, Name, ItemType):
        """ Delete(self: cFrameObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteLateralBracing(self, Name, MyType, ItemType):
        """ DeleteLateralBracing(self: cFrameObj, Name: str, MyType: int, ItemType: eItemType) -> int """
        pass

    def DeleteLoadDistributed(self, Name, LoadPat, ItemType):
        """ DeleteLoadDistributed(self: cFrameObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteLoadPoint(self, Name, LoadPat, ItemType):
        """ DeleteLoadPoint(self: cFrameObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteLoadTemperature(self, Name, LoadPat, ItemType):
        """ DeleteLoadTemperature(self: cFrameObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteMass(self, Name, ItemType):
        """ DeleteMass(self: cFrameObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteModifiers(self, Name, ItemType):
        """ DeleteModifiers(self: cFrameObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteSpring(self, Name, ItemType):
        """ DeleteSpring(self: cFrameObj, Name: str, ItemType: eItemType) -> int """
        pass

    def GetAllFrames(self, NumberNames, MyName, PropName, StoryName, PointName1, PointName2, Point1X, Point1Y, Point1Z, Point2X, Point2Y, Point2Z, Angle, Offset1X, Offset2X, Offset1Y, Offset2Y, Offset1Z, Offset2Z, CardinalPoint, csys):
        """ GetAllFrames(self: cFrameObj, NumberNames: int, MyName: Array[str], PropName: Array[str], StoryName: Array[str], PointName1: Array[str], PointName2: Array[str], Point1X: Array[float], Point1Y: Array[float], Point1Z: Array[float], Point2X: Array[float], Point2Y: Array[float], Point2Z: Array[float], Angle: Array[float], Offset1X: Array[float], Offset2X: Array[float], Offset1Y: Array[float], Offset2Y: Array[float], Offset1Z: Array[float], Offset2Z: Array[float], CardinalPoint: Array[int], csys: str) -> (int, int, Array[str], Array[str], Array[str], Array[str], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[int]) """
        pass

    def GetColumnSpliceOverwrite(self, Name, SpliceOption, Height):
        """ GetColumnSpliceOverwrite(self: cFrameObj, Name: str, SpliceOption: int, Height: float) -> (int, int, float) """
        pass

    def GetCurved_2(self, Name, CurveType, Tension, NumPnts, gx, gy, gz):
        """ GetCurved_2(self: cFrameObj, Name: str, CurveType: int, Tension: float, NumPnts: int, gx: Array[float], gy: Array[float], gz: Array[float]) -> (int, int, float, int, Array[float], Array[float], Array[float]) """
        pass

    def GetDesignOrientation(self, Name, DesignOrientation):
        """ GetDesignOrientation(self: cFrameObj, Name: str, DesignOrientation: eFrameDesignOrientation) -> (int, eFrameDesignOrientation) """
        pass

    def GetDesignProcedure(self, Name, MyType):
        """ GetDesignProcedure(self: cFrameObj, Name: str, MyType: int) -> (int, int) """
        pass

    def GetElm(self, Name, NElm, Elm, RDI, RDJ):
        """ GetElm(self: cFrameObj, Name: str, NElm: int, Elm: Array[str], RDI: Array[float], RDJ: Array[float]) -> (int, int, Array[str], Array[float], Array[float]) """
        pass

    def GetEndLengthOffset(self, Name, AutoOffset, Length1, Length2, RZ):
        """ GetEndLengthOffset(self: cFrameObj, Name: str, AutoOffset: bool, Length1: float, Length2: float, RZ: float) -> (int, bool, float, float, float) """
        pass

    def GetGroupAssign(self, Name, NumberGroups, Groups):
        """ GetGroupAssign(self: cFrameObj, Name: str, NumberGroups: int, Groups: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetGUID(self, Name, GUID):
        """ GetGUID(self: cFrameObj, Name: str, GUID: str) -> (int, str) """
        pass

    def GetHingeAssigns(self, Name, NumberHinges, HingeNum, Prop, MyType, Behavior, Source, RD):
        """ GetHingeAssigns(self: cFrameObj, Name: str, NumberHinges: int, HingeNum: Array[int], Prop: Array[str], MyType: Array[int], Behavior: Array[int], Source: Array[str], RD: Array[float]) -> (int, int, Array[int], Array[str], Array[int], Array[int], Array[str], Array[float]) """
        pass

    def GetHingeAssigns_1(self, Name, NumberHinges, HingeNum, Prop, MyType, Behavior, Source, LocType, RD, AD):
        """ GetHingeAssigns_1(self: cFrameObj, Name: str, NumberHinges: int, HingeNum: Array[int], Prop: Array[str], MyType: Array[int], Behavior: Array[int], Source: Array[str], LocType: Array[eHingeLocationType], RD: Array[float], AD: Array[float]) -> (int, int, Array[int], Array[str], Array[int], Array[int], Array[str], Array[eHingeLocationType], Array[float], Array[float]) """
        pass

    def GetInsertionPoint(self, Name, CardinalPoint, Mirror2, StiffTransform, Offset1, Offset2, CSys):
        """ GetInsertionPoint(self: cFrameObj, Name: str, CardinalPoint: int, Mirror2: bool, StiffTransform: bool, Offset1: Array[float], Offset2: Array[float], CSys: str) -> (int, int, bool, bool, Array[float], Array[float], str) """
        pass

    def GetLabelFromName(self, Name, Label, Story):
        """ GetLabelFromName(self: cFrameObj, Name: str, Label: str, Story: str) -> (int, str, str) """
        pass

    def GetLabelNameList(self, NumberNames, MyName, MyLabel, MyStory):
        """ GetLabelNameList(self: cFrameObj, NumberNames: int, MyName: Array[str], MyLabel: Array[str], MyStory: Array[str]) -> (int, int, Array[str], Array[str], Array[str]) """
        pass

    def GetLateralBracing(self, Name, NumberItems, FrameName, MyType, Loc, RD1, RD2, Dist1, Dist2):
        """ GetLateralBracing(self: cFrameObj, Name: str, NumberItems: int, FrameName: Array[str], MyType: Array[int], Loc: Array[int], RD1: Array[float], RD2: Array[float], Dist1: Array[float], Dist2: Array[float]) -> (int, int, Array[str], Array[int], Array[int], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLoadDistributed(self, Name, NumberItems, FrameName, LoadPat, MyType, CSys, Dir, RD1, RD2, Dist1, Dist2, Val1, Val2, ItemType):
        """ GetLoadDistributed(self: cFrameObj, Name: str, NumberItems: int, FrameName: Array[str], LoadPat: Array[str], MyType: Array[int], CSys: Array[str], Dir: Array[int], RD1: Array[float], RD2: Array[float], Dist1: Array[float], Dist2: Array[float], Val1: Array[float], Val2: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[int], Array[str], Array[int], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLoadPoint(self, Name, NumberItems, FrameName, LoadPat, MyType, CSys, Dir, RelDist, Dist, Val, ItemType):
        """ GetLoadPoint(self: cFrameObj, Name: str, NumberItems: int, FrameName: Array[str], LoadPat: Array[str], MyType: Array[int], CSys: Array[str], Dir: Array[int], RelDist: Array[float], Dist: Array[float], Val: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[int], Array[str], Array[int], Array[float], Array[float], Array[float]) """
        pass

    def GetLoadTemperature(self, Name, NumberItems, FrameName, LoadPat, MyType, Val, PatternName, ItemType):
        """ GetLoadTemperature(self: cFrameObj, Name: str, NumberItems: int, FrameName: Array[str], LoadPat: Array[str], MyType: Array[int], Val: Array[float], PatternName: Array[str], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[int], Array[float], Array[str]) """
        pass

    def GetLocalAxes(self, Name, Ang, Advanced):
        """ GetLocalAxes(self: cFrameObj, Name: str, Ang: float, Advanced: bool) -> (int, float, bool) """
        pass

    def GetMass(self, Name, MassOverL):
        """ GetMass(self: cFrameObj, Name: str, MassOverL: float) -> (int, float) """
        pass

    def GetMaterialOverwrite(self, Name, PropName):
        """ GetMaterialOverwrite(self: cFrameObj, Name: str, PropName: str) -> (int, str) """
        pass

    def GetModifiers(self, Name, Value):
        """ GetModifiers(self: cFrameObj, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def GetNameFromLabel(self, Label, Story, Name):
        """ GetNameFromLabel(self: cFrameObj, Label: str, Story: str, Name: str) -> (int, str) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cFrameObj, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetNameListOnStory(self, StoryName, NumberNames, MyName):
        """ GetNameListOnStory(self: cFrameObj, StoryName: str, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetOutputStations(self, Name, MyType, MaxSegSize, MinSections, NoOutPutAndDesignAtElementEnds, NoOutPutAndDesignAtPointLoads):
        """ GetOutputStations(self: cFrameObj, Name: str, MyType: int, MaxSegSize: float, MinSections: int, NoOutPutAndDesignAtElementEnds: bool, NoOutPutAndDesignAtPointLoads: bool) -> (int, int, float, int, bool, bool) """
        pass

    def GetPier(self, Name, PierName):
        """ GetPier(self: cFrameObj, Name: str, PierName: str) -> (int, str) """
        pass

    def GetPoints(self, Name, Point1, Point2):
        """ GetPoints(self: cFrameObj, Name: str, Point1: str, Point2: str) -> (int, str, str) """
        pass

    def GetReleases(self, Name, II, JJ, StartValue, EndValue):
        """ GetReleases(self: cFrameObj, Name: str, II: Array[bool], JJ: Array[bool], StartValue: Array[float], EndValue: Array[float]) -> (int, Array[bool], Array[bool], Array[float], Array[float]) """
        pass

    def GetSection(self, Name, PropName, SAuto):
        """ GetSection(self: cFrameObj, Name: str, PropName: str, SAuto: str) -> (int, str, str) """
        pass

    def GetSectionNonPrismatic(self, Name, PropName, SVarTotalLength, SVarRelStartLoc):
        """ GetSectionNonPrismatic(self: cFrameObj, Name: str, PropName: str, SVarTotalLength: float, SVarRelStartLoc: float) -> (int, str, float, float) """
        pass

    def GetSelected(self, Name, Selected):
        """ GetSelected(self: cFrameObj, Name: str, Selected: bool) -> (int, bool) """
        pass

    def GetSpandrel(self, Name, SpandrelName):
        """ GetSpandrel(self: cFrameObj, Name: str, SpandrelName: str) -> (int, str) """
        pass

    def GetSpringAssignment(self, Name, SpringProp):
        """ GetSpringAssignment(self: cFrameObj, Name: str, SpringProp: str) -> (int, str) """
        pass

    def GetSupports(self, Name, SupportName1, SupportType1, SupportName2, SupportType2):
        """ GetSupports(self: cFrameObj, Name: str, SupportName1: str, SupportType1: eObjType, SupportName2: str, SupportType2: eObjType) -> (int, str, eObjType, str, eObjType) """
        pass

    def GetTCLimits(self, Name, LimitCompressionExists, LimitCompression, LimitTensionExists, LimitTension):
        """ GetTCLimits(self: cFrameObj, Name: str, LimitCompressionExists: bool, LimitCompression: float, LimitTensionExists: bool, LimitTension: float) -> (int, bool, float, bool, float) """
        pass

    def GetTransformationMatrix(self, Name, Value, IsGlobal):
        """ GetTransformationMatrix(self: cFrameObj, Name: str, Value: Array[float], IsGlobal: bool) -> (int, Array[float]) """
        pass

    def GetTypeOAPI(self, Name, MyType):
        """ GetTypeOAPI(self: cFrameObj, Name: str, MyType: str) -> (int, str) """
        pass

    def SetColumnSpliceOverwrite(self, Name, SpliceOption, Height, ItemType):
        """ SetColumnSpliceOverwrite(self: cFrameObj, Name: str, SpliceOption: int, Height: float, ItemType: eItemType) -> int """
        pass

    def SetDesignProcedure(self, Name, MyType, ItemType):
        """ SetDesignProcedure(self: cFrameObj, Name: str, MyType: int, ItemType: eItemType) -> int """
        pass

    def SetEndLengthOffset(self, Name, AutoOffset, Length1, Length2, RZ, ItemType):
        """ SetEndLengthOffset(self: cFrameObj, Name: str, AutoOffset: bool, Length1: float, Length2: float, RZ: float, ItemType: eItemType) -> int """
        pass

    def SetGroupAssign(self, Name, GroupName, Remove, ItemType):
        """ SetGroupAssign(self: cFrameObj, Name: str, GroupName: str, Remove: bool, ItemType: eItemType) -> int """
        pass

    def SetGUID(self, Name, GUID):
        """ SetGUID(self: cFrameObj, Name: str, GUID: str) -> int """
        pass

    def SetInsertionPoint(self, Name, CardinalPoint, Mirror2, StiffTransform, Offset1, Offset2, CSys, ItemType):
        """ SetInsertionPoint(self: cFrameObj, Name: str, CardinalPoint: int, Mirror2: bool, StiffTransform: bool, Offset1: Array[float], Offset2: Array[float], CSys: str, ItemType: eItemType) -> (int, Array[float], Array[float]) """
        pass

    def SetLateralBracing(self, Name, MyType, Loc, MyDist1, MyDist2, RelDist, ItemType):
        """ SetLateralBracing(self: cFrameObj, Name: str, MyType: int, Loc: int, MyDist1: float, MyDist2: float, RelDist: bool, ItemType: eItemType) -> int """
        pass

    def SetLoadDistributed(self, Name, LoadPat, MyType, Dir, Dist1, Dist2, Val1, Val2, CSys, RelDist, Replace, ItemType):
        """ SetLoadDistributed(self: cFrameObj, Name: str, LoadPat: str, MyType: int, Dir: int, Dist1: float, Dist2: float, Val1: float, Val2: float, CSys: str, RelDist: bool, Replace: bool, ItemType: eItemType) -> int """
        pass

    def SetLoadPoint(self, Name, LoadPat, MyType, Dir, Dist, Val, CSys, RelDist, Replace, ItemType):
        """ SetLoadPoint(self: cFrameObj, Name: str, LoadPat: str, MyType: int, Dir: int, Dist: float, Val: float, CSys: str, RelDist: bool, Replace: bool, ItemType: eItemType) -> int """
        pass

    def SetLoadTemperature(self, Name, LoadPat, MyType, Val, PatternName, Replace, ItemType):
        """ SetLoadTemperature(self: cFrameObj, Name: str, LoadPat: str, MyType: int, Val: float, PatternName: str, Replace: bool, ItemType: eItemType) -> int """
        pass

    def SetLocalAxes(self, Name, Ang, ItemType):
        """ SetLocalAxes(self: cFrameObj, Name: str, Ang: float, ItemType: eItemType) -> int """
        pass

    def SetMass(self, Name, MassOverL, Replace, ItemType):
        """ SetMass(self: cFrameObj, Name: str, MassOverL: float, Replace: bool, ItemType: eItemType) -> int """
        pass

    def SetMaterialOverwrite(self, Name, PropName, ItemType):
        """ SetMaterialOverwrite(self: cFrameObj, Name: str, PropName: str, ItemType: eItemType) -> int """
        pass

    def SetModifiers(self, Name, Value, ItemType):
        """ SetModifiers(self: cFrameObj, Name: str, Value: Array[float], ItemType: eItemType) -> (int, Array[float]) """
        pass

    def SetOutputStations(self, Name, MyType, MaxSegSize, MinSections, NoOutPutAndDesignAtElementEnds, NoOutPutAndDesignAtPointLoads, ItemType):
        """ SetOutputStations(self: cFrameObj, Name: str, MyType: int, MaxSegSize: float, MinSections: int, NoOutPutAndDesignAtElementEnds: bool, NoOutPutAndDesignAtPointLoads: bool, ItemType: eItemType) -> int """
        pass

    def SetPier(self, Name, PierName, ItemType):
        """ SetPier(self: cFrameObj, Name: str, PierName: str, ItemType: eItemType) -> int """
        pass

    def SetReleases(self, Name, II, JJ, StartValue, EndValue, ItemType):
        """ SetReleases(self: cFrameObj, Name: str, II: Array[bool], JJ: Array[bool], StartValue: Array[float], EndValue: Array[float], ItemType: eItemType) -> (int, Array[bool], Array[bool], Array[float], Array[float]) """
        pass

    def SetSection(self, Name, PropName, ItemType, SVarRelStartLoc, SVarTotalLength):
        """ SetSection(self: cFrameObj, Name: str, PropName: str, ItemType: eItemType, SVarRelStartLoc: float, SVarTotalLength: float) -> int """
        pass

    def SetSelected(self, Name, Selected, ItemType):
        """ SetSelected(self: cFrameObj, Name: str, Selected: bool, ItemType: eItemType) -> int """
        pass

    def SetSpandrel(self, Name, SpandrelName, ItemType):
        """ SetSpandrel(self: cFrameObj, Name: str, SpandrelName: str, ItemType: eItemType) -> int """
        pass

    def SetSpringAssignment(self, Name, SpringProp, ItemType):
        """ SetSpringAssignment(self: cFrameObj, Name: str, SpringProp: str, ItemType: eItemType) -> int """
        pass

    def SetTCLimits(self, Name, LimitCompressionExists, LimitCompression, LimitTensionExists, LimitTension, ItemType):
        """ SetTCLimits(self: cFrameObj, Name: str, LimitCompressionExists: bool, LimitCompression: float, LimitTensionExists: bool, LimitTension: float, ItemType: eItemType) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cFunction:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cFunction, Name: str, NewName: str) -> int """
        pass

    def ConvertToUser(self, Name):
        """ ConvertToUser(self: cFunction, Name: str) -> int """
        pass

    def Count(self, FuncType):
        """ Count(self: cFunction, FuncType: int) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cFunction, Name: str) -> int """
        pass

    def GetNameList(self, NumberNames, MyName, FuncType):
        """ GetNameList(self: cFunction, NumberNames: int, MyName: Array[str], FuncType: int) -> (int, int, Array[str]) """
        pass

    def GetTypeOAPI(self, Name, FuncType, AddType):
        """ GetTypeOAPI(self: cFunction, Name: str, FuncType: int, AddType: int) -> (int, int, int) """
        pass

    def GetValues(self, Name, NumberItems, MyTime, Value):
        """ GetValues(self: cFunction, Name: str, NumberItems: int, MyTime: Array[float], Value: Array[float]) -> (int, int, Array[float], Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FuncRS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FuncRS(self: cFunction) -> cFunctionRS

"""

    FuncTH = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FuncTH(self: cFunction) -> cFunctionTH

"""



class cFunctionRS:
    # no doc
    def GetNTC2008(self, Name, ParamsOption, Latitude, Longitude, Island, LimitState, UsageClass, NomLife, PeakAccel, F0, Tcs, SpecType, SoilType, Topography, hRatio, Damping, q):
        """ GetNTC2008(self: cFunctionRS, Name: str, ParamsOption: int, Latitude: float, Longitude: float, Island: int, LimitState: int, UsageClass: int, NomLife: float, PeakAccel: float, F0: float, Tcs: float, SpecType: int, SoilType: int, Topography: int, hRatio: float, Damping: float, q: float) -> (int, int, float, float, int, int, int, float, float, float, float, int, int, int, float, float, float) """
        pass

    def GetNTC2018(self, Name, ParamsOption, Latitude, Longitude, Island, LimitState, UsageClass, NomLife, PeakAccel, F0, Tcs, SpecType, SoilType, Topography, hRatio, Damping, q):
        """ GetNTC2018(self: cFunctionRS, Name: str, ParamsOption: int, Latitude: float, Longitude: float, Island: int, LimitState: int, UsageClass: int, NomLife: float, PeakAccel: float, F0: float, Tcs: float, SpecType: int, SoilType: int, Topography: int, hRatio: float, Damping: float, q: float) -> (int, int, float, float, int, int, int, float, float, float, float, int, int, int, float, float, float) """
        pass

    def SetNTC2008(self, Name, ParamsOption, Latitude, Longitude, Island, LimitState, UsageClass, NomLife, PeakAccel, F0, Tcs, SpecType, SoilType, Topography, hRatio, Damping, q):
        """ SetNTC2008(self: cFunctionRS, Name: str, ParamsOption: int, Latitude: float, Longitude: float, Island: int, LimitState: int, UsageClass: int, NomLife: float, PeakAccel: float, F0: float, Tcs: float, SpecType: int, SoilType: int, Topography: int, hRatio: float, Damping: float, q: float) -> int """
        pass

    def SetNTC2018(self, Name, ParamsOption, Latitude, Longitude, Island, LimitState, UsageClass, NomLife, PeakAccel, F0, Tcs, SpecType, SoilType, Topography, hRatio, Damping, q):
        """ SetNTC2018(self: cFunctionRS, Name: str, ParamsOption: int, Latitude: float, Longitude: float, Island: int, LimitState: int, UsageClass: int, NomLife: float, PeakAccel: float, F0: float, Tcs: float, SpecType: int, SoilType: int, Topography: int, hRatio: float, Damping: float, q: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cFunctionTH:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cGenDispl:
    # no doc
    def Add(self, Name, MyType):
        """ Add(self: cGenDispl, Name: str, MyType: int) -> int """
        pass

    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cGenDispl, Name: str, NewName: str) -> int """
        pass

    def Count(self):
        """ Count(self: cGenDispl) -> int """
        pass

    def CountPoint(self, Name, Count):
        """ CountPoint(self: cGenDispl, Name: str, Count: int) -> (int, int) """
        pass

    def Delete(self, Name):
        """ Delete(self: cGenDispl, Name: str) -> int """
        pass

    def DeletePoint(self, Name, PointName):
        """ DeletePoint(self: cGenDispl, Name: str, PointName: str) -> int """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cGenDispl, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetPoint(self, Name, NumberItems, PointName, U1, U2, U3, R1, R2, R3):
        """ GetPoint(self: cGenDispl, Name: str, NumberItems: int, PointName: Array[str], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float]) -> (int, int, Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetTypeGenDispl(self, Name, MyType):
        """ GetTypeGenDispl(self: cGenDispl, Name: str, MyType: int) -> (int, int) """
        pass

    def GetTypeOAPI(self, name, MyType):
        """ GetTypeOAPI(self: cGenDispl, name: str, MyType: int) -> (int, int) """
        pass

    def SetPoint(self, Name, PointName, SF):
        """ SetPoint(self: cGenDispl, Name: str, PointName: str, SF: Array[float]) -> (int, Array[float]) """
        pass

    def SetType(self, Name, MyType):
        """ SetType(self: cGenDispl, Name: str, MyType: int) -> int """
        pass

    def SetTypeOAPI(self, Name, MyType):
        """ SetTypeOAPI(self: cGenDispl, Name: str, MyType: int) -> int """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cGenRefLine:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cGridSys:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cGridSys, Name: str, NewName: str) -> int """
        pass

    def Count(self):
        """ Count(self: cGridSys) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cGridSys, Name: str) -> int """
        pass

    def GetGridSys(self, Name, x, y, RZ):
        """ GetGridSys(self: cGridSys, Name: str, x: float, y: float, RZ: float) -> (int, float, float, float) """
        pass

    def GetGridSysCartesian(self, Name, Xo, Yo, RZ, StoryRangeIsDefault, TopStory, BottomStory, BubbleSize, GridColor, NumXLines, GridLineIDX, OrdinateX, VisibleX, BubbleLocX, NumYLines, GridLineIDY, OrdinateY, VisibleY, BubbleLocY, NumGenLines, GridLineIDGen, GenOrdX1, GenOrdY1, GenOrdX2, GenOrdY2, VisibleGen, BubbleLocGen):
        """ GetGridSysCartesian(self: cGridSys, Name: str, Xo: float, Yo: float, RZ: float, StoryRangeIsDefault: bool, TopStory: str, BottomStory: str, BubbleSize: float, GridColor: int, NumXLines: int, GridLineIDX: Array[str], OrdinateX: Array[float], VisibleX: Array[bool], BubbleLocX: Array[str], NumYLines: int, GridLineIDY: Array[str], OrdinateY: Array[float], VisibleY: Array[bool], BubbleLocY: Array[str], NumGenLines: int, GridLineIDGen: Array[str], GenOrdX1: Array[float], GenOrdY1: Array[float], GenOrdX2: Array[float], GenOrdY2: Array[float], VisibleGen: Array[bool], BubbleLocGen: Array[str]) -> (int, float, float, float, bool, str, str, float, int, int, Array[str], Array[float], Array[bool], Array[str], int, Array[str], Array[float], Array[bool], Array[str], int, Array[str], Array[float], Array[float], Array[float], Array[float], Array[bool], Array[str]) """
        pass

    def GetGridSysCylindrical(self, Name, Xo, Yo, RZ, StoryRangeIsDefault, TopStory, BottomStory, BubbleSize, GridColor, NumRLines, GridLineIDR, OrdinateR, VisibleR, BubbleLocR, NumTLines, GridLineIDT, OrdinateT, VisibleT, BubbleLocT):
        """ GetGridSysCylindrical(self: cGridSys, Name: str, Xo: float, Yo: float, RZ: float, StoryRangeIsDefault: bool, TopStory: str, BottomStory: str, BubbleSize: float, GridColor: int, NumRLines: int, GridLineIDR: Array[str], OrdinateR: Array[float], VisibleR: Array[bool], BubbleLocR: Array[str], NumTLines: int, GridLineIDT: Array[str], OrdinateT: Array[float], VisibleT: Array[bool], BubbleLocT: Array[str]) -> (int, float, float, float, bool, str, str, float, int, int, Array[str], Array[float], Array[bool], Array[str], int, Array[str], Array[float], Array[bool], Array[str]) """
        pass

    def GetGridSysType(self, Name, GridSysType):
        """ GetGridSysType(self: cGridSys, Name: str, GridSysType: str) -> (int, str) """
        pass

    def GetGridSys_2(self, Name, Xo, Yo, RZ, GridSysType, NumXLines, NumYLines, GridLineIDX, GridLineIDY, OrdinateX, OrdinateY, VisibleX, VisibleY, BubbleLocX, BubbleLocY):
        """ GetGridSys_2(self: cGridSys, Name: str, Xo: float, Yo: float, RZ: float, GridSysType: str, NumXLines: int, NumYLines: int, GridLineIDX: Array[str], GridLineIDY: Array[str], OrdinateX: Array[float], OrdinateY: Array[float], VisibleX: Array[bool], VisibleY: Array[bool], BubbleLocX: Array[str], BubbleLocY: Array[str]) -> (int, float, float, float, str, int, int, Array[str], Array[str], Array[float], Array[float], Array[bool], Array[bool], Array[str], Array[str]) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cGridSys, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetNameTypeList(self, NumberNames, GridSysName, GridSysType):
        """ GetNameTypeList(self: cGridSys, NumberNames: int, GridSysName: Array[str], GridSysType: Array[str]) -> (int, int, Array[str], Array[str]) """
        pass

    def GetTransformationMatrix(self, Name, Value):
        """ GetTransformationMatrix(self: cGridSys, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def SetGridSys(self, Name, x, y, RZ):
        """ SetGridSys(self: cGridSys, Name: str, x: float, y: float, RZ: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cGroup:
    # no doc
    def Count(self):
        """ Count(self: cGroup) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cGroup, Name: str) -> int """
        pass

    def GetAssignments(self, Name, NumberItems, ObjectType, ObjectName):
        """ GetAssignments(self: cGroup, Name: str, NumberItems: int, ObjectType: Array[int], ObjectName: Array[str]) -> (int, int, Array[int], Array[str]) """
        pass

    def GetGroup(self, Name, Color, SpecifiedForSelection, SpecifiedForSectionCutDefinition, SpecifiedForSteelDesign, SpecifiedForConcreteDesign, SpecifiedForAluminumDesign, SpecifiedForColdFormedDesign, SpecifiedForStaticNLActiveStage, SpecifiedForBridgeResponseOutput, SpecifiedForAutoSeismicOutput, SpecifiedForAutoWindOutput, SpecifiedForMassAndWeight):
        """ GetGroup(self: cGroup, Name: str, Color: int, SpecifiedForSelection: bool, SpecifiedForSectionCutDefinition: bool, SpecifiedForSteelDesign: bool, SpecifiedForConcreteDesign: bool, SpecifiedForAluminumDesign: bool, SpecifiedForColdFormedDesign: bool, SpecifiedForStaticNLActiveStage: bool, SpecifiedForBridgeResponseOutput: bool, SpecifiedForAutoSeismicOutput: bool, SpecifiedForAutoWindOutput: bool, SpecifiedForMassAndWeight: bool) -> (int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) """
        pass

    def GetGroup_1(self, Name, color, SpecifiedForSelection, SpecifiedForSectionCutDefinition, SpecifiedForSteelDesign, SpecifiedForConcreteDesign, SpecifiedForAluminumDesign, SpecifiedForStaticNLActiveStage, SpecifiedForAutoSeismicOutput, SpecifiedForAutoWindOutput, SpecifiedForMassAndWeight, SpecifiedForSteelJoistDesign, SpecifiedForWallDesign, SpecifiedForBasePlateDesign, SpecifiedForConnectionDesign):
        """ GetGroup_1(self: cGroup, Name: str, color: int, SpecifiedForSelection: bool, SpecifiedForSectionCutDefinition: bool, SpecifiedForSteelDesign: bool, SpecifiedForConcreteDesign: bool, SpecifiedForAluminumDesign: bool, SpecifiedForStaticNLActiveStage: bool, SpecifiedForAutoSeismicOutput: bool, SpecifiedForAutoWindOutput: bool, SpecifiedForMassAndWeight: bool, SpecifiedForSteelJoistDesign: bool, SpecifiedForWallDesign: bool, SpecifiedForBasePlateDesign: bool, SpecifiedForConnectionDesign: bool) -> (int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cGroup, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def SetGroup(self, Name, Color, SpecifiedForSelection, SpecifiedForSectionCutDefinition, SpecifiedForSteelDesign, SpecifiedForConcreteDesign, SpecifiedForAluminumDesign, SpecifiedForColdFormedDesign, SpecifiedForStaticNLActiveStage, SpecifiedForBridgeResponseOutput, SpecifiedForAutoSeismicOutput, SpecifiedForAutoWindOutput, SpecifiedForMassAndWeight):
        """ SetGroup(self: cGroup, Name: str, Color: int, SpecifiedForSelection: bool, SpecifiedForSectionCutDefinition: bool, SpecifiedForSteelDesign: bool, SpecifiedForConcreteDesign: bool, SpecifiedForAluminumDesign: bool, SpecifiedForColdFormedDesign: bool, SpecifiedForStaticNLActiveStage: bool, SpecifiedForBridgeResponseOutput: bool, SpecifiedForAutoSeismicOutput: bool, SpecifiedForAutoWindOutput: bool, SpecifiedForMassAndWeight: bool) -> int """
        pass

    def SetGroup_1(self, Name, color, SpecifiedForSelection, SpecifiedForSectionCutDefinition, SpecifiedForSteelDesign, SpecifiedForConcreteDesign, SpecifiedForAluminumDesign, SpecifiedForStaticNLActiveStage, SpecifiedForAutoSeismicOutput, SpecifiedForAutoWindOutput, SpecifiedForMassAndWeight, SpecifiedForSteelJoistDesign, SpecifiedForWallDesign, SpecifiedForBasePlateDesign, SpecifiedForConnectionDesign):
        """ SetGroup_1(self: cGroup, Name: str, color: int, SpecifiedForSelection: bool, SpecifiedForSectionCutDefinition: bool, SpecifiedForSteelDesign: bool, SpecifiedForConcreteDesign: bool, SpecifiedForAluminumDesign: bool, SpecifiedForStaticNLActiveStage: bool, SpecifiedForAutoSeismicOutput: bool, SpecifiedForAutoWindOutput: bool, SpecifiedForMassAndWeight: bool, SpecifiedForSteelJoistDesign: bool, SpecifiedForWallDesign: bool, SpecifiedForBasePlateDesign: bool, SpecifiedForConnectionDesign: bool) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cHelper:
    # no doc
    def CreateObject(self, fullPath):
        """ CreateObject(self: cHelper, fullPath: str) -> cOAPI """
        pass

    def CreateObjectHost(self, hostName, fullPath):
        """ CreateObjectHost(self: cHelper, hostName: str, fullPath: str) -> cOAPI """
        pass

    def CreateObjectHostPort(self, hostName, portNumber, fullPath):
        """ CreateObjectHostPort(self: cHelper, hostName: str, portNumber: int, fullPath: str) -> cOAPI """
        pass

    def CreateObjectProgID(self, progID):
        """ CreateObjectProgID(self: cHelper, progID: str) -> cOAPI """
        pass

    def CreateObjectProgIDHost(self, hostName, progID):
        """ CreateObjectProgIDHost(self: cHelper, hostName: str, progID: str) -> cOAPI """
        pass

    def CreateObjectProgIDHostPort(self, hostName, portNumber, progID):
        """ CreateObjectProgIDHostPort(self: cHelper, hostName: str, portNumber: int, progID: str) -> cOAPI """
        pass

    def GetOAPIVersionNumber(self):
        """ GetOAPIVersionNumber(self: cHelper) -> float """
        pass

    def GetObject(self, typeName):
        """ GetObject(self: cHelper, typeName: str) -> cOAPI """
        pass

    def GetObjectHost(self, hostName, progID):
        """ GetObjectHost(self: cHelper, hostName: str, progID: str) -> cOAPI """
        pass

    def GetObjectHostPort(self, hostName, portNumber, progID):
        """ GetObjectHostPort(self: cHelper, hostName: str, portNumber: int, progID: str) -> cOAPI """
        pass

    def GetObjectProcess(self, typeName, pid):
        """ GetObjectProcess(self: cHelper, typeName: str, pid: int) -> cOAPI """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cLineElm:
    # no doc
    def Count(self):
        """ Count(self: cLineElm) -> int """
        pass

    def GetEndLengthOffset(self, Name, Length1, Length2, RZ):
        """ GetEndLengthOffset(self: cLineElm, Name: str, Length1: float, Length2: float, RZ: float) -> (int, float, float, float) """
        pass

    def GetInsertionPoint(self, Name, Offset1, Offset2):
        """ GetInsertionPoint(self: cLineElm, Name: str, Offset1: Array[float], Offset2: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetLoadDistributed(self, Name, NumberItems, LineName, LoadPat, MyType, CSys, Dir, RD1, RD2, Dist1, Dist2, Val1, Val2, ItemTypeElm):
        """ GetLoadDistributed(self: cLineElm, Name: str, NumberItems: int, LineName: Array[str], LoadPat: Array[str], MyType: Array[int], CSys: Array[str], Dir: Array[int], RD1: Array[float], RD2: Array[float], Dist1: Array[float], Dist2: Array[float], Val1: Array[float], Val2: Array[float], ItemTypeElm: eItemTypeElm) -> (int, int, Array[str], Array[str], Array[int], Array[str], Array[int], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLoadPoint(self, Name, NumberItems, LineName, LoadPat, MyType, CSys, Dir, RelDist, Dist, Val, ItemTypeElm):
        """ GetLoadPoint(self: cLineElm, Name: str, NumberItems: int, LineName: Array[str], LoadPat: Array[str], MyType: Array[int], CSys: Array[str], Dir: Array[int], RelDist: Array[float], Dist: Array[float], Val: Array[float], ItemTypeElm: eItemTypeElm) -> (int, int, Array[str], Array[str], Array[int], Array[str], Array[int], Array[float], Array[float], Array[float]) """
        pass

    def GetLoadTemperature(self, Name, NumberItems, LineName, LoadPat, MyType, Val, PatternName, ItemTypeElm):
        """ GetLoadTemperature(self: cLineElm, Name: str, NumberItems: int, LineName: Array[str], LoadPat: Array[str], MyType: Array[int], Val: Array[float], PatternName: Array[str], ItemTypeElm: eItemTypeElm) -> (int, int, Array[str], Array[str], Array[int], Array[float], Array[str]) """
        pass

    def GetLocalAxes(self, Name, Ang):
        """ GetLocalAxes(self: cLineElm, Name: str, Ang: float) -> (int, float) """
        pass

    def GetMaterialOverwrite(self, Name, PropName):
        """ GetMaterialOverwrite(self: cLineElm, Name: str, PropName: str) -> (int, str) """
        pass

    def GetModifiers(self, Name, Value):
        """ GetModifiers(self: cLineElm, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cLineElm, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetObj(self, Name, Obj, ObjType, RDI, RDJ):
        """ GetObj(self: cLineElm, Name: str, Obj: str, ObjType: int, RDI: float, RDJ: float) -> (int, str, int, float, float) """
        pass

    def GetPoints(self, Name, Point1, Point2):
        """ GetPoints(self: cLineElm, Name: str, Point1: str, Point2: str) -> (int, str, str) """
        pass

    def GetProperty(self, Name, PropName, ObjType, Var, SVarRelStartLoc, SVarTotalLength):
        """ GetProperty(self: cLineElm, Name: str, PropName: str, ObjType: int, Var: bool, SVarRelStartLoc: float, SVarTotalLength: float) -> (int, str, int, bool, float, float) """
        pass

    def GetReleases(self, Name, II, JJ, StartValue, EndValue):
        """ GetReleases(self: cLineElm, Name: str, II: Array[bool], JJ: Array[bool], StartValue: Array[float], EndValue: Array[float]) -> (int, Array[bool], Array[bool], Array[float], Array[float]) """
        pass

    def GetTCLimits(self, Name, LimitCompressionExists, LimitCompression, LimitTensionExists, LimitTension):
        """ GetTCLimits(self: cLineElm, Name: str, LimitCompressionExists: bool, LimitCompression: float, LimitTensionExists: bool, LimitTension: float) -> (int, bool, float, bool, float) """
        pass

    def GetTransformationMatrix(self, Name, Value):
        """ GetTransformationMatrix(self: cLineElm, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cLinkElm:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cLinkObj:
    # no doc
    def AddByCoord(self, XI, YI, ZI, XJ, YJ, ZJ, Name, IsSingleJoint, PropName, UserName, CSys):
        """ AddByCoord(self: cLinkObj, XI: float, YI: float, ZI: float, XJ: float, YJ: float, ZJ: float, Name: str, IsSingleJoint: bool, PropName: str, UserName: str, CSys: str) -> (int, str) """
        pass

    def AddByPoint(self, Point1, Point2, Name, IsSingleJoint, PropName, UserName):
        """ AddByPoint(self: cLinkObj, Point1: str, Point2: str, Name: str, IsSingleJoint: bool, PropName: str, UserName: str) -> (int, str) """
        pass

    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cLinkObj, Name: str, NewName: str) -> int """
        pass

    def Count(self):
        """ Count(self: cLinkObj) -> int """
        pass

    def Delete(self, Name, ItemType):
        """ Delete(self: cLinkObj, Name: str, ItemType: eItemType) -> int """
        pass

    def GetElm(self, Name, Elm):
        """ GetElm(self: cLinkObj, Name: str, Elm: str) -> (int, str) """
        pass

    def GetGroupAssign(self, Name, NumberGroups, Groups):
        """ GetGroupAssign(self: cLinkObj, Name: str, NumberGroups: int, Groups: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetGUID(self, Name, GUID):
        """ GetGUID(self: cLinkObj, Name: str, GUID: str) -> (int, str) """
        pass

    def GetLocalAxes(self, Name, Ang, Advanced):
        """ GetLocalAxes(self: cLinkObj, Name: str, Ang: float, Advanced: bool) -> (int, float, bool) """
        pass

    def GetLocalAxesAdvanced(self, Name, Active, AxVectOpt, AxCSys, AxDir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect):
        """ GetLocalAxesAdvanced(self: cLinkObj, Name: str, Active: bool, AxVectOpt: int, AxCSys: str, AxDir: Array[int], AxPt: Array[str], AxVect: Array[float], Plane2: int, PlVectOpt: int, PlCSys: str, PlDir: Array[int], PlPt: Array[str], PlVect: Array[float]) -> (int, bool, int, str, Array[int], Array[str], Array[float], int, int, str, Array[int], Array[str], Array[float]) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cLinkObj, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetNameListOnStory(self, StoryName, NumberNames, MyName):
        """ GetNameListOnStory(self: cLinkObj, StoryName: str, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetPoints(self, Name, Point1, Point2):
        """ GetPoints(self: cLinkObj, Name: str, Point1: str, Point2: str) -> (int, str, str) """
        pass

    def GetProperty(self, Name, PropName):
        """ GetProperty(self: cLinkObj, Name: str, PropName: str) -> (int, str) """
        pass

    def GetSelected(self, Name, Selected):
        """ GetSelected(self: cLinkObj, Name: str, Selected: bool) -> (int, bool) """
        pass

    def GetTransformationMatrix(self, Name, Value, IsGlobal):
        """ GetTransformationMatrix(self: cLinkObj, Name: str, Value: Array[float], IsGlobal: bool) -> (int, Array[float]) """
        pass

    def SetGroupAssign(self, Name, GroupName, Remove, ItemType):
        """ SetGroupAssign(self: cLinkObj, Name: str, GroupName: str, Remove: bool, ItemType: eItemType) -> int """
        pass

    def SetGUID(self, Name, GUID):
        """ SetGUID(self: cLinkObj, Name: str, GUID: str) -> int """
        pass

    def SetLocalAxes(self, Name, Ang, ItemType):
        """ SetLocalAxes(self: cLinkObj, Name: str, Ang: float, ItemType: eItemType) -> int """
        pass

    def SetLocalAxesAdvanced(self, Name, Active, AxVectOpt, AxCSys, AxDir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect, ItemType):
        """ SetLocalAxesAdvanced(self: cLinkObj, Name: str, Active: bool, AxVectOpt: int, AxCSys: str, AxDir: Array[int], AxPt: Array[str], AxVect: Array[float], Plane2: int, PlVectOpt: int, PlCSys: str, PlDir: Array[int], PlPt: Array[str], PlVect: Array[float], ItemType: eItemType) -> (int, Array[int], Array[str], Array[float], Array[int], Array[str], Array[float]) """
        pass

    def SetProperty(self, Name, PropName, ItemType):
        """ SetProperty(self: cLinkObj, Name: str, PropName: str, ItemType: eItemType) -> int """
        pass

    def SetSelected(self, Name, Selected, ItemType):
        """ SetSelected(self: cLinkObj, Name: str, Selected: bool, ItemType: eItemType) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cLoadCases:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cLoadCases, Name: str, NewName: str) -> int """
        pass

    def Count(self, CaseType):
        """ Count(self: cLoadCases, CaseType: eLoadCaseType) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cLoadCases, Name: str) -> int """
        pass

    def GetNameList(self, NumberNames, MyName, CaseType):
        """ GetNameList(self: cLoadCases, NumberNames: int, MyName: Array[str], CaseType: eLoadCaseType) -> (int, int, Array[str]) """
        pass

    def GetTypeOAPI(self, Name, CaseType, SubType):
        """ GetTypeOAPI(self: cLoadCases, Name: str, CaseType: eLoadCaseType, SubType: int) -> (int, eLoadCaseType, int) """
        pass

    def GetTypeOAPI_1(self, Name, CaseType, SubType, DesignType, DesignTypeOption, Auto):
        """ GetTypeOAPI_1(self: cLoadCases, Name: str, CaseType: eLoadCaseType, SubType: int, DesignType: eLoadPatternType, DesignTypeOption: int, Auto: int) -> (int, eLoadCaseType, int, eLoadPatternType, int, int) """
        pass

    def SetDesignType(self, Name, DesignTypeOption, DesignType):
        """ SetDesignType(self: cLoadCases, Name: str, DesignTypeOption: int, DesignType: eLoadPatternType) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Buckling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Buckling(self: cLoadCases) -> cCaseBuckling

"""

    DirHistLinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirHistLinear(self: cLoadCases) -> cCaseDirectHistoryLinear

"""

    DirHistNonlinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirHistNonlinear(self: cLoadCases) -> cCaseDirectHistoryNonlinear

"""

    HyperStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HyperStatic(self: cLoadCases) -> cCaseHyperStatic

"""

    ModalEigen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModalEigen(self: cLoadCases) -> cCaseModalEigen

"""

    ModalRitz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModalRitz(self: cLoadCases) -> cCaseModalRitz

"""

    ModHistLinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModHistLinear(self: cLoadCases) -> cCaseModalHistoryLinear

"""

    ModHistNonlinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModHistNonlinear(self: cLoadCases) -> cCaseModalHistoryNonlinear

"""

    ResponseSpectrum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResponseSpectrum(self: cLoadCases) -> cCaseResponseSpectrum

"""

    StaticLinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticLinear(self: cLoadCases) -> cCaseStaticLinear

"""

    StaticNonlinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticNonlinear(self: cLoadCases) -> cCaseStaticNonlinear

"""

    StaticNonlinearStaged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticNonlinearStaged(self: cLoadCases) -> cCaseStaticNonlinearStaged

"""



class cLoadPatterns:
    # no doc
    def Add(self, Name, MyType, SelfWTMultiplier, AddAnalysisCase):
        """ Add(self: cLoadPatterns, Name: str, MyType: eLoadPatternType, SelfWTMultiplier: float, AddAnalysisCase: bool) -> int """
        pass

    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cLoadPatterns, Name: str, NewName: str) -> int """
        pass

    def Count(self):
        """ Count(self: cLoadPatterns) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cLoadPatterns, Name: str) -> int """
        pass

    def GetAutoSeismicCode(self, Name, CodeName):
        """ GetAutoSeismicCode(self: cLoadPatterns, Name: str, CodeName: str) -> (int, str) """
        pass

    def GetAutoWindCode(self, Name, CodeName):
        """ GetAutoWindCode(self: cLoadPatterns, Name: str, CodeName: str) -> (int, str) """
        pass

    def GetLoadType(self, Name, MyType):
        """ GetLoadType(self: cLoadPatterns, Name: str, MyType: eLoadPatternType) -> (int, eLoadPatternType) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cLoadPatterns, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetSelfWTMultiplier(self, Name, SelfWTMultiplier):
        """ GetSelfWTMultiplier(self: cLoadPatterns, Name: str, SelfWTMultiplier: float) -> (int, float) """
        pass

    def SetLoadType(self, Name, MyType):
        """ SetLoadType(self: cLoadPatterns, Name: str, MyType: eLoadPatternType) -> int """
        pass

    def SetSelfWTMultiplier(self, Name, SelfWTMultiplier):
        """ SetSelfWTMultiplier(self: cLoadPatterns, Name: str, SelfWTMultiplier: float) -> int """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AutoSeismic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSeismic(self: cLoadPatterns) -> cAutoSeismic

"""

    AutoWind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoWind(self: cLoadPatterns) -> cAutoWind

"""



class cNamedDisplay:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cNamedSet:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cOAPI:
    # no doc
    def ApplicationExit(self, FileSave):
        """ ApplicationExit(self: cOAPI, FileSave: bool) -> int """
        pass

    def ApplicationStart(self):
        """ ApplicationStart(self: cOAPI) -> int """
        pass

    def GetOAPIVersionNumber(self):
        """ GetOAPIVersionNumber(self: cOAPI) -> float """
        pass

    def Hide(self):
        """ Hide(self: cOAPI) -> int """
        pass

    def InternalExec(self, operation):
        """ InternalExec(self: cOAPI, operation: int) -> int """
        pass

    def SetAsActiveObject(self):
        """ SetAsActiveObject(self: cOAPI) -> int """
        pass

    def Unhide(self):
        """ Unhide(self: cOAPI) -> int """
        pass

    def UnsetAsActiveObject(self):
        """ UnsetAsActiveObject(self: cOAPI) -> int """
        pass

    def Visible(self):
        """ Visible(self: cOAPI) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SapModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SapModel(self: cOAPI) -> cSapModel

"""



class cOptions:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPattern:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPierLabel:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPierLabel, Name: str, NewName: str) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPierLabel, Name: str) -> int """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cPierLabel, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetPier(self, Name):
        """ GetPier(self: cPierLabel, Name: str) -> int """
        pass

    def GetSectionProperties(self, Name, NumberStories, StoryName, AxisAngle, NumAreaObjs, NumLineObjs, WidthBot, ThicknessBot, WidthTop, ThicknessTop, MatProp, CGBotX, CGBotY, CGBotZ, CGTopX, CGTopY, CGTopZ):
        """ GetSectionProperties(self: cPierLabel, Name: str, NumberStories: int, StoryName: Array[str], AxisAngle: Array[float], NumAreaObjs: Array[int], NumLineObjs: Array[int], WidthBot: Array[float], ThicknessBot: Array[float], WidthTop: Array[float], ThicknessTop: Array[float], MatProp: Array[str], CGBotX: Array[float], CGBotY: Array[float], CGBotZ: Array[float], CGTopX: Array[float], CGTopY: Array[float], CGTopZ: Array[float]) -> (int, int, Array[str], Array[float], Array[int], Array[int], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetPier(self, Name):
        """ SetPier(self: cPierLabel, Name: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPluginCallback:
    # no doc
    def Finish(self, iVal):
        """ Finish(self: cPluginCallback, iVal: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ErrorFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorFlag(self: cPluginCallback) -> int

"""

    Finished = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Finished(self: cPluginCallback) -> bool

"""



class cPluginContract:
    # no doc
    def Info(self, Text):
        """ Info(self: cPluginContract, Text: str) -> (int, str) """
        pass

    def Main(self, SapModel, ISapPlugin):
        """ Main(self: cPluginContract, SapModel: cSapModel, ISapPlugin: cPluginCallback) -> (cSapModel, cPluginCallback) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPointElm:
    # no doc
    def Count(self):
        """ Count(self: cPointElm) -> int """
        pass

    def CountConstraint(self, Count, Name):
        """ CountConstraint(self: cPointElm, Count: int, Name: str) -> (int, int) """
        pass

    def CountLoadDispl(self, Count, Name, LoadPat):
        """ CountLoadDispl(self: cPointElm, Count: int, Name: str, LoadPat: str) -> (int, int) """
        pass

    def CountLoadForce(self, Count, Name, LoadPat):
        """ CountLoadForce(self: cPointElm, Count: int, Name: str, LoadPat: str) -> (int, int) """
        pass

    def CountRestraint(self):
        """ CountRestraint(self: cPointElm) -> int """
        pass

    def CountSpring(self):
        """ CountSpring(self: cPointElm) -> int """
        pass

    def GetConnectivity(self, Name, NumberItems, ObjectType, ObjectName, PointNumber):
        """ GetConnectivity(self: cPointElm, Name: str, NumberItems: int, ObjectType: Array[int], ObjectName: Array[str], PointNumber: Array[int]) -> (int, int, Array[int], Array[str], Array[int]) """
        pass

    def GetConstraint(self, Name, NumberItems, PointName, ConstraintName, ItemTypeElm):
        """ GetConstraint(self: cPointElm, Name: str, NumberItems: int, PointName: Array[str], ConstraintName: Array[str], ItemTypeElm: eItemTypeElm) -> (int, int, Array[str], Array[str]) """
        pass

    def GetCoordCartesian(self, Name, X, Y, Z, CSys):
        """ GetCoordCartesian(self: cPointElm, Name: str, X: float, Y: float, Z: float, CSys: str) -> (int, float, float, float) """
        pass

    def GetLoadDispl(self, Name, NumberItems, PointName, LoadPat, LcStep, CSys, U1, U2, U3, R1, R2, R3, ItemTypeElm):
        """ GetLoadDispl(self: cPointElm, Name: str, NumberItems: int, PointName: Array[str], LoadPat: Array[str], LcStep: Array[int], CSys: Array[str], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float], ItemTypeElm: eItemTypeElm) -> (int, int, Array[str], Array[str], Array[int], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLoadForce(self, Name, NumberItems, PointName, LoadPat, LcStep, CSys, F1, F2, F3, M1, M2, M3, ItemTypeElm):
        """ GetLoadForce(self: cPointElm, Name: str, NumberItems: int, PointName: Array[str], LoadPat: Array[str], LcStep: Array[int], CSys: Array[str], F1: Array[float], F2: Array[float], F3: Array[float], M1: Array[float], M2: Array[float], M3: Array[float], ItemTypeElm: eItemTypeElm) -> (int, int, Array[str], Array[str], Array[int], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLocalAxes(self, Name, A, B, C):
        """ GetLocalAxes(self: cPointElm, Name: str, A: float, B: float, C: float) -> (int, float, float, float) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cPointElm, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetObj(self, Name, Obj, ObjType):
        """ GetObj(self: cPointElm, Name: str, Obj: str, ObjType: int) -> (int, str, int) """
        pass

    def GetPatternValue(self, Name, PatternName, Value):
        """ GetPatternValue(self: cPointElm, Name: str, PatternName: str, Value: float) -> (int, float) """
        pass

    def GetRestraint(self, Name, Value):
        """ GetRestraint(self: cPointElm, Name: str, Value: Array[bool]) -> (int, Array[bool]) """
        pass

    def GetSpring(self, Name, K):
        """ GetSpring(self: cPointElm, Name: str, K: Array[float]) -> (int, Array[float]) """
        pass

    def GetSpringCoupled(self, Name, K):
        """ GetSpringCoupled(self: cPointElm, Name: str, K: Array[float]) -> (int, Array[float]) """
        pass

    def GetTransformationMatrix(self, Name, Value):
        """ GetTransformationMatrix(self: cPointElm, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def IsSpringCoupled(self, Name, IsCoupled):
        """ IsSpringCoupled(self: cPointElm, Name: str, IsCoupled: bool) -> (int, bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPointObj:
    # no doc
    def AddCartesian(self, X, Y, Z, Name, UserName, CSys, MergeOff, MergeNumber):
        """ AddCartesian(self: cPointObj, X: float, Y: float, Z: float, Name: str, UserName: str, CSys: str, MergeOff: bool, MergeNumber: int) -> (int, str) """
        pass

    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPointObj, Name: str, NewName: str) -> int """
        pass

    def Count(self):
        """ Count(self: cPointObj) -> int """
        pass

    def CountLoadDispl(self, Count, Name, LoadPat):
        """ CountLoadDispl(self: cPointObj, Count: int, Name: str, LoadPat: str) -> (int, int) """
        pass

    def CountLoadForce(self, Count, Name, LoadPat):
        """ CountLoadForce(self: cPointObj, Count: int, Name: str, LoadPat: str) -> (int, int) """
        pass

    def CountPanelZone(self):
        """ CountPanelZone(self: cPointObj) -> int """
        pass

    def CountRestraint(self):
        """ CountRestraint(self: cPointObj) -> int """
        pass

    def CountSpring(self):
        """ CountSpring(self: cPointObj) -> int """
        pass

    def DeleteLoadDispl(self, Name, LoadPat, ItemType):
        """ DeleteLoadDispl(self: cPointObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteLoadForce(self, Name, LoadPat, ItemType):
        """ DeleteLoadForce(self: cPointObj, Name: str, LoadPat: str, ItemType: eItemType) -> int """
        pass

    def DeleteMass(self, Name, ItemType):
        """ DeleteMass(self: cPointObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeletePanelZone(self, Name, ItemType):
        """ DeletePanelZone(self: cPointObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteRestraint(self, Name, ItemType):
        """ DeleteRestraint(self: cPointObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteSpecialPoint(self, Name, ItemType):
        """ DeleteSpecialPoint(self: cPointObj, Name: str, ItemType: eItemType) -> int """
        pass

    def DeleteSpring(self, Name, ItemType):
        """ DeleteSpring(self: cPointObj, Name: str, ItemType: eItemType) -> int """
        pass

    def GetAllPoints(self, NumberNames, MyName, X, Y, Z, csys):
        """ GetAllPoints(self: cPointObj, NumberNames: int, MyName: Array[str], X: Array[float], Y: Array[float], Z: Array[float], csys: str) -> (int, int, Array[str], Array[float], Array[float], Array[float]) """
        pass

    def GetCommonTo(self, Name, CommonTo):
        """ GetCommonTo(self: cPointObj, Name: str, CommonTo: int) -> (int, int) """
        pass

    def GetConnectivity(self, Name, NumberItems, ObjectType, ObjectName, PointNumber):
        """ GetConnectivity(self: cPointObj, Name: str, NumberItems: int, ObjectType: Array[int], ObjectName: Array[str], PointNumber: Array[int]) -> (int, int, Array[int], Array[str], Array[int]) """
        pass

    def GetCoordCartesian(self, Name, X, Y, Z, CSys):
        """ GetCoordCartesian(self: cPointObj, Name: str, X: float, Y: float, Z: float, CSys: str) -> (int, float, float, float) """
        pass

    def GetCoordCylindrical(self, Name, R, Theta, Z, CSys):
        """ GetCoordCylindrical(self: cPointObj, Name: str, R: float, Theta: float, Z: float, CSys: str) -> (int, float, float, float) """
        pass

    def GetCoordSpherical(self, Name, R, A, B, CSys):
        """ GetCoordSpherical(self: cPointObj, Name: str, R: float, A: float, B: float, CSys: str) -> (int, float, float, float) """
        pass

    def GetDiaphragm(self, Name, DiaphragmOption, DiaphragmName):
        """ GetDiaphragm(self: cPointObj, Name: str, DiaphragmOption: eDiaphragmOption, DiaphragmName: str) -> (int, eDiaphragmOption, str) """
        pass

    def GetElm(self, Name, Elm):
        """ GetElm(self: cPointObj, Name: str, Elm: str) -> (int, str) """
        pass

    def GetGroupAssign(self, Name, NumberGroups, Groups):
        """ GetGroupAssign(self: cPointObj, Name: str, NumberGroups: int, Groups: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetGUID(self, Name, GUID):
        """ GetGUID(self: cPointObj, Name: str, GUID: str) -> (int, str) """
        pass

    def GetLabelFromName(self, Name, Label, Story):
        """ GetLabelFromName(self: cPointObj, Name: str, Label: str, Story: str) -> (int, str, str) """
        pass

    def GetLabelNameList(self, NumberNames, MyName, MyLabel, MyStory):
        """ GetLabelNameList(self: cPointObj, NumberNames: int, MyName: Array[str], MyLabel: Array[str], MyStory: Array[str]) -> (int, int, Array[str], Array[str], Array[str]) """
        pass

    def GetLoadDispl(self, Name, NumberItems, PointName, LoadPat, LcStep, CSys, U1, U2, U3, R1, R2, R3, ItemType):
        """ GetLoadDispl(self: cPointObj, Name: str, NumberItems: int, PointName: Array[str], LoadPat: Array[str], LcStep: Array[int], CSys: Array[str], U1: Array[float], U2: Array[float], U3: Array[float], R1: Array[float], R2: Array[float], R3: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[int], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLoadForce(self, Name, NumberItems, PointName, LoadPat, LcStep, CSys, F1, F2, F3, M1, M2, M3, ItemType):
        """ GetLoadForce(self: cPointObj, Name: str, NumberItems: int, PointName: Array[str], LoadPat: Array[str], LcStep: Array[int], CSys: Array[str], F1: Array[float], F2: Array[float], F3: Array[float], M1: Array[float], M2: Array[float], M3: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[int], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLocalAxes(self, Name, A, B, C, Advanced):
        """ GetLocalAxes(self: cPointObj, Name: str, A: float, B: float, C: float, Advanced: bool) -> (int, float, float, float, bool) """
        pass

    def GetMass(self, Name, M):
        """ GetMass(self: cPointObj, Name: str, M: Array[float]) -> (int, Array[float]) """
        pass

    def GetNameFromLabel(self, Label, Story, Name):
        """ GetNameFromLabel(self: cPointObj, Label: str, Story: str, Name: str) -> (int, str) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cPointObj, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetNameListOnStory(self, StoryName, NumberNames, MyName):
        """ GetNameListOnStory(self: cPointObj, StoryName: str, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetPanelZone(self, Name, PropType, Thickness, K1, K2, LinkProp, Connectivity, LocalAxisFrom, LocalAxisAngle):
        """ GetPanelZone(self: cPointObj, Name: str, PropType: int, Thickness: float, K1: float, K2: float, LinkProp: str, Connectivity: int, LocalAxisFrom: int, LocalAxisAngle: float) -> (int, int, float, float, float, str, int, int, float) """
        pass

    def GetRestraint(self, Name, Value):
        """ GetRestraint(self: cPointObj, Name: str, Value: Array[bool]) -> (int, Array[bool]) """
        pass

    def GetSelected(self, Name, Selected):
        """ GetSelected(self: cPointObj, Name: str, Selected: bool) -> (int, bool) """
        pass

    def GetSpecialPoint(self, Name, SpecialPoint):
        """ GetSpecialPoint(self: cPointObj, Name: str, SpecialPoint: bool) -> (int, bool) """
        pass

    def GetSpring(self, Name, K):
        """ GetSpring(self: cPointObj, Name: str, K: Array[float]) -> (int, Array[float]) """
        pass

    def GetSpringAssignment(self, Name, SpringProp):
        """ GetSpringAssignment(self: cPointObj, Name: str, SpringProp: str) -> (int, str) """
        pass

    def GetSpringCoupled(self, Name, K):
        """ GetSpringCoupled(self: cPointObj, Name: str, K: Array[float]) -> (int, Array[float]) """
        pass

    def GetTransformationMatrix(self, Name, Value, IsGlobal):
        """ GetTransformationMatrix(self: cPointObj, Name: str, Value: Array[float], IsGlobal: bool) -> (int, Array[float]) """
        pass

    def IsSpringCoupled(self, Name, IsCoupled):
        """ IsSpringCoupled(self: cPointObj, Name: str, IsCoupled: bool) -> (int, bool) """
        pass

    def SetDiaphragm(self, Name, DiaphragmOption, DiaphragmName):
        """ SetDiaphragm(self: cPointObj, Name: str, DiaphragmOption: eDiaphragmOption, DiaphragmName: str) -> int """
        pass

    def SetGroupAssign(self, Name, GroupName, Remove, ItemType):
        """ SetGroupAssign(self: cPointObj, Name: str, GroupName: str, Remove: bool, ItemType: eItemType) -> int """
        pass

    def SetGUID(self, Name, GUID):
        """ SetGUID(self: cPointObj, Name: str, GUID: str) -> int """
        pass

    def SetLoadDispl(self, Name, LoadPat, Value, Replace, CSys, ItemType):
        """ SetLoadDispl(self: cPointObj, Name: str, LoadPat: str, Value: Array[float], Replace: bool, CSys: str, ItemType: eItemType) -> (int, Array[float]) """
        pass

    def SetLoadForce(self, Name, LoadPat, Value, Replace, CSys, ItemType):
        """ SetLoadForce(self: cPointObj, Name: str, LoadPat: str, Value: Array[float], Replace: bool, CSys: str, ItemType: eItemType) -> (int, Array[float]) """
        pass

    def SetMass(self, Name, M, ItemType, IsLocalCSys, Replace):
        """ SetMass(self: cPointObj, Name: str, M: Array[float], ItemType: eItemType, IsLocalCSys: bool, Replace: bool) -> (int, Array[float]) """
        pass

    def SetMassByVolume(self, Name, MatProp, M, ItemType, IsLocalCSys, Replace):
        """ SetMassByVolume(self: cPointObj, Name: str, MatProp: str, M: Array[float], ItemType: eItemType, IsLocalCSys: bool, Replace: bool) -> (int, Array[float]) """
        pass

    def SetMassByWeight(self, Name, M, ItemType, IsLocalCSys, Replace):
        """ SetMassByWeight(self: cPointObj, Name: str, M: Array[float], ItemType: eItemType, IsLocalCSys: bool, Replace: bool) -> (int, Array[float]) """
        pass

    def SetPanelZone(self, Name, PropType, Thickness, K1, K2, LinkProp, Connectivity, LocalAxisFrom, LocalAxisAngle, ItemType):
        """ SetPanelZone(self: cPointObj, Name: str, PropType: int, Thickness: float, K1: float, K2: float, LinkProp: str, Connectivity: int, LocalAxisFrom: int, LocalAxisAngle: float, ItemType: eItemType) -> int """
        pass

    def SetRestraint(self, Name, Value, ItemType):
        """ SetRestraint(self: cPointObj, Name: str, Value: Array[bool], ItemType: eItemType) -> (int, Array[bool]) """
        pass

    def SetSelected(self, Name, Selected, ItemType):
        """ SetSelected(self: cPointObj, Name: str, Selected: bool, ItemType: eItemType) -> int """
        pass

    def SetSpecialPoint(self, Name, SpecialPoint, ItemType):
        """ SetSpecialPoint(self: cPointObj, Name: str, SpecialPoint: bool, ItemType: eItemType) -> int """
        pass

    def SetSpring(self, Name, K, ItemType, IsLocalCSys, Replace):
        """ SetSpring(self: cPointObj, Name: str, K: Array[float], ItemType: eItemType, IsLocalCSys: bool, Replace: bool) -> (int, Array[float]) """
        pass

    def SetSpringAssignment(self, Name, SpringProp, ItemType):
        """ SetSpringAssignment(self: cPointObj, Name: str, SpringProp: str, ItemType: eItemType) -> int """
        pass

    def SetSpringCoupled(self, Name, K, ItemType, IsLocalCSys, Replace):
        """ SetSpringCoupled(self: cPointObj, Name: str, K: Array[float], ItemType: eItemType, IsLocalCSys: bool, Replace: bool) -> (int, Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropArea:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPropArea, Name: str, NewName: str) -> int """
        pass

    def Count(self, PropType):
        """ Count(self: cPropArea, PropType: int) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPropArea, Name: str) -> int """
        pass

    def GetDeck(self, Name, DeckType, ShellType, MatProp, Thickness, color, notes, GUID):
        """ GetDeck(self: cPropArea, Name: str, DeckType: eDeckType, ShellType: eShellType, MatProp: str, Thickness: float, color: int, notes: str, GUID: str) -> (int, eDeckType, eShellType, str, float, int, str, str) """
        pass

    def GetDeckFilled(self, Name, SlabDepth, RibDepth, RibWidthTop, RibWidthBot, RibSpacing, ShearThickness, UnitWeight, ShearStudDia, ShearStudHt, ShearStudFu):
        """ GetDeckFilled(self: cPropArea, Name: str, SlabDepth: float, RibDepth: float, RibWidthTop: float, RibWidthBot: float, RibSpacing: float, ShearThickness: float, UnitWeight: float, ShearStudDia: float, ShearStudHt: float, ShearStudFu: float) -> (int, float, float, float, float, float, float, float, float, float, float) """
        pass

    def GetDeckSolidSlab(self, Name, SlabDepth, ShearStudDia, ShearStudHt, ShearStudFu):
        """ GetDeckSolidSlab(self: cPropArea, Name: str, SlabDepth: float, ShearStudDia: float, ShearStudHt: float, ShearStudFu: float) -> (int, float, float, float, float) """
        pass

    def GetDeckUnfilled(self, Name, RibDepth, RibWidthTop, RibWidthBot, RibSpacing, ShearThickness, UnitWeight):
        """ GetDeckUnfilled(self: cPropArea, Name: str, RibDepth: float, RibWidthTop: float, RibWidthBot: float, RibSpacing: float, ShearThickness: float, UnitWeight: float) -> (int, float, float, float, float, float, float) """
        pass

    def GetModifiers(self, Name, Value):
        """ GetModifiers(self: cPropArea, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def GetNameList(self, NumberNames, MyName, PropType):
        """ GetNameList(self: cPropArea, NumberNames: int, MyName: Array[str], PropType: int) -> (int, int, Array[str]) """
        pass

    def GetShellDesign(self, Name, MatProp, SteelLayoutOption, DesignCoverTopDir1, DesignCoverTopDir2, DesignCoverBotDir1, DesignCoverBotDir2):
        """ GetShellDesign(self: cPropArea, Name: str, MatProp: str, SteelLayoutOption: int, DesignCoverTopDir1: float, DesignCoverTopDir2: float, DesignCoverBotDir1: float, DesignCoverBotDir2: float) -> (int, str, int, float, float, float, float) """
        pass

    def GetShellLayer(self, Name, NumberLayers, LayerName, Dist, Thickness, MatProp, Nonlinear, MatAng, NumIntegrationPts):
        """ GetShellLayer(self: cPropArea, Name: str, NumberLayers: int, LayerName: Array[str], Dist: Array[float], Thickness: Array[float], MatProp: Array[str], Nonlinear: Array[bool], MatAng: Array[float], NumIntegrationPts: Array[int]) -> (int, int, Array[str], Array[float], Array[float], Array[str], Array[bool], Array[float], Array[int]) """
        pass

    def GetShellLayer_1(self, Name, NumberLayers, LayerName, Dist, Thickness, MyType, NumIntegrationPts, MatProp, MatAng, S11Type, S22Type, S12Type):
        """ GetShellLayer_1(self: cPropArea, Name: str, NumberLayers: int, LayerName: Array[str], Dist: Array[float], Thickness: Array[float], MyType: Array[int], NumIntegrationPts: Array[int], MatProp: Array[str], MatAng: Array[float], S11Type: Array[int], S22Type: Array[int], S12Type: Array[int]) -> (int, int, Array[str], Array[float], Array[float], Array[int], Array[int], Array[str], Array[float], Array[int], Array[int], Array[int]) """
        pass

    def GetShellLayer_2(self, Name, NumberLayers, LayerName, Dist, Thickness, MyType, NumIntegrationPts, MatProp, MatAng, MatBehavior, S11Type, S22Type, S12Type):
        """ GetShellLayer_2(self: cPropArea, Name: str, NumberLayers: int, LayerName: Array[str], Dist: Array[float], Thickness: Array[float], MyType: Array[int], NumIntegrationPts: Array[int], MatProp: Array[str], MatAng: Array[float], MatBehavior: Array[int], S11Type: Array[int], S22Type: Array[int], S12Type: Array[int]) -> (int, int, Array[str], Array[float], Array[float], Array[int], Array[int], Array[str], Array[float], Array[int], Array[int], Array[int], Array[int]) """
        pass

    def GetSlab(self, Name, SlabType, ShellType, MatProp, Thickness, color, notes, GUID):
        """ GetSlab(self: cPropArea, Name: str, SlabType: eSlabType, ShellType: eShellType, MatProp: str, Thickness: float, color: int, notes: str, GUID: str) -> (int, eSlabType, eShellType, str, float, int, str, str) """
        pass

    def GetSlabRibbed(self, Name, OverallDepth, SlabThickness, StemWidthTop, StemWidthBot, RibSpacing, RibsParallelTo):
        """ GetSlabRibbed(self: cPropArea, Name: str, OverallDepth: float, SlabThickness: float, StemWidthTop: float, StemWidthBot: float, RibSpacing: float, RibsParallelTo: int) -> (int, float, float, float, float, float, int) """
        pass

    def GetSlabWaffle(self, Name, OverallDepth, SlabThickness, StemWidthTop, StemWidthBot, RibSpacingDir1, RibSpacingDir2):
        """ GetSlabWaffle(self: cPropArea, Name: str, OverallDepth: float, SlabThickness: float, StemWidthTop: float, StemWidthBot: float, RibSpacingDir1: float, RibSpacingDir2: float) -> (int, float, float, float, float, float, float) """
        pass

    def GetTypeOAPI(self, Name, PropType):
        """ GetTypeOAPI(self: cPropArea, Name: str, PropType: int) -> (int, int) """
        pass

    def GetWall(self, Name, WallPropType, ShellType, MatProp, Thickness, color, notes, GUID):
        """ GetWall(self: cPropArea, Name: str, WallPropType: eWallPropType, ShellType: eShellType, MatProp: str, Thickness: float, color: int, notes: str, GUID: str) -> (int, eWallPropType, eShellType, str, float, int, str, str) """
        pass

    def GetWallAutoSelectList(self, Name, AutoSelectList, StartingProperty):
        """ GetWallAutoSelectList(self: cPropArea, Name: str, AutoSelectList: Array[str], StartingProperty: str) -> (int, Array[str], str) """
        pass

    def SetDeck(self, Name, DeckType, ShellType, MatProp, Thickness, color, notes, GUID):
        """ SetDeck(self: cPropArea, Name: str, DeckType: eDeckType, ShellType: eShellType, MatProp: str, Thickness: float, color: int, notes: str, GUID: str) -> int """
        pass

    def SetDeckFilled(self, Name, SlabDepth, RibDepth, RibWidthTop, RibWidthBot, RibSpacing, ShearThickness, UnitWeight, ShearStudDia, ShearStudHt, ShearStudFu):
        """ SetDeckFilled(self: cPropArea, Name: str, SlabDepth: float, RibDepth: float, RibWidthTop: float, RibWidthBot: float, RibSpacing: float, ShearThickness: float, UnitWeight: float, ShearStudDia: float, ShearStudHt: float, ShearStudFu: float) -> int """
        pass

    def SetDeckSolidSlab(self, Name, SlabDepth, ShearStudDia, ShearStudHt, ShearStudFu):
        """ SetDeckSolidSlab(self: cPropArea, Name: str, SlabDepth: float, ShearStudDia: float, ShearStudHt: float, ShearStudFu: float) -> int """
        pass

    def SetDeckUnfilled(self, Name, RibDepth, RibWidthTop, RibWidthBot, RibSpacing, ShearThickness, UnitWeight):
        """ SetDeckUnfilled(self: cPropArea, Name: str, RibDepth: float, RibWidthTop: float, RibWidthBot: float, RibSpacing: float, ShearThickness: float, UnitWeight: float) -> int """
        pass

    def SetModifiers(self, Name, Value):
        """ SetModifiers(self: cPropArea, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def SetShellDesign(self, Name, MatProp, SteelLayoutOption, DesignCoverTopDir1, DesignCoverTopDir2, DesignCoverBotDir1, DesignCoverBotDir2):
        """ SetShellDesign(self: cPropArea, Name: str, MatProp: str, SteelLayoutOption: int, DesignCoverTopDir1: float, DesignCoverTopDir2: float, DesignCoverBotDir1: float, DesignCoverBotDir2: float) -> int """
        pass

    def SetShellLayer(self, Name, NumberLayers, LayerName, Dist, Thickness, MatProp, Nonlinear, MatAng, NumIntegrationPts):
        """ SetShellLayer(self: cPropArea, Name: str, NumberLayers: int, LayerName: Array[str], Dist: Array[float], Thickness: Array[float], MatProp: Array[str], Nonlinear: Array[bool], MatAng: Array[float], NumIntegrationPts: Array[int]) -> (int, Array[str], Array[float], Array[float], Array[str], Array[bool], Array[float], Array[int]) """
        pass

    def SetShellLayer_1(self, Name, NumberLayers, LayerName, Dist, Thickness, MyType, NumIntegrationPts, MatProp, MatAng, S11Type, S22Type, S12Type):
        """ SetShellLayer_1(self: cPropArea, Name: str, NumberLayers: int, LayerName: Array[str], Dist: Array[float], Thickness: Array[float], MyType: Array[int], NumIntegrationPts: Array[int], MatProp: Array[str], MatAng: Array[float], S11Type: Array[int], S22Type: Array[int], S12Type: Array[int]) -> (int, int, Array[str], Array[float], Array[float], Array[int], Array[int], Array[str], Array[float], Array[int], Array[int], Array[int]) """
        pass

    def SetShellLayer_2(self, Name, NumberLayers, LayerName, Dist, Thickness, MyType, NumIntegrationPts, MatProp, MatAng, MatBehavior, S11Type, S22Type, S12Type):
        """ SetShellLayer_2(self: cPropArea, Name: str, NumberLayers: int, LayerName: Array[str], Dist: Array[float], Thickness: Array[float], MyType: Array[int], NumIntegrationPts: Array[int], MatProp: Array[str], MatAng: Array[float], MatBehavior: Array[int], S11Type: Array[int], S22Type: Array[int], S12Type: Array[int]) -> (int, int, Array[str], Array[float], Array[float], Array[int], Array[int], Array[str], Array[float], Array[int], Array[int], Array[int], Array[int]) """
        pass

    def SetSlab(self, Name, SlabType, ShellType, MatProp, Thickness, color, notes, GUID):
        """ SetSlab(self: cPropArea, Name: str, SlabType: eSlabType, ShellType: eShellType, MatProp: str, Thickness: float, color: int, notes: str, GUID: str) -> int """
        pass

    def SetSlabRibbed(self, Name, OverallDepth, SlabThickness, StemWidthTop, StemWidthBot, RibSpacing, RibsParallelTo):
        """ SetSlabRibbed(self: cPropArea, Name: str, OverallDepth: float, SlabThickness: float, StemWidthTop: float, StemWidthBot: float, RibSpacing: float, RibsParallelTo: int) -> int """
        pass

    def SetSlabWaffle(self, Name, OverallDepth, SlabThickness, StemWidthTop, StemWidthBot, RibSpacingDir1, RibSpacingDir2):
        """ SetSlabWaffle(self: cPropArea, Name: str, OverallDepth: float, SlabThickness: float, StemWidthTop: float, StemWidthBot: float, RibSpacingDir1: float, RibSpacingDir2: float) -> int """
        pass

    def SetWall(self, Name, WallPropType, ShellType, MatProp, Thickness, color, notes, GUID):
        """ SetWall(self: cPropArea, Name: str, WallPropType: eWallPropType, ShellType: eShellType, MatProp: str, Thickness: float, color: int, notes: str, GUID: str) -> int """
        pass

    def SetWallAutoSelectList(self, Name, AutoSelectList, StartingProperty):
        """ SetWallAutoSelectList(self: cPropArea, Name: str, AutoSelectList: Array[str], StartingProperty: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropAreaSpring:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPropAreaSpring, Name: str, NewName: str) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPropAreaSpring, Name: str) -> int """
        pass

    def GetAreaSpringProp(self, Name, U1, U2, U3, NonlinearOption3, SpringOption, SoilProfile, EndLengthRatio, Period, color, notes, iGUID):
        """ GetAreaSpringProp(self: cPropAreaSpring, Name: str, U1: float, U2: float, U3: float, NonlinearOption3: int, SpringOption: int, SoilProfile: str, EndLengthRatio: float, Period: float, color: int, notes: str, iGUID: str) -> (int, float, float, float, int, int, str, float, float, int, str, str) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cPropAreaSpring, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def SetAreaSpringProp(self, Name, U1, U2, U3, NonlinearOption3, SpringOption, SoilProfile, EndLengthRatio, Period, color, notes, iGUID):
        """ SetAreaSpringProp(self: cPropAreaSpring, Name: str, U1: float, U2: float, U3: float, NonlinearOption3: int, SpringOption: int, SoilProfile: str, EndLengthRatio: float, Period: float, color: int, notes: str, iGUID: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropFrame:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPropFrame, Name: str, NewName: str) -> int """
        pass

    def Count(self, PropType):
        """ Count(self: cPropFrame, PropType: eFramePropType) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPropFrame, Name: str) -> int """
        pass

    def GetAllFrameProperties(self, NumberNames, MyName, PropType, t3, t2, tf, tw, t2b, tfb):
        """ GetAllFrameProperties(self: cPropFrame, NumberNames: int, MyName: Array[str], PropType: Array[eFramePropType], t3: Array[float], t2: Array[float], tf: Array[float], tw: Array[float], t2b: Array[float], tfb: Array[float]) -> (int, int, Array[str], Array[eFramePropType], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetAllFrameProperties_2(self, NumberNames, MyName, PropType, t3, t2, tf, tw, t2b, tfb, Area):
        """ GetAllFrameProperties_2(self: cPropFrame, NumberNames: int, MyName: Array[str], PropType: Array[eFramePropType], t3: Array[float], t2: Array[float], tf: Array[float], tw: Array[float], t2b: Array[float], tfb: Array[float], Area: Array[float]) -> (int, int, Array[str], Array[eFramePropType], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetAngle(self, Name, FileName, MatProp, T3, T2, Tf, Tw, Color, Notes, GUID):
        """ GetAngle(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, int, str, str) """
        pass

    def GetAutoSelectSteel(self, Name, NumberItems, SectName, AutoStartSection, Notes, GUID):
        """ GetAutoSelectSteel(self: cPropFrame, Name: str, NumberItems: int, SectName: Array[str], AutoStartSection: str, Notes: str, GUID: str) -> (int, int, Array[str], str, str, str) """
        pass

    def GetChannel(self, Name, FileName, MatProp, T3, T2, Tf, Tw, Color, Notes, GUID):
        """ GetChannel(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, int, str, str) """
        pass

    def GetCircle(self, Name, FileName, MatProp, T3, Color, Notes, GUID):
        """ GetCircle(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, int, str, str) """
        pass

    def GetConcreteL(self, Name, FileName, MatProp, T3, T2, Tf, TwC, TwT, MirrorAbout2, MirrorAbout3, Color, Notes, GUID):
        """ GetConcreteL(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, TwC: float, TwT: float, MirrorAbout2: bool, MirrorAbout3: bool, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, float, bool, bool, int, str, str) """
        pass

    def GetConcreteTee(self, Name, FileName, MatProp, T3, T2, Tf, TwF, TwT, MirrorAbout3, Color, Notes, GUID):
        """ GetConcreteTee(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, TwF: float, TwT: float, MirrorAbout3: bool, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, float, bool, int, str, str) """
        pass

    def GetCoverPlatedI(self, Name, SectName, FyTopFlange, FyWeb, FyBotFlange, Tc, Bc, MatPropTop, Tcb, Bcb, MatPropBot, Color, Notes, GUID):
        """ GetCoverPlatedI(self: cPropFrame, Name: str, SectName: str, FyTopFlange: float, FyWeb: float, FyBotFlange: float, Tc: float, Bc: float, MatPropTop: str, Tcb: float, Bcb: float, MatPropBot: str, Color: int, Notes: str, GUID: str) -> (int, str, float, float, float, float, float, str, float, float, str, int, str, str) """
        pass

    def GetDblAngle(self, Name, FileName, MatProp, T3, T2, Tf, Tw, Dis, Color, Notes, GUID):
        """ GetDblAngle(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Dis: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, float, int, str, str) """
        pass

    def GetDblChannel(self, Name, FileName, MatProp, T3, T2, Tf, Tw, Dis, Color, Notes, GUID):
        """ GetDblChannel(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Dis: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, float, int, str, str) """
        pass

    def GetGeneral(self, Name, FileName, MatProp, T3, T2, Area, As2, As3, Torsion, I22, I33, S22, S33, Z22, Z33, R22, R33, Color, Notes, GUID):
        """ GetGeneral(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Area: float, As2: float, As3: float, Torsion: float, I22: float, I33: float, S22: float, S33: float, Z22: float, Z33: float, R22: float, R33: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, float, float, float, float, float, float, float, float, float, float, int, str, str) """
        pass

    def GetISection(self, Name, FileName, MatProp, T3, T2, Tf, Tw, T2b, Tfb, Color, Notes, GUID):
        """ GetISection(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, T2b: float, Tfb: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, float, float, int, str, str) """
        pass

    def GetMaterial(self, Name, MatProp):
        """ GetMaterial(self: cPropFrame, Name: str, MatProp: str) -> (int, str) """
        pass

    def GetModifiers(self, Name, Value):
        """ GetModifiers(self: cPropFrame, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def GetNameInPropFile(self, Name, NameInFile, FileName, MatProp, PropType):
        """ GetNameInPropFile(self: cPropFrame, Name: str, NameInFile: str, FileName: str, MatProp: str, PropType: eFramePropType) -> (int, str, str, str, eFramePropType) """
        pass

    def GetNameList(self, NumberNames, MyName, PropType):
        """ GetNameList(self: cPropFrame, NumberNames: int, MyName: Array[str], PropType: eFramePropType) -> (int, int, Array[str]) """
        pass

    def GetNonPrismatic(self, Name, NumberItems, StartSec, EndSec, MyLength, MyType, EI33, EI22, Color, Notes, GUID):
        """ GetNonPrismatic(self: cPropFrame, Name: str, NumberItems: int, StartSec: Array[str], EndSec: Array[str], MyLength: Array[float], MyType: Array[int], EI33: Array[int], EI22: Array[int], Color: int, Notes: str, GUID: str) -> (int, int, Array[str], Array[str], Array[float], Array[int], Array[int], Array[int], int, str, str) """
        pass

    def GetPipe(self, Name, FileName, MatProp, T3, TW, Color, Notes, GUID):
        """ GetPipe(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, TW: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, int, str, str) """
        pass

    def GetPlate(self, Name, FileName, MatProp, T3, T2, Color, Notes, GUID):
        """ GetPlate(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, int, str, str) """
        pass

    def GetPropFileNameList(self, FileName, NumberNames, MyName, MyPropType, PropType):
        """ GetPropFileNameList(self: cPropFrame, FileName: str, NumberNames: int, MyName: Array[str], MyPropType: Array[eFramePropType], PropType: eFramePropType) -> (int, int, Array[str], Array[eFramePropType]) """
        pass

    def GetRebarBeam(self, Name, MatPropLong, MatPropConfine, CoverTop, CoverBot, TopLeftArea, TopRightArea, BotLeftArea, BotRightArea):
        """ GetRebarBeam(self: cPropFrame, Name: str, MatPropLong: str, MatPropConfine: str, CoverTop: float, CoverBot: float, TopLeftArea: float, TopRightArea: float, BotLeftArea: float, BotRightArea: float) -> (int, str, str, float, float, float, float, float, float) """
        pass

    def GetRebarColumn(self, Name, MatPropLong, MatPropConfine, Pattern, ConfineType, Cover, NumberCBars, NumberR3Bars, NumberR2Bars, RebarSize, TieSize, TieSpacingLongit, Number2DirTieBars, Number3DirTieBars, ToBeDesigned):
        """ GetRebarColumn(self: cPropFrame, Name: str, MatPropLong: str, MatPropConfine: str, Pattern: int, ConfineType: int, Cover: float, NumberCBars: int, NumberR3Bars: int, NumberR2Bars: int, RebarSize: str, TieSize: str, TieSpacingLongit: float, Number2DirTieBars: int, Number3DirTieBars: int, ToBeDesigned: bool) -> (int, str, str, int, int, float, int, int, int, str, str, float, int, int, bool) """
        pass

    def GetRebarColumn_1(self, Name, MatPropLong, MatPropConfine, Pattern, ConfineType, Cover, NumberCBars, NumberR3Bars, NumberR2Bars, RebarSize, TieSize, TieSpacingLongit, Number2DirTieBars, Number3DirTieBars, ToBeDesigned, LongitCornerRebarSize, LongitRebarArea, LongitCornerRebarArea):
        """ GetRebarColumn_1(self: cPropFrame, Name: str, MatPropLong: str, MatPropConfine: str, Pattern: int, ConfineType: int, Cover: float, NumberCBars: int, NumberR3Bars: int, NumberR2Bars: int, RebarSize: str, TieSize: str, TieSpacingLongit: float, Number2DirTieBars: int, Number3DirTieBars: int, ToBeDesigned: bool, LongitCornerRebarSize: str, LongitRebarArea: float, LongitCornerRebarArea: float) -> (int, str, str, int, int, float, int, int, int, str, str, float, int, int, bool, str, float, float) """
        pass

    def GetRectangle(self, Name, FileName, MatProp, T3, T2, Color, Notes, GUID):
        """ GetRectangle(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, int, str, str) """
        pass

    def GetRod(self, Name, FileName, MatProp, T3, Color, Notes, GUID):
        """ GetRod(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, int, str, str) """
        pass

    def GetSDSection(self, Name, MatProp, NumberItems, ShapeName, MyType, DesignType, Color, Notes, GUID):
        """ GetSDSection(self: cPropFrame, Name: str, MatProp: str, NumberItems: int, ShapeName: Array[str], MyType: Array[int], DesignType: int, Color: int, Notes: str, GUID: str) -> (int, str, int, Array[str], Array[int], int, int, str, str) """
        pass

    def GetSectProps(self, Name, Area, As2, As3, Torsion, I22, I33, S22, S33, Z22, Z33, R22, R33):
        """ GetSectProps(self: cPropFrame, Name: str, Area: float, As2: float, As3: float, Torsion: float, I22: float, I33: float, S22: float, S33: float, Z22: float, Z33: float, R22: float, R33: float) -> (int, float, float, float, float, float, float, float, float, float, float, float, float) """
        pass

    def GetSteelAngle(self, Name, FileName, MatProp, T3, T2, Tf, Tw, r, MirrorAbout2, MirrorAbout3, Color, Notes, GUID):
        """ GetSteelAngle(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, r: float, MirrorAbout2: bool, MirrorAbout3: bool, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, float, bool, bool, int, str, str) """
        pass

    def GetSteelTee(self, Name, FileName, MatProp, T3, T2, Tf, Tw, r, MirrorAbout3, Color, Notes, GUID):
        """ GetSteelTee(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, r: float, MirrorAbout3: bool, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, float, bool, int, str, str) """
        pass

    def GetTee(self, Name, FileName, MatProp, T3, T2, Tf, Tw, Color, Notes, GUID):
        """ GetTee(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, int, str, str) """
        pass

    def GetTrapezoidal(self, Name, FileName, MatProp, T3, T2, T2b, Color, Notes, GUID):
        """ GetTrapezoidal(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, T2b: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, int, str, str) """
        pass

    def GetTube(self, Name, FileName, MatProp, T3, T2, Tf, Tw, Color, Notes, GUID):
        """ GetTube(self: cPropFrame, Name: str, FileName: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Color: int, Notes: str, GUID: str) -> (int, str, str, float, float, float, float, int, str, str) """
        pass

    def GetTypeOAPI(self, Name, PropType):
        """ GetTypeOAPI(self: cPropFrame, Name: str, PropType: eFramePropType) -> (int, eFramePropType) """
        pass

    def GetTypeRebar(self, Name, MyType):
        """ GetTypeRebar(self: cPropFrame, Name: str, MyType: int) -> (int, int) """
        pass

    def ImportProp(self, Name, MatProp, FileName, PropName, Color, Notes, GUID):
        """ ImportProp(self: cPropFrame, Name: str, MatProp: str, FileName: str, PropName: str, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetAngle(self, Name, MatProp, T3, T2, Tf, Tw, Color, Notes, GUID):
        """ SetAngle(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetAutoSelectSteel(self, Name, NumberItems, SectName, AutoStartSection, Notes, GUID):
        """ SetAutoSelectSteel(self: cPropFrame, Name: str, NumberItems: int, SectName: Array[str], AutoStartSection: str, Notes: str, GUID: str) -> (int, Array[str]) """
        pass

    def SetChannel(self, Name, MatProp, T3, T2, Tf, Tw, Color, Notes, GUID):
        """ SetChannel(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetCircle(self, Name, MatProp, T3, Color, Notes, GUID):
        """ SetCircle(self: cPropFrame, Name: str, MatProp: str, T3: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetConcreteL(self, Name, MatProp, T3, T2, Tf, TwC, TwT, MirrorAbout2, MirrorAbout3, Color, Notes, GUID):
        """ SetConcreteL(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, TwC: float, TwT: float, MirrorAbout2: bool, MirrorAbout3: bool, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetConcreteTee(self, Name, MatProp, T3, T2, Tf, TwF, TwT, MirrorAbout3, Color, Notes, GUID):
        """ SetConcreteTee(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, TwF: float, TwT: float, MirrorAbout3: bool, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetCoverPlatedI(self, Name, SectName, FyTopFlange, FyWeb, FyBotFlange, Tc, Bc, MatPropTop, Tcb, Bcb, MatPropBot, Color, Notes, GUID):
        """ SetCoverPlatedI(self: cPropFrame, Name: str, SectName: str, FyTopFlange: float, FyWeb: float, FyBotFlange: float, Tc: float, Bc: float, MatPropTop: str, Tcb: float, Bcb: float, MatPropBot: str, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetDblAngle(self, Name, MatProp, T3, T2, Tf, Tw, Dis, Color, Notes, GUID):
        """ SetDblAngle(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Dis: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetDblChannel(self, Name, MatProp, T3, T2, Tf, Tw, Dis, Color, Notes, GUID):
        """ SetDblChannel(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Dis: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetGeneral(self, Name, MatProp, T3, T2, Area, As2, As3, Torsion, I22, I33, S22, S33, Z22, Z33, R22, R33, Color, Notes, GUID):
        """ SetGeneral(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Area: float, As2: float, As3: float, Torsion: float, I22: float, I33: float, S22: float, S33: float, Z22: float, Z33: float, R22: float, R33: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetISection(self, Name, MatProp, T3, T2, Tf, Tw, T2b, Tfb, Color, Notes, GUID):
        """ SetISection(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, T2b: float, Tfb: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetMaterial(self, Name, MatProp):
        """ SetMaterial(self: cPropFrame, Name: str, MatProp: str) -> int """
        pass

    def SetModifiers(self, Name, Value):
        """ SetModifiers(self: cPropFrame, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def SetNonPrismatic(self, Name, NumberItems, StartSec, EndSec, MyLength, MyType, EI33, EI22, Color, Notes, GUID):
        """ SetNonPrismatic(self: cPropFrame, Name: str, NumberItems: int, StartSec: Array[str], EndSec: Array[str], MyLength: Array[float], MyType: Array[int], EI33: Array[int], EI22: Array[int], Color: int, Notes: str, GUID: str) -> (int, Array[str], Array[str], Array[float], Array[int], Array[int], Array[int]) """
        pass

    def SetPipe(self, Name, MatProp, T3, TW, Color, Notes, GUID):
        """ SetPipe(self: cPropFrame, Name: str, MatProp: str, T3: float, TW: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetPlate(self, Name, MatProp, T3, T2, Color, Notes, GUID):
        """ SetPlate(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetRebarBeam(self, Name, MatPropLong, MatPropConfine, CoverTop, CoverBot, TopLeftArea, TopRightArea, BotLeftArea, BotRightArea):
        """ SetRebarBeam(self: cPropFrame, Name: str, MatPropLong: str, MatPropConfine: str, CoverTop: float, CoverBot: float, TopLeftArea: float, TopRightArea: float, BotLeftArea: float, BotRightArea: float) -> int """
        pass

    def SetRebarColumn(self, Name, MatPropLong, MatPropConfine, Pattern, ConfineType, Cover, NumberCBars, NumberR3Bars, NumberR2Bars, RebarSize, TieSize, TieSpacingLongit, Number2DirTieBars, Number3DirTieBars, ToBeDesigned):
        """ SetRebarColumn(self: cPropFrame, Name: str, MatPropLong: str, MatPropConfine: str, Pattern: int, ConfineType: int, Cover: float, NumberCBars: int, NumberR3Bars: int, NumberR2Bars: int, RebarSize: str, TieSize: str, TieSpacingLongit: float, Number2DirTieBars: int, Number3DirTieBars: int, ToBeDesigned: bool) -> int """
        pass

    def SetRectangle(self, Name, MatProp, T3, T2, Color, Notes, GUID):
        """ SetRectangle(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetRod(self, Name, MatProp, T3, Color, Notes, GUID):
        """ SetRod(self: cPropFrame, Name: str, MatProp: str, T3: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetSDSection(self, Name, MatProp, DesignType, Color, Notes, GUID):
        """ SetSDSection(self: cPropFrame, Name: str, MatProp: str, DesignType: int, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetSteelAngle(self, Name, MatProp, T3, T2, Tf, Tw, r, MirrorAbout2, MirrorAbout3, Color, Notes, GUID):
        """ SetSteelAngle(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, r: float, MirrorAbout2: bool, MirrorAbout3: bool, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetSteelTee(self, Name, MatProp, T3, T2, Tf, Tw, r, MirrorAbout3, Color, Notes, GUID):
        """ SetSteelTee(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, r: float, MirrorAbout3: bool, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetTee(self, Name, MatProp, T3, T2, Tf, Tw, Color, Notes, GUID):
        """ SetTee(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetTrapezoidal(self, Name, MatProp, T3, T2, T2b, Color, Notes, GUID):
        """ SetTrapezoidal(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, T2b: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetTube(self, Name, MatProp, T3, T2, Tf, Tw, Color, Notes, GUID):
        """ SetTube(self: cPropFrame, Name: str, MatProp: str, T3: float, T2: float, Tf: float, Tw: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SDShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SDShape(self: cPropFrame) -> cPropFrameSDShape

"""



class cPropFrameSDShape:
    # no doc
    def GetAngle(self, Name, ShapeName, MatProp, PropName, Color, XCenter, YCenter, H, Bf, Tf, Tw, Rotation):
        """ GetAngle(self: cPropFrameSDShape, Name: str, ShapeName: str, MatProp: str, PropName: str, Color: int, XCenter: float, YCenter: float, H: float, Bf: float, Tf: float, Tw: float, Rotation: float) -> (int, str, str, int, float, float, float, float, float, float, float) """
        pass

    def GetConcreteL(self, Name, ShapeName, MatProp, PropName, Color, XCenter, YCenter, H, Bf, Tf, Tw, Rotation, MirrorAbout2, MirrorAbout3):
        """ GetConcreteL(self: cPropFrameSDShape, Name: str, ShapeName: str, MatProp: str, PropName: str, Color: int, XCenter: float, YCenter: float, H: float, Bf: float, Tf: float, Tw: float, Rotation: float, MirrorAbout2: bool, MirrorAbout3: bool) -> (int, str, str, int, float, float, float, float, float, float, float, bool, bool) """
        pass

    def GetConcreteTee(self, Name, ShapeName, MatProp, PropName, Color, XCenter, YCenter, H, Bf, Tf, Tw, Rotation, MirrorAbout3):
        """ GetConcreteTee(self: cPropFrameSDShape, Name: str, ShapeName: str, MatProp: str, PropName: str, Color: int, XCenter: float, YCenter: float, H: float, Bf: float, Tf: float, Tw: float, Rotation: float, MirrorAbout3: bool) -> (int, str, str, int, float, float, float, float, float, float, float, bool) """
        pass

    def GetISection(self, Name, ShapeName, MatProp, PropName, Color, XCenter, YCenter, H, Bf, Tf, Tw, Bfb, Tfb, Rotation):
        """ GetISection(self: cPropFrameSDShape, Name: str, ShapeName: str, MatProp: str, PropName: str, Color: int, XCenter: float, YCenter: float, H: float, Bf: float, Tf: float, Tw: float, Bfb: float, Tfb: float, Rotation: float) -> (int, str, str, int, float, float, float, float, float, float, float, float, float) """
        pass

    def GetReinfCircle(self, Name, ShapeName, XCenter, YCenter, Diameter, NumBars, Rotation, RebarSize, MatRebar):
        """ GetReinfCircle(self: cPropFrameSDShape, Name: str, ShapeName: str, XCenter: float, YCenter: float, Diameter: float, NumBars: int, Rotation: float, RebarSize: str, MatRebar: str) -> (int, float, float, float, int, float, str, str) """
        pass

    def GetReinfCorner(self, Name, ShapeName, NumberItems, PointNum, RebarSize):
        """ GetReinfCorner(self: cPropFrameSDShape, Name: str, ShapeName: str, NumberItems: int, PointNum: Array[int], RebarSize: Array[str]) -> (int, int, Array[int], Array[str]) """
        pass

    def GetReinfEdge(self, Name, ShapeName, NumberItems, EdgeNum, RebarSize, Spacing, Cover):
        """ GetReinfEdge(self: cPropFrameSDShape, Name: str, ShapeName: str, NumberItems: int, EdgeNum: Array[int], RebarSize: Array[str], Spacing: Array[float], Cover: Array[float]) -> (int, int, Array[int], Array[str], Array[float], Array[float]) """
        pass

    def GetReinfLine(self, Name, ShapeName, X1, Y1, X2, Y2, Spacing, RebarSize, EndBars, MatRebar):
        """ GetReinfLine(self: cPropFrameSDShape, Name: str, ShapeName: str, X1: float, Y1: float, X2: float, Y2: float, Spacing: float, RebarSize: str, EndBars: bool, MatRebar: str) -> (int, float, float, float, float, float, str, bool, str) """
        pass

    def GetReinfRectangular(self, Name, ShapeName, XCenter, YCenter, H, W, Rotation, MatRebar):
        """ GetReinfRectangular(self: cPropFrameSDShape, Name: str, ShapeName: str, XCenter: float, YCenter: float, H: float, W: float, Rotation: float, MatRebar: str) -> (int, float, float, float, float, float, str) """
        pass

    def GetReinfSingle(self, Name, ShapeName, XCenter, YCenter, RebarSize, MatRebar):
        """ GetReinfSingle(self: cPropFrameSDShape, Name: str, ShapeName: str, XCenter: float, YCenter: float, RebarSize: str, MatRebar: str) -> (int, float, float, str, str) """
        pass

    def GetSolidCircle(self, Name, ShapeName, MatProp, SSOverwrite, Color, XCenter, YCenter, Diameter, Reinf, NumberBars, Rotation, Cover, RebarSize, MatRebar):
        """ GetSolidCircle(self: cPropFrameSDShape, Name: str, ShapeName: str, MatProp: str, SSOverwrite: str, Color: int, XCenter: float, YCenter: float, Diameter: float, Reinf: bool, NumberBars: int, Rotation: float, Cover: float, RebarSize: str, MatRebar: str) -> (int, str, str, int, float, float, float, bool, int, float, float, str, str) """
        pass

    def GetSolidRect(self, Name, ShapeName, MatProp, SSOverwrite, Color, XCenter, YCenter, H, W, Rotation, Reinf, MatRebar):
        """ GetSolidRect(self: cPropFrameSDShape, Name: str, ShapeName: str, MatProp: str, SSOverwrite: str, Color: int, XCenter: float, YCenter: float, H: float, W: float, Rotation: float, Reinf: bool, MatRebar: str) -> (int, str, str, int, float, float, float, float, float, bool, str) """
        pass

    def GetTee(self, Name, ShapeName, MatProp, PropName, Color, XCenter, YCenter, H, Bf, Tf, Tw, Rotation):
        """ GetTee(self: cPropFrameSDShape, Name: str, ShapeName: str, MatProp: str, PropName: str, Color: int, XCenter: float, YCenter: float, H: float, Bf: float, Tf: float, Tw: float, Rotation: float) -> (int, str, str, int, float, float, float, float, float, float, float) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropLineSpring:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPropLineSpring, Name: str, NewName: str) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPropLineSpring, Name: str) -> int """
        pass

    def GetLineSpringProp(self, Name, U1, U2, U3, R1, NonlinearOption2, NonlinearOption3, color, notes, iGUID):
        """ GetLineSpringProp(self: cPropLineSpring, Name: str, U1: float, U2: float, U3: float, R1: float, NonlinearOption2: int, NonlinearOption3: int, color: int, notes: str, iGUID: str) -> (int, float, float, float, float, int, int, int, str, str) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cPropLineSpring, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def SetLineSpringProp(self, Name, U1, U2, U3, R1, NonlinearOption2, NonlinearOption3, color, notes, iGUID):
        """ SetLineSpringProp(self: cPropLineSpring, Name: str, U1: float, U2: float, U3: float, R1: float, NonlinearOption2: int, NonlinearOption3: int, color: int, notes: str, iGUID: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropLink:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPropLink, Name: str, NewName: str) -> int """
        pass

    def Count(self, PropType):
        """ Count(self: cPropLink, PropType: eLinkPropType) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPropLink, Name: str) -> int """
        pass

    def GetAcceptanceCriteria(self, Name, AcceptanceType, Symmetric, Active, IOPos, LSPos, CPPos, IONeg, LSNeg, CPNeg):
        """ GetAcceptanceCriteria(self: cPropLink, Name: str, AcceptanceType: int, Symmetric: bool, Active: Array[bool], IOPos: Array[float], LSPos: Array[float], CPPos: Array[float], IONeg: Array[float], LSNeg: Array[float], CPNeg: Array[float]) -> (int, int, bool, Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetDamper(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, C, CExp, DJ2, DJ3, Notes, GUID):
        """ GetDamper(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], C: Array[float], CExp: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], float, float, str, str) """
        pass

    def GetDamperBilinear(self, Name, dof, Fixed, Nonlinear, ke, ce, k, c, CY, ForceLimit, dj2, dj3, notes, GUID):
        """ GetDamperBilinear(self: cPropLink, Name: str, dof: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], ke: Array[float], ce: Array[float], k: Array[float], c: Array[float], CY: Array[float], ForceLimit: Array[float], dj2: float, dj3: float, notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], float, float, str, str) """
        pass

    def GetDamperFrictionSpring(self, Name, dof, Fixed, Nonlinear, ke, ce, k, K1, K2, u0, us, direction, dj2, dj3, notes, GUID):
        """ GetDamperFrictionSpring(self: cPropLink, Name: str, dof: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], ke: Array[float], ce: Array[float], k: Array[float], K1: Array[float], K2: Array[float], u0: Array[float], us: Array[float], direction: Array[int], dj2: float, dj3: float, notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[int], float, float, str, str) """
        pass

    def GetFrictionIsolator(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Slow, Fast, Rate, Radius, Damping, DJ2, DJ3, Notes, GUID):
        """ GetFrictionIsolator(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Slow: Array[float], Fast: Array[float], Rate: Array[float], Radius: Array[float], Damping: float, DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], float, float, float, str, str) """
        pass

    def GetGap(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Dis, DJ2, DJ3, Notes, GUID):
        """ GetGap(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Dis: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], float, float, str, str) """
        pass

    def GetHook(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Dis, DJ2, DJ3, Notes, GUID):
        """ GetHook(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Dis: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], float, float, str, str) """
        pass

    def GetLinear(self, Name, DOF, Fixed, Ke, Ce, DJ2, DJ3, KeCoupled, CeCoupled, Notes, GUID):
        """ GetLinear(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Ke: Array[float], Ce: Array[float], DJ2: float, DJ3: float, KeCoupled: bool, CeCoupled: bool, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[float], Array[float], float, float, bool, bool, str, str) """
        pass

    def GetMultiLinearElastic(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, DJ2, DJ3, Notes, GUID):
        """ GetMultiLinearElastic(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], float, float, str, str) """
        pass

    def GetMultiLinearPlastic(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, DJ2, DJ3, Notes, GUID):
        """ GetMultiLinearPlastic(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], float, float, str, str) """
        pass

    def GetMultiLinearPoints(self, Name, DOF, NumberPoints, F, D, MyType, A1, A2, B1, B2, Eta):
        """ GetMultiLinearPoints(self: cPropLink, Name: str, DOF: int, NumberPoints: int, F: Array[float], D: Array[float], MyType: int, A1: float, A2: float, B1: float, B2: float, Eta: float) -> (int, int, Array[float], Array[float], int, float, float, float, float, float) """
        pass

    def GetNameList(self, NumberNames, MyName, PropType):
        """ GetNameList(self: cPropLink, NumberNames: int, MyName: Array[str], PropType: eLinkPropType) -> (int, int, Array[str]) """
        pass

    def GetPDelta(self, Name, Value):
        """ GetPDelta(self: cPropLink, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def GetPlasticWen(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Yield, Ratio, Exp, DJ2, DJ3, Notes, GUID):
        """ GetPlasticWen(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Yield: Array[float], Ratio: Array[float], Exp: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], float, float, str, str) """
        pass

    def GetRubberIsolator(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Yield, Ratio, DJ2, DJ3, Notes, GUID):
        """ GetRubberIsolator(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Yield: Array[float], Ratio: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], float, float, str, str) """
        pass

    def GetSpringData(self, Name, DefinedForThisLength, DefinedForThisArea):
        """ GetSpringData(self: cPropLink, Name: str, DefinedForThisLength: float, DefinedForThisArea: float) -> (int, float, float) """
        pass

    def GetTCFrictionIsolator(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Slow, Fast, Rate, Radius, SlowT, FastT, RateT, Kt, Dis, Dist, Damping, DJ2, DJ3, Notes, GUID):
        """ GetTCFrictionIsolator(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Slow: Array[float], Fast: Array[float], Rate: Array[float], Radius: Array[float], SlowT: Array[float], FastT: Array[float], RateT: Array[float], Kt: float, Dis: float, Dist: float, Damping: float, DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], float, float, float, float, float, float, str, str) """
        pass

    def GetTypeOAPI(self, Name, PropType):
        """ GetTypeOAPI(self: cPropLink, Name: str, PropType: eLinkPropType) -> (int, eLinkPropType) """
        pass

    def GetWeightAndMass(self, Name, W, M, R1, R2, R3):
        """ GetWeightAndMass(self: cPropLink, Name: str, W: float, M: float, R1: float, R2: float, R3: float) -> (int, float, float, float, float, float) """
        pass

    def SetAcceptanceCriteria(self, Name, AcceptanceType, Symmetric, Active, IOPos, LSPos, CPPos, IONeg, LSNeg, CPNeg):
        """ SetAcceptanceCriteria(self: cPropLink, Name: str, AcceptanceType: int, Symmetric: bool, Active: Array[bool], IOPos: Array[float], LSPos: Array[float], CPPos: Array[float], IONeg: Array[float], LSNeg: Array[float], CPNeg: Array[float]) -> (int, Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetDamper(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, C, CExp, DJ2, DJ3, Notes, GUID):
        """ SetDamper(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], C: Array[float], CExp: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetDamperBilinear(self, Name, dof, Fixed, Nonlinear, ke, ce, k, c, CY, ForceLimit, dj2, dj3, notes, GUID):
        """ SetDamperBilinear(self: cPropLink, Name: str, dof: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], ke: Array[float], ce: Array[float], k: Array[float], c: Array[float], CY: Array[float], ForceLimit: Array[float], dj2: float, dj3: float, notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetDamperFrictionSpring(self, Name, dof, Fixed, Nonlinear, ke, ce, k, K1, K2, u0, us, direction, dj2, dj3, notes, GUID):
        """ SetDamperFrictionSpring(self: cPropLink, Name: str, dof: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], ke: Array[float], ce: Array[float], k: Array[float], K1: Array[float], K2: Array[float], u0: Array[float], us: Array[float], direction: Array[int], dj2: float, dj3: float, notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[int]) """
        pass

    def SetFrictionIsolator(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Slow, Fast, Rate, Radius, Damping, DJ2, DJ3, Notes, GUID):
        """ SetFrictionIsolator(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Slow: Array[float], Fast: Array[float], Rate: Array[float], Radius: Array[float], Damping: float, DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetGap(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Dis, DJ2, DJ3, Notes, GUID):
        """ SetGap(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Dis: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetHook(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Dis, DJ2, DJ3, Notes, GUID):
        """ SetHook(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Dis: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetLinear(self, Name, DOF, Fixed, Ke, Ce, DJ2, DJ3, KeCoupled, CeCoupled, Notes, GUID):
        """ SetLinear(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Ke: Array[float], Ce: Array[float], DJ2: float, DJ3: float, KeCoupled: bool, CeCoupled: bool, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[float], Array[float]) """
        pass

    def SetMultiLinearElastic(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, DJ2, DJ3, Notes, GUID):
        """ SetMultiLinearElastic(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float]) """
        pass

    def SetMultiLinearPlastic(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, DJ2, DJ3, Notes, GUID):
        """ SetMultiLinearPlastic(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float]) """
        pass

    def SetMultiLinearPoints(self, Name, DOF, NumberPoints, F, D, MyType, A1, A2, B1, B2, Eta):
        """ SetMultiLinearPoints(self: cPropLink, Name: str, DOF: int, NumberPoints: int, F: Array[float], D: Array[float], MyType: int, A1: float, A2: float, B1: float, B2: float, Eta: float) -> (int, Array[float], Array[float]) """
        pass

    def SetPDelta(self, Name, Value):
        """ SetPDelta(self: cPropLink, Name: str, Value: Array[float]) -> (int, Array[float]) """
        pass

    def SetPlasticWen(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Yield, Ratio, Exp, DJ2, DJ3, Notes, GUID):
        """ SetPlasticWen(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Yield: Array[float], Ratio: Array[float], Exp: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetRubberIsolator(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Yield, Ratio, DJ2, DJ3, Notes, GUID):
        """ SetRubberIsolator(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Yield: Array[float], Ratio: Array[float], DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetSpringData(self, Name, DefinedForThisLength, DefinedForThisArea):
        """ SetSpringData(self: cPropLink, Name: str, DefinedForThisLength: float, DefinedForThisArea: float) -> int """
        pass

    def SetTCFrictionIsolator(self, Name, DOF, Fixed, Nonlinear, Ke, Ce, K, Slow, Fast, Rate, Radius, SlowT, FastT, RateT, Kt, Dis, Dist, Damping, DJ2, DJ3, Notes, GUID):
        """ SetTCFrictionIsolator(self: cPropLink, Name: str, DOF: Array[bool], Fixed: Array[bool], Nonlinear: Array[bool], Ke: Array[float], Ce: Array[float], K: Array[float], Slow: Array[float], Fast: Array[float], Rate: Array[float], Radius: Array[float], SlowT: Array[float], FastT: Array[float], RateT: Array[float], Kt: float, Dis: float, Dist: float, Damping: float, DJ2: float, DJ3: float, Notes: str, GUID: str) -> (int, Array[bool], Array[bool], Array[bool], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetWeightAndMass(self, Name, W, M, R1, R2, R3):
        """ SetWeightAndMass(self: cPropLink, Name: str, W: float, M: float, R1: float, R2: float, R3: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropMaterial:
    # no doc
    def AddMaterial(self, Name, MatType, Region, Standard, Grade, UserName):
        """ AddMaterial(self: cPropMaterial, Name: str, MatType: eMatType, Region: str, Standard: str, Grade: str, UserName: str) -> (int, str) """
        pass

    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPropMaterial, Name: str, NewName: str) -> int """
        pass

    def Count(self, MatType):
        """ Count(self: cPropMaterial, MatType: eMatType) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPropMaterial, Name: str) -> int """
        pass

    def GetDamping(self, Name, ModalRatio, ViscousMassCoeff, ViscousStiffCoeff, HystereticMassCoeff, HystereticStiffCoeff, Temp):
        """ GetDamping(self: cPropMaterial, Name: str, ModalRatio: float, ViscousMassCoeff: float, ViscousStiffCoeff: float, HystereticMassCoeff: float, HystereticStiffCoeff: float, Temp: float) -> (int, float, float, float, float, float) """
        pass

    def GetMassSource(self, MyOption, NumberLoads, LoadPat, SF):
        """ GetMassSource(self: cPropMaterial, MyOption: int, NumberLoads: int, LoadPat: Array[str], SF: Array[float]) -> (int, int, int, Array[str], Array[float]) """
        pass

    def GetMassSource_1(self, IncludeElements, IncludeAddedMass, IncludeLoads, NumberLoads, LoadPat, sf):
        """ GetMassSource_1(self: cPropMaterial, IncludeElements: bool, IncludeAddedMass: bool, IncludeLoads: bool, NumberLoads: int, LoadPat: Array[str], sf: Array[float]) -> (int, bool, bool, bool, int, Array[str], Array[float]) """
        pass

    def GetMaterial(self, Name, MatType, Color, Notes, GUID):
        """ GetMaterial(self: cPropMaterial, Name: str, MatType: eMatType, Color: int, Notes: str, GUID: str) -> (int, eMatType, int, str, str) """
        pass

    def GetMPAnisotropic(self, Name, E, U, A, G, Temp):
        """ GetMPAnisotropic(self: cPropMaterial, Name: str, E: Array[float], U: Array[float], A: Array[float], G: Array[float], Temp: float) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetMPIsotropic(self, Name, E, U, A, G, Temp):
        """ GetMPIsotropic(self: cPropMaterial, Name: str, E: float, U: float, A: float, G: float, Temp: float) -> (int, float, float, float, float) """
        pass

    def GetMPOrthotropic(self, Name, E, U, A, G, Temp):
        """ GetMPOrthotropic(self: cPropMaterial, Name: str, E: Array[float], U: Array[float], A: Array[float], G: Array[float], Temp: float) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetMPUniaxial(self, Name, E, A, Temp):
        """ GetMPUniaxial(self: cPropMaterial, Name: str, E: float, A: float, Temp: float) -> (int, float, float) """
        pass

    def GetNameList(self, NumberNames, MyName, MatType):
        """ GetNameList(self: cPropMaterial, NumberNames: int, MyName: Array[str], MatType: eMatType) -> (int, int, Array[str]) """
        pass

    def GetOConcrete(self, Name, Fc, IsLightweight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FrictionAngle, DilatationalAngle, Temp):
        """ GetOConcrete(self: cPropMaterial, Name: str, Fc: float, IsLightweight: bool, FcsFactor: float, SSType: int, SSHysType: int, StrainAtFc: float, StrainUltimate: float, FrictionAngle: float, DilatationalAngle: float, Temp: float) -> (int, float, bool, float, int, int, float, float, float, float) """
        pass

    def GetOConcrete_1(self, Name, Fc, IsLightweight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FinalSlope, FrictionAngle, DilatationalAngle, Temp):
        """ GetOConcrete_1(self: cPropMaterial, Name: str, Fc: float, IsLightweight: bool, FcsFactor: float, SSType: int, SSHysType: int, StrainAtFc: float, StrainUltimate: float, FinalSlope: float, FrictionAngle: float, DilatationalAngle: float, Temp: float) -> (int, float, bool, float, int, int, float, float, float, float, float) """
        pass

    def GetONoDesign(self, Name, FrictionAngle, DilatationalAngle, Temp):
        """ GetONoDesign(self: cPropMaterial, Name: str, FrictionAngle: float, DilatationalAngle: float, Temp: float) -> (int, float, float) """
        pass

    def GetORebar(self, Name, Fy, Fu, EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainUltimate, UseCaltransSSDefaults, Temp):
        """ GetORebar(self: cPropMaterial, Name: str, Fy: float, Fu: float, EFy: float, EFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainUltimate: float, UseCaltransSSDefaults: bool, Temp: float) -> (int, float, float, float, float, int, int, float, float, bool) """
        pass

    def GetORebar_1(self, Name, Fy, Fu, EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainUltimate, FinalSlope, UseCaltransSSDefaults, Temp):
        """ GetORebar_1(self: cPropMaterial, Name: str, Fy: float, Fu: float, EFy: float, EFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainUltimate: float, FinalSlope: float, UseCaltransSSDefaults: bool, Temp: float) -> (int, float, float, float, float, int, int, float, float, float, bool) """
        pass

    def GetOSteel(self, Name, Fy, Fu, EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainAtMaxStress, StrainAtRupture, Temp):
        """ GetOSteel(self: cPropMaterial, Name: str, Fy: float, Fu: float, EFy: float, EFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainAtMaxStress: float, StrainAtRupture: float, Temp: float) -> (int, float, float, float, float, int, int, float, float, float) """
        pass

    def GetOSteel_1(self, Name, Fy, Fu, EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainAtMaxStress, StrainAtRupture, FinalSlope, Temp):
        """ GetOSteel_1(self: cPropMaterial, Name: str, Fy: float, Fu: float, EFy: float, EFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainAtMaxStress: float, StrainAtRupture: float, FinalSlope: float, Temp: float) -> (int, float, float, float, float, int, int, float, float, float, float) """
        pass

    def GetOTendon(self, Name, Fy, Fu, SSType, SSHysType, Temp):
        """ GetOTendon(self: cPropMaterial, Name: str, Fy: float, Fu: float, SSType: int, SSHysType: int, Temp: float) -> (int, float, float, int, int) """
        pass

    def GetOTendon_1(self, Name, Fy, Fu, SSType, SSHysType, FinalSlope, Temp):
        """ GetOTendon_1(self: cPropMaterial, Name: str, Fy: float, Fu: float, SSType: int, SSHysType: int, FinalSlope: float, Temp: float) -> (int, float, float, int, int, float) """
        pass

    def GetSSCurve(self, Name, NumberPoints, PointID, Strain, Stress, SectName, RebarArea, Temp):
        """ GetSSCurve(self: cPropMaterial, Name: str, NumberPoints: int, PointID: Array[int], Strain: Array[float], Stress: Array[float], SectName: str, RebarArea: float, Temp: float) -> (int, int, Array[int], Array[float], Array[float]) """
        pass

    def GetTemp(self, Name, NumberItems, Temp):
        """ GetTemp(self: cPropMaterial, Name: str, NumberItems: int, Temp: Array[float]) -> (int, int, Array[float]) """
        pass

    def GetTypeOAPI(self, Name, MatType, SymType):
        """ GetTypeOAPI(self: cPropMaterial, Name: str, MatType: eMatType, SymType: int) -> (int, eMatType, int) """
        pass

    def GetWeightAndMass(self, Name, W, M, Temp):
        """ GetWeightAndMass(self: cPropMaterial, Name: str, W: float, M: float, Temp: float) -> (int, float, float) """
        pass

    def SetDamping(self, Name, ModalRatio, ViscousMassCoeff, ViscousStiffCoeff, HystereticMassCoeff, HystereticStiffCoeff, Temp):
        """ SetDamping(self: cPropMaterial, Name: str, ModalRatio: float, ViscousMassCoeff: float, ViscousStiffCoeff: float, HystereticMassCoeff: float, HystereticStiffCoeff: float, Temp: float) -> int """
        pass

    def SetMassSource(self, MyOption, NumberLoads, LoadPat, SF):
        """ SetMassSource(self: cPropMaterial, MyOption: int, NumberLoads: int, LoadPat: Array[str], SF: Array[float]) -> (int, Array[str], Array[float]) """
        pass

    def SetMassSource_1(self, IncludeElements, IncludeAddedMass, IncludeLoads, NumberLoads, LoadPat, sf):
        """ SetMassSource_1(self: cPropMaterial, IncludeElements: bool, IncludeAddedMass: bool, IncludeLoads: bool, NumberLoads: int, LoadPat: Array[str], sf: Array[float]) -> (int, bool, bool, bool, Array[str], Array[float]) """
        pass

    def SetMaterial(self, Name, MatType, Color, Notes, GUID):
        """ SetMaterial(self: cPropMaterial, Name: str, MatType: eMatType, Color: int, Notes: str, GUID: str) -> int """
        pass

    def SetMPAnisotropic(self, Name, E, U, A, G, Temp):
        """ SetMPAnisotropic(self: cPropMaterial, Name: str, E: Array[float], U: Array[float], A: Array[float], G: Array[float], Temp: float) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetMPIsotropic(self, Name, E, U, A, Temp):
        """ SetMPIsotropic(self: cPropMaterial, Name: str, E: float, U: float, A: float, Temp: float) -> int """
        pass

    def SetMPOrthotropic(self, Name, E, U, A, G, Temp):
        """ SetMPOrthotropic(self: cPropMaterial, Name: str, E: Array[float], U: Array[float], A: Array[float], G: Array[float], Temp: float) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def SetMPUniaxial(self, Name, E, A, Temp):
        """ SetMPUniaxial(self: cPropMaterial, Name: str, E: float, A: float, Temp: float) -> int """
        pass

    def SetOConcrete(self, Name, Fc, IsLightweight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FrictionAngle, DilatationalAngle, Temp):
        """ SetOConcrete(self: cPropMaterial, Name: str, Fc: float, IsLightweight: bool, FcsFactor: float, SSType: int, SSHysType: int, StrainAtFc: float, StrainUltimate: float, FrictionAngle: float, DilatationalAngle: float, Temp: float) -> int """
        pass

    def SetOConcrete_1(self, Name, Fc, IsLightweight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FinalSlope, FrictionAngle, DilatationalAngle, Temp):
        """ SetOConcrete_1(self: cPropMaterial, Name: str, Fc: float, IsLightweight: bool, FcsFactor: float, SSType: int, SSHysType: int, StrainAtFc: float, StrainUltimate: float, FinalSlope: float, FrictionAngle: float, DilatationalAngle: float, Temp: float) -> int """
        pass

    def SetONoDesign(self, Name, FrictionAngle, DilatationalAngle, Temp):
        """ SetONoDesign(self: cPropMaterial, Name: str, FrictionAngle: float, DilatationalAngle: float, Temp: float) -> int """
        pass

    def SetORebar(self, Name, Fy, Fu, EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainUltimate, UseCaltransSSDefaults, Temp):
        """ SetORebar(self: cPropMaterial, Name: str, Fy: float, Fu: float, EFy: float, EFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainUltimate: float, UseCaltransSSDefaults: bool, Temp: float) -> int """
        pass

    def SetORebar_1(self, Name, Fy, Fu, EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainUltimate, FinalSlope, UseCaltransSSDefaults, Temp):
        """ SetORebar_1(self: cPropMaterial, Name: str, Fy: float, Fu: float, EFy: float, EFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainUltimate: float, FinalSlope: float, UseCaltransSSDefaults: bool, Temp: float) -> int """
        pass

    def SetOSteel(self, Name, Fy, Fu, EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainAtMaxStress, StrainAtRupture, Temp):
        """ SetOSteel(self: cPropMaterial, Name: str, Fy: float, Fu: float, EFy: float, EFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainAtMaxStress: float, StrainAtRupture: float, Temp: float) -> int """
        pass

    def SetOSteel_1(self, Name, Fy, Fu, EFy, EFu, SSType, SSHysType, StrainAtHardening, StrainAtMaxStress, StrainAtRupture, FinalSlope, Temp):
        """ SetOSteel_1(self: cPropMaterial, Name: str, Fy: float, Fu: float, EFy: float, EFu: float, SSType: int, SSHysType: int, StrainAtHardening: float, StrainAtMaxStress: float, StrainAtRupture: float, FinalSlope: float, Temp: float) -> int """
        pass

    def SetOTendon(self, Name, Fy, Fu, SSType, SSHysType, Temp):
        """ SetOTendon(self: cPropMaterial, Name: str, Fy: float, Fu: float, SSType: int, SSHysType: int, Temp: float) -> int """
        pass

    def SetOTendon_1(self, Name, Fy, Fu, SSType, SSHysType, FinalSlope, Temp):
        """ SetOTendon_1(self: cPropMaterial, Name: str, Fy: float, Fu: float, SSType: int, SSHysType: int, FinalSlope: float, Temp: float) -> int """
        pass

    def SetSSCurve(self, Name, NumberPoints, PointID, Strain, Stress, Temp):
        """ SetSSCurve(self: cPropMaterial, Name: str, NumberPoints: int, PointID: Array[int], Strain: Array[float], Stress: Array[float], Temp: float) -> (int, Array[int], Array[float], Array[float]) """
        pass

    def SetTemp(self, Name, NumberItems, Temp):
        """ SetTemp(self: cPropMaterial, Name: str, NumberItems: int, Temp: Array[float]) -> (int, Array[float]) """
        pass

    def SetWeightAndMass(self, Name, MyOption, Value, Temp):
        """ SetWeightAndMass(self: cPropMaterial, Name: str, MyOption: int, Value: float, Temp: float) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    TimeDep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeDep(self: cPropMaterial) -> cPropMaterialTD

"""



class cPropMaterialTD:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropPointSpring:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPropPointSpring, Name: str, NewName: str) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPropPointSpring, Name: str) -> int """
        pass

    def GetLinks(self, Name, NumberLinks, LinkNames, LinkAxialDirs, LinkAngles):
        """ GetLinks(self: cPropPointSpring, Name: str, NumberLinks: int, LinkNames: Array[str], LinkAxialDirs: Array[int], LinkAngles: Array[float]) -> (int, int, Array[str], Array[int], Array[float]) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cPropPointSpring, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetPointSpringProp(self, Name, SpringOption, k, CSys, SoilProfile, Footing, Period, color, notes, iGUID):
        """ GetPointSpringProp(self: cPropPointSpring, Name: str, SpringOption: int, k: Array[float], CSys: str, SoilProfile: str, Footing: str, Period: float, color: int, notes: str, iGUID: str) -> (int, int, Array[float], str, str, str, float, int, str, str) """
        pass

    def SetLinks(self, Name, NumberLinks, LinkNames, LinkAxialDirs, LinkAngles):
        """ SetLinks(self: cPropPointSpring, Name: str, NumberLinks: int, LinkNames: Array[str], LinkAxialDirs: Array[int], LinkAngles: Array[float]) -> (int, Array[str], Array[int], Array[float]) """
        pass

    def SetPointSpringProp(self, Name, SpringOption, k, CSys, SoilProfile, Footing, Period, color, notes, iGUID):
        """ SetPointSpringProp(self: cPropPointSpring, Name: str, SpringOption: int, k: Array[float], CSys: str, SoilProfile: str, Footing: str, Period: float, color: int, notes: str, iGUID: str) -> (int, Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropRebar:
    # no doc
    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cPropRebar, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetNameListWithData(self, NumberNames, MyName, Areas, Diameters, MyGUID):
        """ GetNameListWithData(self: cPropRebar, NumberNames: int, MyName: Array[str], Areas: Array[float], Diameters: Array[float], MyGUID: Array[str]) -> (int, int, Array[str], Array[float], Array[float], Array[str]) """
        pass

    def GetRebarProps(self, Name, Area, Diameter):
        """ GetRebarProps(self: cPropRebar, Name: str, Area: float, Diameter: float) -> (int, float, float) """
        pass

    def GetRebarPropsWithGUID(self, Name, Area, Diameter, MyGUID):
        """ GetRebarPropsWithGUID(self: cPropRebar, Name: str, Area: float, Diameter: float, MyGUID: str) -> (int, float, float, str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cPropTendon:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cPropTendon, Name: str, NewName: str) -> int """
        pass

    def Count(self):
        """ Count(self: cPropTendon) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cPropTendon, Name: str) -> int """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cPropTendon, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetProp(self, Name, MatProp, ModelingOption, Area, Color, Notes, GUID):
        """ GetProp(self: cPropTendon, Name: str, MatProp: str, ModelingOption: int, Area: float, Color: int, Notes: str, GUID: str) -> (int, str, int, float, int, str, str) """
        pass

    def SetProp(self, Name, MatProp, ModelingOption, Area, Color, Notes, GUID):
        """ SetProp(self: cPropTendon, Name: str, MatProp: str, ModelingOption: int, Area: float, Color: int, Notes: str, GUID: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cSapModel:
    # no doc
    def GetDatabaseUnits(self):
        """ GetDatabaseUnits(self: cSapModel) -> eUnits """
        pass

    def GetDatabaseUnits_2(self, forceUnits, lengthUnits, temperatureUnits):
        """ GetDatabaseUnits_2(self: cSapModel, forceUnits: eForce, lengthUnits: eLength, temperatureUnits: eTemperature) -> (int, eForce, eLength, eTemperature) """
        pass

    def GetMergeTol(self, MergeTol):
        """ GetMergeTol(self: cSapModel, MergeTol: float) -> (int, float) """
        pass

    def GetModelFilename(self, IncludePath):
        """ GetModelFilename(self: cSapModel, IncludePath: bool) -> str """
        pass

    def GetModelFilepath(self):
        """ GetModelFilepath(self: cSapModel) -> str """
        pass

    def GetModelIsLocked(self):
        """ GetModelIsLocked(self: cSapModel) -> bool """
        pass

    def GetPresentCoordSystem(self):
        """ GetPresentCoordSystem(self: cSapModel) -> str """
        pass

    def GetPresentUnits(self):
        """ GetPresentUnits(self: cSapModel) -> eUnits """
        pass

    def GetPresentUnits_2(self, forceUnits, lengthUnits, temperatureUnits):
        """ GetPresentUnits_2(self: cSapModel, forceUnits: eForce, lengthUnits: eLength, temperatureUnits: eTemperature) -> (int, eForce, eLength, eTemperature) """
        pass

    def GetProgramInfo(self, ProgramName, ProgramVersion, ProgramLevel):
        """ GetProgramInfo(self: cSapModel, ProgramName: str, ProgramVersion: str, ProgramLevel: str) -> (int, str, str, str) """
        pass

    def GetProjectInfo(self, NumberItems, Item, Data):
        """ GetProjectInfo(self: cSapModel, NumberItems: int, Item: Array[str], Data: Array[str]) -> (int, int, Array[str], Array[str]) """
        pass

    def GetVersion(self, Version, MyVersionNumber):
        """ GetVersion(self: cSapModel, Version: str, MyVersionNumber: float) -> (int, str, float) """
        pass

    def InitializeNewModel(self, Units):
        """ InitializeNewModel(self: cSapModel, Units: eUnits) -> int """
        pass

    def SetMergeTol(self, MergeTol):
        """ SetMergeTol(self: cSapModel, MergeTol: float) -> int """
        pass

    def SetModelIsLocked(self, Lockit):
        """ SetModelIsLocked(self: cSapModel, Lockit: bool) -> int """
        pass

    def SetPresentUnits(self, Units):
        """ SetPresentUnits(self: cSapModel, Units: eUnits) -> int """
        pass

    def SetPresentUnits_2(self, forceUnits, lengthUnits, temperatureUnits):
        """ SetPresentUnits_2(self: cSapModel, forceUnits: eForce, lengthUnits: eLength, temperatureUnits: eTemperature) -> int """
        pass

    def SetProjectInfo(self, Item, Data):
        """ SetProjectInfo(self: cSapModel, Item: str, Data: str) -> int """
        pass

    def TreeIsUpdateSuspended(self, IsSuspended):
        """ TreeIsUpdateSuspended(self: cSapModel, IsSuspended: bool) -> (int, bool) """
        pass

    def TreeResumeUpdateData(self):
        """ TreeResumeUpdateData(self: cSapModel) -> int """
        pass

    def TreeSuspendUpdateData(self, updateAtResume):
        """ TreeSuspendUpdateData(self: cSapModel, updateAtResume: bool) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Analyze = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Analyze(self: cSapModel) -> cAnalyze

"""

    AreaElm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaElm(self: cSapModel) -> cAreaElm

"""

    AreaObj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaObj(self: cSapModel) -> cAreaObj

"""

    ConstraintDef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstraintDef(self: cSapModel) -> cConstraint

"""

    DatabaseTables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DatabaseTables(self: cSapModel) -> cDatabaseTables

"""

    DesignCompositeBeam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignCompositeBeam(self: cSapModel) -> cDesignCompositeBeam

"""

    DesignConcrete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignConcrete(self: cSapModel) -> cDesignConcrete

"""

    DesignConcreteSlab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignConcreteSlab(self: cSapModel) -> cDesignConcreteSlab

"""

    DesignResults = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignResults(self: cSapModel) -> cDesignResults

"""

    DesignShearWall = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignShearWall(self: cSapModel) -> cDesignShearWall

"""

    DesignSteel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignSteel(self: cSapModel) -> cDesignSteel

"""

    Detailing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Detailing(self: cSapModel) -> cDetailing

"""

    Diaphragm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diaphragm(self: cSapModel) -> cDiaphragm

"""

    EditArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditArea(self: cSapModel) -> cEditArea

"""

    EditFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditFrame(self: cSapModel) -> cEditFrame

"""

    EditGeneral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditGeneral(self: cSapModel) -> cEditGeneral

"""

    EditPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditPoint(self: cSapModel) -> cEditPoint

"""

    File = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: File(self: cSapModel) -> cFile

"""

    FrameObj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameObj(self: cSapModel) -> cFrameObj

"""

    Func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Func(self: cSapModel) -> cFunction

"""

    GDispl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GDispl(self: cSapModel) -> cGenDispl

"""

    GridSys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridSys(self: cSapModel) -> cGridSys

"""

    GroupDef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupDef(self: cSapModel) -> cGroup

"""

    LineElm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineElm(self: cSapModel) -> cLineElm

"""

    LinkElm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkElm(self: cSapModel) -> cLinkElm

"""

    LinkObj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkObj(self: cSapModel) -> cLinkObj

"""

    LoadCases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCases(self: cSapModel) -> cLoadCases

"""

    LoadPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadPatterns(self: cSapModel) -> cLoadPatterns

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: cSapModel) -> cOptions

"""

    PatternDef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternDef(self: cSapModel) -> cPattern

"""

    PierLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PierLabel(self: cSapModel) -> cPierLabel

"""

    PointElm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointElm(self: cSapModel) -> cPointElm

"""

    PointObj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointObj(self: cSapModel) -> cPointObj

"""

    PropArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropArea(self: cSapModel) -> cPropArea

"""

    PropAreaSpring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropAreaSpring(self: cSapModel) -> cPropAreaSpring

"""

    PropFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropFrame(self: cSapModel) -> cPropFrame

"""

    PropLineSpring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropLineSpring(self: cSapModel) -> cPropLineSpring

"""

    PropLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropLink(self: cSapModel) -> cPropLink

"""

    PropMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropMaterial(self: cSapModel) -> cPropMaterial

"""

    PropPointSpring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropPointSpring(self: cSapModel) -> cPropPointSpring

"""

    PropRebar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropRebar(self: cSapModel) -> cPropRebar

"""

    PropTendon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropTendon(self: cSapModel) -> cPropTendon

"""

    RespCombo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RespCombo(self: cSapModel) -> cCombo

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: cSapModel) -> cAnalysisResults

"""

    SelectObj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectObj(self: cSapModel) -> cSelect

"""

    SpandrelLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpandrelLabel(self: cSapModel) -> cSpandrelLabel

"""

    Story = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Story(self: cSapModel) -> cStory

"""

    TendonObj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TendonObj(self: cSapModel) -> cTendonObj

"""

    Tower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tower(self: cSapModel) -> cTower

"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: View(self: cSapModel) -> cView

"""



class cSelect:
    # no doc
    def All(self, Deselect):
        """ All(self: cSelect, Deselect: bool) -> int """
        pass

    def ClearSelection(self):
        """ ClearSelection(self: cSelect) -> int """
        pass

    def GetSelected(self, NumberItems, ObjectType, ObjectName):
        """ GetSelected(self: cSelect, NumberItems: int, ObjectType: Array[int], ObjectName: Array[str]) -> (int, int, Array[int], Array[str]) """
        pass

    def Group(self, Name, Deselect):
        """ Group(self: cSelect, Name: str, Deselect: bool) -> int """
        pass

    def InvertSelection(self):
        """ InvertSelection(self: cSelect) -> int """
        pass

    def PreviousSelection(self):
        """ PreviousSelection(self: cSelect) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cSpandrelLabel:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cSpandrelLabel, Name: str, NewName: str) -> int """
        pass

    def Delete(self, Name):
        """ Delete(self: cSpandrelLabel, Name: str) -> int """
        pass

    def GetNameList(self, NumberNames, MyName, IsMultiStory):
        """ GetNameList(self: cSpandrelLabel, NumberNames: int, MyName: Array[str], IsMultiStory: Array[bool]) -> (int, int, Array[str], Array[bool]) """
        pass

    def GetSectionProperties(self, Name, NumberStories, StoryName, NumAreaObj, NumLineObj, Length, DepthLeft, ThickLeft, DepthRight, ThickRight, MatProp, CGLeftX, CGLeftY, CGLeftZ, CGRightX, CGRightY, CGRightZ):
        """ GetSectionProperties(self: cSpandrelLabel, Name: str, NumberStories: int, StoryName: Array[str], NumAreaObj: Array[int], NumLineObj: Array[int], Length: Array[float], DepthLeft: Array[float], ThickLeft: Array[float], DepthRight: Array[float], ThickRight: Array[float], MatProp: Array[str], CGLeftX: Array[float], CGLeftY: Array[float], CGLeftZ: Array[float], CGRightX: Array[float], CGRightY: Array[float], CGRightZ: Array[float]) -> (int, int, Array[str], Array[int], Array[int], Array[float], Array[float], Array[float], Array[float], Array[float], Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetSpandrel(self, Name, IsMultiStory):
        """ GetSpandrel(self: cSpandrelLabel, Name: str, IsMultiStory: bool) -> (int, bool) """
        pass

    def SetSpandrel(self, Name, IsMultiStory):
        """ SetSpandrel(self: cSpandrelLabel, Name: str, IsMultiStory: bool) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cStory:
    # no doc
    def GetElevation(self, Name, Elevation):
        """ GetElevation(self: cStory, Name: str, Elevation: float) -> (int, float) """
        pass

    def GetGUID(self, Name, GUID):
        """ GetGUID(self: cStory, Name: str, GUID: str) -> (int, str) """
        pass

    def GetHeight(self, Name, Height):
        """ GetHeight(self: cStory, Name: str, Height: float) -> (int, float) """
        pass

    def GetMasterStory(self, Name, IsMasterStory):
        """ GetMasterStory(self: cStory, Name: str, IsMasterStory: bool) -> (int, bool) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cStory, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetSimilarTo(self, Name, IsMasterStory, SimilarToStory):
        """ GetSimilarTo(self: cStory, Name: str, IsMasterStory: bool, SimilarToStory: str) -> (int, bool, str) """
        pass

    def GetSplice(self, Name, SpliceAbove, SpliceHeight):
        """ GetSplice(self: cStory, Name: str, SpliceAbove: bool, SpliceHeight: float) -> (int, bool, float) """
        pass

    def GetStories(self, NumberStories, StoryNames, StoryElevations, StoryHeights, IsMasterStory, SimilarToStory, SpliceAbove, SpliceHeight):
        """ GetStories(self: cStory, NumberStories: int, StoryNames: Array[str], StoryElevations: Array[float], StoryHeights: Array[float], IsMasterStory: Array[bool], SimilarToStory: Array[str], SpliceAbove: Array[bool], SpliceHeight: Array[float]) -> (int, int, Array[str], Array[float], Array[float], Array[bool], Array[str], Array[bool], Array[float]) """
        pass

    def GetStories_2(self, BaseElevation, NumberStories, StoryNames, StoryElevations, StoryHeights, IsMasterStory, SimilarToStory, SpliceAbove, SpliceHeight, color):
        """ GetStories_2(self: cStory, BaseElevation: float, NumberStories: int, StoryNames: Array[str], StoryElevations: Array[float], StoryHeights: Array[float], IsMasterStory: Array[bool], SimilarToStory: Array[str], SpliceAbove: Array[bool], SpliceHeight: Array[float], color: Array[int]) -> (int, float, int, Array[str], Array[float], Array[float], Array[bool], Array[str], Array[bool], Array[float], Array[int]) """
        pass

    def SetElevation(self, Name, Elevation):
        """ SetElevation(self: cStory, Name: str, Elevation: float) -> int """
        pass

    def SetGUID(self, Name, GUID):
        """ SetGUID(self: cStory, Name: str, GUID: str) -> int """
        pass

    def SetHeight(self, Name, Height):
        """ SetHeight(self: cStory, Name: str, Height: float) -> int """
        pass

    def SetMasterStory(self, Name, IsMasterStory):
        """ SetMasterStory(self: cStory, Name: str, IsMasterStory: bool) -> int """
        pass

    def SetSimilarTo(self, Name, SimilarToStory):
        """ SetSimilarTo(self: cStory, Name: str, SimilarToStory: str) -> int """
        pass

    def SetSplice(self, Name, SpliceAbove, SpliceHeight):
        """ SetSplice(self: cStory, Name: str, SpliceAbove: bool, SpliceHeight: float) -> int """
        pass

    def SetStories(self, StoryNames, StoryElevations, StoryHeights, IsMasterStory, SimilarToStory, SpliceAbove, SpliceHeight):
        """ SetStories(self: cStory, StoryNames: Array[str], StoryElevations: Array[float], StoryHeights: Array[float], IsMasterStory: Array[bool], SimilarToStory: Array[str], SpliceAbove: Array[bool], SpliceHeight: Array[float]) -> int """
        pass

    def SetStories_2(self, BaseElevation, NumberStories, StoryNames, StoryHeights, IsMasterStory, SimilarToStory, SpliceAbove, SpliceHeight, color):
        """ SetStories_2(self: cStory, BaseElevation: float, NumberStories: int, StoryNames: Array[str], StoryHeights: Array[float], IsMasterStory: Array[bool], SimilarToStory: Array[str], SpliceAbove: Array[bool], SpliceHeight: Array[float], color: Array[int]) -> (int, Array[str], Array[float], Array[bool], Array[str], Array[bool], Array[float], Array[int]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cTendonObj:
    # no doc
    def ChangeName(self, Name, NewName):
        """ ChangeName(self: cTendonObj, Name: str, NewName: str) -> int """
        pass

    def Count(self):
        """ Count(self: cTendonObj) -> int """
        pass

    def GetDatumOffset(self, Name, NumberItems, TendonName, DatumOffset, ItemType):
        """ GetDatumOffset(self: cTendonObj, Name: str, NumberItems: int, TendonName: Array[str], DatumOffset: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[float]) """
        pass

    def GetDrawingPoint(self, Name, NumberItems, TendonName, DrawingPointID, gx, gy, gz, ItemType):
        """ GetDrawingPoint(self: cTendonObj, Name: str, NumberItems: int, TendonName: Array[str], DrawingPointID: Array[str], gx: Array[float], gy: Array[float], gz: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[float], Array[float], Array[float]) """
        pass

    def GetGroupAssign(self, Name, NumberGroups, Groups):
        """ GetGroupAssign(self: cTendonObj, Name: str, NumberGroups: int, Groups: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetLoadForceStress_1(self, Name, NumberItems, TendonName, LoadPatFinal, LoadPatTransfer, JackFrom, LoadType, LoadValue, LossSpecification, ItemType):
        """ GetLoadForceStress_1(self: cTendonObj, Name: str, NumberItems: int, TendonName: Array[str], LoadPatFinal: Array[str], LoadPatTransfer: Array[str], JackFrom: Array[int], LoadType: Array[int], LoadValue: Array[float], LossSpecification: Array[int], ItemType: eItemType) -> (int, int, Array[str], Array[str], Array[str], Array[int], Array[int], Array[float], Array[int]) """
        pass

    def GetLossesDetailed(self, Name, NumberItems, TendonName, CurvatureCoeff, WobbleCoeff, LossAnchorage, LossShortening, LossCreep, LossShrinkage, LossSteelRelax, ItemType):
        """ GetLossesDetailed(self: cTendonObj, Name: str, NumberItems: int, TendonName: Array[str], CurvatureCoeff: Array[float], WobbleCoeff: Array[float], LossAnchorage: Array[float], LossShortening: Array[float], LossCreep: Array[float], LossShrinkage: Array[float], LossSteelRelax: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLossesFixed(self, Name, NumberItems, TendonName, StressingFixed, LongTermFixed, ItemType):
        """ GetLossesFixed(self: cTendonObj, Name: str, NumberItems: int, TendonName: Array[str], StressingFixed: Array[float], LongTermFixed: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[float], Array[float]) """
        pass

    def GetLossesPercent(self, Name, NumberItems, TendonName, StressingPercent, LongTermPercent, ItemType):
        """ GetLossesPercent(self: cTendonObj, Name: str, NumberItems: int, TendonName: Array[str], StressingPercent: Array[float], LongTermPercent: Array[float], ItemType: eItemType) -> (int, int, Array[str], Array[float], Array[float]) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cTendonObj, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetNameListOnStory(self, StoryName, NumberNames, MyName):
        """ GetNameListOnStory(self: cTendonObj, StoryName: str, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def GetNumberStrands(self, Name, NumberItems, TendonName, NumberStrands, ItemType):
        """ GetNumberStrands(self: cTendonObj, Name: str, NumberItems: int, TendonName: Array[str], NumberStrands: Array[int], ItemType: eItemType) -> (int, int, Array[str], Array[int]) """
        pass

    def GetProperty(self, Name, PropName):
        """ GetProperty(self: cTendonObj, Name: str, PropName: str) -> (int, str) """
        pass

    def GetSelected(self, Name, Selected):
        """ GetSelected(self: cTendonObj, Name: str, Selected: bool) -> (int, bool) """
        pass

    def GetTendonGeometry(self, Name, NumberPoints, X, Y, Z, CSys):
        """ GetTendonGeometry(self: cTendonObj, Name: str, NumberPoints: int, X: Array[float], Y: Array[float], Z: Array[float], CSys: str) -> (int, int, Array[float], Array[float], Array[float]) """
        pass

    def SetGroupAssign(self, Name, GroupName, Remove, ItemType):
        """ SetGroupAssign(self: cTendonObj, Name: str, GroupName: str, Remove: bool, ItemType: eItemType) -> int """
        pass

    def SetSelected(self, Name, Selected, ItemType):
        """ SetSelected(self: cTendonObj, Name: str, Selected: bool, ItemType: eItemType) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cTower:
    # no doc
    def AddCopyOfTower(self, TowerName, NewTowerName):
        """ AddCopyOfTower(self: cTower, TowerName: str, NewTowerName: str) -> int """
        pass

    def AddNewTower(self, TowerName, NumberStories, TypicalStoryHeight, BotttomStoryHeight):
        """ AddNewTower(self: cTower, TowerName: str, NumberStories: int, TypicalStoryHeight: float, BotttomStoryHeight: float) -> int """
        pass

    def AllowMultipleTowers(self, AllowMultTowers, RetainedTower, Combine):
        """ AllowMultipleTowers(self: cTower, AllowMultTowers: bool, RetainedTower: str, Combine: bool) -> int """
        pass

    def DeleteTower(self, TowerName, Associate, AssocWithTower):
        """ DeleteTower(self: cTower, TowerName: str, Associate: bool, AssocWithTower: str) -> int """
        pass

    def GetActiveTower(self, TowerName):
        """ GetActiveTower(self: cTower, TowerName: str) -> (int, str) """
        pass

    def GetNameList(self, NumberNames, MyName):
        """ GetNameList(self: cTower, NumberNames: int, MyName: Array[str]) -> (int, int, Array[str]) """
        pass

    def RenameTower(self, TowerName, NewTowerName):
        """ RenameTower(self: cTower, TowerName: str, NewTowerName: str) -> int """
        pass

    def SetActiveTower(self, TowerName):
        """ SetActiveTower(self: cTower, TowerName: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class cView:
    # no doc
    def RefreshView(self, Window, Zoom):
        """ RefreshView(self: cView, Window: int, Zoom: bool) -> int """
        pass

    def RefreshWindow(self, Window):
        """ RefreshWindow(self: cView, Window: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class e2DFrameType(Enum, IComparable, IFormattable, IConvertible):
    """ enum e2DFrameType, values: ConcentricBraced (1), EccentricBraced (2), PortalFrame (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ConcentricBraced = None
    EccentricBraced = None
    PortalFrame = None
    value__ = None


class e3DFrameType(Enum, IComparable, IFormattable, IConvertible):
    """ enum e3DFrameType, values: BeamSlab (2), FlatPlate (3), OpenFrame (0), PerimeterFrame (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BeamSlab = None
    FlatPlate = None
    OpenFrame = None
    PerimeterFrame = None
    value__ = None


class eAreaDesignOrientation(Enum, IComparable, IFormattable, IConvertible):
    """ enum eAreaDesignOrientation, values: Floor (2), Null (4), Other (5), Ramp_DO_NOT_USE (3), Wall (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Floor = None
    Null = None
    Other = None
    Ramp_DO_NOT_USE = None
    value__ = None
    Wall = None


class eBridgeCodeAASHTO(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeCodeAASHTO, values: AASHTO_LRFD_2007 (1), AASHTO_LRFD_2012 (2), AASHTO_LRFD_2014 (3), AASHTO_LRFD_2017 (4), AASHTO_LRFD_2020 (5), AASHTO_STD_2002 (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AASHTO_LRFD_2007 = None
    AASHTO_LRFD_2012 = None
    AASHTO_LRFD_2014 = None
    AASHTO_LRFD_2017 = None
    AASHTO_LRFD_2020 = None
    AASHTO_STD_2002 = None
    value__ = None


class eBridgeCodeInterims(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeCodeInterims, values: Interim_2011 (1), Interim_2012 (2), Interim_2013 (3), Interim_2014 (4), Interim_2015 (5), NoInterims (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Interim_2011 = None
    Interim_2012 = None
    Interim_2013 = None
    Interim_2014 = None
    Interim_2015 = None
    NoInterims = None
    value__ = None


class eBridgeObjectBentPart(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeObjectBentPart, values: Bearing (3), CapBeam (1), Column (2), Wall (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bearing = None
    CapBeam = None
    Column = None
    value__ = None
    Wall = None


class eBridgeObjectFoundationPart(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeObjectFoundationPart, values: Footing (1), FoundationSpring (4), Pile (3), PileCap (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Footing = None
    FoundationSpring = None
    Pile = None
    PileCap = None
    value__ = None


class eBridgeObjectType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeObjectType, values: General (0), Segmental (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    General = None
    Segmental = None
    value__ = None


class eBridgeObjectUserPointType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeObjectUserPointType, values: General (0), SegmentalTendon (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    General = None
    SegmentalTendon = None
    value__ = None


class eBridgeResponseDesignRating(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeResponseDesignRating, values: Design_Crack_Bot_Crack_Width (55), Design_Crack_Top_Bot_Crack_Widths (56), Design_Crack_Top_Crack_Width (54), Design_Fatigue_Bot_Flange_Lateral_Bending_Stress_Range (75), Design_Fatigue_Bot_Flange_Tensile_Stress_Range_Without_FLB (74), Design_Fatigue_DC_Ratio_Web_Shear (76), Design_Fatigue_Top_Flange_Tensile_Stress_Range_Without_FLB (73), Design_Flexure_Moment_About_Horizontal_Axis_M3 (64), Design_Principal_Stress_Beam_Web_Bot (61), Design_Principal_Stress_Beam_Web_Top (60), Design_Principal_Stress_Envelope (57), Design_Principal_Stress_Neutral_Axis (62), Design_Principal_Stress_Web_Bot (59), Design_Principal_Stress_Web_Top (58), Design_Shear_Controlling_DC_Ratio (43), Design_Shear_Controlling_Shear_DC_Ratio (34), Design_Shear_Controlling_Torsion_DC_Ratio (35), Design_Shear_Demand_Concrete_Shear_Capacity_Ratio (33), Design_Shear_Longit_Rebar_Area (45), Design_Shear_Longit_Rebar_Area_Beam (50), Design_Shear_Longit_Rebar_Area_Bot_Flange (48), Design_Shear_Longit_Rebar_Area_Bot_Slab (46), Design_Shear_Longit_Rebar_Area_Slab (49), Design_Shear_Longit_Rebar_Area_Top_Slab (47), Design_Shear_Longit_Torsional_Rebar_Area_PerL (51), Design_Shear_Rebar_Area_PerL (44), Design_Shear_Required_Extra_Longit_Rebar_Area (37), Design_Shear_Required_Extra_Longit_Rebar_Area_Beam (42), Design_Shear_Required_Extra_Longit_Rebar_Area_Bot_Slab (39), Design_Shear_Required_Extra_Longit_Rebar_Area_For_Torsion (38), Design_Shear_Required_Extra_Longit_Rebar_Area_Slab (41), Design_Shear_Required_Extra_Longit_Rebar_Area_Top_Slab (40), Design_Shear_Required_Extra_Shear_Rebar_Area_PerL (36), Design_Shear_Torsion_Plus_Shear_Rebar_Area_PerL (53), Design_Shear_Torsion_Rebar_Area_PerL (52), Design_Strength_DC_Ratio_FlexureShearInteract_Neg (71), Design_Strength_DC_Ratio_FlexureShearInteract_Pos (70), Design_Strength_DC_Ratio_Negative_Moment (66), Design_Strength_DC_Ratio_Net_Section_Fracture_Neg (69), Design_Strength_DC_Ratio_Net_Section_Fracture_Pos (68), Design_Strength_DC_Ratio_Positive_Moment (65), Design_Strength_DC_Ratio_Shear (67), Design_Strength_Total_Nominal_Shear_Force_6_10_10_4_2 (72), Design_Tendon_Stress_Controlling_DC_Ratio (63), Rating_Flexure (81), Rating_Flexure_Factored_Moment_Resistance (82), Rating_Flexure_Factored_Moment_Resistance_UMr (83), Rating_Flexure_Live_load_Capacity_Factor_F (84), Rating_MinRebar_Flexure_Rating (92), Rating_MinRebar_Min_Of_Abs_1_2Mcr_And_Abs_1_33Mu_For_Neg (91), Rating_MinRebar_Min_Of_Abs_1_2Mcr_And_Abs_1_33Mu_For_Pos (90), Rating_Service (93), Rating_Service_Flexure_Rating (89), Rating_Shear (77), Rating_Shear_Factored_Shear_Resistance (78), Rating_Shear_Factored_Shear_Resistance_UVr (79), Rating_Shear_Live_load_Capacity_Factor_F (80), Rating_Strength_Flexure_Rating (86), Rating_Strength_Live_load_Capacity_Factor_F_Moment_M3 (87), Rating_Strength_Live_load_Capacity_Factor_F_Shear_V2 (88), Rating_Strength_Shear_Rating (85), S11_Longitudinal_Beam_Bot_Center (39), S11_Longitudinal_Beam_Bot_Envelope (32), S11_Longitudinal_Beam_Bot_Left (29), S11_Longitudinal_Beam_Bot_Right (31), S11_Longitudinal_Beam_Top_Center (10), S11_Longitudinal_Beam_Top_Envelope (12), S11_Longitudinal_Beam_Top_Left (9), S11_Longitudinal_Beam_Top_Right (11), S11_Longitudinal_Bot_Center (15), S11_Longitudinal_Bot_Envelope (18), S11_Longitudinal_Bot_Left (13), S11_Longitudinal_Bot_Left_Corner (14), S11_Longitudinal_Bot_Right (16), S11_Longitudinal_Bot_Right_Corner (17), S11_Longitudinal_Girder_Bot_Envelope (21), S11_Longitudinal_Girder_Bot_Left (19), S11_Longitudinal_Girder_Bot_Right (20), S11_Longitudinal_Slab_Bot_Beam_Center (24), S11_Longitudinal_Slab_Bot_Beam_Left (23), S11_Longitudinal_Slab_Bot_Beam_Right (25), S11_Longitudinal_Slab_Bot_Center (26), S11_Longitudinal_Slab_Bot_Envelope (28), S11_Longitudinal_Slab_Bot_Left (22), S11_Longitudinal_Slab_Bot_Right (27), S11_Longitudinal_Slab_Top_Beam_Center (6), S11_Longitudinal_Slab_Top_Center (5), S11_Longitudinal_Slab_Top_Envelope (8), S11_Longitudinal_Slab_Top_Left (4), S11_Longitudinal_Slab_Top_Right (7), S11_Longitudinal_Top_Center (1), S11_Longitudinal_Top_Envelope (3), S11_Longitudinal_Top_Left (0), S11_Longitudinal_Top_Right (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Design_Crack_Bot_Crack_Width = None
    Design_Crack_Top_Bot_Crack_Widths = None
    Design_Crack_Top_Crack_Width = None
    Design_Fatigue_Bot_Flange_Lateral_Bending_Stress_Range = None
    Design_Fatigue_Bot_Flange_Tensile_Stress_Range_Without_FLB = None
    Design_Fatigue_DC_Ratio_Web_Shear = None
    Design_Fatigue_Top_Flange_Tensile_Stress_Range_Without_FLB = None
    Design_Flexure_Moment_About_Horizontal_Axis_M3 = None
    Design_Principal_Stress_Beam_Web_Bot = None
    Design_Principal_Stress_Beam_Web_Top = None
    Design_Principal_Stress_Envelope = None
    Design_Principal_Stress_Neutral_Axis = None
    Design_Principal_Stress_Web_Bot = None
    Design_Principal_Stress_Web_Top = None
    Design_Shear_Controlling_DC_Ratio = None
    Design_Shear_Controlling_Shear_DC_Ratio = None
    Design_Shear_Controlling_Torsion_DC_Ratio = None
    Design_Shear_Demand_Concrete_Shear_Capacity_Ratio = None
    Design_Shear_Longit_Rebar_Area = None
    Design_Shear_Longit_Rebar_Area_Beam = None
    Design_Shear_Longit_Rebar_Area_Bot_Flange = None
    Design_Shear_Longit_Rebar_Area_Bot_Slab = None
    Design_Shear_Longit_Rebar_Area_Slab = None
    Design_Shear_Longit_Rebar_Area_Top_Slab = None
    Design_Shear_Longit_Torsional_Rebar_Area_PerL = None
    Design_Shear_Rebar_Area_PerL = None
    Design_Shear_Required_Extra_Longit_Rebar_Area = None
    Design_Shear_Required_Extra_Longit_Rebar_Area_Beam = None
    Design_Shear_Required_Extra_Longit_Rebar_Area_Bot_Slab = None
    Design_Shear_Required_Extra_Longit_Rebar_Area_For_Torsion = None
    Design_Shear_Required_Extra_Longit_Rebar_Area_Slab = None
    Design_Shear_Required_Extra_Longit_Rebar_Area_Top_Slab = None
    Design_Shear_Required_Extra_Shear_Rebar_Area_PerL = None
    Design_Shear_Torsion_Plus_Shear_Rebar_Area_PerL = None
    Design_Shear_Torsion_Rebar_Area_PerL = None
    Design_Strength_DC_Ratio_FlexureShearInteract_Neg = None
    Design_Strength_DC_Ratio_FlexureShearInteract_Pos = None
    Design_Strength_DC_Ratio_Negative_Moment = None
    Design_Strength_DC_Ratio_Net_Section_Fracture_Neg = None
    Design_Strength_DC_Ratio_Net_Section_Fracture_Pos = None
    Design_Strength_DC_Ratio_Positive_Moment = None
    Design_Strength_DC_Ratio_Shear = None
    Design_Strength_Total_Nominal_Shear_Force_6_10_10_4_2 = None
    Design_Tendon_Stress_Controlling_DC_Ratio = None
    Rating_Flexure = None
    Rating_Flexure_Factored_Moment_Resistance = None
    Rating_Flexure_Factored_Moment_Resistance_UMr = None
    Rating_Flexure_Live_load_Capacity_Factor_F = None
    Rating_MinRebar_Flexure_Rating = None
    Rating_MinRebar_Min_Of_Abs_1_2Mcr_And_Abs_1_33Mu_For_Neg = None
    Rating_MinRebar_Min_Of_Abs_1_2Mcr_And_Abs_1_33Mu_For_Pos = None
    Rating_Service = None
    Rating_Service_Flexure_Rating = None
    Rating_Shear = None
    Rating_Shear_Factored_Shear_Resistance = None
    Rating_Shear_Factored_Shear_Resistance_UVr = None
    Rating_Shear_Live_load_Capacity_Factor_F = None
    Rating_Strength_Flexure_Rating = None
    Rating_Strength_Live_load_Capacity_Factor_F_Moment_M3 = None
    Rating_Strength_Live_load_Capacity_Factor_F_Shear_V2 = None
    Rating_Strength_Shear_Rating = None
    S11_Longitudinal_Beam_Bot_Center = None
    S11_Longitudinal_Beam_Bot_Envelope = None
    S11_Longitudinal_Beam_Bot_Left = None
    S11_Longitudinal_Beam_Bot_Right = None
    S11_Longitudinal_Beam_Top_Center = None
    S11_Longitudinal_Beam_Top_Envelope = None
    S11_Longitudinal_Beam_Top_Left = None
    S11_Longitudinal_Beam_Top_Right = None
    S11_Longitudinal_Bot_Center = None
    S11_Longitudinal_Bot_Envelope = None
    S11_Longitudinal_Bot_Left = None
    S11_Longitudinal_Bot_Left_Corner = None
    S11_Longitudinal_Bot_Right = None
    S11_Longitudinal_Bot_Right_Corner = None
    S11_Longitudinal_Girder_Bot_Envelope = None
    S11_Longitudinal_Girder_Bot_Left = None
    S11_Longitudinal_Girder_Bot_Right = None
    S11_Longitudinal_Slab_Bot_Beam_Center = None
    S11_Longitudinal_Slab_Bot_Beam_Left = None
    S11_Longitudinal_Slab_Bot_Beam_Right = None
    S11_Longitudinal_Slab_Bot_Center = None
    S11_Longitudinal_Slab_Bot_Envelope = None
    S11_Longitudinal_Slab_Bot_Left = None
    S11_Longitudinal_Slab_Bot_Right = None
    S11_Longitudinal_Slab_Top_Beam_Center = None
    S11_Longitudinal_Slab_Top_Center = None
    S11_Longitudinal_Slab_Top_Envelope = None
    S11_Longitudinal_Slab_Top_Left = None
    S11_Longitudinal_Slab_Top_Right = None
    S11_Longitudinal_Top_Center = None
    S11_Longitudinal_Top_Envelope = None
    S11_Longitudinal_Top_Left = None
    S11_Longitudinal_Top_Right = None
    value__ = None


class eBridgeResponseDisplDOF(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeResponseDisplDOF, values: Avg_Longitudinal_Rotation (4), Longitudinal_Displacement (2), Longitudinal_Rotation (3), Transverse_Displacement (1), Vertical_Displacement (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Avg_Longitudinal_Rotation = None
    Longitudinal_Displacement = None
    Longitudinal_Rotation = None
    Transverse_Displacement = None
    value__ = None
    Vertical_Displacement = None


class eBridgeResponseDisplLoc(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeResponseDisplLoc, values: Left_Web (5), Left_Web_Bottom (4), Left_Web_Top (3), Right_Web (8), Right_Web_Bottom (7), Right_Web_Top (6), Slab_Center (9), Web (2), Web_Bottom (1), Web_Top (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Left_Web = None
    Left_Web_Bottom = None
    Left_Web_Top = None
    Right_Web = None
    Right_Web_Bottom = None
    Right_Web_Top = None
    Slab_Center = None
    value__ = None
    Web = None
    Web_Bottom = None
    Web_Top = None


class eBridgeResponseForce(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeResponseForce, values: Axial_Force_P (1), Moment_About_Horizontal_Axis_M3 (6), Moment_About_Vertical_Axis_M2 (5), Shear_Horizontal_V3 (3), Shear_Vertical_V2 (2), Torsion_T (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Axial_Force_P = None
    Moment_About_Horizontal_Axis_M3 = None
    Moment_About_Vertical_Axis_M2 = None
    Shear_Horizontal_V3 = None
    Shear_Vertical_V2 = None
    Torsion_T = None
    value__ = None


class eBridgeResponsePart(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeResponsePart, values: All_Beams (7), All_Girders (6), All_Slabs (9), All_Webs (8), Beam (3), Entire_Bridge_Section (1), Entire_Section_Plus_All_Girders (10), Girder (2), Slab (5), Web (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    All_Beams = None
    All_Girders = None
    All_Slabs = None
    All_Webs = None
    Beam = None
    Entire_Bridge_Section = None
    Entire_Section_Plus_All_Girders = None
    Girder = None
    Slab = None
    value__ = None
    Web = None


class eBridgeResponseStress(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeResponseStress, values: S11_Lateral_Bending_Bot (25), S11_Lateral_Bending_Top (22), S11_Lateral_Bending_Top_ULeft (23), S11_Lateral_Bending_Top_URight (24), S11_Longitudinal_Bot_Beam_Left (16), S11_Longitudinal_Bot_Beam_Right (17), S11_Longitudinal_Bot_Center (14), S11_Longitudinal_Bot_Envelope (18), S11_Longitudinal_Bot_Left (13), S11_Longitudinal_Bot_Right (15), S11_Longitudinal_Top_Beam_Center (3), S11_Longitudinal_Top_Bot_Center (20), S11_Longitudinal_Top_Bot_Left (19), S11_Longitudinal_Top_Bot_Right (21), S11_Longitudinal_Top_Center (1), S11_Longitudinal_Top_Envelope (4), S11_Longitudinal_Top_Left (0), S11_Longitudinal_Top_Right (2), S11_Longitudinal_Top_ULeft_Center (6), S11_Longitudinal_Top_ULeft_Envelope (8), S11_Longitudinal_Top_ULeft_Left (5), S11_Longitudinal_Top_ULeft_Right (7), S11_Longitudinal_Top_URight_Center (10), S11_Longitudinal_Top_URight_Envelope (12), S11_Longitudinal_Top_URight_Left (9), S11_Longitudinal_Top_URight_Right (11) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    S11_Lateral_Bending_Bot = None
    S11_Lateral_Bending_Top = None
    S11_Lateral_Bending_Top_ULeft = None
    S11_Lateral_Bending_Top_URight = None
    S11_Longitudinal_Bot_Beam_Left = None
    S11_Longitudinal_Bot_Beam_Right = None
    S11_Longitudinal_Bot_Center = None
    S11_Longitudinal_Bot_Envelope = None
    S11_Longitudinal_Bot_Left = None
    S11_Longitudinal_Bot_Right = None
    S11_Longitudinal_Top_Beam_Center = None
    S11_Longitudinal_Top_Bot_Center = None
    S11_Longitudinal_Top_Bot_Left = None
    S11_Longitudinal_Top_Bot_Right = None
    S11_Longitudinal_Top_Center = None
    S11_Longitudinal_Top_Envelope = None
    S11_Longitudinal_Top_Left = None
    S11_Longitudinal_Top_Right = None
    S11_Longitudinal_Top_ULeft_Center = None
    S11_Longitudinal_Top_ULeft_Envelope = None
    S11_Longitudinal_Top_ULeft_Left = None
    S11_Longitudinal_Top_ULeft_Right = None
    S11_Longitudinal_Top_URight_Center = None
    S11_Longitudinal_Top_URight_Envelope = None
    S11_Longitudinal_Top_URight_Left = None
    S11_Longitudinal_Top_URight_Right = None
    value__ = None


class eBridgeSegmentConstructionMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeSegmentConstructionMethod, values: CastInPlace (1), Precast (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CastInPlace = None
    Precast = None
    value__ = None


class eBridgeSegmentType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeSegmentType, values: Closure (3), PierTable (1), Rigid (0), Segment (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Closure = None
    PierTable = None
    Rigid = None
    Segment = None
    value__ = None


class eBridgeTendonCategory(Enum, IComparable, IFormattable, IConvertible):
    """ enum eBridgeTendonCategory, values: BottomSpan (2), Cantilever (1), Continuity (4), General (0), TopSpan (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BottomSpan = None
    Cantilever = None
    Continuity = None
    General = None
    TopSpan = None
    value__ = None


class eCNameType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eCNameType, values: LoadCase (0), LoadCombo (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LoadCase = None
    LoadCombo = None
    value__ = None


class eConstraintAxis(Enum, IComparable, IFormattable, IConvertible):
    """ enum eConstraintAxis, values: AutoAxis (4), X (1), Y (2), Z (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AutoAxis = None
    value__ = None
    X = None
    Y = None
    Z = None


class eConstraintType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eConstraintType, values: Beam (5), Body (1), Diaphragm (2), Equal (6), Line (13), Local (7), Plate (3), Rod (4), Weld (8) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Beam = None
    Body = None
    Diaphragm = None
    Equal = None
    Line = None
    Local = None
    Plate = None
    Rod = None
    value__ = None
    Weld = None


class eDeckType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eDeckType, values: Filled (1), SolidSlab (3), Unfilled (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Filled = None
    SolidSlab = None
    Unfilled = None
    value__ = None


class eDesignActionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eDesignActionType, values: LongTermComposite (3), NonComposite (1), Other (5), ShortTermComposite (2), Staged (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LongTermComposite = None
    NonComposite = None
    Other = None
    ShortTermComposite = None
    Staged = None
    value__ = None


class eDiaphragmOption(Enum, IComparable, IFormattable, IConvertible):
    """ enum eDiaphragmOption, values: DefinedDiaphragm (3), Disconnect (1), FromShellObject (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefinedDiaphragm = None
    Disconnect = None
    FromShellObject = None
    value__ = None


class eForce(Enum, IComparable, IFormattable, IConvertible):
    """ enum eForce, values: kgf (5), kip (2), kN (4), lb (1), N (3), NotApplicable (0), tonf (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    kgf = None
    kip = None
    kN = None
    lb = None
    N = None
    NotApplicable = None
    tonf = None
    value__ = None


class eFrameDesignOrientation(Enum, IComparable, IFormattable, IConvertible):
    """ enum eFrameDesignOrientation, values: Beam (2), Brace (3), Column (1), Null (4), Other (5) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Beam = None
    Brace = None
    Column = None
    Null = None
    Other = None
    value__ = None


class eFramePropType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eFramePropType, values: Angle (4), Auto (12), Box (6), Bridge (16), BucklingRestrainedBrace (33), BuiltupICoverplate (23), BuiltupIHybrid (26), BuiltupUHybrid (27), Channel (2), Circle (9), Cold_2C (18), Cold_2L (21), Cold_Box (42), Cold_C (17), Cold_Hat (22), Cold_I (43), Cold_L (20), Cold_Pipe (44), Cold_T (45), Cold_Z (19), Concrete_L (28), ConcreteBox (36), ConcreteCross (38), ConcretePipe (37), ConcreteTee (35), CoreBrace_BRB (34), DbChannel (11), DblAngle (5), EncasedCircle (32), EncasedRectangle (31), FilledPipe (30), FilledTube (29), General (10), I (1), Joist (15), PCCGirderI (24), PCCGirderSuperT (41), PCCGirderU (25), Pipe (7), Rectangular (8), SD (13), SteelPlate (39), SteelRod (40), T (3), Trapezoidal (46), Variable (14) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Angle = None
    Auto = None
    Box = None
    Bridge = None
    BucklingRestrainedBrace = None
    BuiltupICoverplate = None
    BuiltupIHybrid = None
    BuiltupUHybrid = None
    Channel = None
    Circle = None
    Cold_2C = None
    Cold_2L = None
    Cold_Box = None
    Cold_C = None
    Cold_Hat = None
    Cold_I = None
    Cold_L = None
    Cold_Pipe = None
    Cold_T = None
    Cold_Z = None
    ConcreteBox = None
    ConcreteCross = None
    ConcretePipe = None
    ConcreteTee = None
    Concrete_L = None
    CoreBrace_BRB = None
    DbChannel = None
    DblAngle = None
    EncasedCircle = None
    EncasedRectangle = None
    FilledPipe = None
    FilledTube = None
    General = None
    I = None
    Joist = None
    PCCGirderI = None
    PCCGirderSuperT = None
    PCCGirderU = None
    Pipe = None
    Rectangular = None
    SD = None
    SteelPlate = None
    SteelRod = None
    T = None
    Trapezoidal = None
    value__ = None
    Variable = None


class eHingeLocationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eHingeLocationType, values: OffsetFromIEnd (2), OffsetFromJEnd (3), RelativeDistance (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OffsetFromIEnd = None
    OffsetFromJEnd = None
    RelativeDistance = None
    value__ = None


class eItemType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eItemType, values: Group (1), Objects (0), SelectedObjects (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Group = None
    Objects = None
    SelectedObjects = None
    value__ = None


class eItemTypeElm(Enum, IComparable, IFormattable, IConvertible):
    """ enum eItemTypeElm, values: Element (1), GroupElm (2), ObjectElm (0), SelectionElm (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Element = None
    GroupElm = None
    ObjectElm = None
    SelectionElm = None
    value__ = None


class eLength(Enum, IComparable, IFormattable, IConvertible):
    """ enum eLength, values: cm (5), ft (2), inch (1), m (6), micron (3), mm (4), NotApplicable (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    cm = None
    ft = None
    inch = None
    m = None
    micron = None
    mm = None
    NotApplicable = None
    value__ = None


class eLinkPropType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eLinkPropType, values: Damper (2), Gap (3), Hook (4), Isolator1 (6), Isolator2 (7), Isolator3 (10), Linear (1), MultilinearElastic (8), MultilinearPlastic (9), PlasticWen (5) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Damper = None
    Gap = None
    Hook = None
    Isolator1 = None
    Isolator2 = None
    Isolator3 = None
    Linear = None
    MultilinearElastic = None
    MultilinearPlastic = None
    PlasticWen = None
    value__ = None


class eLoadCaseType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eLoadCaseType, values: Buckling (10), HyperStatic (14), LinearDynamic (7), LinearHistory (5), LinearStatic (1), LinearStaticMultiStep (13), Modal (3), MovingLoad (9), NonlinearDynamic (8), NonlinearHistory (6), NonlinearStatic (2), PowerSpectralDensity (12), ResponseSpectrum (4), SteadyState (11) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Buckling = None
    HyperStatic = None
    LinearDynamic = None
    LinearHistory = None
    LinearStatic = None
    LinearStaticMultiStep = None
    Modal = None
    MovingLoad = None
    NonlinearDynamic = None
    NonlinearHistory = None
    NonlinearStatic = None
    PowerSpectralDensity = None
    ResponseSpectrum = None
    SteadyState = None
    value__ = None


class eLoadPatternType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eLoadPatternType, values: ActiveEarthPressure (45), Bouyancy (36), Braking (15), Centrifugal (16), Construction (39), Creep (29), Dead (1), DeadManufacture (42), DeadWater (41), DeadWearing (40), DownDrag (23), EarthHydrostatic (43), EarthSurcharge (22), EuroLm1Char (48), EuroLm1Freq (49), EuroLm2 (50), EuroLm3 (51), EuroLm4 (52), Friction (17), HorizontalEarthPressure (20), Hyperstatic (35), Ice (18), Impact (38), Live (3), LiveLoadSurcharge (31), LockedInForces (32), Move (9), MoveDeflection (57), MoveFatigue (55), MoveFatiguePermit (56), MoveTrain (58), Notional (12), Other (8), PassiveEarthPressure (44), PatternAuto (60), PatternLive (13), PedestrianLL (33), PedestrianLLReduced (46), Permit (54), Prestress (34), PrestressTransfer (59), Quake (5), QuakeDrift (61), QuakeVerticalOnly (62), ReduceLive (4), Rooflive (11), SeaState (53), Settlement (27), Shrinkage (28), Snow (7), SnowHighAltitude (47), StreamFlow (37), SuperDead (2), Temperature (10), TemperatureGradient (26), VehicleCollision (24), VerticalEarthPressure (21), VesselCollision (25), WaterloadPressure (30), Wave (14), Wind (6), WindOnLiveLoad (19) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveEarthPressure = None
    Bouyancy = None
    Braking = None
    Centrifugal = None
    Construction = None
    Creep = None
    Dead = None
    DeadManufacture = None
    DeadWater = None
    DeadWearing = None
    DownDrag = None
    EarthHydrostatic = None
    EarthSurcharge = None
    EuroLm1Char = None
    EuroLm1Freq = None
    EuroLm2 = None
    EuroLm3 = None
    EuroLm4 = None
    Friction = None
    HorizontalEarthPressure = None
    Hyperstatic = None
    Ice = None
    Impact = None
    Live = None
    LiveLoadSurcharge = None
    LockedInForces = None
    Move = None
    MoveDeflection = None
    MoveFatigue = None
    MoveFatiguePermit = None
    MoveTrain = None
    Notional = None
    Other = None
    PassiveEarthPressure = None
    PatternAuto = None
    PatternLive = None
    PedestrianLL = None
    PedestrianLLReduced = None
    Permit = None
    Prestress = None
    PrestressTransfer = None
    Quake = None
    QuakeDrift = None
    QuakeVerticalOnly = None
    ReduceLive = None
    Rooflive = None
    SeaState = None
    Settlement = None
    Shrinkage = None
    Snow = None
    SnowHighAltitude = None
    StreamFlow = None
    SuperDead = None
    Temperature = None
    TemperatureGradient = None
    value__ = None
    VehicleCollision = None
    VerticalEarthPressure = None
    VesselCollision = None
    WaterloadPressure = None
    Wave = None
    Wind = None
    WindOnLiveLoad = None


class eMatCoupledType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eMatCoupledType, values: ModifiedDarwinPecknoldConcrete (3), None (1), VonMisesPlasticity (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ModifiedDarwinPecknoldConcrete = None
    None = None
    value__ = None
    VonMisesPlasticity = None


class eMatType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eMatType, values: Aluminum (4), ColdFormed (5), Concrete (2), Masonry (8), NoDesign (3), Rebar (6), Steel (1), Tendon (7) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Aluminum = None
    ColdFormed = None
    Concrete = None
    Masonry = None
    NoDesign = None
    Rebar = None
    Steel = None
    Tendon = None
    value__ = None


class eMatTypeAluminum(Enum, IComparable, IFormattable, IConvertible):
    """ enum eMatTypeAluminum, values: SubType_5052_H34 (3), SubType_6061_T6 (1), SubType_6063_T6 (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SubType_5052_H34 = None
    SubType_6061_T6 = None
    SubType_6063_T6 = None
    value__ = None


class eMatTypeColdFormed(Enum, IComparable, IFormattable, IConvertible):
    """ enum eMatTypeColdFormed, values: ASTM_A653SQGr33 (1), ASTM_A653SQGr50 (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ASTM_A653SQGr33 = None
    ASTM_A653SQGr50 = None
    value__ = None


class eMatTypeConcrete(Enum, IComparable, IFormattable, IConvertible):
    """ enum eMatTypeConcrete, values: Chinese_C20_NormalWeight (9), Chinese_C30_NormalWeight (10), Chinese_C40_NormalWeight (11), EN_C12_NormalWeight (22), EN_C16_NormalWeight (23), EN_C20_NormalWeight (24), EN_C25_NormalWeight (25), EN_C30_NormalWeight (26), EN_C35_NormalWeight (27), EN_C40_NormalWeight (28), EN_C45_NormalWeight (29), EN_C50_NormalWeight (30), EN_C55_NormalWeight (31), EN_C60_NormalWeight (32), EN_C70_NormalWeight (33), EN_C80_NormalWeight (34), EN_C90_NormalWeight (35), FC3000_LightWeight (5), FC3000_NormalWeight (1), FC4000_LightWeight (6), FC4000_NormalWeight (2), FC5000_LightWeight (7), FC5000_NormalWeight (3), FC6000_LightWeight (8), FC6000_NormalWeight (4), Indian_M15_NormalWeight (12), Indian_M20_NormalWeight (13), Indian_M25_NormalWeight (14), Indian_M30_NormalWeight (15), Indian_M35_NormalWeight (16), Indian_M40_NormalWeight (17), Indian_M45_NormalWeight (18), Indian_M50_NormalWeight (19), Indian_M55_NormalWeight (20), Indian_M60_NormalWeight (21) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Chinese_C20_NormalWeight = None
    Chinese_C30_NormalWeight = None
    Chinese_C40_NormalWeight = None
    EN_C12_NormalWeight = None
    EN_C16_NormalWeight = None
    EN_C20_NormalWeight = None
    EN_C25_NormalWeight = None
    EN_C30_NormalWeight = None
    EN_C35_NormalWeight = None
    EN_C40_NormalWeight = None
    EN_C45_NormalWeight = None
    EN_C50_NormalWeight = None
    EN_C55_NormalWeight = None
    EN_C60_NormalWeight = None
    EN_C70_NormalWeight = None
    EN_C80_NormalWeight = None
    EN_C90_NormalWeight = None
    FC3000_LightWeight = None
    FC3000_NormalWeight = None
    FC4000_LightWeight = None
    FC4000_NormalWeight = None
    FC5000_LightWeight = None
    FC5000_NormalWeight = None
    FC6000_LightWeight = None
    FC6000_NormalWeight = None
    Indian_M15_NormalWeight = None
    Indian_M20_NormalWeight = None
    Indian_M25_NormalWeight = None
    Indian_M30_NormalWeight = None
    Indian_M35_NormalWeight = None
    Indian_M40_NormalWeight = None
    Indian_M45_NormalWeight = None
    Indian_M50_NormalWeight = None
    Indian_M55_NormalWeight = None
    Indian_M60_NormalWeight = None
    value__ = None


class eMatTypeRebar(Enum, IComparable, IFormattable, IConvertible):
    """ enum eMatTypeRebar, values: ASTM_A615Gr40 (1), ASTM_A615Gr60 (2), ASTM_A615Gr75 (3), ASTM_A706 (4), Chinese_HPB235 (5), Chinese_HRB335 (6), Chinese_HRB400 (7), Indian_HYSD415 (9), Indian_HYSD500 (10), Indian_HYSD550 (11), Indian_Mild250 (8) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ASTM_A615Gr40 = None
    ASTM_A615Gr60 = None
    ASTM_A615Gr75 = None
    ASTM_A706 = None
    Chinese_HPB235 = None
    Chinese_HRB335 = None
    Chinese_HRB400 = None
    Indian_HYSD415 = None
    Indian_HYSD500 = None
    Indian_HYSD550 = None
    Indian_Mild250 = None
    value__ = None


class eMatTypeSteel(Enum, IComparable, IFormattable, IConvertible):
    """ enum eMatTypeSteel, values: ASTM_A36 (1), ASTM_A500GrB_Fy42 (3), ASTM_A500GrB_Fy46 (4), ASTM_A53GrB (2), ASTM_A572Gr50 (5), ASTM_A913Gr50 (6), ASTM_A992_Fy50 (7), Chinese_Q235 (8), Chinese_Q345 (9), Chinese_Q355 (16), EN100252_S235 (12), EN100252_S275 (13), EN100252_S355 (14), EN100252_S450 (15), Indian_Fe250 (10), Indian_Fe345 (11) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ASTM_A36 = None
    ASTM_A500GrB_Fy42 = None
    ASTM_A500GrB_Fy46 = None
    ASTM_A53GrB = None
    ASTM_A572Gr50 = None
    ASTM_A913Gr50 = None
    ASTM_A992_Fy50 = None
    Chinese_Q235 = None
    Chinese_Q345 = None
    Chinese_Q355 = None
    EN100252_S235 = None
    EN100252_S275 = None
    EN100252_S355 = None
    EN100252_S450 = None
    Indian_Fe250 = None
    Indian_Fe345 = None
    value__ = None


class eMatTypeTendon(Enum, IComparable, IFormattable, IConvertible):
    """ enum eMatTypeTendon, values: ASTM_A416Gr250 (1), ASTM_A416Gr270 (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ASTM_A416Gr250 = None
    ASTM_A416Gr270 = None
    value__ = None


class eNamedSetType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eNamedSetType, values: All (0), BridgeCalculationReport (17), BridgeSeismicReport (15), BridgeSuperstructureResponse (16), JointTHResponseSpectra (8), NamedDisplay (9), PlotFunctionTraces (10), PushoverCurve (11), RunAnalysis (2), RunBridgeDesignSeismic (5), RunBridgeDesignSubstructure (4), RunBridgeDesignSuperstructure (3), RunBridgeRatingSuperstructure (6), RunMemberRating (7), TableGroupSuperset (14), TableSet (13), UpdateBridgeObject (1), VirtualWork (12) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    All = None
    BridgeCalculationReport = None
    BridgeSeismicReport = None
    BridgeSuperstructureResponse = None
    JointTHResponseSpectra = None
    NamedDisplay = None
    PlotFunctionTraces = None
    PushoverCurve = None
    RunAnalysis = None
    RunBridgeDesignSeismic = None
    RunBridgeDesignSubstructure = None
    RunBridgeDesignSuperstructure = None
    RunBridgeRatingSuperstructure = None
    RunMemberRating = None
    TableGroupSuperset = None
    TableSet = None
    UpdateBridgeObject = None
    value__ = None
    VirtualWork = None


class eObjType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eObjType, values: Area (3), Frame (2), Point (1), Solid (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Area = None
    Frame = None
    Point = None
    Solid = None
    value__ = None


class eReturnCode(Enum, IComparable, IFormattable, IConvertible):
    """ enum eReturnCode, values: Deprecated (-98), NoError (0), NotApplicable (-100), NotImplemented (-99), TableDoesNotExist (-96), TableIsObsolete (-97), UnspecifiedError (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Deprecated = None
    NoError = None
    NotApplicable = None
    NotImplemented = None
    TableDoesNotExist = None
    TableIsObsolete = None
    UnspecifiedError = None
    value__ = None


class eShellType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eShellType, values: Layered (6), Membrane (3), PlateThick_DO_NOT_USE (5), PlateThin_DO_NOT_USE (4), ShellThick (2), ShellThin (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Layered = None
    Membrane = None
    PlateThick_DO_NOT_USE = None
    PlateThin_DO_NOT_USE = None
    ShellThick = None
    ShellThin = None
    value__ = None


class eSlabType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eSlabType, values: Drop (1), Footing (6), Mat (5), Ribbed (3), Slab (0), Stiff_DO_NOT_USE (2), Waffle (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Drop = None
    Footing = None
    Mat = None
    Ribbed = None
    Slab = None
    Stiff_DO_NOT_USE = None
    value__ = None
    Waffle = None


class eSuperObjectClass(Enum, IComparable, IFormattable, IConvertible):
    """ enum eSuperObjectClass, values: BridgeFoundation (3), Foundation (2), None (0), SuperObject (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BridgeFoundation = None
    Foundation = None
    None = None
    SuperObject = None
    value__ = None


class eTemperature(Enum, IComparable, IFormattable, IConvertible):
    """ enum eTemperature, values: C (2), F (1), NotApplicable (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    C = None
    F = None
    NotApplicable = None
    value__ = None


class eTemplateType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eTemplateType, values: Advanced (17), Barrel (12), Beam (2), BracedFrame (7), Bridge (11), BridgeWizard (23), CableBridges (29), Clear (1), Cylinder (13), Dome (14), EccentricFrame (8), Floor (16), Frame2D (21), Frame3D (22), Grid (0), PerimeterFrame (9), PipesAndPlates (24), PortalFrame (6), ShearWall (15), Shells (25), SlopedTruss (3), SolidModels (26), SpaceFrame (10), SpaceTruss (5), Staircases (28), StorageStructures (27), Truss2D (19), Truss3D (20), UndergoundConcrete (18), VerticalTruss (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Advanced = None
    Barrel = None
    Beam = None
    BracedFrame = None
    Bridge = None
    BridgeWizard = None
    CableBridges = None
    Clear = None
    Cylinder = None
    Dome = None
    EccentricFrame = None
    Floor = None
    Frame2D = None
    Frame3D = None
    Grid = None
    PerimeterFrame = None
    PipesAndPlates = None
    PortalFrame = None
    ShearWall = None
    Shells = None
    SlopedTruss = None
    SolidModels = None
    SpaceFrame = None
    SpaceTruss = None
    Staircases = None
    StorageStructures = None
    Truss2D = None
    Truss3D = None
    UndergoundConcrete = None
    value__ = None
    VerticalTruss = None


class eUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum eUnits, values: kgf_cm_C (14), kgf_m_C (8), kgf_mm_C (7), kip_ft_F (4), kip_in_F (3), kN_cm_C (13), kN_m_C (6), kN_mm_C (5), lb_ft_F (2), lb_in_F (1), N_cm_C (15), N_m_C (10), N_mm_C (9), Ton_cm_C (16), Ton_m_C (12), Ton_mm_C (11) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    kgf_cm_C = None
    kgf_mm_C = None
    kgf_m_C = None
    kip_ft_F = None
    kip_in_F = None
    kN_cm_C = None
    kN_mm_C = None
    kN_m_C = None
    lb_ft_F = None
    lb_in_F = None
    N_cm_C = None
    N_mm_C = None
    N_m_C = None
    Ton_cm_C = None
    Ton_mm_C = None
    Ton_m_C = None
    value__ = None


class eWallPierRebarLayerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eWallPierRebarLayerType, values: Confinement_EndZoneI (5), Confinement_EndZoneJ (6), Diagonal_Each (7), Horizontal_Distributed_MiddleZone_Eachface (2), Vertical_Distributed_EndZoneI_Total (3), Vertical_Distributed_EndZoneJ_Total (4), Vertical_Distributed_MiddleZone_Eachface (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Confinement_EndZoneI = None
    Confinement_EndZoneJ = None
    Diagonal_Each = None
    Horizontal_Distributed_MiddleZone_Eachface = None
    value__ = None
    Vertical_Distributed_EndZoneI_Total = None
    Vertical_Distributed_EndZoneJ_Total = None
    Vertical_Distributed_MiddleZone_Eachface = None


class eWallPropType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eWallPropType, values: AutoSelectList (2), Specified (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AutoSelectList = None
    Specified = None
    value__ = None


class eWallSpandrelRebarLayerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum eWallSpandrelRebarLayerType, values: Diagonal_Each (5), Horizontal_Bottom_Total (2), Horizontal_Distributed_Eachface (3), Horizontal_Top_Total (1), Vertical_Ties_Distributed (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Diagonal_Each = None
    Horizontal_Bottom_Total = None
    Horizontal_Distributed_Eachface = None
    Horizontal_Top_Total = None
    value__ = None
    Vertical_Ties_Distributed = None


class Helper(MarshalByRefObject, cHelper):
    """ Helper() """
    def InitializeLifetimeService(self):
        """ InitializeLifetimeService(self: Helper) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause 
             the object to be assigned a new identity when it is marshaled across a remoting boundary. 
             A value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject 
             object's identity to its clone, which will cause remoting client calls to be routed to 
             the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    StartService = None
    StartServiceDefaultPortTCP = 11647
    StartServiceDefaultPortTCPEnvironmentVariable = 'ETABSv1_cOAPI_DEFAULT_PORT'
    StartServiceName = 'ETABSv1.Helper+StartService'


