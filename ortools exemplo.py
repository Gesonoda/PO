import ortools.linear_solver.pywraplp as otlp

#invocar o framework
solver = otlp.Solver('teste', otlp.Solver.GLOP_LINEAR_PROGRAMMING)

#criar as variáveis do problema
x = solver.NumVar(0,10,'x')
y = solver.NumVar(0,10,'y')

#definir as restrições
r1=-x+2*y<=8
r2=2*x+y<=14
r3=2*x-y<=10
solver.Add(r1)
solver.Add(r2)
solver.Add(r3)

#definir a função objetivo
solver.Maximize(x+y)

results = solver.Solve()
if results ==otlp.Solver.OPTIMAL:
    print('resultado encontrado')
else:
    print('resultado não encontrado')
print('X=', x.solution_value())
print('Y=', y.solution_value())