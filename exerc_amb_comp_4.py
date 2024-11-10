import pandas as pd

#VARIÁVEIS - CONJUNTOS 
print('1. EM UM EXPERIMENTO DE DOCKING MOLECULAR UTILIZANDO TRÊS FERRAMENTAS DIFERENTES, FORAM OBTIDOS OS TRÊS TRÊS CONJUNTOS DE RMSD DA TABELA ABAIXO. CONSIDERANDO OS VALORES DESTA TABELA, CRIE OS 3 CONJUNTOS USANDO VARIÁVEIS DO TIPO CONJUNTO EM PYTHON.')
ferramentas = {
    'Ferramenta 1': ['1.9', '1.8', '5.7', '1.6', '5.8', '1.7', '9.6', '5.9', '9.5', '6.5', '6.2', '1.1', '4.4', '3.5', '2.9', '4.7', '4.6', '5.2', '5.3'],
    'Ferramenta 2': ['4.7', '3.6', '6.2', '7.1', '7', '5.6', '5.7', '3.4', '3.3', '2.1', '3.8', '3.9', '5', '5.1', '1.9', '9.5', '1.0', '1.3', '5.4'],
    'Ferramenta 3': ['2.2', '3.3', '5.1', '3', '3.7', '9.1', '8.8', '8.5', '2', '4.1', '6.1', '4.9', '1.1', '0.5', '0.8', '3.2', '6.9', '9.3', '9.5']
}

tabela_ferramentas = pd.DataFrame(ferramentas)

print(tabela_ferramentas)
A1 = {1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1, 4.4, 3.5, 2.9, 4.7, 4.6, 5.2, 5.3}
B2 = {4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5, 1.0, 1.3, 5.4}
C3 = {2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2, 6.9, 9.3, 9.5}

# A SEGUIR, CODIFIQUE EM PYTHON AS SEGUINTES TAREFAS:
print('A) VERIFIQUE AS DIFERENÇAS ENTRE OS CONJUNTOS (1,2) (1,3) E (2,3)')

print('Diferença 1 e 2:', A1.difference(B2))
print('Diferença 1 e 3:', A1.difference(C3))
print('Diferença 3 e 3:', B2.difference(C3))

print('B) RETORNE AS INTERSECÇÕES ENTRE (1,2) (1,3) E (2,3)')
print('Interseção 1 e 2:', A1.intersection(B2))
print('Interseção 1 e 3:', A1.intersection(C3))
print('Interseção 2 e 3:', B2.intersection(C3))

print('C) INSIRA TODOS OS ELEMENTOS DO CONJUNTO 2 E 3 NO CONJUNTO 1')
print('Tamanho A1:', len(A1))
print('Tamanho B2:',len(B2))
print('Tamanho C3:',len(C3))

for elemento in B2:
    A1.add(elemento)
for elemento in C3:
    A1.add(elemento)

print('D) RETORNE O TAMANHO DO CONJUNTO FORMADO PELA TAREFA (C)')
print(len(A1))

print('2. DADOS OS SEGUINTES CONJUNTOS')
A = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27}
B = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24}
C = {2, 6, 10, 18, 20}
D = {1, 30, 5, 11, 17, 16, 22, 26}
print(A)
print(B)
print(C)
print(D) 
# CODIFIQUE EM PYTHON AS VARIÁVEIS QUE OS REPRESENTAM E REALIZE AS SEGUINTES TAREFAS:

print('A) VERIFIQUE A INTERSEÇÃO E DIFERENÇA ENTRE O CONJUNTO A E B.')
print('Interseção:', A.intersection(B))
print('Diferença:', A.difference(B))

print('B) VERIFIQUE SE O CONJUNTO A E B SÃO DISJUNTOS AO CONJUNTO D')
print('Disjunção A e D:', A.isdisjoint(D))
print('Disjunção A e B:', B.isdisjoint(B))

print('C) RETORNE SE O CONJUNTO C É SUBCONJUNTO DE A E B')
print('C é subconjunto de A?',C.issubset(A))
print('C é subconjunto de B?',C.issubset(B))

print('D) ACRESCENTE OS ELEMENTOS 18, 23, 25, 63 NO CONJUNTO D')
print(D)
D.update([18, 23, 25, 63])
print('Conjunto alterado:', D)
