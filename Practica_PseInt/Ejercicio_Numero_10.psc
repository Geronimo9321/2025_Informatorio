Algoritmo Verificar_Contrasena
	Definir contrasena_Guardada, contrasena_Ingresada Como Caracter
	
	contrasena_Guardada <- "1234"
	
	Escribir "Ingresar contrase�a: "
	Leer contrasena_Ingresada
	
	Si contrasena_Ingresada = contrasena_Guardada Entonces
		Escribir "Contrase�a correcta. Bienvenido."
	SiNo
		Escribir "Contrase�a incorrecta. Algo salio mal."
	FinSi
FinAlgoritmo
