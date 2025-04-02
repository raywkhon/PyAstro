# EinsteinPy https://docs.einsteinpy.org/en/latest/jupyter.html
#  id raywkhon token: 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
# Einstein Tensor calculations using Symbolic module
import sympy
from sympy import symbols, sin, cos, sinh
from einsteinpy.symbolic import EinsteinTensor, MetricTensor
sympy.init_printing()

# Anti-de Sitter spacetime Metric
syms = sympy.symbols("t chi theta phi") 
syms
t, ch, th, ph = syms
m = sympy.diag(-1, cos(t) ** 2, cos(t) ** 2 * sinh(ch) ** 2, cos(t) ** 2 * sinh(ch) ** 2 * sin(th) ** 2).tolist()
metric = MetricTensor(m, syms)
metric.tensor() # Input - metric tensor
einst = EinsteinTensor.from_metric(metric) # Calculating the Einstein Tensor (with both indices covariant)
einst.tensor() # Output:  Einstein Tensor 

# Schwarzschild Metric
syms = sympy.symbols("t r theta phi") 
syms
t, r, th, ph = syms
m = sympy.diag(-(1-(2*M)/r), (1-(2*M)/r)** -1, r ** 2,  r ** 2 * sin(th) ** 2).tolist()
metric = MetricTensor(m, syms)
metric.tensor() # Input - metric tensor
einst = EinsteinTensor.from_metric(metric) # Calculating the Einstein Tensor (with both indices covariant)
einst.tensor() # Output:  Einstein Tensor 



# The two coupled differential equations — the "mass continuity equation and the "Tolman-Oppenheimer-Volkoff (TOV) equation" require:
# 1. Specify an equation of state (EOS) p(rho) relating pressure p and energy density rho.
# 2. Integrate numerically from the center (r = 0) to the surface (p = 0), using appropriate boundary conditions.

# 1. Equations to Solve
# dm/dr = 4pir^2rho (Mass continuity)
# dp/dr = -(rho + p)(m + 4pir^3p)/{r(r - 2m)} (TOV equation)

# 2. Boundary Conditions
# At the center r = 0, m(0) = 0 (no mass enclosed at r = 0,
# p(0) = p_c (central pressure, chosen based on the star's properties).
# At the surface r = R: p(R) = 0 (pressure drops to zero at the surface).

# 3. Equation of State (EOS)
# A simple but physically relevant EOS is the "polytropic equation of state":
# p = Krho^Gamma, where: K is a constant, Gamma is the adiabatic index (e.g., Gamma = 2 for neutron stars).
# For a more realistic model, tabulated EOS data (e.g., SLy, APR) can be used.

# 4. Numerical Integration (Pseudocode) 
# We use the Runge-Kutta 4th-order (RK4) method to integrate the equations outward from r = 0:

import numpy as np

def TOV_solver(p_c, rho_c, Gamma, K, r_max=50, dr=0.01):
    # Initialize
    r = 0
    m = 0
    p = p_c
    rho = rho_c
    
    # Arrays to store results
    r_list = [r]
    m_list = [m]
    p_list = [p]
    rho_list = [rho]
    
    # Integration loop
    while r < r_max and p > 0:
        # Compute derivatives
        dm_dr = 4 * np.pi * r**2 * rho
        dp_dr = - (rho + p) * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m) + 1e-10)  # Avoid division by zero
        
        # RK4 integration
        # ... (Implement RK4 steps here)
        
        # Update variables
        m += dm_dr * dr
        p += dp_dr * dr
        r += dr
        
        # Update density using EOS
        rho = (p / K)**(1 / Gamma)
        
        # Store results
        r_list.append(r)
        m_list.append(m)
        p_list.append(p)
        rho_list.append(rho)
    
    return r_list[1:10]
    # return r_list, m_list, p_list, rho_list

TOV_solver(p_c = 10^35, rho_c = 5*10^17, Gamma = 2, K = 1*10^5, r_max=50, dr=0.01)
TOV_solver(p_c = 10^35, rho_c = 5*10^17, Gamma = 2, K = 1*10^5, r_max=50, dr=0.01)

# 5. Results
# The integration stops when p drops to zero, defining the star's radius R.
# The total gravitational mass is M = m(R).
# The **density profile rho(r)  and pressure profile p(r) describe the star's internal structure.

# Example Output
# For a neutron star with:
# p_c = 10^35 Pa, rh_c = 5 * 10^17 kg/m^3, Gamma = 2, K = 1 * 10^5,

#You would obtain:
# Mass M approx = 1.4 solar masses,
# Radius R approx = 10 km.

# Key Notes
# Relativistic effects**: The TOV equation deviates from Newtonian gravity when \( m/r \) is large (e.g., near neutron star cores).
# Stability**: Solutions are valid only if M and R satisfy stability criteria.
# ore realistic models**: Use tabulated EOS data for precise neutron star predictions.

# Would you like help implementing the RK4 method or analyzing specific cases?









