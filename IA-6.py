#Problem 1
def problem1():
 # Create a list of week days
 Week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
 #list of sales in comparison to each day
 Sale_list = [50, 75, 150, 125, 100]
 #Maximum sales value
 max_sales = max(Sale_list)
 #Index of max sales
 max_index = Sale_list.index(max_sales)
 #Day corresponding to the max sales
 max_day = Week_list[max_index]
 #Results
 print(f"The Max sales is $ {max_sales}")
 print(f"The Max sales day is {max_day}")
#Problem 2
def problem2():
 #Empty list to store user numbers
 num_list = []
 #Loop for collecting numbers
 while True:
value = float(input("Enter value (or 0 to end):"))
#Break loop if user enters 0
if value == 0:
break
else:
num_list.append(value)
 #Display list of numbers
 print(num_list)
 #Only calculate range if the list is not empty
if len(num_list) > 0:
#Find max and min
max_value = max(num_list)



min_value = min(num_list)
#Calculate the range
num_range = max_value - min_value
#Display range using f string
print(f"Range = {num_range}")
 else:
print ("No numbers were entered")
#Main Program
def main():
 print(" Problem 1")
 problem1()
 print("\nProblem 2")
 problem2()
#Main function to run program
main()
