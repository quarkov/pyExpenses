pyExpenses
=======
This project aims to provide tools for parsing and visualising expenses data.  
By now it offers a group of functions allowing aggregation and visualisation data by month or by year.  
However there's no GUI yet, it's possible to utilize scripts anyway.
<br>


# Dependencies:
Python3, matplotlib, numpy


# Howto:
Clone the project project and launch _run.py_ 
Passing two arguments: the first one is a year, the second one is a month   
(its number) will result in a pie chart with monthly expenses.  
If skip passing a month number, result will be a yearly report.
  
Long story short,

`python3 run.py 2020 3` will result in:  
![2020, March Expenses](/demos/2020_3.png)  
  
`python3 run.py 2020` will result in:  
![2020 Expenses](/demos/2020.png)  
  
Use your own data (following naming conventions demonstrated in the provided csv) and try for yourself.
