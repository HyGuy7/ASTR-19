print("My favorite animal is a Wolf.")

#define a class
class Wolf:
	#set animal atributes
	def __init__(self, arm_length, leg_length, eye_count, has_tail, is_furry):
		self.arm_length = arm_length #Arm length(float)
		self.leg_length = leg_length # Leg length(floaT)
		self.eye_count = eye_count #Number of eyes(integer)
		self.has_tail = has_tail #Tail? (bool)
		self.is_furry = is_furry #Furry? (bool)

		#DEfine the animals atributes
	def describe(self):
			print("Wolf Atributes:")
			print(f" - Arm length: {self.arm_length} meters")
			print(f" - Leg length: {self.arm_length} meters")
			print(f" - Eye count: {self.eye_count} eyes")
			print(f" - Is Furry?: {'Yes' if self.is_furry else 'No'}")
			print(f" - Has a tail?: {'Yes' if self.has_tail else 'No'}")

# Create an instance of the class with tha animal atribute values
def main():
	my_favorite_animal = Wolf(arm_length=0.505, leg_length=0.505, eye_count=2, has_tail=True, is_furry=True)

	#Call the method to print details
	my_favorite_animal.describe()

# Execute the main function
if __name__ == "__main__":
	main()
