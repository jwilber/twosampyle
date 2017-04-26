import pytest
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from twosampyle.permchisquare import ChiSquaredTest



def pValueShouldBeBetweenZeroAndOne(): 
	obs = [26816, 3624, 1039, 311, 771]
    ex = [26146.5, 3939.9, 1044.3, 310.5, 1119.8]
	chisq = ChiSquaredTest(obs, ex)
	assert 0 <= chisq.pvalue() <= 1


# def test_pValueShouldBeOneIfDataExactlyTheSame(): 
# 	data = pd.DataFrame({"trt1": [1,2,3], "trt2": [1,2,3]})
# 	p = PermTest(data)
# 	p.format_data()
# 	assert p.pvalue() >= .9999


# def test_pValueShouldBeVeryCloseToZeroIfDataExtremelyDifferent(): 
# 	data = pd.DataFrame({"trt1": [1,2,3], "trt2": [1000,24000,-4000]})
# 	p = PermTest(data)
# 	p.format_data()
# 	assert p.pvalue() < 1e-5