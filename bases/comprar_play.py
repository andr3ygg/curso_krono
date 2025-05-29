from time import sleep
cartera = 100
ingreso_mensual = 50
caprichos = 20
precio_play = 500
precio_calcetines = 100
mes = 0 # January
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
play_comprada = False
calcetines_comprados = False


while  play_comprada == False or calcetines_comprados == False:

    cartera += ingreso_mensual
    cartera -= caprichos
    if mes == 12:
        mes = 0
    #print(f"Estamos en el mes: {meses[mes]}")
    mes += 1

    if play_comprada == False:
        if cartera >= precio_play:
            cartera -= precio_play
            play_comprada = True
            print("Play comprada")
            sleep(1)
            print(f"Mes: {meses[mes]}")
            sleep(1)
            print(f"Dinero restante: {cartera}")
            sleep(1)
            print(f"Ahora hay que ahorrar {precio_calcetines-cartera} para comprar los calcetines")
            sleep(3)


    # SI queremos comprar los calcetines, ejecutar. Sino, entonces remover la linea 33-38 y línea 23
    if play_comprada == True:
        if cartera >= precio_calcetines:
            cartera -= precio_calcetines
            calcetines_comprados = True
            print("Calcetines comprados")
            sleep(1)
            print(f"Mes: {meses[mes]}")
            sleep(1)
            print(f"Dinero restante: {cartera}")

        #else:
            #print("Hay que seguir ahorrando para los calcetines")

        
        
        
    #print(f"Dinero ingresado. Total: {dinero}")
    #print(f"Dinero despues de caprichos: {dinero}")
    
    
