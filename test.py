#En caso de querer usar .format para introducir variables entre los corchetes dentro del print o donde sea que lo necesites.
texto = "Hola, me llamo Miti y tengo {1} años. Mi compañero es {0}" 
contador = 100
palabra = "jaume"
#print(texto.format(contador,palabra))

#Con .center puedes centrar un string donde quieras, se puede hacer hasta a pelo, sin utilizar variables.
#print("uwu".center(150))

#Con .count devuelve el número de veces que valor concreto ocurre en un string
#print(texto.count("o"))

ejemplo = "Jajajajaj eres muy graciosete no? Bobo."

#print(ejemplo.endswith("Bobo.")) #Permite ver si el string acaba con un determinado valor, devuelve un booleano.

lista = list(ejemplo) #Se utiliza el constructor cuando queremos separar todo, si se usa una lista normal puedes meter más strings
lista2 = ["Hola", "Mundo"]
print(lista.count('a')) #De esta forma haces un contador de las veces que se repite X en un string.
#print(lista2)
        

