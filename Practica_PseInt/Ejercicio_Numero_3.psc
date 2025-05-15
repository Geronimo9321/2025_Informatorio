Algoritmo SumaDeNumero
	
	Definir numero, contador, suma Como Entero
	suma <- 0
	
	Escribir "Ingresar un número: "
	Leer numero
	
	Si numero <= 0 Entonces
		numero <- 10
	FinSi
	
	Para contador <- 1 Hasta numero Con Paso 1 Hacer
		suma <- suma + contador
	FinPara
	
	Escribir "La suma de los números desde 1 hasta ", numero, " es: "
FinAlgoritmo
