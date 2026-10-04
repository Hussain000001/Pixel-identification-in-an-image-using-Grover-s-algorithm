# Pixel Identification in an Image Using Grover's Algorithm

A Master's thesis project exploring the application of **Grover's quantum search algorithm** to image processing and pixel identification.

## About the Project

This project investigates how quantum search techniques can be applied to identify and locate specific pixels within a grayscale image.

The work combines concepts from:

- Quantum computing
- Grover's search algorithm
- Quantum image processing
- NEQR (Novel Enhanced Quantum Representation)
- Image processing
- Quantum circuit simulation

The project demonstrates the representation of grayscale image information using quantum states and the use of Grover's algorithm for searching for a target pixel.

## Project Objective

The primary objective of this project is to explore the use of Grover's quantum search algorithm for identifying a particular pixel in an image.

The thesis demonstrates the approach using a small grayscale image and quantum circuit simulations.

## Quantum Image Representation

The project uses **NEQR (Novel Enhanced Quantum Representation)** to represent image information.

For the 2 × 2 example considered in the thesis:

- 2 qubits represent the pixel position.
- 8 qubits represent the grayscale intensity.
- A total of 10 qubits are used for the image representation.

The four pixel positions are represented by:

| Pixel Position | Grayscale Value |
|---|---:|
| `00` | 0 |
| `01` | 100 |
| `10` | 200 |
| `11` | 255 |

The corresponding intensity values are encoded as 8-bit binary strings.

## Grover's Algorithm

Grover's algorithm is used as a quantum search procedure to identify a marked state.

The implementation includes:

1. Preparation of the quantum state.
2. Construction of a phase oracle.
3. Construction of the Grover diffuser.
4. Repeated Grover iterations.
5. Measurement of the quantum register.
6. Analysis of the resulting measurement distribution.

## Implementations

The repository contains the original implementations associated with the Master's thesis.

### Qiskit

The Qiskit implementation includes:

- NEQR image encoding
- Quantum circuit construction
- Grover oracle
- Grover diffuser
- Quantum circuit simulation

### Cirq

The Cirq implementation demonstrates Grover's algorithm for identifying the minimum-intensity (darkest) pixel in a randomly generated 2 × 2 grayscale image.

## Repository Structure

```text
.
├── README.md
├── requirements.txt
│
├── code/
│   └── original/
│       ├── qiskit_neqr.py
│       ├── qiskit_grover.py
│       └── cirq_grover.py
│
├── results/
│
└── thesis/
    └── Final project thesis.pdf
