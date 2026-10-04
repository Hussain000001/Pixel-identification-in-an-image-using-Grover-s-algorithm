# Cirq implementation of Grover's algorithm

import cirq
import sympy
import numpy as np
import seaborn as sns
import collections
import matplotlib.pyplot as plt
from cirq.contrib.svg import SVGCircuit
from PIL import Image
import random
from cirq import plot_state_histogram as plt_hist


# Generate a random 2 x 2 grayscale image
image1 = np.random.randint(255, size=(2, 2))

plt.imshow(image1, cmap='gray', vmin=0, vmax=255)
plt.show()

plt.imsave('grayimg.jpeg', image1, cmap='gray')


# Load the image
FILENAME = 'grayimg.jpeg'
image2 = Image.open(FILENAME)
pixels = np.asarray(image2)

print(pixels)


# Get qubits to use in the circuit for Grover's algorithm

# Number of qubits
nqubits = 3

# Get qubit registers
qubits = cirq.LineQubit.range(nqubits)

# Ancilla qubit
ancilla = cirq.NamedQubit("Ancilla")

# Find the position of the minimum pixel value
xprime = np.unravel_index(np.min(pixels), pixels.shape)


def make_oracle(qubits, ancilla, xprime):
    """
    Implements the function:
    f(x) = 1 if x == x'
    f(x) = 0 if x != x'
    """

    # For x' = (1, 1), the oracle is just a Toffoli gate.
    # For a general x', negate the zero bits and implement a Toffoli.

    # Negate zero bits, if necessary
    yield (
        cirq.X(q)
        for (q, bit) in zip(qubits, xprime)
        if not bit
    )

    # Do the Toffoli
    yield cirq.TOFFOLI(
        qubits[0],
        qubits[1],
        ancilla
    )

    # Negate zero bits, if necessary
    yield (
        cirq.X(q)
        for (q, bit) in zip(qubits, xprime)
        if not bit
    )


def grover_iteration(qubits, ancilla, oracle):
    """Performs one round of the Grover iteration."""

    circuit = cirq.Circuit()

    # Create an equal superposition over input qubits
    circuit.append(cirq.H.on_each(*qubits))

    # Put the output qubit in the |-> state
    circuit.append([
        cirq.X(ancilla),
        cirq.H(ancilla)
    ])

    # Query the oracle
    circuit.append(oracle)

    # Construct Grover operator
    circuit.append(cirq.H.on_each(*qubits))
    circuit.append(cirq.X.on_each(*qubits))
    circuit.append(cirq.H.on(qubits[1]))
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.H.on(qubits[1]))
    circuit.append(cirq.X.on_each(*qubits))
    circuit.append(cirq.H.on_each(*qubits))

    # Measure the input register
    circuit.append(
        cirq.measure(*qubits, key="result")
    )

    return circuit


# Create the circuit for Grover's algorithm

# Make oracle (black box)
oracle = make_oracle(
    qubits,
    ancilla,
    xprime
)

# Embed the oracle into a quantum circuit
# implementing Grover's algorithm
circuit = grover_iteration(
    qubits,
    ancilla,
    oracle
)

print("Circuit for Grover's algorithm:")
print(circuit)


# Simulate the circuit for Grover's algorithm

def bitstring(bits):
    return "".join(str(int(b)) for b in bits)


# Sample from the circuit
simulator = cirq.Simulator()

result = simulator.run(
    circuit,
    repetitions=1000
)


# Look at the sampled bitstrings
frequencies = result.histogram(
    key="result",
    fold_func=bitstring
)

print(
    'Sampled results:\n{}'.format(frequencies)
)


# Check if we actually found the secret value
most_black_bitstring = frequencies.most_common(1)[0][0]

print(
    "\nMost black pixel: {}".format(
        most_black_bitstring
    )
)


# Plotting 3D histogram of results

image = np.array(image1)

a = image.min()

image = np.where(
    image == a,
    1,
    image
)

image = np.where(
    image != 1,
    0,
    image
)

print(image)

data_array = np.array(image)

fig = plt.figure()

ax = fig.add_subplot(
    111,
    projection='3d'
)

x_data, y_data = np.meshgrid(
    np.arange(data_array.shape[0]),
    np.arange(data_array.shape[1])
)

x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = data_array.flatten()

ax.bar3d(
    x_data,
    y_data,
    np.zeros(len(z_data)),
    0.93,
    0.93,
    z_data
)

plt.show()
