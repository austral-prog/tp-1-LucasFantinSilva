def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    avarage=(nota1+nota2+nota3)/3
    nota_max=max(nota1,nota2,nota3)
    nota_min=min(nota1,nota2,nota3)
    faltan=10-avarage
    print(avarage)
    print(nota_max)
    print(nota_min)
    print(faltan)
grades()