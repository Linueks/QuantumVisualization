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
vacuum_state = qt.fock(5, 0)
annihilation = qt.destroy(5)
creation = qt.create(5)
#print(vacuum_state)
#print(annihilation)
#print(annihilation * vacuum_state)
#print(creation * vacuum_state == annihilation.dag() * vacuum_state)
#print(creation**2 == creation * creation)



# ------------------------------------------------------------------------------
# Number operator'
#print(creation * annihilation == qt.num(5))
number_operator = qt.num(5)
#print(number_operator * vacuum_state)
#print(number_operator * creation * vacuum_state)
#print(number_operator * creation**2 * vacuum_state)



# ------------------------------------------------------------------------------
# In last print number operator gives 2sqrt2 instead of 2
# because we didn't normalize.

#print(number_operator * (creation**2 * vacuum_state).unit())



# ------------------------------------------------------------------------------
# We can generate higher number Fock state without repeated creation
fock_5_state = qt.fock(5, 4)
print(fock_5_state)
print(number_operator * fock_5_state)
