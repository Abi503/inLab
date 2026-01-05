
basic = float(input("Enter Basic Salary: "))


hra = 0.20 * basic
da = 0.10 * basic


gross_salary = basic + hra + da


tax = 0.05 * gross_salary


net_salary = gross_salary - tax


print("Basic Salary:", basic)
print("HRA (20%):", hra)
print("DA (10%):", da)
print("Gross Salary:", gross_salary)
print("Tax (5%):", tax)
print("Net Salary:", net_salary)
