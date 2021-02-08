# Keith Rehermann
# Use single qubit to implement random number generator

from pytket import Circuit
from pytket.backends.ibm import AerStateBackend, AerBackend, AerUnitaryBackend, IBMQBackend, IBMQEmulatorBackend
import numpy as np
def random_qbits(n_qbits):

    c = Circuit(n_qbits)
    for i in range(n_qbits):
        c.H(i)

    print(c)

    aer_state_be = AerStateBackend()

    state_handle = aer_state_be.process_circuit(c)
    state_vector = aer_state_be.get_result(state_handle).get_state()
    print(state_vector)


    c.measure_all()

    aer_be = AerBackend()
    shots_handle = aer_be.process_circuit(c, n_shots=10,seed=1)
    shots = aer_be.get_result(shots_handle).get_shots()
    print(shots)

#TODO converts shots array to base 10 and base 2 numbers


def random_bit():
    c = Circuit(1)
    c.H(0)
    c.measure_all()

    aer_be = AerBackend()
    shots_handle = aer_be.process_circuit(c, n_shots=1)
    shots = aer_be.get_result(shots_handle).get_shots().flatten()
    
    return shots[0]

print(random_bit())