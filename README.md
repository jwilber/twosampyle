# twosampyle

[![Build Status](https://travis-ci.org/jwilber/twosampyle.svg?branch=master)](https://travis-ci.org/jwilber/twosampyle)

`twosampyle` is a minimalist Python module for testing two sample (A/B) tests. It was created with the following design objectives:

1. **Ease of use**: `twosampyle` has a uniform API and all statistical tests share the same methods and attributes. Think of something along the lines of sci-kit learn's API, but for statistical tests instead of machine learning.

2. **Minimalism** : `twosampyle` only includes functionality that you'll need, and (in its current form) only incudes the following methods:

	- 
	- 
	-
	-
	-


## Getting Started: Testing with `twosampyle`


`twosampyle` currently includes the following statistical tests:

- **Nonparametric**

		- `PermTest()`: Implementation of the classic permutation test.
		- `PermutedChiSquare()`: Nonparametric implementation of the chisquare test for independence.

- **Parametric**

		- `ttest`:
		- `Chisquare`:

- **Bayesian**

		- `BayesianAB`: Bayesian A/B Test


As state previously, each test contains the following methods





