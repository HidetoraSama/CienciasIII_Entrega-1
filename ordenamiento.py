import csv
from cola import Cola
from pila import Pila

datafile = open('infoLibros.csv', 'r')
datareader = csv.reader(datafile, delimiter = ';')
data = Cola()

for row in datareader:
	data.encolar(row)

#info = [list(i) for i in zip(*data)]

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
while (not titulos.es_vacia()):
	#Primer orden por titulos
	tempMin = min(titulos.items)

	cTitulo = titulos.desencolar()
	cAutor = autores.desencolar()
	cTematica = tematicas.desencolar()
	cPagina = paginas.desencolar()
	cEditorial = editoriales.desencolar()

	if (cTitulo != tempMin):
		titulos.encolar(cTitulo)
		autores.encolar(cAutor)
		tematicas.encolar(cTematica)
		paginas.encolar(cPagina)
		editoriales.encolar(cEditorial)
	else:
		res.encolar([tempMin, cAutor, cTematica, cPagina, cEditorial])

#print(resR1.items)

print('-------------------Original-------------------')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data.items]))

print('\n--------------------Orden 1-------------------')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in res.items]))