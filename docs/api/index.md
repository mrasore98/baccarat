# API Reference

This section provides detailed documentation for the Baccarat API.

## Overview

Baccarat is a framework for running Monte Carlo simulations using NumPy. It provides:

- A base `Simulator` class for implementing custom simulations
- Parameter descriptors that generate random values according to specific distributions
- Vectorized operations for high performance

## Module Structure

- [`simulator`](simulator.md): Contains the `Simulator` base class
- [`params`](params/index.md): Contains parameter descriptor classes for simulations
  - [`params.base`](params/base.md): Base parameter class
  - [`params.gaussian`](params/gaussian.md): Gaussian distribution parameters
  - [`params.uniform`](params/uniform.md): Uniform distribution parameters
  - [`params.static`](params/static.md): Static (fixed) parameters