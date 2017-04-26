import pytest
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import t 
from twosampyle.ttest import TTest 

def test_pValueShouldBeBetweenZeroAndOne(): 
	tt = TTest([1,2,3,4], [4,5,6,7])
	assert 0 <= tt.pvalue() <= 1