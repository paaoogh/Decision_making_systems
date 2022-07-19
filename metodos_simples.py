def optimistic(dic): #maximax
    better_values = []
    for i in dic.values():
        opcion = dic.keys()[dic.values().index(i)]

        big = max(i)
        indice = i.index(big)
        better_values.append(big,indice,opcion)

    biggest_value = max(better_values,key=lambda item:item[0])
    value = biggest_value[0]
    ind = biggest_value[1]
    option = biggest_value[2]
    return value,ind,option

def optimistic_min(dic): #minimin
    opcion = dic.keys()[dic.values().index(i)]

    better_values = []
    for i in dic.values():
        big = min(i)
        indice = i.index(big)
        better_values.append(big,indice,opcion)

    biggest_value = min(better_values,key=lambda item:item[0])
    value = biggest_value[0]
    ind = biggest_value[1]
    option = biggest_value[2]
    return value,ind,option

def conservador_maximizar(dic): #maximin
    opcion = dic.keys()[dic.values().index(i)]

    better_values = []
    for i in dic.values():
        big = max(i)
        indice = i.index(big)
        better_values.append(big,indice,opcion)

    biggest_value = min(better_values,key=lambda item:item[0])
    value = biggest_value[0]
    ind = biggest_value[1]
    option = biggest_value[2]
    return value,ind,option

def conservador_minimizar(dic): #minimax
    opcion = dic.keys()[dic.values().index(i)]

    better_values = []
    for i in dic.values():
        big = min(i)
        indice = i.index(big)
        better_values.append(big,indice,opcion)

    biggest_value = max(better_values,key=lambda item:item[0])
    value = biggest_value[0]
    ind = biggest_value[1]
    option = biggest_value[2]
    return value,ind,option


opciones = list(map(str,input().split()))
dic = {}
for i in opciones:
    valores = list(map(float,input().split()))
    dic[i] = valores

metodo = int(input('Seleccione el tiempo de método: 1-optimista 2-optimista de minimin  3-convervador_maximizar 4-conservador_minimizar'))
if metodo == 1:
    valor,opcion,x = optimistic(dic)
elif metodo == 2:
    valor,opcion,x = optimistic_min(dic)
elif metodo == 3:
    valor,opcion,x = conservador_maximizar(dic)
elif metodo == 4:
    valor,opcion,x = conservador_minimizar(dic)

print("La opción más viable es: ",x)
print("Puede dar el valor ",valor)