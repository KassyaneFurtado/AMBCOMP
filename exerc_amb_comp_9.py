#ESTRUTURAS DE REPETIÇÃO
import statistics

print ('1. Escreva um programa que calcule e escreva a tabela de graus Centígrados em função dos graus Farenheit que variem entre 1 e 150 de 1 em 1:')

for F in range(1, 151):
    C = (5/9) * (F - 32)
    print(f"{F} F = {C:.2f} C")

print()

print('2. Utilizando as estruturas de repetição, verifique se as seguintes sequências são uma sequência de DNA {A, G, T, C}, RNA {U, C, A, G}, PROTEÍNA {A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y} ou nenhuma delas (nesse caso, imprima as letras que não fazem parte do alfabeto):')
print('1º sequência: ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN')
print('2º sequência: TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT')
print('3º sequência: ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN')

def verificar_sequencia(sequencia):
    dna = {'A', 'G', 'T', 'C'}
    rna = {'U', 'C', 'A', 'G'}
    proteina = {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'}
    
    # Identificar letras inválidas
    letras_invalidas = set(sequencia) - (dna | rna | proteina)
    
    if letras_invalidas:
        print(f"Letras inválidas: {letras_invalidas}")
        return  # Sai da função se houver letras inválidas

    # Verificar o tipo de sequência
    if all(base in dna for base in sequencia):
        print("A sequência é de DNA.")
    elif all(base in rna for base in sequencia):
        print("A sequência é de RNA.")
    elif all(base in proteina for base in sequencia):
        print("A sequência é de proteína.")
    else:
        print("A sequência não pertence a nenhum dos grupos.")

print("Resultados:")
print("1º sequência: ")
verificar_sequencia('ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN')
print("2º sequência: ")
verificar_sequencia('TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT')
print("3º sequência: ")
verificar_sequencia('ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN')

print()
            
print('3. Utilizando as estruturas de repetição, gere e imprima a sequência complemento reverso da seguinte sequência de DNA:')
print('TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT')

sequencia_dna = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'

complemento = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

sequencia_complemento = ''
for nucleotideo in sequencia_dna:
    sequencia_complemento += complemento[nucleotideo]

sequencia_complemento_reverso = sequencia_complemento[::-1]
print('Sequência complemento reverso:', sequencia_complemento_reverso)

print()

print('4. Escreva um programa que calcule o fatorial de um número recebido como entrada. Lembre-se que o fatorial de um número é igual ao número multiplicado n sucessivamente por n-1, n-2, .. 1. Exemplo: fat(6) = 6 x 5 x 4 x 3 x 2 x 1 = 720.')

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")

print()

print('5. Escreva um programa que liste a tabuada (produtos) dos números de 1 a 15.')

for i in range(1, 16):
    print(f"Tabuada do {i}:")
    for j in range(11):
        print(f"{i} x {j} = {i * j}")
    print()

print()

print('6. Considerando a seguinte sequência e tabela de massas (Tabela 1), escreva um programa em Python que calcule a massa molar da sequência:')
print('VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHT ISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL')

massas_aminoacidos = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

def calcular_massa_molar(sequencia):
    massa_total = 0
    for aminoacido in sequencia:
        if aminoacido in massas_aminoacidos:
            massa_total += massas_aminoacidos[aminoacido]
        else:
            print(f"Aminoácido inválido: {aminoacido}")
    return massa_total

sequencia = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"
massa_molar = calcular_massa_molar(sequencia)
print(f"Massa molar da sequência: {massa_molar:.2f} g/mol")

print()

print('7. Considerando a Tabela 2 que contem dados de defensinas de plantas, obtenha / calcule e imprima:')

sequencias = [
    "KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC",
    "ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF",
    "ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN",
    "ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN",
    "ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN",
    "ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR",
    "ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF"
]

print('A) a menor sequência e seu comprimento')
menor_sequencia = min(sequencias, key=len)
comprimento_menor = len(menor_sequencia)
print(f"A menor sequência é: {menor_sequencia} com comprimento {comprimento_menor}")

print('B) a maior sequência e seu comprimento')
maior_sequencia = max(sequencias, key=len)
comprimento_maior = len(maior_sequencia)
print(f"A maior sequência é: {maior_sequencia} com comprimento {comprimento_maior}")

print('C) a média entre os comprimentos das sequências')
comprimentos = [len(seq) for seq in sequencias]
media_comprimentos = sum(comprimentos) / len(comprimentos)
print(f"A média dos comprimentos das sequências é: {media_comprimentos:.2f}")

print('D) a mediana entre os comprimentos das sequências')
mediana_comprimentos = statistics.median(comprimentos)
print(f"A mediana dos comprimentos das sequências é: {mediana_comprimentos}")

print()

print('8. Considerando as assinaturas moleculares (fingerprints) hipotéticas das tabelas abaixo, calcule a distância de Tanimoto:')
A = [0,0,1,0,0,1,1,0,1,1,0,1]
B = [0,1,0,0,1,1,0,1,1,0,0,0]

# Calcular a interseção e a união
interseccao = sum(1 for a, b in zip(A, B) if a == 1 and b == 1)
uniao = sum(1 for a, b in zip(A, B) if a == 1 or b == 1)

# Calcular a distância de Tanimoto
if uniao == 0:  # Para evitar divisão por zero
    distancia_tanimoto = 0
else:
    distancia_tanimoto = interseccao / uniao


print(f"Interseção: {interseccao}")
print(f"União: {uniao}")
print(f"Distância de Tanimoto: {distancia_tanimoto:.2f}")

