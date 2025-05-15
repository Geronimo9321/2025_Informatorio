Algoritmo Verificar_Contrasena
	Definir contrasena_Guardada, contrasena_Ingresada Como Caracter
	
	contrasena_Guardada <- "1234"
	
	Escribir "Ingresar contraseña: "
	Leer contrasena_Ingresada
	
	Si contrasena_Ingresada = contrasena_Guardada Entonces
		Escribir "Contraseña correcta. Bienvenido."
	SiNo
		Escribir "Contraseña incorrecta. Algo salio mal."
	FinSi
FinAlgoritmo
