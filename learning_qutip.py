import numpy as np
import matplotlib.pyplot as plt
import qutip as qt


# Manually specifying input data
#input_data = [[1], [2], [3], [4], [5]]
input_data = np.arange(0, 5, 1)
q_object = qt.Qobj(input_data)
random_input = np.random.rand(4, 4)
q_object_random = qt.Qobj(random_input)

#print(q_object)
#print(q_object_random)


# ------------------------------------------------------------------------------
# Using predefined
# qutip has a bunch of operators predefined.
state = qt.fock(4, 2)
#print(state)



# ------------------------------------------------------------------------------
# Manipulating States and Operators
# creating a Fock vacuum state and an annihilation operator
hilbert_space_levels = 5

vacuum_state = qt.fock(hilbert_space_levels, 0)
annihilation = qt.destroy(hilbert_space_levels)
creation = qt.create(hilbert_space_levels)
#print(f'vacuum state: \n {vacuum_state}')
#print(annihilation)
#print(annihilation * vacuum_state)
#print(creation * vacuum_state == annihilation.dag() * vacuum_state)
#print(creation**2 == creation * creation)



# ------------------------------------------------------------------------------
# Number operator'
#print(creation * annihilation == qt.num(hilbert_space_levels))
number_operator = qt.num(hilbert_space_levels)
#print(number_operator * vacuum_state)
#print(number_operator * creation * vacuum_state)
#print(number_operator * creation**2 * vacuum_state)



# ------------------------------------------------------------------------------
# In last print number operator gives 2sqrt2 instead of 2
# because we didn't normalize.

#print(number_operator * (creation**2 * vacuum_state).unit())



# ------------------------------------------------------------------------------
# We can generate higher number Fock state without repeated creation
fock_4_state = qt.fock(hilbert_space_levels, 4)
#print(fock_4_state)
#print(number_operator * fock_4_state)



# ------------------------------------------------------------------------------
# Generating superpositions
superposition = (vacuum_state + fock_4_state).unit()
#print(superposition)
#print(number_operator * superposition)



# ------------------------------------------------------------------------------
# Generate coherent and squeezed states
displace_operator = qt.displace(hilbert_space_levels, 1j)
squeeze_operator = qt.squeeze(hilbert_space_levels, np.complex(0.25, 0.25))
#print(f'displacement operator: \n {displace_operator}')
#print(f'squeeze operator: \n {squeeze_operator}')

#print(displace_operator * vacuum_state)
#print(squeeze_operator * vacuum_state)
#print(displace_operator * vacuum_state == qt.states.coherent(hilbert_space_levels, 1j))



# ------------------------------------------------------------------------------
# Generating Density Matrices
ket = qt.basis(5, 2)
density = ket * ket.dag()
density_2 = qt.fock_dm(5, 2)
density_3 = qt.ket2dm(ket)
#print(ket)
#print(density)
#print(density == density_2 == density_3)

# If we want to create a density matrix with equal classical probabilities
# of being found in the ket(2) or ket(4) we can do
superposition = (0.5 * qt.fock_dm(5, 2) + 0.5 * qt.fock_dm(5, 4))
#print(superposition)

# Other predefined density matrices
coherent_state_dm = qt.coherent_dm(5, 1.25)
thermal_state_dm = qt.thermal_dm(5, 1.25)
#print(coherent_state_dm)
#print(thermal_state_dm)





































#bottom
