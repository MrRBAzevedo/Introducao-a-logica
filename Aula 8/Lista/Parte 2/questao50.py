for i in range(11):
    celsius = i * 10
    fahrenheit = celsius * (9/5) + 32
    kelvin = celsius + 273.15

    if celsius < 15:
        cla = 'frio'
    elif celsius <= 25:
        cla = 'agradável'
    else:
        cla = 'quente'

    print(f'|    {str(celsius).ljust(10)}|    {str(fahrenheit).ljust(10)}|   {str(kelvin).ljust(10)}|   {cla.ljust(12)}| ')