Algoritmo PalabraInvertida
	
	Definir palabra, palabra_invertida Como Caracter
	Definir i Como Entero
	
	Escribir "Ingresar una palabra: "
	Leer palabra
	
	palabra_invertida <- ""
	
	Para i <- Longitud(palabra) Hasta 1 Con Paso -1
		palabra_invertida <- palabra_invertida + Subcadena(palabra, i, i)
	FinPara
	
	Escribir "La palabra al revés es: ", palabra_invertida
FinAlgoritmo
