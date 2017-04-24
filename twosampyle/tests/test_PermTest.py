import pytest
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from twosampyle.permtest import PermTest

# ask Stefan: should I create data in each test or create some here and then use it in test?
# also ask about naming convention

# def test_DiffMeansForSameDataShouldBeZero():
# 	data = pd.DataFrame({"trt1": range(5), "trt2": range(5)})
# 	p = PermTest(data)
# 	p.format_data()
# 	diffmean = p.diff_means()
# 	assert diffmean < 1e-5, "Difference of Means for the same data should be zero"


# def test_InputNotCorrectShapesShouldRaiseError():
# 	with pytest.raises(ValueError):
# 		data = {"trt1": [1,2], "trt2": [1,2,3]}
# 		p = PermTest(data)
	


# def test_simPermDsnShouldReturnListOfSizeK(): 
# 	data = pd.DataFrame({"trt1": [1,2,3,4], "trt2": [2,3,4,5]})
# 	p = PermTest(data)
# 	p.format_data()
# 	sim_data = p.simPermDsn(k=5)
# 	assert len(sim_data) == 5

# def test_PermTestShouldLoadDataAsIs():
# 	data={"trt1":[1,2,3,4,5], "trt2":[40,50,60,70,79]}
# 	df = pd.DataFrame(data)
# 	p = PermTest(df)
# 	assert p.data.shape == df.shape


# def test_formatForDataWithNameAndFormatForDataWithoutNameShouldBeTheSame(): 
# 	data = pd.DataFrame({"trt1": range(5), "trt2": range(5)})
# 	p1 = PermTest(data)
# 	p2 = PermTest(data)
# 	assert p1.format_data() == p2.format_data('trt1', 'trt2')

# def test_pValueShouldBeVeryCloseToZeroIfDataExtremelyDifferent(): 
# 	data = pd.DataFrame({"trt1": [1,2,3], "trt2": [1000,24000,-4000]})
# 	p = PermTest(data)
# 	p.format_data()
# 	assert p.pvalue() < 1e-5


def test_pValueShouldBeOneIfDataExactlyTheSame(): 
	data = pd.DataFrame({"trt1": [1,2,3], "trt2": [1,2,3]})
	p = PermTest(data)
	p.format_data()
	assert p.pvalue() >= .9999

def test_pValueShouldBeBetweenZeroAndOne(): 
	data = pd.DataFrame({"trt1": [1,2,3], "trt2": [4,5,3]})
	p = PermTest(data)
	p.format_data()
	assert 0 <= p.pvalue() <= 1

