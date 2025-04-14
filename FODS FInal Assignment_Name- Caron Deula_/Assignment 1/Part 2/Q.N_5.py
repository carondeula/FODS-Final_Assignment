
# Taking input from the user
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (in %): "))
t = float(input("Enter the time period (in years): "))

simple_interest = (p * r * t) / 100
print(f"Simple Interest: {simple_interest}")
