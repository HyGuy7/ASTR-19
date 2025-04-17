#Define the function f(x) that returns x**3 + 8

def f(x):
	return x**3+8


#Define the main function to call f(x)
def main():
	x = 9
	result = f(x)
	print(f"f({x}) = {result}")

	#Check if the result is over 27 and print YAY if true
	if result > 27:
		print("YAY!")

#IF main execute main
if __name__ == "__main__":
	main()