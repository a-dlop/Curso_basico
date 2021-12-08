# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:34:11 2021

@author: Daniel
"""
"""
This is the LifeStore_SalesList data:
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
from lifestore_file import lifestore_products,lifestore_sales,lifestore_searches


"---------------------id_producto+nombre_producto----------------------------"
nombre_producto=[(product[0],product[1]) for product in lifestore_products]#lista con nombre e id de producto
precios_por_id=[(item[1],item[2]) for item in lifestore_products] #lista con id_product y precio del producto



"---------------------id_categoria_producto----------------------------------"



id_categorias=[(product[0],product[3]) for product in lifestore_products] #Lista con las categorias e id
categorias_productos=[product[3] for product in lifestore_products] #Extracción de las categorias de los productos
nombre_categorias=[]
for categoria in categorias_productos: #Bucle para hallar el nombre de todas las categorias en el grupo
    if categoria not in nombre_categorias:
        nombre_categorias.append(categoria)
conteo_categorias=[(nombre,categorias_productos.count(nombre)) for nombre in nombre_categorias] #Lista con el nombre y numero productos dentro de esa categoria 
id_categoria_producto=[] #Lista para guardar en duplas el nombre de la categoria y los id_product que pertenecen a ella
for categoria in nombre_categorias:
    lista=[]
    for entrada in lifestore_products:
        if entrada[3]==categoria:
            lista.append(entrada[0])
    id_categoria_producto.append((categoria,lista)) #Creacion de una lista con duplas que tiene como primer entrada el tipo de producto y la segunda una lista con todos los productos que son de ese tipo

       


"----------------------------Productos mas vendidos y buscados en general------------------------------------------------------"    
venta_producto=[product[1] for product in lifestore_sales] #Extraccion ids de productos de la lista de ventas
numero_ventas=sorted([(i,[venta for venta in venta_producto].count(i)) for i in range(len(lifestore_products))],key=lambda dupla:dupla[1] ,reverse=True)#creacion de lista de duplas que contienen el id y cuantas veces fueron vendidos ordenado
id_ventas_no_cero=[i for i in numero_ventas if i[1]>0]




"---------------------Busquedas------------------------------------------------------------------------------"



#numero_de_busquedas_por_producto=sorted([[busqueda[1] for busqueda in busquedas_ordenadas].count(i) for i in range(len(lifestore_products))])
busquedas_ordenadas=sorted(lifestore_searches,key=lambda dupla:dupla[1]) #Se ordenan los registros segun el id del producto
numero_busquedas=[[busqueda[1] for busqueda in busquedas_ordenadas].count(i) for i in range(len(lifestore_products))] #Conteo del numero de veces que un objeto ha sido buscado
id_producto=[product[0] for product in lifestore_products ]#lista con los id del producto
id_numdebusquedas=[(id_producto[i],numero_busquedas[i]) for i in range(len(numero_busquedas))] #duplas ordenadas de productos segun el numero de busquedas 
id_ordenado_busquedas=sorted(id_numdebusquedas,key=lambda dupla:dupla[1],reverse=True)#ordena de mayor a menor
id_productos_no_cero=[i for i in sorted(id_numdebusquedas,key=lambda dupla:dupla[1],reverse=True) if i[1]>0] #Dupla de productos que recibieron al menos una visita      



"--------------------productos mas buscados y vendidos en general----------------------------------------------------------"
"""print("Los productos mas buscados son:")
j=1
for i in id_productos_no_cero[0:5]:
    
    print(j,'.-',lifestore_products[i[0]-1][1]," con",i[1]," busquedas.")
    j+=1
j=1    
print("los productos mas vendidoss son:",)
for i in id_ventas_no_cero[0:6]:
    print(j,'.-',lifestore_products[i[0]-1][1],"con",i[1],'busquedas.')
    j+=1"""
    
"---------------------busquedas y ventas por categoria-----------------------"
id_busqueda_categoria=[] #lista para almacenar categorias y busquedas
for categoria in id_categoria_producto:
    ordenado=[busquedas for busquedas in id_ordenado_busquedas if busquedas[0] in categoria[1]   ]
    id_busqueda_categoria.append((categoria[0],ordenado))

id_venta_categoria=[]#lista para almacenar categorias y ventas
for categoria in id_categoria_producto:
    ventas=[venta for venta in numero_ventas if venta[0] in categoria[1]] #Crea lista con el numero de productos y su categoria
    id_venta_categoria.append((categoria[0],ventas))    

