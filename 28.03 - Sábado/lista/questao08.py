import math

tempo = float(input('Insira o tempo: '))

horas = math.floor(tempo)
minutos = math.floor((tempo - horas) * 60)

print(f'Tempo: {horas} {'hora' if (horas == 1) else 'horas'} e {minutos} {'minuto' if (minutos == 1) else 'minutos'}.')