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


# Using predefined
# qutip has a bunch of operators predefined.
state = qt.fock(4, 2)
#print(state)
