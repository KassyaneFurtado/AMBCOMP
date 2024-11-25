#ESTRUTURA CONDICIONAIS

print('Para os exercícios desta lista, considere a seguinte lista de sequências e faça programas em Python que execute as tarefas descritas abaixo:')

'''
    "A": "Ala", #ALANINA
    "C": "Cys", #CISTEÍNA
    "D": "Asp", #ASPARTATO
    "E": "Glu", #GLUTAMATO
    "F": "Phe", #FENILALANINA
    "G": "Gly", #GLICINA
    "H": "His", #HISTIDINA
    "I": "Ile", #ISOLEUCINA
    "K": "Lys", #LISINA
    "L": "Leu", #LEUCINA
    "M": "Met", #METIONINA
    "N": "Asn", #ASPARAGINA
    "P": "Pro", #PROLINA
    "Q": "Gin", #GLUTAMINA
    "R": "Arg", #ARGININA
    "S": "Ser", #SERINA
    "T": "Thr", #TREONINA
    "V": "Val", #VALINA
    "W": "Trp", #TRIPTOFANO
    "Y": "Tyr" #TIROSINA
'''

A = "LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK"
print("Sequência A", A)
 
B = "KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS"
print("Sequência B", B)

C = "CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR"
print("Sequência C", C)

print("1. Imprima apenas as sequências com 80 ou mais aminoácidos.")

sequencias = ["LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK",
              "KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS",
              "CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR"]


for seq in sequencias:
    if len(seq) >= 80:
        print(seq)

print("2. Imprima apenas as sequências cujo tamanho seja maior que a média de tamanho das sequências.")

print("A=",len(A), "B=", len(B), "C=", len(C))
media = (len(A) + len(B) + len(C))/3
print("Média de tamanho das sequências:", media)

for seq in sequencias:
    if len(seq) > media:
        print(seq)

print("3. Imprima apenas as sequências que possuam pelo menos uma histidina (H) e nenhuma prolina (P).")

for seq in sequencias:
    if 'H' in seq and 'P' not in seq:
        print(seq)
    else:
        print("Não se encaixa nos requisitos")


print("4. Identifique e imprima a maior dentre as três sequências a seguir.")

maior = max(sequencias, key=len)
print(maior)

print("5. Imprima as três sequências em ordem crescente de tamanho.")

sequencias.sort(key=len)
for seq in sequencias:
    print(seq)