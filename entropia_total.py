from entropia import entropia
lista_entropia = list()
p_total = int(input('Positivo: '))
n_total = int(input('Negativo: '))
d_total = int(input('Dominio: '))
entropia_total = entropia(p_total,n_total,d_total)
cantidad = int(input("Ingrese la cantidad: "))
for valor in range(1,cantidad+1):
    print(f'Para la raiz nro{valor}: ')
    p = int(input('Positivo: '))
    n = int(input('Negativo: '))
    d = int(input('Dominio: '))
    lista_entropia.append(dict(p=p,n=n,d=d,entropia_propia=entropia(p,n,d)))
suma = 0
for valor in lista_entropia:
    suma += valor.get('d')/d_total*valor.get('entropia_propia')
ganancia = entropia_total - suma
print(f'La ganancia es de: {ganancia:1.4f}')