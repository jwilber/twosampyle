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
	tt = TTest([1,2,3,4,5,6,7,4,4,4,3,2,1,2,1.5,8,1,2,3],
		100000,1000,1000,1000,4000,5000,6000,24000,-4000,5000,60000,40000,555555,33333355555555,434343,43434,1e5,2e5,4e5])
	assert tt.pvalue() < 1e-4


def test_pValueShouldBeOneIfDataExactlyTheSame(): 
	tt = TTest()
	assert tt.pvalue(range(100000),range(100000)) >= .9999