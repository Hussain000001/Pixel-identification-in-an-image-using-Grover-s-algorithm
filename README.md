# Pixel Identification in an Image Using Grover's Algorithm

A Master's thesis project exploring the application of Grover's quantum search algorithm to pixel identification in grayscale images, using quantum image representation and quantum circuit simulation

## About the Project

This project investigates how quantum search techniques can be used to identify and locate a target pixel within a grayscale image. The thesis explores NEQR (Novel Enhanced Quantum Representation) for representing pixel position and intensity, followed by Grover's algorithm for quantum search.

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

## Project Workflow

The project follows these main steps:

1. **Create a grayscale image**
   - A 2×2 grayscale image is used as the test image.

2. **Represent the image using NEQR**
   - Pixel positions are represented using 2 qubits.
   - Pixel intensities are represented using 8 qubits.

3. **Construct the Grover oracle**
   - The oracle marks the target pixel state.

4. **Apply amplitude amplification**
   - The Grover diffuser amplifies the probability of the marked state.

5. **Measure the quantum circuit**
   - The circuit is executed using the Qiskit Aer simulator.

6. **Identify the target pixel**
   - The most probable measurement result corresponds to the target pixel.

7. **Analyze the result**
   - The measurement distribution is visualized using a histogram.

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
├── CITATION.cff
├── requirements.txt
│
├── code/
│   ├── modern/
│   │   └── grover_pixel_search.py
│   │
│   └── original/
│       ├── qiskit_neqr.py
│       ├── qiskit_grover.py
│       └── cirq_grover.py
│
├── results/
│   ├── README.md
│   ├── original_2x2_image.png
│   └── grover_histogram.png
│
└── thesis/
    └── Final project thesis.pdf

## Quantum Representation

For the 2×2 grayscale image, each pixel is represented by:

- **2 qubits** for the pixel position
- **8 qubits** for the grayscale intensity

Therefore, the complete representation uses **10 qubits**.

The four pixels are represented as:

| Pixel position | Grayscale value | Binary representation |
|---|---:|---|
| `(0,0)` | 0 | `00000000` |
| `(0,1)` | 100 | `01100100` |
| `(1,0)` | 200 | `11001000` |
| `(1,1)` | 255 | `11111111` |

The darkest pixel in this example is the pixel at `(0,0)`, with intensity `0`.

## Results

### Input Image

The experiment uses a 2×2 grayscale image with the following pixel intensities:

```text
[[  0, 100],
 [200, 255]]

The darkest pixel has intensity 0 and is located at position (0,0).

![Original 2×2 grayscale image](results/original_2x2_image.png)

### Grover Search

Grover's algorithm was used to search for the target state corresponding to the darkest pixel.

For this 2×2 example, the target state is:

```text
0000000000

### Conclusion

The simulation successfully recovered the marked quantum state corresponding to the darkest pixel in the 2×2 grayscale image:

Position:  (0,0)
Intensity: 0

Position:  (0,0)
Intensity: 0

## Modern Implementation

The repository includes a modern Qiskit implementation in:

`code/modern/grover_pixel_search.py`

This implementation uses current Qiskit and Qiskit Aer APIs to demonstrate Grover's search on a 10-qubit system.

For the 2×2 example, the target state is:

```text
0000000000

### Grover Search Result

Grover's algorithm successfully identifies the darkest pixel. The measurement result `0000000000` corresponds to the pixel at position `(0,0)` with intensity `0`.

![Grover histogram](results/grover_histogram.png)

## How to Run

## Thesis

This repository is based on the Master's thesis:

**"Pixel identification in an image using Grover's algorithm"**

**Author:** Mohd Hussain Mir  
**Degree:** Master of Science in Physics  
**Institution:** National Institute of Technology Srinagar  
**Supervisor:** Dr. Harkirat Singh

The complete thesis is available in the [`thesis/`](thesis/) directory.

### 1. Clone the repository

```bash
git clone https://github.com/Hussain000001/Pixel-identification-in-an-image-using-Grover-s-algorithm.git
cd Pixel-identification-in-an-image-using-Grover-s-algorithm
