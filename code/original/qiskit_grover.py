# Grover algorithm used in NEQR

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator


def diffuser(n):
    # Create a quantum circuit on n qubits
    qc = QuantumCircuit(n, name='Diffuser')

    # Apply Hadamard gates to all qubits
    qc.h(range(n))

    # Call the phase oracle applied to the zero state
    qc.append(phase_oracle(n, [0]), range(n))

    # Apply Hadamard gates to all qubits
    qc.h(range(n))

    return qc


def phase_oracle(n, indices_to_mark, name='Oracle'):
    # Create a quantum circuit on n qubits
    qc = QuantumCircuit(n, name=name)

    # Create the identity matrix on n qubits
    oracle_matrix = np.identity(2**n)

    # Add the -1 phase to marked elements
    for index_to_mark in indices_to_mark:
        oracle_matrix[index_to_mark, index_to_mark] = -1

    # Convert the matrix into an operator
    # and add it to the quantum circuit
    qc.unitary(Operator(oracle_matrix), range(n))

    return qc


def Grover(n, indices_of_marked_elements):
    # Create a quantum circuit on n qubits
    qc = QuantumCircuit(n, n)

    # Determine r
    r = int(
        np.floor(
            np.pi / 4
            * np.sqrt(
                2**n / len(indices_of_marked_elements)
            )
        )
    )

    print(
        f'{n} qubits, basis states '
        f'{indices_of_marked_elements} marked, '
        f'{r} rounds'
    )

    # Step 1: Apply Hadamard gates on all qubits
    qc.h(range(n))

    # Step 2: Apply r rounds of the phase oracle and diffuser
    for _ in range(r):
        qc.append(
            phase_oracle(n, indices_of_marked_elements),
            range(n)
        )
        qc.append(diffuser(n), range(n))

    # Step 3: Measure all qubits
    qc.measure(range(n), range(n))

    return qc


# The thesis contains the following placeholder:
# mycircuit = Grover(n, [marked bitstring])

# mycircuit.draw()

# The following lines were also included in the thesis:
# from qiskit import Aer, execute
# simulator = Aer.get_backend('qasm_simulator')
# counts = execute(
#     mycircuit,
#     backend=simulator,
#     shots=1000
# ).result().get_counts(mycircuit)

# from qiskit.visualization import plot_histogram
# plot_histogram(counts)
