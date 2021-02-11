from pytket import Circuit
from pytket.backends.ibm import AerStateBackend, AerBackend, AerUnitaryBackend, IBMQBackend, IBMQEmulatorBackend
import numpy as np
from pytket.utils import Graph

def seperable_qbits(n:int):

    c = Circuit(n)
    for i in range(n-1):
        c.H(i)

    aer_state_be = AerStateBackend()

    state_handle = aer_state_be.process_circuit(c)
    state_vector = aer_state_be.get_result(state_handle).get_state()
    print(state_vector)
    Graph(c).view_DAG()

if __name__ == '__main__':
    seperable_qbits(3)    