"-------------------------------imprimir las categorias menor venta --------------------------"
"""for i in range(len(id_venta_categoria)):
   print(id_venta_categoria[i][0],'\n')
   if len(id_venta_categoria[i][1])<5:
       for j in range(len(id_venta_categoria[i][1])): 
        print(j+1,'.- ',nombre_producto[id_venta_categoria[i][1][-j][0]-1][1])
   else:
       for j in range(1,6):
           print(j,'.-',nombre_producto[id_venta_categoria[i][1][-j][0]-1][1])"""

"-----------------------------imprimir las categorias de menor busqueda-----------------------------------"

"""for i in range(len(id_busqueda_categoria)):
    print(id_busqueda_categoria[i][0],'\n')
    if len(id_busqueda_categoria[i][1])<10:
        for j in range(len(id_busqueda_categoria[i][1])):
            print(j+1,'.-',nombre_producto[id_busqueda_categoria[i][1][-j][0]-1][1])
    else:
        for j in range(1,11):
            print(j,' .-', nombre_producto[id_busqueda_categoria[i][1][-j][0]-1][1])"""
"--------------------Ventas por fecha---------------------------------------"


nombre_mes=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
z=[(int(venta[3][3:5]),venta[1]) for venta in lifestore_sales] #Dupla (mes de compra, id_producto)
ordenado=sorted(z,key=lambda dupla:dupla[0]) #ordena listas de duplas segun el mes (la entrada 0 de cada dupla)
numero_de_ventas_por_mes=[[elemento[0] for elemento in ordenado].count(i) for i in range(1,13)]
ganancias_por_mes=[]
mes_menores_ventas=[i for i, j in enumerate(numero_de_ventas_por_mes) if j == min(numero_de_ventas_por_mes)]
mes_mayores_ventas=[i for i, j in enumerate(numero_de_ventas_por_mes) if j == max(numero_de_ventas_por_mes)]
for i in range(1,13):
    ventas=0
    for elemento in ordenado:
        if elemento[0]==i :
            ventas+=precios_por_id[elemento[1]-1][1]
    ganancias_por_mes.append(ventas)



"--------------------Mejor y peor calificados--------------------------------------------------"   
calificados=sorted([(sales[1],sales[2]) for sales in lifestore_sales], key= lambda dupla:dupla[1])    




"-------------------login------------------------------------------------------"
if __name__ == "__main__":
    # Definamos nuestro usuario y nuestra contraseña aquí.
    # Estas son secreto del programa, las personas que no
    # hayan leído el código no deberían saberlas.
    USUARIO = 'Dan'
    CONTRASENA = 'gatitos'

    #  Definamos aqui la cantidad de intentos permitidos
    INTENTOS = 3

    # Vamos a controlar la cantidad de repeticiones
    # dentro del ciclo usando nuestra variable 'intentos',
    # nuestras condiciones de escape son 2:
    #  * que se termine la cantidad de intentos posibles
    #  * que acceda correctamente
    #
    # Usar un ciclo while, con la condicion True
    # como se ejemplifica debajo, puede causar un bucle
    # infinito si no tiene una instruccion de salida.
    # En este ejemplo vamos a usar break y exit().
    while True:
        # Antes de dejarle intentar, veamos si tiene intentos
        if INTENTOS == 0:
            # En caso de que no tenga intentos, terminaremos
            # con el programa
            exit()
        username = input('Ingrese su nombre de usuario:\n > ')
        password = input('Ingrese la contraseña:\n > ')
        # revisemos si son correctos
        if username == USUARIO:
        # En este punto, la persona ingreso correctamente
        # el usuario, comprobemos la contraseña ahora.
            if password == CONTRASENA:
                # Llegado a este punto, el ciclo puede terminar
                # la persona ingreso correctamente usuario y
                # contrasena
                break
        else:
            # En caso de que el usuario no sea correcto,
            # no hace falta ya comprobar la contrasena.
            # Le restamos un intento directamente y le hacemos
            # saber sobre su error, y la cantidad de intentos
            # restantes.
            INTENTOS = INTENTOS - 1
            # \n significa salto de linea, aqui la usamos para
            # mostrar el mensaje entre dos lineas blancas en consola.
            # la variable INTENTOS esta entre llaves, para imprimirla
            # en esa parte del mensaje, lo hacemos variable
            # porque en cada iteracion, el numero se ira restando,
            # y asi tenemos un mensaje personalizado cada vez
            # la f al inicio es un requisito para poder utilizar
            # el formato de una variable entre llaves {}
            print(f'\n!! Usuario/Contraseña incorrecto(s), {INTENTOS} restantes !!\n')
    # El programa llegara a este punto unicamente si la persona
    # pudo ingresar correctamente usuario y contrasena, a partir de
    # aqui, el programa queda a salvo de intrusos.
    print(f"\n\n\nBienvenido! {USUARIO}")
    
    
