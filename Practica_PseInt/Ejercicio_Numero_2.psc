Algoritmo Ejercicio_Numero_1
	
	Definir numero_1 Como Entero
	Definir numero_2 Como Entero
	
	Escribir "Ingresar el primer número: "
	Leer numero_1
	
	Escribir "Ingresar el segundo número: "
	Leer numero_2
	
	Si numero_1 > numero_2 Entonces
		Escribir "El mayor es: ", numero_1
		Escribir "El menor es: ", numero_2
	SiNo
		Si numero_2 > numero_1 Entonces
			Escribir "El mayor es: ", numero_2
			Escribir "El menor es: ", numero_1
		SiNo
			Escribir "Ambos números son iguales."
		FinSi
	FinSi
FinAlgoritmo
