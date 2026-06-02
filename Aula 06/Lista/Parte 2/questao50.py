cel = 0

while cel <= 100:
    fah = cel * (9/5) + 32
    kel = cel + 273.15
    
    if cel < 15:
        cla = 'frio'
    elif cel <= 25:
        cla = 'agradável'
    else:
        cla = 'quente'

    print(f'|    {str(cel).ljust(10)}|    {str(fah).ljust(10)}|   {str(kel).ljust(10)}|   {cla.ljust(12)}| ')

    cel += 10

