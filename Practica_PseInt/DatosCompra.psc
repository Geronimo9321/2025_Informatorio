Algoritmo DatosCompra
    
    //Se desea comprar una PC y una impresora. Calcular el precio total: 
    //el cual está dado por la suma de los precios de costos, los porcentajes de ganancia del vendedor y un 21% de IVA. 
    //Supóngase una ganancia del vendedor del 12% por la PC y 7% por la impresora. 
    //Se leen los costos y se imprimen el precio total de ventas.
    
    Definir precio_PC Como Real
    Definir precio_IMP Como Real
    Definir Total Como Real
    
    Imprimir "ingrese el costo de la pc"
    Leer precio_PC
    Imprimir  "ingrese el costo de la impresora"
    Leer precio_IMP
    
    precio_PC := precio_PC * 1.12 
    // OTRA FORMA DE CALCULAR precio_PC := precio_PC + (precio_PC * 12/100)
    precio_PC := precio_PC * 1.21
    // OTRA FORMA DE CALCULAR precio_PC := precio_PC + (precio_PC * 21/100)
    precio_IMP := precio_IMP * 1.07
    precio_IMP := precio_IMP * 1.21
    
    Total := precio_IMP + precio_PC
    
    Imprimir  "El total a pagar es de: $" Total
    
FinAlgoritmo