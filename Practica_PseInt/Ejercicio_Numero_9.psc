Algoritmo Ejercicio_MayorDe5
	Definir num_1, num_2, num_3, num_4, num_5, mayor Como Entero
	
	Escribir "Ingresar un número Aleatorio: "
	Leer num_1
	mayor <- num_1
	
	Escribir "Ingresar un número Aleatorio: "
	Leer num_2
	Si num_2 > mayor Entonces
		mayor <- num_2
	FinSi
	
	Escribir "Ingresar un número Aleatorio: "
	Leer num_3
	Si num_3 > mayor Entonces
		mayor <- num_3
	FinSi
	
	Escribir "Ingresar un número Aleatorio: "
	Leer num_4
	Si num_4 > mayor Entonces
		mayor <- num_4
	FinSi
	
	Escribir "Ingresar un número Aleatorio: "
	Leer num_5
	Si num_5 > mayor Entonces
		mayor <- num_5
	FinSi
	
	Escribir "El número mayor es: ", mayor
FinAlgoritmo
