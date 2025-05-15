Algoritmo NumeroOperador
	
	Definir num1, num2, resultado Como Real
	Definir operador Como Caracter
	
	Escribir "Ingresar un número: "
	Leer num1
	
	Escribir "Ingresar otro número: "
	Leer num2
	
	Escribir "Ingresar el operador (+, -, *, /): "
	Leer operador
	
	Si operador = "+" Entonces
		resultado <- num1 + num2
		Escribir "El resultado es: ", resultado
	SiNo
		Si operador = "-" Entonces
			resultado <- num1 - num2
			Escribir "El resultado es: ", resultado
		SiNo
			Si operador = "*" Entonces
				resultado <- num1 * num2
				Escribir "El resultado es: ", resultado
			SiNo
				Si operador = "/" Entonces
					Si num2 <> 0 Entonces
						resultado <- num1 / num2
						Escribir "El resultado es: ", resultado
					SiNo
						Escribir "Error: No se puede dividir por cero."
					FinSi
				SiNo
					Escribir "Operador no válido."
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
