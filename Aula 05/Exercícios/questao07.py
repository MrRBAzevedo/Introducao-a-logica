salario = float(input("Digite o salário bruto: "))

salario = salario * 0.89

if salario <= 2000:
   pass
elif salario <= 5000:
   salario = salario * 0.85
else:
   salario = salario * 0.725

print(f"Salário líquido: R$ {salario:.2f}")
