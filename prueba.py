
def mezclar_arreglos(arr1, arr2):
    arreglo_respuesta = []
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            arreglo_respuesta = arreglo_respuesta + [arr1[i]]
            arreglo_respuesta = arreglo_respuesta + [arr2[i]]
    elif len(arr1) > len(arr2):
        for i in range(len(arr1)):
            if i < len(arr2):
                arreglo_respuesta = arreglo_respuesta + [arr1[i]]
                arreglo_respuesta = arreglo_respuesta + [arr2[i]]
            else:
                arreglo_respuesta = arreglo_respuesta + [arr1[i]]
    else:
        for i in range(len(arr2)):
            if i < len(arr1):
                arreglo_respuesta = arreglo_respuesta + [arr1[i]]
                arreglo_respuesta = arreglo_respuesta + [arr2[i]]
            else:
                arreglo_respuesta = arreglo_respuesta + [arr2[i]]
            
    print(arreglo_respuesta)

mezclar_arreglos(["a", "b", "c", "d"], [1, 2, 3])