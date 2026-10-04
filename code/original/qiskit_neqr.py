# NEQR
# Importing standard Qiskit libraries and configuring account

import qiskit as qk
from qiskit import QuantumCircuit, Aer, IBMQ
from qiskit import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import plot_histogram
from math import pi
from qiskit.quantum_info import Operator
import numpy as np
import matplotlib as mp
from qiskit.aqua.algorithms import QSVM

from qiskit import QuantumRegister, ClassicalRegister


# Initialize the quantum circuit for the image

# Pixel position
idx = QuantumRegister(2, 'idx')

# Grayscale pixel intensity value
intensity = QuantumRegister(8, 'intensity')

# Classical register
cr = ClassicalRegister(10, 'cr')

# Create the quantum circuit for the image
qc_image = QuantumCircuit(intensity, idx, cr)

# Set the total number of qubits
num_qubits = qc_image.num_qubits


# Initialize the quantum circuit

# Add Identity gates to the intensity values
for idx in range(intensity.size):
    qc_image.i(idx)


# Add Hadamard gates to the pixel positions
qc_image.h(8)
qc_image.h(9)


# Encode the first pixel
# Since its value is 0, the thesis applies identity gates here

value00 = '01100100'

for idx in range(num_qubits):
    qc_image.i(idx)


# Encode the second pixel whose value is (01100100)

value01 = '01100100'

# Add the NOT gate to set the position at 01
qc_image.x(qc_image.num_qubits - 1)

# Reverse the value so it is in the same order when measured
for idx, px_value in enumerate(value01[::-1]):
    if px_value == '1':
        qc_image.ccx(num_qubits - 1, num_qubits - 2, idx)

# Reset the NOT gate
qc_image.x(qc_image.num_qubits - 1)


# Encode the third pixel whose value is (11001000)

value10 = '11001000'

# Add the X gate to set the required pixel position
qc_image.x(num_qubits - 2)

for idx, px_value in enumerate(value10[::-1]):
    if px_value == '1':
        qc_image.ccx(num_qubits - 1, num_qubits - 2, idx)

qc_image.x(num_qubits - 2)


# Encode the fourth pixel

value11 = '11111111'

for idx, px_value in enumerate(value11):
    if px_value == '1':
        qc_image.ccx(num_qubits - 1, num_qubits - 2, idx)


# Measurement
qc_image.barrier()
qc_image.measure(range(10), range(10))


# Run the circuit on the QASM simulator
qasm_sim = Aer.get_backend('qasm_simulator')

t_qc_image = transpile(qc_image, qasm_sim)

qobj = assemble(t_qc_image, shots=8192)

job_neqr = qasm_sim.run(qobj)

result_neqr = job_neqr.result()

counts_neqr = result_neqr.get_counts()


# Display encoded values
print('Encoded: 00 = 0')
print('Encoded: 01 = 01100100')
print('Encoded: 10 = 11001000')
print('Encoded: 11 = 1')

print(counts_neqr)

plot_histogram(counts_neqr)
