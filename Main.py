import csv
from cola import Cola

datafile = open('infoLibros.csv', 'r')
datareader = csv.reader(datafile, delimiter = ';')
data = Cola()

for row in datareader:
	data.encolar(row)

titulos = Cola()
for slist in data.items:
	titulos.encolar(slist[0])

autores = Cola()
for slist in data.items:
	autores.encolar(slist[1])

tematicas = Cola()
for slist in data.items:
	tematicas.encolar(slist[2])

paginas = Cola()
for slist in data.items:
	paginas.encolar(slist[3])

editoriales = Cola()
for slist in data.items:
	editoriales.encolar(slist[4])

res = Cola()
while (not tematicas.es_vacia()):
	#Primer orden por tematica
	tempMin = min(tematicas.items)

	cTitulo = titulos.desencolar()
	cAutor = autores.desencolar()
	cTematica = tematicas.desencolar()
	cPagina = paginas.desencolar()
	cEditorial = editoriales.desencolar()

	#Revisa si tematica en cabeza es el minimo
	if (cTematica != tempMin):#Si difiere pone los registros al final de la cola
		titulos.encolar(cTitulo)
		autores.encolar(cAutor)
		tematicas.encolar(cTematica)
		paginas.encolar(cPagina)
		editoriales.encolar(cEditorial)
	else:#Si no difiere se ubica en la cola del resultado
		res.encolar([cTitulo, cAutor, cTematica, cPagina, cEditorial])

titulos = Cola()
for i in range(0, len(res.items)):
	titulos.encolar(res.items[i][0])

autores = Cola()
for i in range(0, len(res.items)):
	autores.encolar(res.items[i][1])

tematicas = Cola()
for i in range(0, len(res.items)):
	tematicas.encolar(res.items[i][2])

paginas = Cola()
for i in range(0, len(res.items)):
	paginas.encolar(res.items[i][3])

editoriales = Cola()
for i in range(0, len(res.items)):
	editoriales.encolar(res.items[i][4])

resFinal = Cola()
resb = Cola()
#Segundo filtro por cantidad de paginas, sacado de las tematicas ya ordenadas
while (not tematicas.es_vacia()):
	#cola para almacenar los ordenamientos temporales

	cTitulo = titulos.desencolar()
	cAutor = autores.desencolar()
	cTematica = tematicas.desencolar()
	cPagina = paginas.desencolar()
	cEditorial = editoriales.desencolar()

	#Verifica iguales y los pasa a una nueva cola para ordenarlos
	if(not tematicas.es_vacia()):
		if (cTematica == tematicas.cabeza()):
			resb.encolar([cTitulo, cAutor, cTematica, cPagina, cEditorial])
		else:#Si difieren, se prepara para ordenar la actual resb y pasarla a resFinal
			print('\n')
			print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in resb.items]))
			resb = Cola()#setea una nueva lista para los siguientes en repetirse(si existen)

print('-------------------Original-------------------')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data.items]))

print('\n------------Orden por tematica--------------')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in res.items]))