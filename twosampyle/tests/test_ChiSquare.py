import pytest
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from twosampyle.permchisquare import ChiSquaredTest



def pValueShouldBeBetweenZeroAndOne(): 
	observed = [26816, 3624, 1039, 311, 771]
	expected = [26146.5, 3939.9, 1044.3, 310.5, 1119.8]
	chisq = ChiSquaredTest(observed, expected)
	assert 0 <= chisq.pvalue() <= 1


def test_pValueShouldBeOneIfDataExactlyTheSame(): 
	observed = range(100000)
	expected = range(100000)
	chi = ChiSquaredTest(observed, expected)
	assert chi.pvalue() >= .9999


def test_pValueShouldBeVeryCloseToZeroIfDataExtremelyDifferent(): 
	observed = [1,5,4,6,8,4,5,6,5]
	expected = [1e5,4e3,5e4,6e5,4e5,3e4,3e5,2e5,4e6]
	chi = ChiSquaredTest(observed, expected)
	assert chi.pvalue() < 1e-4