# EinsteinPy https://docs.einsteinpy.org/en/stable/

# Einstein Tensor calculations using Symbolic module
import sympy
from sympy import symbols, sin, cos, sinh
from einsteinpy.symbolic import EinsteinTensor, MetricTensor

sympy.init_printing()

# Defining the Anti-de Sitter spacetime Metric
syms = sympy.symbols("t chi theta phi") 
asyms
t, ch, th, ph = syms
m = sympy.diag(-1, cos(t) ** 2, cos(t) ** 2 * sinh(ch) ** 2, cos(t) ** 2 * sinh(ch) ** 2 * sin(th) ** 2).tolist()
metric = MetricTensor(m, syms)
metric.tensor()
# Calculating the Einstein Tensor (with both indices covariant)
einst = EinsteinTensor.from_metric(metric)
einst.tensor()

from sympy import *
syms2  = sympy.symbols("r chi theta lamda")
syms2
r, ch, th, la = syms2

m2 = sympy.diag(-exp(2*ch), exp(2*la), r ** 2, r ** 2 * sin(th) ** 2).tolist()
metric2 = MetricTensor(m2, syms2)
metric2.tensor()

einst2 = EinsteinTensor.from_metric(metric2)
einst2.tensor() 

import pytearcat as pt
t, r, theta, phi = pt.coords('t,r,theta,phi')
k, c = pt.con('k','c')
a = pt.fun('a','t')
ds = 'ds2 = -dt**2 + a***2*(1/(1-k*r**2))*dr**2 + \ r**2*dtheta**2 + r**2*sin(theta)**2*dphi**2'
g = pt.metric(ds)

