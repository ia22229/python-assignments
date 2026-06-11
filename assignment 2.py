unit = int(input("Enter the number of units consumed : "))
if unit <= 100 :
    bill = 0
elif unit <= 200 :
    bill = (unit - 100) * 2
elif unit <= 300 :
    100 * 2 + (unit - 200) * 4
elif unit <= 400 :
    bill = 100 * 2 + 100 * 4 + (unit - 300) * 6
elif unit <= 500 :
    bill = 100 * 2 + 100 * 4 + 100 * 6 + (unit - 400) * 8
else :
    bill = 100 * 2 + 100 * 4 + 100 * 6 + 100 * 8 + (unit - 500) * 10
print("Your electricity bill is : ", bill)


km = float(input("Enter the distance in kilometers : "))
if km <= 10 :
    fare = km * 110
elif km <= 90 :
    fare = 10 * 110 + (km - 10) * 100
elif km <= 140 :
    fare = 10 * 110 + 80 * 100 + (km - 90) * 70
else :
    fare = 10 * 110 + 80 * 100 + 50 * 70 + (km - 140) * 50
print("Your taxi fare is : ", fare)


current_salary = int(input("Please enter the current salary : "))
experience = int(input("Please enter the years of experience : "))
if experience >= 20 :
    bonus = current_salary * .2
elif experience >= 15 :
    bonus = current_salary * .17
elif experience >=  10 :
    bonus = current_salary * .12
elif experience >= 5 :
    bonus = current_salary * .08
elif experience >= 2 :
    bonus = current_salary * .03
else :
    bonus = 0
print("The bonus amount is : ", bonus)
net_salary = current_salary + bonus
print("The net salary is : ", net_salary)
