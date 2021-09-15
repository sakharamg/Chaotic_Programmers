q1
=====

Add stuff here
------------



Question 4
=====

Input
------------

   A .csv file containing DataBreach data is received as the input.
   It contains 1 header + 295 rows of data (total 296 lines). It has
   5 columns (as mentioned in the header): **Entity, Year, Records, Organization type,
   Method**.


Output
------------

There are two plots:

1. A plot with average DataBreach Record for that specific category and that specific Year for all organization types
2. A range-boxplot for each method of data breach, showing the min and max records of data breach for each year.



Function
------------

The q4.py file reads the input datbreach csv file, filters allowed organization_types and methods and then produces plots as described.



Question 5
=====

Input
------------

   A .npy file, that represents an image to be decoded.


Output
------------

There are two output files:

1. A plot representing the decoded image.
2. A text file containing the decoded key.



Function
------------

The q5.py file reads the input .npy file to a numpy array and then performs linear contrast enhancement to decode the original image.


