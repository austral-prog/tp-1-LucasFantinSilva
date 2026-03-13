def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12
    promedio=(num1+num2+num3+num4)/4
    num_max=max(num1,num2,num3,num4)
    num_min=min(num1,num2,num3,num4)
    rango=num_max-num_min
    print(promedio)
    print(num_max)
    print(num_min)
    print(rango)
statistics()