import matplotlib.pyplot as plt

nomes=['Georgia', 'Lucas', 'Miguel', 'Catarina', 'Jamily']
salarios = [1000,1100,1110,1200,1300]

plt.figure(0)
plt.plot(nomes, salarios, color='red')
# plt.show()
plt.savefig('grafico1.png')

plt.figure(1)
plt.bar(nomes, salarios)
# plt.show()
plt.savefig('grafico2.png')