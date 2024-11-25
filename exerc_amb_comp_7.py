#OPERADORES
import pandas as pd

print(" 1. Um problema comum em bioinformática estrutural é a comparação entre estruturas moleculares. Nesse exercício, alinhamos estruturalmente dois resíduos de glicina (amarela e roxa - Figura 1) e apresentamos as coordenadas tridimensionais (x, y, z) (Tabelas 1 e 2). Considerando estas tabelas de coordenadas x, y, z dos átomos dos dois resíduos de glicina, calcule o RMSD (Root Mean Square Deviation) entre elas segundo a Equação: Figura 1 - Dois resíduos de glicina sobrepostos")

Tabela1 = {
    "ATOMO": ["N", "CA", "C", "O"],
    "x": [108.304, 108.477, 109.907, 110.821],
    "y": [100.827, 100.389, 100.555, 100.799],
    "z": [67.992, 69.362, 69.817, 69.027]
}

Tabela1 = pd.DataFrame(Tabela1)
print(Tabela1)
print("Glicina número 1")

Tabela2 = {
    "ATOMO": ["N", "CA", "C", "O"],
    "x": [107.670, 108.477, 109.513,110.667],
    "y": [101.359, 100.389, 101.011, 100.572],
    "z": [70.074, 69.362,68.450, 68.425]
}

Tabela2 = pd.DataFrame(Tabela2)
print(Tabela2)
print("Glicina número 2")

print("Equação 1 - RMSD (Considere N=4 que é o número de átomos)")



print("2. Em biologia molecular, o conteúdo GC (guanina e citosina) é o percentual de bases nitrogenadas em uma molécula de DNA ou RNA que são guanina ou citosina (dentre as quatro bases possíveis). Para as seguintes sequências calcule usando os operadores vistos em aula o percentual de conteúdo GC, imprimindo os resultados:")

print("Sequência A: ATGATCTCGTAATTAACCGGAATTTTGGGCC")
print("Saída esperada: 41.93")
print("Sequência B: GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA")
print("Saída esperada: 44.44")

SeqA = "ATGATCTCGTAATTAACCGGAATTTTGGGCC"
conteudoC = "C"
conteudoG = "G"
ocorrencias = (SeqA.count(conteudoC)+ SeqA.count(conteudoG))
print(ocorrencias)
porcentagem = (ocorrencias/len(SeqA))*100
print("A porcentagem de ocorrencias de conteúdo GC na Sequência A é de:", porcentagem,"%")

SeqB = "GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA"
conteudoC = "C"
conteudoG = "G"
ocorrencias = (SeqB.count(conteudoC)+ SeqB.count(conteudoG))
print(ocorrencias)
porcentagem = (ocorrencias/len(SeqB))*100
print("A porcentagem de ocorrencias de conteúdo GC na Sequência B é de:", porcentagem,"%")