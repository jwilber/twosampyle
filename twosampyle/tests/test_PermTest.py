import pytest
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# ask Stefan: should I create data in each test or create some here and then use it in test?
# also ask about naming convention

def test_DiffMeansForSameDataShouldBeZero():
	from twosampyle.permtest import PermTest
	data = pd.DataFrame({"trt1": [1:20], "trt2": [1:20})
	p = PermTest(data)
	p.format_data()
	diffmean = p.diffmean()
	assert diffmean < 1e-5, "Difference of Means for the same data should be zero"


def test_InputNotCorrectShapesShouldRaiseError():
	with pytest.raises(ValueError):
		data = {"trt1": [1,2], "trt2": [1,2,3]}

def test_simPermDsnShouldReturnListOfSizeK():
	pass

def test_PermTestShouldLoadDataAsIs():
    from twosampyle.permtest import PermTest  # should this import always be in the test?
    data = {"trt1": [1,2,3,4,5,6,7,8,9,10], "trt2": [40,50,60,70,70,60,50,30,40,20]}
    df = pd.DataFrame(data)
    p = PermTest(df)
    assert p.data.shape == df.shape


def test_formatForDataWithNameAndFormatForDataWithoutNameShouldBeTheSame():
	pass

def pValueShouldBeVeryCloseToZeroIfDataExtremelyDifferent():
	pass

def pValueShouldBeOneIfDataExactlyTheSame():
	pass

def pValueShouldBeBetweenZeroAndOne():
	pass

