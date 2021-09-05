import numpy as np
import pandas as pd
import copy

idades = np.array([10,15,20,18,20])
notas = np.array([9,8,5,7,10])

# print(notas[idades==20])
# print(np.mean(idades))

tabela = pd.DataFrame({'nome':['Georgia', 'Lucas', 'Miguel', 'Georgia'], 'idade':[24,17,13,8]})
# print(tabela.idade[tabela.nome=='Georgia'])

#numpy -> operações matemáticas
#pandas -> manipulação de dados

tabela2 = np.array(tabela)
# print(tabela2)
# print(tabela2[2,1])

tabela3 = copy.deepcopy(tabela)     #se não usar o copy, a tabela original é alterada
tabela3.loc[0, 'idade'] = 3
print(tabela3)
print(tabela)