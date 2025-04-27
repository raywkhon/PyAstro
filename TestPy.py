import sympy
from sympy import symbols, sin, cos, sinh, Matrix
from sympy import init_session
from einsteinpy.symbolic import EinsteinTensor, MetricTensor
# sympy.init_printing(use_unicode=True)
sympy.init_printing()
init_session

syms = sympy.symbols("t x y z") 
sympy.symbols("A W") 
t, x, y, z = syms
# M = Matrix([[-1,0,0,0], [0,cos(t) ** 2,0,0],[0,0,cos(t) ** 2 * sinh(ch) ** 2,0], [0,0,0,cos(t) ** 2 * sinh(ch) ** 2 * sin(th) ** 2]])
M = ([[-1,0,0,0], [0,1,0,0],[0,0,1,A*sin(W*(t-x))], [0,0,A*sin(W*(t-x)),1]])
M
metric = MetricTensor(M, syms)
metric.tensor() # Input - metric tensor
einst = EinsteinTensor.from_metric(metric) # Calculating the Einstein Tensor (with both indices covariant)
print(metric[0,0])
sympy.pprint(metric[0,0])
print(einst[0,0])
sympy.pprint(einst[0,0])
einst.tensor() # Output:  Einstein Tensor 
  
# Anti-de Sitter spacetime Metric
syms = sympy.symbols("t chi theta phi") 
syms
t, ch, th, ph = syms
m = sympy.diag(-1, cos(t) ** 2, cos(t) ** 2 * sinh(ch) ** 2, cos(t) ** 2 * sinh(ch) ** 2 * sin(th) ** 2).tolist()
metric = MetricTensor(m, syms)
metric.tensor() # Input - metric tensor
einst = EinsteinTensor.from_metric(metric) # Calculating the Einstein Tensor (with both indices covariant)
einst.tensor() # Output:  Einstein Tensor 
