Algoritmo Numero_Multiplo
	
	Definir numero, multiplicador, resultado Como Entero
	
	Escribir "Ingrese un número para ver su tabla de multiplicar: "
	Leer numero
	
	Para multiplicador <- 1 Hasta 10 Con Paso 1 Hacer
		resultado <- numero * multiplicador
		Escribir numero " x ", multiplicador, " = ", resultado
	FinPara
FinAlgoritmo
