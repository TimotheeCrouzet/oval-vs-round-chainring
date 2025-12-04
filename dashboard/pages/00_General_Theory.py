import streamlit as st

st.title("📘 Pedaling Theory and Force Model")

st.markdown("""
This section introduces the biomechanical model used to simulate pedaling and
to compute the torque applied to both round and oval chainrings.  
The theory presented here follows the structure of my TIPE presentation
(pages 16 to 19).
""")

# ---------------------------------------------------------------
# 1. Force model (from slide: "Simulation du pédalage")
# ---------------------------------------------------------------
st.header("1. Pedaling Force Model")

st.markdown("""
During a crank revolution, the cyclist produces a force that varies with the
pedaling angle \\(\\theta\\).  
To reproduce realistic torque curves, we use an empirical model combining a
horizontal and vertical force component:

""")

st.latex(r"""
F(\theta) = H \, |\cos^n(\theta)| + V \, |\sin^n(\theta)|
""")

st.markdown("""
Where:
- **H** = horizontal force amplitude  
- **V** = vertical force amplitude  
- **n** = exponent shaping the force curve  

In the calibrated model (from slide 16 of the presentation):
""")

st.markdown("""
- **n = 3**  
- **H = 30 N**  
- **V = 150 N**
""")

st.image("dashboard/images/force_model.png", caption="Force model and experimental calibration (TIPE slide 16)")

# ---------------------------------------------------------------
# 2. Geometry and effective radius of an oval chainring
# ---------------------------------------------------------------
st.header("2. Geometry of an Oval Chainring")

st.markdown("""
An oval chainring is defined by:
- a **semi-major axis** \\(a\\)
- a **semi-minor axis** \\(b\\)
- an orientation angle (timing)

Because of its shape, the distance between the crank axis and the chain varies
during the rotation. This quantity is called the **effective radius**.
""")

st.latex(r"""
r(\theta) = 
\frac{ab}{
\sqrt{(b\cos\theta)^2 + (a\sin\theta)^2}
}
""")

st.markdown("""
This radius determines how much torque is transmitted to the chain for a given
pedaling force.  

Below is the schematic representation of the radius variation:
""")

st.image("dashboard/images/effective_radius.png", caption="Effective radius of the oval chainring (TIPE slide 18)")

# ---------------------------------------------------------------
# 3. Torque calculation
# ---------------------------------------------------------------
st.header("3. Torque Applied to the Chainring")

st.markdown("""
The torque produced by the cyclist is the product of the applied force and
the lever arm.  
For an oval chainring, this lever arm is precisely the **effective radius**
\\( r(\\theta) \\).

Thus, the instantaneous torque is:
""")

st.latex(r"""
C_{\text{chainring}}(\theta) = r(\theta) \cdot F(\theta)
""")

st.markdown("""
This expression is used in all simulations that follow (dead-spot duration,
average torque, and optimal settings).
""")

st.image("dashboard/images/torque_chainring.png", caption="Torque comparison for round and oval chainrings (TIPE slide 19)")

# ---------------------------------------------------------------
# Summary
# ---------------------------------------------------------------
st.header("Summary")

st.markdown("""
- We model pedaling force with a realistic sinusoidal-based expression.  
- Oval chainrings introduce a varying effective radius.  
- The torque is simply the product of this radius and the modeled force.  
- This theory is the basis for all numeric simulations in the dashboard.
""")
