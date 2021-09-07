from gurobipy import *

# PROBLEMA DE MAXIMIZAÇÃO
# FO: MAX x + y
# sujeito a:
#      -x+2y<=8
#      2x+y<=14
#      2x-y<=14
#      0<=x<=10
#      0<=y<=10


model = Model('exemplo')
x = model.addVar(obj=1, vtype='C', name='x')
y = model.addVar(obj=1, vtype='C', name='y')

# #obj-> coeficiente da variável; peso da variavel na FO
# vtype-> tipo da variável (continuous, binary, integer, semicont or semiint)
# name-> nome da variável

model.update()
#faz com que as variáveis sejam gravadas como variáveis de otimização

#RESTIÇÕES

# L1 = LinExpr([-1,2], [x,y])
#expressão linar com os pesos das variáveis
model.addConstr(-x+2*y<= 8)
#adiciona a restrição

# L2 = LinExpr([2,1],[x,y])
model.addConstr(2*x+y<=14)

# L3 = LinExpr([2,-1], [x,y])
model.addConstr(2*x-y<= 10)


#FUNÇÃO OBJETIVO:
model.ModelSense=-1
# (-1 = maximizar)
model.optimize()
print('x=', x.X)
print('y=', y.X)
