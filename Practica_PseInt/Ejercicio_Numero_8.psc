Algoritmo Ejercicio_Factorial
	Definir numero, factorial, contador Como Entero
	
	Escribir "Ingresar un n�mero entero: "
	Leer numero
	
	Si numero < 0 Entonces
		Escribir "No se puede calcular el factorial de un n�mero negativo."
	SiNo
		factorial <- 1 
		Para contador <- 1 Hasta numero Con Paso 1
			factorial <- factorial * contador
		FinPara
		
		Escribir "El factorial de ", numero, " es: ", factorial
	FinSi
FinAlgoritmo
