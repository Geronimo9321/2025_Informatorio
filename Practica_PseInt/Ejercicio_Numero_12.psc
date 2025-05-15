Algoritmo Sumar_Negativo
	
	Definir numero, suma Como Entero
	
	suma <- 0
	
	Repetir
		Escribir "Ingresar un número: "
		Leer numero
		
		Si numero >= 0 Entonces
			suma <- suma + numero
		FinSi
		
	Hasta Que numero < 0
	
	Escribir "La suma total es: ", suma
FinAlgoritmo
