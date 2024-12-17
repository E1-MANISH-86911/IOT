#Write a function to return simple interest

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return float(si)
p = float(input("Enter the value of principle: "))
r = float(input("Enter the value of rate: "))
t = float(input("Enter the value of time: "))
print(f"Simple interest: {simple_interest(p, r, t)}")