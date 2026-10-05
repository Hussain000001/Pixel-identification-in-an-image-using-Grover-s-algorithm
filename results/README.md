# Results

This directory contains the experimental results and visual outputs from the quantum image encoding and Grover search implementation.

## Input Image

The experiment uses a 2×2 grayscale image with the following pixel intensities:

\[
\begin{bmatrix}
0 & 100 \\
200 & 255
\end{bmatrix}
\]

The darkest pixel has intensity 0 and is located at position `(0,0)`.

![Original 2×2 grayscale image](original_2x2_image.png)

## NEQR Encoding

The four pixels are encoded using 10 qubits:

| Position | Intensity | Binary intensity |
|----------|-----------|------------------|
| `00` | 0 | `00000000` |
| `01` | 100 | `01100100` |
| `10` | 200 | `11001000` |
| `11` | 255 | `11111111` |

The NEQR simulation successfully reproduced all four encoded states.

## Grover Search

Grover's algorithm was then used to search for the pixel with minimum intensity.

The target state was:

```text
0000000000
