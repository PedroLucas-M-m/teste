din = int(input('Digite o valor total do dinheiro: '))
cem = 0 
cinquenta = 0 
vinte = 0 
dez = 0
cinco = 0 
um = 0
while (din > 0):
    if (din >= 100):
        cem += 1
        din = din - 100
        
    elif (din >= 50):
        cinquenta += 1
        din = din - 50
        
    elif (din >= 20):
        vinte += 1
        din = din - 20
    
    elif (din >= 10):
        dez += 1
        din = din - 10
    elif (din >= 5):
        cinco += 1
        din = din - 5
        
    elif (din >= 1):
        um += 1
        din = din - 1
        

print("Numero de Notas 100:",cem)
print("Numero de Notas 50: ",cinquenta)
print("Numero de Notas 20: ",vinte)
print("Numero de Notas 10: ",dez)
print("Numero de Notas 5: ",cinco)
print("Numero de Notas 1: ",um)
