# Einstein Tensor calculations using Symbolic module
import sympy
from sympy import symbols, sin, cos, sinh, Matrix
from sympy import init_session
from einsteinpy.symbolic import EinsteinTensor, MetricTensor
# sympy.init_printing(use_unicode=True)
sympy.init_printing() # Enable the best printer available in current environment
init_session # import everything in SymPy, create common Symbols, setup plotting, and rung init.printing()

syms = sympy.symbols("t x y z") 
A, W = sympy.symbols("A W") 
t, x, y, z = syms
M = ([[-1,0,0,0], [0,1,0,0],[0,0,1,A*sin(W*(t-x))], [0,0,A*sin(W*(t-x)),1]])
metric = MetricTensor(M, syms)
metric.tensor() # Input - metric tensor
einst = EinsteinTensor.from_metric(metric) # Calculating the Einstein Tensor (with both indices covariant)
einst.tensor() # Output:  Einstein Tensor 
print(metric[0,0])
sympy.pprint(metric[0,0])
print(einst[0,0])
sympy.pprint(einst[0,0])
einst.order
einst.config

# Contravariant & Covariant indices in Tensors (Symbolic)
import sympy
from einsteinpy.symbolic import ChristoffelSymbols, RiemannCurvatureTensor
from einsteinpy.symbolic.predefined import Schwarzschild
sympy.init_printing()
# Analysing the schwarzschild metric along with performing various operations
sch = Schwarzschild()
sch.tensor()

metric = MetricTensor(M, syms)
metric.tensor() # Input - metric tensor
print(metric[0,0])
sympy.pprint(metric[0,0])
metric_inv = metric.inv()
metric_inv.tensor()
print(metric_inv[3,3])
sympy.pprint(metric_inv[3,3])

sch_inv = sch.inv()
sch_inv.tensor()
print(sch_inv[3,3])
sympy.pprint(sch_inv[3,3])
 
# Obtaining Christoffel Symbols from Metric Tensor
chr_metric_inv = ChristoffelSymbols.from_metric(metric_inv) 
chr_metric_inv.tensor()
print(chr_metric_inv[3,3,2])
sympy.pprint(chr_metric_inv[3])
chr_metric_inv.order
chr_metric_inv.config

chr = ChristoffelSymbols.from_metric(sch_inv) # can be initialized from sch also
chr.tensor()
print(chr[3,3,2])
sympy.pprint(chr[3])
chr.order
chr.config

# Changing the first index to covariant
new_chr = chr.change_config('lll') # changing the configuration to (covariant, covariant, covariant)
new_chr.tensor()
new_chr.config

# Any arbitary index configuration would also work!
new_chr2 = new_chr.change_config('lul')
new_chr2.tensor()
 
# Obtaining Riemann Tensor from Christoffel Symbols and manipulating it’s indices
rm_chr_metric_inv = RiemannCurvatureTensor.from_christoffels(chr_metric_inv)
rm_chr_metric_inv[0,0,:,:]
rm_chr_metric_inv[0,2,1,3]
rm_chr_metric_inv.config
rm_chr_metric_inv.tensor()

rm = RiemannCurvatureTensor.from_christoffels(new_chr2)
rm[0,0,:,:]
rm.config

rm2 = rm.change_config("uuuu")
rm2[0,0,:,:]

rm3 = rm2.change_config("lulu")
rm3[0,0,:,:]

rm4 = rm3.change_config("ulll")
rm4.simplify()
rm4[0,0,:,:]
 
# It is seen that rm and rm4 are same as they have the same configuration
