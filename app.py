import random

'''
Método Potássio-Argônio:
Idade: Idade da rocha em anos
Ar-40: Razão isotópica de Ar-40 (Ar-40 / K total)
K-40: Razão isotópica de K-40 (K-40 / K total)
t_0: Tempo inicial (1.24 bilhões de anos)
dec: Constante de decaimento de K-40 (5.54e-12 anos^-1)
'''

def calc_idade_algo_pot_argo(ar_40, k_40):
    t_0 = 1.24e9
    dec = 5.54e-12
    idade =  (t_0 / dec) * (ar_40 / k_40)
    return idade / 1e9

def gerar_exemplos(n):
    exemplos = []
    for i in range(n):
        ar_40 = random.uniform(0.00001, 0.0001) 
        k_40 = random.uniform(0.00001, 0.0001)
        exemplos.append((ar_40, k_40))
    return exemplos

def main():
    exemplosRochas = gerar_exemplos(10)

    for i, (ar_40,k_40) in enumerate(exemplosRochas, 1):
        idade = calc_idade_algo_pot_argo(ar_40, k_40)
        print(f'Rocha {i}: ar_40 = {ar_40:e}, k_40 = {k_40:e}, idade = {idade:e} bilhões de anos')

if __name__ == "__main__":
    main()