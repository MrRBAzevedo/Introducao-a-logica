tempo = 0
tipo_anterior = '0'
amigos = []
n = int(input())

for i in range(n):
    tipo, amigo = input().split()
    amigo = int(amigo)

    if tipo == 'R':
        
        found = False
        for a in amigos:
            if a['nome'] == amigo:
                found = True
                a['R'] = tempo
                a['respondida'] = False

        if not found:
            a = {'nome' : amigo, 'R' : tempo, 'T' : 0, 'respondida' : False}
            amigos.append(a)

        tempo += 1

    elif tipo == 'E':
        
        for a in amigos:
            if a['nome'] == amigo:
                dur = tempo - a['R']
                a['T'] += dur
                a['respondida'] = True

        tempo += 1

    elif tipo == 'T':
        if tipo_anterior in ['R', 'E']:
            tempo -= 1
        
        tempo += amigo

    tipo_anterior = tipo

amigos.sort(key=lambda d: d['nome'])

for a in amigos:
    if a['respondida'] == False:
        a['T'] = -1

    print(a['nome'], a['T'])

                
            
            
        

                