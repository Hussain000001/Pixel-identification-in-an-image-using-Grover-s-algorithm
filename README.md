# Pixel Identification with Grover's Algorithm: Interactive Lab

An interactive visual explanation of an M.Sc. Physics thesis project. It shows how a 2×2 grayscale image is encoded as a quantum state with NEQR, and how Grover's algorithm amplifies the marked darkest-pixel state. It is written for students who know basic mathematics and have little or no quantum computing background.

```
Image → position + grayscale value → NEQR → CCX encoding
      → Grover oracle → diffuser → amplitude amplification → measurement → darkest pixel
```

## What you can do

- Click pixels of the image and see their position and intensity in binary.
- See how NEQR ties each position to its intensity as one joint state.
- Step through the encoding circuit one gate at a time (H, temporary X, CCX, restoring X). A branch table shows that only the branch whose controls are `11` is changed.
- Run the full four-pixel encoding to build the complete NEQR state.
- Apply the oracle and the diffuser, run Grover iterations manually or automatically, and compare the simulated probability with the theoretical `sin²((2t+1)θ)`.
- Measure the final state and decode the result to a pixel.
- Edit the 2×2 image in the Playground. The binary values, NEQR table, target and search all update.
- Switch between Beginner and Researcher views, and answer the eight Teaching Mode questions.

## Run locally

No build step, no dependencies, no backend.

```bash
# just open the file
open index.html

# or serve it
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Deploy on Vercel

**CLI**

```bash
npm i -g vercel
vercel login
vercel          # preview deploy; framework preset: Other, no build command
vercel --prod   # production URL
```

**GitHub**

1. Push this folder to a repository.
2. In Vercel choose Add New → Project and import the repository.
3. Set the framework preset to **Other** and leave the build command and output directory empty.
4. Deploy. Later pushes redeploy automatically.

The same file also works on GitHub Pages, Netlify, or any static host.

## Conventions

- Basis states are written as `|intensity q7…q0⟩|position q9 q8⟩`. Qiskit often prints bitstrings in reverse order, so always state the convention when reading measured strings.
- The NEQR state is normalised: `|Ψ⟩ = ½[|00000000⟩|00⟩ + |01100100⟩|01⟩ + |11001000⟩|10⟩ + |11111111⟩|11⟩]`.
- The Grover simulation is exact (not sampled) over the 2¹⁰ = 1024 ten-bit strings with `0000000000` marked, as in the reference Qiskit code. The measurement button samples a single shot from the resulting probabilities.

## Scientific scope

This is a proof-of-concept teaching tool. It demonstrates the integration of NEQR-style image representation with Grover amplitude amplification for a marked target state.

- It does **not** implement a fully coherent quantum minimum-finding algorithm. The target is supplied; the oracle does not read it from the encoded intensities.
- It does **not** demonstrate practical quantum advantage for image processing. A 2×2 image is trivial classically, and state preparation, oracle construction and measurement costs must be included in any end-to-end claim.
- A complete minimum finder would need a reversible comparator, minimum-finding logic, an oracle built from the encoded intensities, and no classical extraction of the minimum beforehand. This is the natural research extension.
- In the thesis simulation, 8183 of 8192 shots landed on the target (about 99.89%). This is a sampled estimate, not an exact probability.

## Credits

Based on the M.Sc. Physics thesis *Pixel identification in an image using Grover's algorithm* by Mohd Hussain Mir, National Institute of Technology Srinagar. Supervisor: Dr. Harkirat Singh.

Related paper: [arXiv:2107.03039](https://arxiv.org/abs/2107.03039)

## Files

| File | Purpose |
|------|---------|
| `index.html` | The complete application (HTML, CSS and JavaScript in one file) |
| `README.md` | This file |

## License

Add a license of your choice before publishing the repository. MIT is a common choice for educational tools.
