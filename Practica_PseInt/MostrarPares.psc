Proceso MostrarParesOImpares
    Definir i, opcion Como Entero
	
    Escribir "Ingrese una opci�n:"
    Escribir "1 - Mostrar n�meros impares del 1 al 100"
    Escribir "2 - Mostrar n�meros pares del 1 al 100"
    Leer opcion
	
    Si opcion = 1 Entonces
        Escribir "N�meros impares del 1 al 100:"
        Para i <- 1 Hasta 100 Con Paso 1 Hacer
            Si i % 2 <> 0 Entonces
                Escribir i
            FinSi
        FinPara
    Sino
        Si opcion = 2 Entonces
            Escribir "N�meros pares del 1 al 100:"
            Para i <- 1 Hasta 100 Con Paso 1 Hacer
                Si i % 2 = 0 Entonces
                    Escribir i
                FinSi
            FinPara
        Sino
            Escribir "Opci�n inv�lida. Debe ingresar 1 o 2."
        FinSi
    FinSi
FinProceso
