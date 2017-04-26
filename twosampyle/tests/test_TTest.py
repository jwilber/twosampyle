import pytest
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import t 
from twosampyle.ttest import TTest 

def test_pValueShouldBeBetweenZeroAndOne(): 
	tt = TTest([1,2,3,4], [4,5,6,7])
	assert 0 <= tt.pvalue() <= 1

def test_pValueShouldBeVeryCloseToZeroIfDataExtremelyDifferent(): 
	tt = TTest([1,2,3,4,5],
		[1e4,2e4,3e4,4e4,5e4])
	assert tt.pvalue(sided='two') < .1


def test_pValueShouldBeOneIfDataExactlyTheSame(): 
	tt = TTest()
	assert tt.pvalue(range(100000),range(100000), sided='two') >= .9