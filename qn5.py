# Accept basic salary
basic = float(input("Enter Basic Salary: "))

# Calculate HRA and DA
hra = 0.20 * basic
da = 0.10 * basic

# Calculate total (gross) salary
gross_salary = basic + hra + da

# Calculate tax
tax = 0.05 * gross_salary

# Calculate net salary
net_salary = gross_salary - tax

# Display results
print("Basic Salary:", basic)
print("HRA (20%):", hra)
print("DA (10%):", da)
print("Gross Salary:", gross_salary)
print("Tax (5%):", tax)
print("Net Salary:", net_salary)
