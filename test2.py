# positive value
# # if negative or 0 ask again
# a = int(input("Input a positive number: "))
# while a <= 0:
#     a = int(input("Please input a positive number:"))
# print(a)

# input salary in 5 days and calculate average salary in that weeks
# total = 0
# for i in range(1, 6):
#     salary = float(input("Salary of day %s: " %i))
#     total = total + salary
# print("average salary: %.2f" % (total/5))

#sentinel value in this example is the nagative input sale value.When user input a negative
# number. It will terminate the loop. 
total = 0
sale = float(input("Input sale value: "))
count = 0
while sale >= 0:
    total+=sale
    count += 1
    sale = float(input("Input sale value: "))
if count != 0:
    print("Average sale: %.2f" % (total/count))