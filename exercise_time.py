def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas= total_segundos//3600
    horas_reales= total_segundos/3600
    minutos_reales=(horas_reales-horas)*60
    minutos=int(minutos_reales)
    segundos=(minutos_reales-minutos)*60//1+1
    print(horas)
    print(minutos)
    print(int(segundos))
time()
