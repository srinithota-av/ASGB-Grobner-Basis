# Adaptive Signature-Based Gröbner Basis (ASGB)

This repository contains the official framework implementation and benchmark verification suite accompanying the research paper: **"Adaptive Signature-Based Gröbner Basis with Dependency-Aware Reduction"**.

## Core Framework Design
ASGB functions as a deterministic scheduling layer situated above signature-compatible polynomial reduction layers. It evaluates candidates using the Adaptive Signature Index (ASI):

$$\Psi(g_{i}) = \lambda_{1}S_{i} + \lambda_{2}D_{i} + \lambda_{3}R_{i} + \lambda_{4}P_{i}$$

## Getting Started
### Dependencies
Ensure you have Python 3.10+ or a running SageMath execution context config installed along with the metadata logging requirements:
```bash
pip install -r requirements.txt
```

### Running the Benchmarks
To trace system environment characteristics and simulate runtime evaluation routines matching experimental Table metrics, run:
```bash
python benchmarks/run_benchmarks.py
```
