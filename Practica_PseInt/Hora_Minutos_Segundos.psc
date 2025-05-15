Algoritmo HoraMinutoSegundo
	
	Definir totalSegundos, horas, minutos, segundos, resto Como Entero
	
	Escribir "Ingrese la cantidad total de segundos: "
	Leer totalSegundos
	
	horas <- trunc(totalSegundos / 3600)
	resto <- totalSegundos % 3600
	
	minutos <- trunc(resto / 60)
	segundos <- resto % 60
	
	Escribir "Equivale a: ", horas, " hora(s), ", minutos, " minuto(s), ", segundos, " segundo(s)." 
FinAlgoritmo
