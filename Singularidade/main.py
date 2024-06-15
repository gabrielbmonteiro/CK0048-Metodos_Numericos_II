from singularidade import Resolver

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("                   Singularidade")
print("---------------------------------------------------\n")

print("Exponecial Simples: ")
for i in range(2,5):
    print("n={} valor={}".format(i, Resolver(i, True) ) )

print("---------------------------------------------------\n")

print("Exponecial Dupla: ")
for i in range(2,5):
    print("n={} valor={}".format(i, Resolver(i, False) ) )
