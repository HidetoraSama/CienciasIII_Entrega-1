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
cTitulo = titulos.desencolar()
cAutor = autores.desencolar()
cTematica = tematicas.desencolar()
cPagina = paginas.desencolar()
cEditorial = editoriales.desencolar()

resb.encolar([cTitulo, cAutor, cTematica, cPagina, cEditorial])
#Separacion seccionada de los ordenamientos por tematica ya existentes
while (not tematicas.es_vacia()):

	#Se verifica si la cabeza es igual a lo ya agregado y se ponen todos en un do while
	if (tematicas.cabeza() == resb.cabeza()[2]):
		cTitulo = titulos.desencolar()
		cAutor = autores.desencolar()
		cTematica = tematicas.desencolar()
		cPagina = paginas.desencolar()
		cEditorial = editoriales.desencolar()

		resb.encolar([cTitulo, cAutor, cTematica, cPagina, cEditorial])
	else:#Si difieren, se prepara para ordenar la actual resb y pasarla a resFinal
		#####Ordenmiento de actual resb y pasarlo a resFinal##########
		temptitulos = Cola()
		for i in range(0, len(resb.items)):
			temptitulos.encolar(resb.items[i][0])

		tempautores = Cola()
		for i in range(0, len(resb.items)):
			tempautores.encolar(resb.items[i][1])

		temptematicas = Cola()
		for i in range(0, len(resb.items)):
			temptematicas.encolar(resb.items[i][2])

		temppaginas = Cola()
		for i in range(0, len(resb.items)):
			temppaginas.encolar(resb.items[i][3])

		tempeditoriales = Cola()
		for i in range(0, len(resb.items)):
			tempeditoriales.encolar(resb.items[i][4])

		while (not temppaginas.es_vacia()):
			#Segundo orden por paginas
			tempMin = min(temppaginas.items)

			tempcTitulo = temptitulos.desencolar()
			tempcAutor = tempautores.desencolar()
			tempcTematica = temptematicas.desencolar()
			tempcPagina = temppaginas.desencolar()
			tempcEditorial = tempeditoriales.desencolar()

			#Revisa si pagina en cabeza es el minimo
			if (tempcPagina != tempMin):#Si difiere pone los registros al final de la cola
				temptitulos.encolar(tempcTitulo)
				tempautores.encolar(tempcAutor)
				temptematicas.encolar(tempcTematica)
				temppaginas.encolar(tempcPagina)
				tempeditoriales.encolar(tempcEditorial)
			else:#Si no difiere se ubica en la cola del resultado
				resFinal.encolar([tempcTitulo, tempcAutor, tempcTematica, tempcPagina, tempcEditorial])
		###############


		resb = Cola()#setea una nueva lista para los siguientes en repetirse(si existen)
		cTitulo = titulos.desencolar()
		cAutor = autores.desencolar()
		cTematica = tematicas.desencolar()
		cPagina = paginas.desencolar()
		cEditorial = editoriales.desencolar()

		resb.encolar([cTitulo, cAutor, cTematica, cPagina, cEditorial])

temptitulos = Cola()
for i in range(0, len(resb.items)):
	temptitulos.encolar(resb.items[i][0])

tempautores = Cola()
for i in range(0, len(resb.items)):
	tempautores.encolar(resb.items[i][1])

temptematicas = Cola()
for i in range(0, len(resb.items)):
	temptematicas.encolar(resb.items[i][2])

temppaginas = Cola()
for i in range(0, len(resb.items)):
	temppaginas.encolar(resb.items[i][3])

tempeditoriales = Cola()
for i in range(0, len(resb.items)):
	tempeditoriales.encolar(resb.items[i][4])

while (not temppaginas.es_vacia()):
	#Segundo orden por paginas
	tempMin = min(temppaginas.items)

	tempcTitulo = temptitulos.desencolar()
	tempcAutor = tempautores.desencolar()
	tempcTematica = temptematicas.desencolar()
	tempcPagina = temppaginas.desencolar()
	tempcEditorial = tempeditoriales.desencolar()

	#Revisa si pagina en cabeza es el minimo
	if (tempcPagina != tempMin):#Si difiere pone los registros al final de la cola
		temptitulos.encolar(tempcTitulo)
		tempautores.encolar(tempcAutor)
		temptematicas.encolar(tempcTematica)
		temppaginas.encolar(tempcPagina)
		tempeditoriales.encolar(tempcEditorial)
	else:#Si no difiere se ubica en la cola del resultado
		resFinal.encolar([tempcTitulo, tempcAutor, tempcTematica, tempcPagina, tempcEditorial])
				
print('-------------------Original-------------------')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data.items]))

print('\n------------Orden por tematica--------------')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in res.items]))

print('\n-----------2do Orden por paginas------------')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in resFinal.items]))

with open("infoLibrosORDENADO.csv","w", newline='') as f:
    wr = csv.writer(f, delimiter=";")
    wr.writerows(resFinal.items)