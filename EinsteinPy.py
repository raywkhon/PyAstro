# EinsteinPy https://docs.einsteinpy.org/en/latest/jupyter.html
#  id raywkhon token: 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
# Einstein Tensor calculations using Symbolic module
import sympy
from sympy import symbols, sin, cos, sinh, Matrix
from einsteinpy.symbolic import EinsteinTensor, MetricTensor
sympy.init_printing()

# M = Matrix([[-1,0,0,0], [0,cos(t) ** 2,0,0],[0,0,cos(t) ** 2 * sinh(ch) ** 2,0], [0,0,0,cos(t) ** 2 * sinh(ch) ** 2 * sin(th) ** 2]])
M = ([[-1,0,0,0], [0,cos(t) ** 2,0,0],[0,0,cos(t) ** 2 * sinh(ch) ** 2,0], [0,0,0,cos(t) ** 2 * sinh(ch) ** 2 * sin(th) ** 2]])
M
metric = MetricTensor(M, syms)
metric.tensor() # Input - metric tensor
einst = EinsteinTensor.from_metric(metric) # Calculating the Einstein Tensor (with both indices covariant)
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
# dm/dr = 4pi*r^2*rho (Mass continuity)
# dp/dr = -(rho + p)(m + 4pi*r^3*p)/{r(r - 2m)} (TOV equation)

# 2. Boundary Conditions
# At the center r = 0, m(0) = 0 (no mass enclosed at r = 0,
# p(0) = p_c (central pressure, chosen based on the star's properties).
# At the surface r = R: p(R) = 0 (pressure drops to zero at the surface).

# 3. Equation of State (EOS)
# A simple but physically relevant EOS is the "polytropic equation of state":
# p = K*rho^Gamma, where: K is a constant, Gamma is the adiabatic index (e.g., Gamma = 2 for neutron stars).
# For a more realistic model, tabulated EOS data (e.g., SLy, APR) can be used.

# 4. Numerical Integration (Pseudocode) 
# We use the Runge-Kutta 4th-order (RK4) method to integrate the equations outward from r = 0:
# Example : for a neutron star with:
# p_c = 10^35 Pa, rh_c = 5 * 10^17 kg/m^3, Gamma = 2, K = 1 * 10^5
#You would obtain:
# Mass M approx = 1.4 solar masses,
# Radius R approx = 10 km.

import numpy as np

def TOV_solver(p_c, rho_c, Gamma, K, r_max, dr):
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
        dp_dr = - (rho + p) * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m) + 1e-10) # Avoid division by zero
        
        # RK4 integration (Implement RK4 steps here)
        
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
    
    return r_list, m_list, p_list, rho_list

TOV_solver(p_c = 10**35, rho_c = 5*10**17, Gamma = 2, K = 1*10**5, r_max=50, dr=0.01)

# 5. Results
# The integration stops when p drops to zero, defining the star's radius R.
# The total gravitational mass is M = m(R).
# The **density profile rho(r)  and pressure profile p(r) describe the star's internal structure.

# Key Notes
# Relativistic effects: The TOV equation deviates from Newtonian gravity when m/r is large (e.g., near neutron star cores).
# Stability: Solutions are valid only if M and R satisfy stability criteria.
# More realistic models: Use tabulated EOS data for precise neutron star predictions

###########
# Implement the RK4 method
###########
import numpy as np
import matplotlib.pyplot as plt

def rk4_integrate_TOV(p_c, rho_c, Gamma, K, r_max=20, dr=0.01):
    # Initialize
    r = 1e-10   # Avoid division by zero at r=0
    m = 0.0
    p = p_c
    rho = rho_c
    # print(f"r = {r}")
    # print(f"m = {m}")
    # print(f"p = {p}")
    # print(f"rho = {rho}")
    # print(f"Gamma = {Gamma}")
    # print(f"K = {K}")
    # print(f"r_max = {r_max}")
    # print(f"dr = {dr}")
    
    # Arrays to store results
    r_list = [r]
    m_list = [m]
    p_list = [p]
    rho_list = [rho]
    # print(f" ")
    # print(f"r_list = {r_list}")
    # print(f"m_list = {m_list}")
    # print(f"p_list = {p_list}")
    # print(f"rho_list = {rho_list}")
    
    def equations(r, m, p):
        rho = (p / K)**(1 / Gamma)
        dm_dr = 4 * np.pi * r**2 * rho
        print(f"rho = {rho}")
        print(f"dm_dr = {dm_dr}")
        if r <= 1e-10:  # Handle division by zero near r=0
            dp_dr = 0.0
        else:
            dp_dr = - (rho + p) * (m + 4 * np.pi * r**3 * p) / (r * (r - 2 * m + 1e-10)) # Small offset to avoid singularity
        print(f"dp_dr = {dp_dr}")
        return dm_dr, dp_dr
    
    # RK4 integration loop
    while r < r_max and p > 0:
    # while r < r_max:
        # Step 1: Compute k1
        dm_dr_k1, dp_dr_k1 = equations(r, m, p)
        k1_m = dr * dm_dr_k1
        k1_p = dr * dp_dr_k1
        
        # Step 2: Compute k2
        dm_dr_k2, dp_dr_k2 = equations(r + dr/2, m + k1_m/2, p + k1_p/2)
        k2_m = dr * dm_dr_k2
        k2_p = dr * dp_dr_k2
        
        # Step 3: Compute k3
        dm_dr_k3, dp_dr_k3 = equations(r + dr/2, m + k2_m/2, p + k2_p/2)
        k3_m = dr * dm_dr_k3
        k3_p = dr * dp_dr_k3
        
        # Step 4: Compute k4
        dm_dr_k4, dp_dr_k4 = equations(r + dr, m + k3_m, p + k3_p)
        k4_m = dr * dm_dr_k4
        k4_p = dr * dp_dr_k4
        
        # Update variables
        m += (k1_m + 2 * k2_m + 2 * k3_m + k4_m) / 6
        p += (k1_p + 2 * k2_p + 2 * k3_p + k4_p) / 6
        r += dr
        
        # Update density using EOS
        rho = (p / K)**(1 / Gamma)
        
        # Store results
        r_list.append(r)
        m_list.append(m)
        p_list.append(p)
        rho_list.append(rho)
        print(f" ")
        print(f"r_list2 = {r_list}")
        print(f"m_list2 = {m_list}")
        print(f"p_list2 = {p_list}")
        print(f"rho_list2 = {rho_list}")
    
    return r_list, m_list, p_list, rho_list

# Parameters (example for a neutron star)
p_c = 1e35  # Central pressure (Pa)
rho_c = 5e17  # Central density (kg/m³)
Gamma = 2
K = 1e5

# Solve TOV equations
r, m, p, rho = rk4_integrate_TOV(p_c, rho_c, Gamma, K)

# Plot results
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(r, m)
plt.xlabel("Radius (km)")
plt.ylabel("Enclosed mass (kg)")
plt.title("Mass Profile")

plt.subplot(1, 3, 2)
plt.plot(r, p)
plt.xlabel("Radius (km)")
plt.ylabel("Pressure (Pa)")
plt.title("Pressure Profile")

plt.subplot(1, 3, 3)
plt.plot(r, rho)
plt.xlabel("Radius (km)")
plt.ylabel("Density (kg/m³)")
plt.title("Density Profile")

plt.tight_layout()
plt.show()

# Star's radius and mass
R = r[-1]  # Surface radius where p=0
M = m[-1]  # Total mass
print(f"Star radius: {R:.2f} km")
print(f"Star mass: {M:.2f} kg (~ {M / 1.9885e30:.2f} solar masses)")

