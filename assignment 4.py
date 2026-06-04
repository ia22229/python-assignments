current_salary = int(input("Please enter the current salary : "))
if current_salary < 10000 :
    tax = 0
elif current_salary < 15000 :
    tax = current_salary * 0.05
elif current_salary < 20000 :
    tax = current_salary * 0.1
elif current_salary < 30000 :
    tax = current_salary * 0.15
else :
    tax = current_salary * 0.18
print("The tax amount is : ", tax)
net_salary = current_salary - tax
print("The net salary is : ", net_salary)