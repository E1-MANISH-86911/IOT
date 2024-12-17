#2) write a function to return compound interest
def compound_interest(p, r, t):
    a = p * (pow((1 + r / 100), t))
    ci = a - p
    return (ci)
p = (float)(input("Enter the value of principle: "))
r = (float)(input("Enter the value of rate: "))
t = (float)(input("Enter the value of time: "))
print(f"compound_interest: {compound_interest(p, r, t)}")