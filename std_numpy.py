import numpy as np 
import pandas as pd
# Carga el archivo de Excel en un DataFrame de Pandas
df = pd.read_excel('data.xlsx',sheet_name='Sheet1')
# comvierte los datos de una columuna de un dataFrame a una lista

#Se crea una función para pasar de listas a arreglo de numpy
def lis2np(colum):
  '''colum es el nombre de la columna del dataFrame '''
  aux=list(df[colum])
  return np.array(aux)

#Se crean los arreglos de numpy
id=lis2np('id')
edad=lis2np('edad')
Nivel_E=lis2np('nivel_edu')
ingreso=lis2np('ingreso_mensual')
categoria=lis2np('sex')
escolaridad=lis2np('anios_esc')


# print(edad)
# print(Nivel_E)
# print(ingreso)
# print(categoria)
# print(escolaridad)

cont1=0
cont2=0
for i in categoria:
  if i == 'Mujer':
    cont1+=1
  else:
    cont2+=1

neM=np.empty(cont1)
neH=np.empty(cont2)


con1=0
con2=0
for i in range(len(categoria)):
	if categoria[i]=='Mujer':
		if con1 <= len(neM)-1:
			neM[con1]=edad[i]
		con1+=1
	else:
		if con2 <= len(neH)-1:
			neH[con2]=edad[i]
		con2+=1
		

print(neM)
print('Tamaño arreglo edad Mujeres', len(neM))
print('-----------------------------')
print(neH)
print('Tamaño arreglo edad Hombres',len(neH))






