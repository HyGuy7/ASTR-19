import numpy as np #import numpy to create arrays
from tabulate import tabulate #package to build tables


#Gereate an array of x and y values
x = np.linspace(0.0,6.28318530718,1000) #generate 1000 values from 0 to 2pi regularly spaced

sin_of_x = np.sin(x) #sinx

#Tables using tabualte
table_data = [(x, sin_of_x) for x,sin_of_x in zip(x,sin_of_x)]

#Create the table 
table_header = ["x","sin_of_x"]
python_table = tabulate(table_data, tablefmt="grid", headers=table_header, floatfmt= ".3f")


#main program that will be executed only when this file is run
def main():
	print(table_data) #quick look into table data
	print(python_table) #quick look into table data


if __name__=="__main__":
	main()
 