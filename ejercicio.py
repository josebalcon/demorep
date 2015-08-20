a = 1
acumulador = 0 
contador = 0

while a == 1:
	notas = int(input("Ingresa tus notas (presiona 0 para promediar) :"))

	if notas > 0:
		acumulador = acumulador + notas 
		contador = contador + 1

	elif notas <= 0:
		a += 1
		promedio = acumulador/contador

		print promedio