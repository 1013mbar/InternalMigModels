proc.py:
read a csv file with columns fipsA and fipsB and remove the the first zero
only applicable if fips code has 6 digits (6 digit fips code -> 5 digit fips code)

readExcel.py:
drop unnecessary columns from the original US census data set and creates fips columns

formatFips.py:
takes the GDP data and removes dots to be able to display the GDP data
adds zeros to fips code to establish 5 digit fips codes

sortedPop.py:
Takes population data and distance data and sorts the population data by
distance from one countyCode

sij.py:
Takes the output of sortedPop.py, harmonizes the distance and population data and creates
a dataFrame with fips, pop and dist ordered by dist

how to process new state data:
Copy state spread sheet
delete MOE columns
format header to one row header
delete EU, ASIA etc flows (not necessary, readExcel.py does that)
delte footer