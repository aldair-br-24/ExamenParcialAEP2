cantidad = int(input("¿Cuantos productos va a registrar?"))

lista = []

for i in range (cantidad):
    num = str(i + 1)
    nombre =input("ingrese el nombre del producto" + num + ":")
    precio =float(input("igrese el precio del producto " + num + ":"))
    categoria = input("Ingrese la categoria del producto" + num + ":")

    producto = [nombre, precio, categoria]
    lista.append(producto)

print(lista)

#cantidad de productos en el catálogo
print(len(lista)) #print(cantidad)

#precio promedio del catálogo
suma = 0
for producto in lista:
    suma = suma + producto[1]
promedio = suma/cantidad
print("el precio promedio es: ", promedio)
#cantidad de productos a superar el precio promedio del catalogo
contador = 0
for producto in lista:
    if producto[1]> promedio:
        contador =contador + 1
print("cantidad de productos quue superan el precio promedio:", contador)

#producto más caro
mas_caro= lista[0]
for producto in lista:
    if producto[1] > mas_caro[1]:
        mas_caro=producto
print("El producto más caro es: ", mas_caro)

#producot más barato
mas_barato= lista[0]
for producto in lista:
    if producto[1] < mas_barato[1]:
        mas_barato=producto
print("El producto más barato es: ", mas_barato)

#Categoria con más productos
categorias = []
cantidades = []

for p in lista:
    categoria=p[2]
    if categorias.count(categoria)== 0:
        categorias.append(categoria)
        cantidades.append(0)
    else:
        pos = categorias.index(categoria)
        cantidades[pos] = cantidades[pos] + 1

num_mas_alto = max(cantidades)
pos_num_mas_alto = cantidades.index(num_mas_alto)
categoria_con_mas_productos = categorias[pos_num_mas_alto]

print("Categoria con más productos:", categoria_con_mas_productos)