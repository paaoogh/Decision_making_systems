import pandas as pd

def tabla(dic):
    #Convertir a una tabla
    opciones_ = len(dic.keys())
    nombre_opciones = []
    for i in range(opciones_):
        nombre_opciones.append("Opcion "+ str(i+1))

    df = pd.DataFrame.from_dict(dic,orient='index')

    #Formato de tabla de tablas de resultados
    demandas = len(list(dic.values())[0])

    nombres = []
    for i in range(demandas):
        nombres.append("Demanda "+ str(i+1))
    df.columns = nombres
    return df


def arrepentimiento(df):
    opciones = {}
    valores_rij = {}
    for i in df.T.index: #OJO QUE TRANSPUSE para hacer posible el loc
        lista = list(df.T.loc[i])

        mejor_decision = max(lista)
        vals = []
        for j in lista:
            vals.append(mejor_decision - j) #Rij
        
        valores_rij[i] = vals
    
    new_df = pd.DataFrame.from_dict(valores_rij) #DataFrame de Rij ordenados OpcionesxDemanda
    maximos = {}
    for i in new_df.index:
        maximos[i] = max(new_df.iloc[i])
    
    maximos_ordenados = dict(sorted(maximos.items(), key=lambda item: item[1])) #Ordenar de menor a mayor
    mejor_opcion = list(maximos_ordenados.keys())[0]
    mejor_opcion_valor = list(maximos_ordenados.values())[0]

    return mejor_opcion,mejor_opcion_valor

if __name__ == "__main__":
    options = list(map(str,input("Introducir opciones de complejos").split())) #complejo d1, d2, d3

    dic = {}
    for i in options:
        valores = list(map(float,input().split())) #Demanda fuerte y demanda debil 
        nombre = "Opcion "+ str(i)
        dic[nombre] = valores

    tabla_ar = tabla(dic)
    opcion,valor = arrepentimiento(tabla_ar)

    print("Mejor opcion con enfoque de arrepentiento es la opcion " + str(opcion+1) + " con valor potencial de " + str(valor))