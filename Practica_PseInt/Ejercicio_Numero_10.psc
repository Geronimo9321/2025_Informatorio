Algoritmo Verificar_Contrasena
	Definir contrasena_Guardada, contrasena_Ingresada Como Caracter
	
	contrasena_Guardada <- "1234"
	
	Escribir "Ingresar contraseņa: "
	Leer contrasena_Ingresada
	
	Si contrasena_Ingresada = contrasena_Guardada Entonces
		Escribir "Contraseņa correcta. Bienvenido."
	SiNo
		Escribir "Contraseņa incorrecta. Algo salio mal."
	FinSi
FinAlgoritmo
