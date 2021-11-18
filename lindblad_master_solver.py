"""
Reading the documentation of qutip
https://qutip.org/docs/latest/guide/dynamics/dynamics-master.html

github@linueks
"""
import qutip as qt
import numpy as np
from simple_jaynes_cummings import create_jaynes_cummings



hilbert_space_levels=10
atom_energy_diff=1.0
cavity_energy_diff=1.25
interaction_strength=0.05
num_atom_levels=2

hamiltonian, operators = create_jaynes_cummings(hilbert_space_levels,
                                                atom_energy_diff,
                                                cavity_energy_diff,
                                                interaction_strength,
                                                num_atom_levels)
#print(hamiltonian)
boson_annihilation, boson_creation, atom_lowering, atom_raising = operators


initial_state = qt.tensor(qt.fock(num_atom_levels, 0),
                    qt.fock(hilbert_space_levels, 5))
#print(initial_state)
times = np.linspace(0.0, 10.0, 200)

result = qt.mesolve(hamiltonian, initial_state, times, )
