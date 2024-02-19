import nbformat
import re
import os
import sqlite3

def read_ipynb(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

# Replace 'your_notebook.ipynb' with the path to your notebook file
notebook = read_ipynb('hw4.ipynb')

# test if all three dataframes are read in correctly
def test_q1():
    assert hw4.pupolation.shape == (28265, 11)
    assert hw4.annual == (27758, 7)
    assert hw4.land == (3198, 35)

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
        if cell.source.count("sns.barplot") > 0 : 
            contains_seaborn = True
        if cell.source.count("plt.bar") > 0 : 
            contains_matplotlib = True
    assert contains_seaborn or contains_matplotlib





















