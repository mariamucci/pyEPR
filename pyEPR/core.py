"""
Main interface module to use pyEPR.

Contains code to conenct to Ansys and to analyze HFSS files using the EPR method.

This module handles the micowave part of the analysis and conenction to

Further contains code to be able to do autogenerated reports,

Copyright Zlatko Minev, Zaki Leghtas, and the pyEPR team
2015, 2016, 2017, 2018, 2019, 2020
"""
# pylint: disable=invalid-name, unused-import



from .project_info import ProjectInfo
from .core_quantum_analysis import QuantumAnalysis
from .core_distributed_analysis import DistributedAnalysis

# Backwards compatability. To be depreciated.
Project_Info = ProjectInfo
pyEPR_HFSSAnalysis = DistributedAnalysis
pyEPR_Analysis = QuantumAnalysis
