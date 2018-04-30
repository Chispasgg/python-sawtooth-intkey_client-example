'''
Created on 26 abr. 2018

@author: chispasgg
'''
from IntKeyClient_v1_0 import IntKeyClient_v1_0
import time
from datetime import datetime

variable = str(datetime.now().strftime('%Y-%m-%d %H:%M'))
print(variable)
# private key file
keyfile = 'usuario.priv'
# sawtooth rest address 
url = 'http://127.0.0.1:8080'


def __mostrar_datos(ik_d):
    print('***********************************************************************************')
    print('Mostrando los datos')
    res = ik_d.list()
    print(res)
    print('***********************************************************************************')


if __name__ == '__main__':
    print('----------------------------------------------------------------------------------')
    print('Cliente intKey de Sawtooth para el master de informatica, "Introducción a Blockchain"')
    print('Autor:')
    print('    Patxi Galán-García')
    print('----------------------------------------------------------------------------------')
    
    print('  -> El archivo clave es: ' + str(keyfile))
    print('  -> El host al que nos conectamos: ' + str(url))
    print('==================================================================================')

    ik_d = IntKeyClient_v1_0(url, keyfile=keyfile)
#     time.sleep(5)
    __mostrar_datos(ik_d)
    
    print('==================================================================================')
    print(' Insertar la variable (' + variable + ') con el valor 1')
    for x in range(10000):
        res = ik_d.set(variable+str(x), 1)
    print(' Resultado:')
    print(res)
    print('==================================================================================')
#     time.sleep(5)
    __mostrar_datos(ik_d)
        
    print('==================================================================================')
    print(' Incrementar la variable (' + variable + ') con el valor 2')
    res = ik_d.inc(variable, 2)
    print(' Resultado:')
    print(res)
    print('==================================================================================')
#     time.sleep(5)
    __mostrar_datos(ik_d)
     
    print('==================================================================================')
    print(' Decrementar la variable (' + variable + ') con el valor 9')
    res = ik_d.dec(variable, 9)
    print(' Resultado:')
    print(res)
    print('==================================================================================')
#     time.sleep(5)
    __mostrar_datos(ik_d)
    
    print('FIN')
