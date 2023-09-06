# Qst 3

# Caso A seja informado como 0 -> A = 0 
def funçao():

    a = int(input("Diga o valor de A: "))
    if a == 0:
        return "Diga um valor diferente"
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))

    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return "A equação não possuiu raizes reais"
    if delta > 0:
        x1 = ((-b + delta ** 0.5) / (2 * a))
        x2 = ((-b - delta ** 0.5) / (2 * a))
        return x1, x2
    if delta == 0:
        print("Essa equação só tem uma raiz real =", x1)
    else:
        print("Essa equação possuiu 2 raizes reais -> x1 =", x1, "x2 =", x2)

print(funçao())