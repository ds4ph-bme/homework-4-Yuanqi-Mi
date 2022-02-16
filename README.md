2. Look at the [chapter on interactive graphics](https://smart-stats.github.io/ds4bio_book/book/_build/html/interactive.html) and, specifically, the code to display a subject's MRICloud data as a sunburst plot. Do the following. Display this subject's data as a [Sankey diagram](https://plotly.com/python/sankey-diagram/). Display as many levels as you can for type = 1, starting from the intracranial volume. Put this in a file called hw4.ipynb.
3. Create a simple webpage containing this graphic and host it on github pages. -Do not- host this off of your assignment repo from github classroom, since this is not public. Instead, you'll have to create a new public repo from your regular github account and add this file. Put the link to your live web page in a markdown cell of your hw4.ipynb file. Note, an easy way to create a webpage with this graphic is to export an ipynb as an html file.
4. Create the opioid sqlite database from [https://smart-stats.github.io/ds4bio_book/book/_build/html/sqlite.html](https://smart-stats.github.io/ds4bio_book/book/_build/html/sqlite.html). However, only go to the step where the csv files are read into the database. Then exit sqlite and you should have a file `opioid.db` that has the data. Next, read the three tables into pandas dataframes and do the data wrangling from the sqlite chapter directly in pandas. Add the python code to your hw4.ipynb file.
5. Create an interactive scatter plot of average number of opiod pills by year plot using plotly. [See the example here](https://www.opencasestudies.org/ocs-bp-opioid-rural-urban/#Data_Import). Don't do the intervals (little vertical lines), only the points. Add your plot to an html file with your repo for your Sanky diagram and host it publicly. Put a link to your hosted file in a markdown cell of your hw4.ipynb file.  Note, an easy way to create a webpage with this graphic is to export an ipynb as an html file.

Reminder, the html files need to be in your own repository (since your github classroom repo is private). However, your hw4.ipynb file should be turned in via your githubclassroom repo.
