import subprocess
subprocess.run(['cls'], shell = True)

dh, mh, ah = map(int, input('Insira a data atual (dd/mm/aaaa): ').split('/'))
da, ma, aa = map(int, input('Insira a data do seu aniversário (dd/mm/aaaa): ').split('/'))

dias_h = dh + mh * 30
dias_a = da + ma * 30

if dias_h < dias_a:
    ah -= 1
    dias_h += 365

anos_idade = ah - aa
dias_idade = dias_h - dias_a

print(f'Você tem {dias_idade % 30} dias, {dias_idade // 30} meses e {anos_idade} anos de idade.')