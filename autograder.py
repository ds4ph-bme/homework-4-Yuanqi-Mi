# read in packages
import nbformat
import re
from nbconvert import PythonExporter
import pytest
import numpy as np

###########################################################################
# modified from hw3 autograder

# Function to convert the notebook to a python file
def convert_notebook_to_py(notebook_path, py_path):
    with open(notebook_path) as fh:
        nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
    exporter = PythonExporter()
    source, _ = exporter.from_notebook_node(nb)
    with open(py_path, 'w+') as fh:
        fh.writelines(source)

# Convert the notebook to py file before testing
convert_notebook_to_py('hw4.ipynb', 'hw4.py')

# also read in this way for other checks
def read_ipynb(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

# read in notebook
notebook = read_ipynb('hw4.ipynb')

# Import the Python script after conversion
import hw4

###########################################################################

### Tests ###

# test if all three dataframes are read in correctly
def test_q1():
    assert hw4.pupolation.shape == (28265, 11)
    assert hw4.annual == (27758, 7)
    assert hw4.land == (3198, 35)

# test merged dataframe
def test_merge():

    # Check if the merged dataframe has the correct shape
    assert hw4.county_info.shape == (28265, 13)

    # Check if the merged DataFrame has the correct column names
    expected_columns = ['?', 'BUYER_COUNTY', 'BUYER_STATE', 'countyfips', 'STATE', 'COUNTY','county_name', 'NAME', 
                        'variable', 'year', 'population', 'Areaname','LND110210D']
    assert list(county_info.columns) == expected_columns

# test the data frame of average number of opioid pills by year
def test_df():
    # Verify that the resulting DataFrame has the correct columns
    assert all(column in hw4.df.columns for column in ['year', 'Average_pills_in_millions'])
    # check use function groupby
    contains_groupby = False
    for cell in notebook.cells:
        if cell.source.count("groupby") > 0 : 
            contains_groupby = True
    assert contains_groupby 

# test if scatterplot was used in matplotlib or seaborn 
def test_visualization():
    contains_seaborn = False
    contains_matplotlib = False
    for cell in notebook.cells:
        if cell.source.count("sns.scatterplot") > 0 : 
            contains_seaborn = True
        if cell.source.count("plt.scatter") > 0 : 
            contains_matplotlib = True
    assert contains_seaborn or contains_matplotlib

# function to read in R file
def read_r(r_path):
    with open(r_path, 'r', encoding='utf-8') as f:
        return f.read()

# read in R file
r_code = read_r('hw4.R')

# check R code
def check_r_code():
    
    # Check if the R code reads in the data frames
    assert re.search(r'read\.csv\("county_annual\.csv"\)', r_code)
    assert re.search(r'read\.csv\("county_pop_arcos\.csv"\)', r_code)
    assert re.search(r'read\.csv\("land_area\.csv"\)', r_code)

    # Check if the R code merge data frame
    assert re.search(r'merge\(population, land_area, by = "countyfips"', r_code)

# test converted dataframe from R file
def test_q4():

    # Check if the converted dataframe has the correct shape
    assert hw4.county_info_R.shape == (28265, 13)

    # Check if the converted dataframe matches the dataframe from question 1
    assert hw4.county_info_R.equals(hw4.county_info)




















