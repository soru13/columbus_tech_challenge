# plain_data.py
"""
    Dado el array de enteros que se pase ocmo parametro, simplemente cae en un ciclo donde se válida que
    sea un array, mientras sea un array continuara en el ciclo mientras los valores se van guardando
    en un array nuevo para despues mostrarlos o ordenarlos si se desea.
"""
#para limpiar el arreglo y empezar con otra prueba o arreglo numerico
import string
from turtle import clear
#lista donde se van almacenando los valores a motrar como resultado
arreglo_plano_de_enteros = []


#Se resolvio por recursividad hasta terminar
def plain_data(arreglo_de_numeros):

    for valor in arreglo_de_numeros:
        if isinstance(valor,list):
            plain_data(valor)
        else:
            if isinstance(valor,int):
                arreglo_plano_de_enteros.append(valor)
            else:
                print("solo numeros")
                break

#envolvemos la función recursiva para retornar el valor
def run(arreglo_de_numeros):
    #inicializamos
    arreglo_plano_de_enteros.clear()
    plain_data(arreglo_de_numeros)
    print(arreglo_plano_de_enteros)
    return arreglo_plano_de_enteros

#Pruebas para validar el resultado
#en lugar de hacer tres funciones identicas para cada caso mejor una sola y mandamos por parametros
import pytest
#decorador según la documentación para pasar los casos como parametros y lo que esperamos
@pytest.mark.parametrize('a, exp',
[
    ([1, [2, [3, [4, 5]]]],[1, 2, 3, 4, 5]),
    ([6, [1, [2, 3], 4], 5], [6, 1, 2, 3, 4, 5]),
    ([[[1, 2,], 3], 4, 5], [1, 2, 3, 4, 5]),
])
def test_casos(a,exp):
    result = run(a)
    assert result == exp

# main.py
if __name__ == '__main__':
    #puedes poner el arreglo que gustes
    test = ['r',2,'t',{}, [45,20],4,5, [2, [3, [4, 5,5]]]]
    test1 = [1, [2, [3, [4, 5]]]]
    test2 = [6, [1, [2, 3], 4], 5]
    test3 = [[[1, 2,], 3], 4, 5]
    run(test)
