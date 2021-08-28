def main():
    #escribe tu código abajo de esta línea
    Peso = float(input("Peso en kg: "))
    Altura = float(input("Altura en m: "))

    if Peso > 0 and Altura > 0:
        Indice = Peso / Altura**2
        if Indice < 20:
            print("PESO BAJO")
        elif Indice >= 20 and Indice < 25:
            print("NORMAL")
        elif Indice >= 25 and Indice < 30:
            print("SOBREPESO")
        elif Indice >= 30 and Indice < 40:
            print("OBESIDAD")
        elif Indice >= 40:
            print("OBESIDAD MORBIDA")
    else:
        print("Revisa tus datos, alguno de ellos es erróneo.")

if __name__=='__main__':
    main()