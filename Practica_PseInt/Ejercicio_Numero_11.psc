Algoritmo ContarDigitos
		Definir numero, digitos Como Entero
		
		Escribir "Ingresar un n�mero: "
		Leer numero  
		
		Si numero < 0 Entonces
			numero <- numero * (-1)
		FinSi
		
		digitos <- 0
		
		Si numero = 0 Entonces
			digitos <- 1
		Sino
			Mientras numero > 0 Hacer
				numero <- trunc(numero / 10)
				digitos <- digitos + 1
			FinMientras
		FinSi
		
		Escribir "El n�mero tiene ", digitos, " d�gito(s)."
	
FinAlgoritmo