"-----------------------------Menu de solicitud de productos------------------------------------------"
print("Bienvenido a LifeStore, ¿que informacion desea revisar?") #Impresion y obtención de datos del usuario
actividades=["1-Productos mas buscado (en general)",
             "2-Productos menos buscado (por categoria)",
             "3-Productos mas vendido(en general)",
             "4-Productos menos vendido (por categoria)",
             "5-Productos mejor calificados",
             "6-Productos peor calificados" ,
             "7.-Total de ingreso y ventas promedio anuales",
             "8.-Total anual y meses con mas ventas"]
for actividad in actividades:
    print(actividad)
#Lectura de actividad
loop='true'
i=0
while (loop=='true'): #Seguira funcionando y pidiendo una opción hasta recibir una respuesta valida
    actividad=input("Por favor escriba la opcion: ")
    i=0 #Variable de conteo para solo revisar las 8 opciones  y en caso de que i>8 pedir una nueva opción
    for num in range(1,9):
        if actividad == str(num) and i<=8:
            loop='False'
            i=i+1
    if i>8:    
        print("Opcion no valida, escriba de nuevo  la opcion")
                    
actividad=int(actividad)   
print("Usted eligio:",actividades[actividad-1]) #Escritura de la opción elegida
    
if actividad==1:
    print("Los productos mas buscados son:")
    j=1
    for i in id_productos_no_cero[0:5]:
    
        print(j,'.-',lifestore_products[i[0]-1][1]," con",i[1]," busquedas.")
        j+=1
    j=1    
if actividad==2:
    "-------------------------------imprimir las categorias menor busqueda --------------------------"
    print("Los productos con menores busquedas por categoria son:\n")
    for i in range(len(id_busqueda_categoria)):
        print(id_busqueda_categoria[i][0],'\n')
        if len(id_busqueda_categoria[i][1])<10:
            for j in range(len(id_busqueda_categoria[i][1])):
                print(j+1,'.-',nombre_producto[id_busqueda_categoria[i][1][-j][0]-1][1])
        else:
            for j in range(1,11):
                print(j,' .-', nombre_producto[id_busqueda_categoria[i][1][-j][0]-1][1])

    
if actividad==3:
    print("los productos mas vendidos son:\n",)
    j=1
    for i in id_ventas_no_cero[0:5]:
        print(j,'.-',lifestore_products[i[0]-1][1],"con",i[1],'busquedas.')
        j+=1
if actividad==4:
    "----------------------------imprimir los productos con menores ventas........................"
    print("Los productos con menores ventas por categoria son:\n")
    for i in range(len(id_venta_categoria)):
        
       print(id_venta_categoria[i][0],'\n')
       if len(id_venta_categoria[i][1])<5:
           for j in range(len(id_venta_categoria[i][1])): #Excepcion en caso de que la lista tenga menos de 5 entradas
            print(j+1,'.- ',nombre_producto[id_venta_categoria[i][1][-j][0]-1][1]) #Imprime los valores con menores ventas, por eso uso el -j
       else:
           for j in range(1,6):
               print(j,'.-',nombre_producto[id_venta_categoria[i][1][-j][0]-1][1])
    
if actividad==5:
    print("Los productos mejor calificados son:") #De una lista donde se ordenaron las entradas por la calificacion
    for i in range(5):
       print(i+1,'.-',nombre_producto[calificados[i][0]-1][1])  #Se imprimen los 5 primeros
if actividad ==6:
    print("productos peor calificados")#DE LA LISTA CALIFICACIONES SE IMPRIMEN LOS ULTIMOS 5
    for i in range(5):
        print(i+1,'.-',nombre_producto[calificados[-i+1][0]-1][1])
if actividad==7:
    print("El total de ingresos anual es de",sum(ganancias_por_mes))
    print("Las ventas promedio por mes es",round(len(ordenado)/12,2),"ventas por mes")
if actividad==8:
    print("Los meses con peores ventas fueron",nombre_mes[mes_menores_ventas[0]],"y",nombre_mes[mes_menores_ventas[1]])
    print("El mes con mayores ventas fue",nombre_mes[mes_mayores_ventas[0]-1])
