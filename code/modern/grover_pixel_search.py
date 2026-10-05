import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram


# --------------------------------------------------
# 1. Create the 2×2 grayscale image
# --------------------------------------------------

image = np.array([
    [0, 100],
    [200, 255]
])

print("Input image:")
print(image)


# --------------------------------------------------
# 2. Create the Grover oracle
# --------------------------------------------------

def phase_oracle(n):
    """Mark the state |000...000>."""

    qc = QuantumCircuit(n)

    qc.x(range(n))

    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)

    qc.x(range(n))

    return qc


# --------------------------------------------------
# 3. Create the Grover diffuser
# --------------------------------------------------

def diffuser(n):
    """Perform amplitude amplification."""

    qc = QuantumCircuit(n)

    qc.h(range(n))
    qc.x(range(n))

    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)

    qc.x(range(n))
    qc.h(range(n))

    return qc


# --------------------------------------------------
# 4. Create the Grover circuit
# --------------------------------------------------

def grover_circuit(n):

    qc = QuantumCircuit(n, n)

    # Create equal superposition
    qc.h(range(n))

    # Number of Grover iterations
    r = int(np.floor(np.pi / 4 * np.sqrt(2**n)))

    print("Number of Grover iterations:", r)

    # Grover iterations
    for _ in range(r):

        qc.compose(
            phase_oracle(n),
            range(n),
            inplace=True
        )

        qc.compose(
            diffuser(n),
            range(n),
            inplace=True
        )

    # Measurement
    qc.measure(range(n), range(n))

    return qc


# --------------------------------------------------
# 5. Build the 10-qubit Grover circuit
# --------------------------------------------------

grover = grover_circuit(10)

print(grover)


# --------------------------------------------------
# 6. Run the circuit using Qiskit Aer
# --------------------------------------------------

simulator = Aer.get_backend("qasm_simulator")

compiled_grover = transpile(
    grover,
    simulator
)

result = simulator.run(
    compiled_grover,
    shots=8192
).result()


# --------------------------------------------------
# 7. Get measurement results
# --------------------------------------------------

counts_grover = result.get_counts()

print("\nMeasurement results:")
print(counts_grover)


# --------------------------------------------------
# 8. Identify the darkest pixel
# --------------------------------------------------

target_state = "0000000000"

target_counts = counts_grover.get(
    target_state,
    0
)

success_probability = (
    target_counts / 8192
)

print("\nTarget state:", target_state)
print("Target counts:", target_counts)
print(
    "Success probability:",
    success_probability * 100,
    "%"
)


# --------------------------------------------------
# 9. Plot Grover measurement histogram
# --------------------------------------------------

plot_histogram(
    counts_grover,
    title="Grover Search for the Darkest Pixel"
)

plt.show()
