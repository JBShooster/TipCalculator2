#Tip Calculator V2
#This version utilizes try/except and functions to create a more comprehensive
#tip calculator experience for the user

import sys
from tip_calculator_as_functions import calculate_rate, calculate_meal_costs
global calculate_rate
global calculate_meal_costs

print("Welcome to Tip Calculator v3! \nUsing the meal cost, tax rate & tip rate, we'll determine the appropriate tip")

def main():
	while True: 
		try:
			meal_base = sys.argv[1]
		except IndexError:
			try:
				meal_base = float(raw_input("\nIndexError: It seem sys.argv[1] is out of index range. \nInput the base cost of your meal. \nUse only numbers. No symbols(i.e 10.50, 234.33, 5.00): "))
				break
			except ValueError:
				meal_base = float(raw_input("\nValueError: That's not a valid int or float \nInput the base cost of your meal. \nUse only numbers. No symbols(i.e 10.50, 234.33, 5.00): "))
				break
			except ZeroDivisionError:
				meal_base = float(raw_input("\nZeroDivisionError: You can't pick zero! \nInput the base cost of your meal. \nUse only numbers. No symbols(i.e 10.50, 234.33, 5.00): "))
				break
			except NameError:
				meal_base = float(raw_input("\nNameError: That's not a valid int or float. \nInput the base cost of your meal. \nUse only numbers. No symbols(i.e 10.50, 234.33, 5.00): "))
				break
			finally:
				print "\nThe base cost of your meal is", meal_base

	while True: 
		try:
			tax_rate = sys.argv[2]
		except IndexError:
			try:
				tax_rate = float(raw_input("\nIndexError: It seem sys.argv[2] is out of range. \nInput the tax rate as a decimal. \n(i.e, 10% would be .1, 15% would be .15 or 5% would be .05): "))
				break
			except ValueError:
				tax_rate = float(raw_input("\nValueError: That's not a valid int or float \nInput the tax rate as a decimal. \n(i.e, 10% would be .1, 15% would be .15 or 5% would be .05): "))
				break
			except ZeroDivisionError:
				tax_rate = float(raw_input("\nZeroDivisionError: You can't pick zero! \nInput the tax rate as a decimal. \n(i.e, 10% would be .1, 15% would be .15 or 5% would be .05): "))
				break
			except NameError:
				tax_rate = float(raw_input("\nNameError: That's not a valid int or float. \nInput the tax rate as a decimal. \n(i.e, 10% would be .1, 15% would be .15 or 5% would be .05): "))
				break
			finally:
				print "\nThe tax rate is", tax_rate * 100, "%"
	while True: 
		try:
			tip_rate = sys.argv[3]
		except IndexError:
			try:
				tip_rate = float(raw_input("\nIndexError: It seem sys.argv[3] is out of range. \nLastly, what percent tip do you want to give? \nRepresent as decimal as you did with tax rate: "))
				break
			except ValueError:
				tip_rate = float(raw_input("\nValueError: That's not a valid int or float \nWhat percent tip do you want to give? \nRepresent as decimal as you did with tax rate: "))
				break
			except ZeroDivisionError:
				tip_rate = float(raw_input("\nZeroDivisionError: You can't pick zero! \nWhat percent tip do you want to give? \nRepresent as decimal as you did with tax rate: "))
				break
			except NameError:
				tip_rate = float(raw_input("\nNameError: That's not a valid int or float. \nWhat percent tip do you want to give? \nRepresent as decimal as you did with tax rate: "))
				break
			finally:
				print "\nYou've chosen to give a", tip_rate * 100, "% tip"

	calculate_meal_costs(meal_base, tax_rate, tip_rate)
	print "\nHere's the breakdown for your meal costs: ", calculate_meal_costs(meal_base,tax_rate,tip_rate) 
	
if __name__ == '__main__':
	main()
	
raw_input("\n\nPress any key to exit...")