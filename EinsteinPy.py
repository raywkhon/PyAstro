# EinsteinPy https://docs.einsteinpy.org/en/latest/jupyter.html
#  id raywkhon token: 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
# Einstein Tensor calculations using Symbolic module
import sympy
from sympy import symbols, sin, cos, sinh
from einsteinpy.symbolic import EinsteinTensor, MetricTensor
sympy.init_printing()

# Defining the Anti-de Sitter spacetime Metric
syms = sympy.symbols("t chi theta phi") 
syms
t, ch, th, ph = syms
m = sympy.diag(-1, cos(t) ** 2, cos(t) ** 2 * sinh(ch) ** 2, cos(t) ** 2 * sinh(ch) ** 2 * sin(th) ** 2).tolist()
metric = MetricTensor(m, syms)
metric.tensor()
# Calculating the Einstein Tensor (with both indices covariant)
einst = EinsteinTensor.from_metric(metric)
einst.tensor()


