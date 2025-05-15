Algoritmo Ejercicio_Promedio
	Definir nota_1, nota_2, nota_3, promedio Como Real
	
	Escribir "Ingresar nota: "
	Leer nota_1
	
	Escribir "Ingresar nota: "
	Leer nota_2
	
	Escribir "Ingresar nota: "
	Leer nota_3
	
	promedio <- (nota_1 + nota_2 + nota_3) / 3
	
	Escribir "El promedio es de: ", promedio
	
	Si promedio >= 6 Entonces
		Escribir "El estudiante aprueba."
	SiNo
		Escribir "El estudiante no aprueba."
	FinSi
FinAlgoritmo
