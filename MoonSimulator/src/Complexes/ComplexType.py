from .Complex import Complex

from .ResidentialComplex import ResidentialComplex

from .NodeComplex import NodeComplex

from .TitaniumComplex import TitaniumComplex

class ComplexType(object):

    @staticmethod
    def GetComplexByType(type: str)-> Complex:
        if (type == "node"):        return NodeComplex
        if (type == "residential"): return ResidentialComplex
        if (type == "titanium"):    return TitaniumComplex
