def currency():
    """
    Ejercicio 13 - Conversión de Moneda

    Dado un monto en pesos argentinos y tasas de cambio, imprimir:
    1. El monto en dólares
    2. El monto en euros
    3. El monto en reales brasileños
    """
    pesos = 10000
    tasa_dolar = 1500  # 1 dólar = 1500 pesos
    tasa_euro = 1600   # 1 euro = 1600 pesos
    tasa_real = 250    # 1 real = 250 pesos
    money_dolar=pesos/tasa_dolar
    money_euro=pesos/tasa_euro
    money_real=pesos/tasa_real
    print(money_dolar)
    print(money_euro)
    print(money_real)
#currency()