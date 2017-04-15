import pytest
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from twosampyle.permtest import PermTest

# ask Stefan: should I create data in each test or create some here and then use it in test?
# also ask about naming convention

def test_DiffMeansForSameDataShouldBeZero():
	import pandas as pd 
	data = pd.DataFrame({"trt1": range(5), "trt2": range(5)})
	p = PermTest(data)
	p.format_data()
	diffmean = p.diffmean()
	assert diffmean < 1e-5, "Difference of Means for the same data should be zero"


def test_InputNotCorrectShapesShouldRaiseError():
	# with pytest.raises(ValueError):
	# 	data = {"trt1": [1,2], "trt2": [1,2,3]}
	# 	p = PermTest(data)
	pass


def test_simPermDsnShouldReturnListOfSizeK():
	import pandas as pd 
	data = pd.DataFrame({"trt1": [1,2,3,4], "trt2": [2,3,4,5]})
	p = PermTest(data)
	p.format_data()
	sim_data = p.simPermDsn(k=5)
	assert len(sim_data) == 6

def test_PermTestShouldLoadDataAsIs():
	import pandas as pd 
    #from twosampyle.permtest import PermTest  # should this import always be in the test?
    data = {"trt1": [1,2,3,4,5,6,7,8,9,10], "trt2": [40,50,60,70,70,60,50,30,40,20]}
    df = pd.DataFrame(data)
    p = PermTest(df)
    assert p.data.shape == df.shape


def test_formatForDataWithNameAndFormatForDataWithoutNameShouldBeTheSame():
	import pandas as pd 
	data = pd.DataFrame({"trt1": range(5), "trt2": range(5)})
	p1 = PermTest(data)
	p2 = PermTest(data)
	assert p1.format_data() == p2.format_data('trt1', 'trt2')

def pValueShouldBeVeryCloseToZeroIfDataExtremelyDifferent():
	import pandas as pd 
	data = pd.DataFrame({"trt1": [1,2,3], "trt2": [1000,24000,-4000]})
	p = PermTest(data)
	p.format_data()
	assert p.pvalue() < 1e-5


def pValueShouldBeOneIfDataExactlyTheSame():
	import pandas as pd 
	data = pd.DataFrame({"trt1": [1,2,3], "trt2": [1,2,3]})
	p = PermTest(data)
	p.format_data()
	assert p.pvalue() >= .9999

def pValueShouldBeBetweenZeroAndOne():
	import pandas as pd 
	data = pd.DataFrame({"trt1": [1,2,3], "trt2": [4,5,3]})
	p = PermTest(data)
	p.format_data()
	assert 0 <= p.pvalue() <= 1

