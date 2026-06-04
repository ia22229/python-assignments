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