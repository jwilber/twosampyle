import pytest
from twosampyle import permtest
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


def test_works():
	pass

def test_DiffMeansForSameDataShouldBeZero():
	pass

def test_InputNotCorrectShapesShouldRaiseError():
	pass

def test_simPermDsnShouldReturnListOfSizeK():
	pass

def test_PermTestShouldLoadDataFine():
    from permtest import PermTest  # should this import always be in the test?
    data = {"trt1": [1,2,3,4,5,6,7,8,9,10], "trt2": [40,50,60,70,70,60,50,30,40,20]}
    df = pd.DataFrame(data)
    p = PermTest(df)
    assert p.data == df