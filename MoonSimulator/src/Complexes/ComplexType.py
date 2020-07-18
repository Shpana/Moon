from .Complex import Complex

from .ResidentialComplex import ResidentialComplex

from .NodeComplex import NodeComplex

from .TitaniumComplex import TitaniumComplex

from .HeliumComplex import HeliumComplex

from .ElectricityComplex import ElectricityComplex


class ComplexType(object):

    @staticmethod
    def GetComplexByType(type: str)-> Complex:
        if (type == "node"):        return NodeComplex
        if (type == "residential"): return ResidentialComplex
        if (type == "titanium"):    return TitaniumComplex
        if (type == "helium"):      return HeliumComplex
        if (type == "electricity"): return ElectricityComplex
