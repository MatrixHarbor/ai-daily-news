Principal = input("Principal: ")
rate = input("Rate: ")
term = input("Term: ")
compound = input("Compound: ")
# make the type of each variable an integer or float
P = int(Principal)
r = float(rate)
t = int(term)
n = int(compound)
A = P * (1 + r / n)**(n*t) # this is the function to compute
interest = A - P
# print(f"Principal: {P}")
# print(f"Rate: {r}")
# print(f"Term: {t}")
# print(f"Compound: {n}")
print(f"Investing 💲{P} in a CD with an {r*100}% interest rate for a term of {t} year\n(s) will earn 💲{interest} in interest for a total payout of 💲{A}")