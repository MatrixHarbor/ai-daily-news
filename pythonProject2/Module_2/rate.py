Principal = input("Principal: ")
Total = input("Total: ")
Term = input("Term: ")
Compound = input("Compound: ")
P = float(Principal)
A = float(Total)
t = int(Term)
n = int(Compound)

# this is another function
r = n * ((A / P)**(1/(n*t))-1) * 100
print(f"The interest rate on a 💲{P} CD that pays out 💲{A} \nover a {t} year term is {r}%")