"""
Reading the documentation of qutip
https://qutip.org/docs/latest/guide/guide-tensor.html

From there:
The simplest possible quantum mechanical description for light-matter
interaction is encapsulated in the Jaynes-Cummings model, which describes the
coupling between a two-level atom and a single-mode electromagnetic field
(a cavity mode). Denoting the energy splitting of the atom and cavity omega_a
and omega_c, respectively, and the atom-cavity interaction strength g, the
Jaynes-Cumming Hamiltonian can be constructed

github@linueks
"""
import numpy as np
import qutip as qt
import matplotlib.pyplot as plt



def create_jaynes_cummings(hilbert_space_levels=3, atom_energy_diff=1.0,
                           cavity_energy_diff=1.25, interaction_strength=0.05):

    boson_annihilation = qt.tensor(qt.identity(2),
                                qt.destroy(hilbert_space_levels))
    boson_creation = qt.tensor(qt.identity(2),
                                qt.create(hilbert_space_levels))

    #print(boson_annihilation.dag() == boson_creation)


    atom_lowering = qt.tensor(qt.destroy(2), qt.identity(hilbert_space_levels))
    atom_raising = qt.tensor(qt.create(2), qt.identity(hilbert_space_levels))
    #print(atom_lowering.dag() == atom_raising)
    pauli_z = qt.tensor(qt.sigmaz(), qt.identity(hilbert_space_levels))


    atom_hamil = 0.5 * atom_energy_diff * pauli_z
    cavity_hamil = cavity_energy_diff * boson_creation * boson_annihilation
    interaction_hamil = interaction_strength \
        * (boson_creation * atom_lowering + boson_annihilation * atom_raising)

    hamiltonian = atom_hamil + cavity_hamil + interaction_hamil

    return hamiltonian





if __name__=='__main__':
    hamiltonian = create_jaynes_cummings()
    print(hamiltonian)
