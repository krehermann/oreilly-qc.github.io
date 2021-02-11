from pytket import Circuit
from pytket.backends.ibm import AerStateBackend, AerBackend, AerUnitaryBackend, IBMQBackend, IBMQEmulatorBackend
import numpy as np
from ch02_01_random_bit import random_bit

# Build the quantum key distribution protocol with eve
#BB84

#qubit to send
c = Circuit(1)

# alice's random number generator
alice_val = random_bit()
#alice_apply_not = random_bit()
alice_apply_had = random_bit()


# qubit starts in |0>, so if alice wants to send 1, need to apply not
if alice_val:
    c.X(0)
if alice_apply_had:
    c.H(0)

# Logically at this point Alice is done with the qubit and sends it. 
# We are lazy and don't represent that explicitly, rather just act on 1
# qubit in the existing circut
spy_exists = True
#TODO implement spy

#Now bob's got the qubit, i.e. control of the circuit
bob_apply_had = random_bit()
if bob_apply_had:
    c.H(0)

c.measure_all()
print("alice_val {}, alice_had {} bob_had {}".format(alice_val, alice_apply_had, bob_apply_had))

aer_be = AerBackend()
shots_handle = aer_be.process_circuit(c, n_shots=100)
shots = aer_be.get_result(shots_handle).get_shots().flatten()
print(shots)
# compare shots to alice's sent value; should match 100% of time if alice and bob have same val of apply_had and else 50%
matches = [v for v in shots if v == alice_val]
print(matches)
frac = len(matches)/len(shots)
print (frac)

#TODO full experiment should loop over calls to random_bit, instead of using shots. 
# The shots simulate the *same* value of the circuit over and over
# really want to simulate different circuits and see the comparision between alice_val and the single shot measurement.

