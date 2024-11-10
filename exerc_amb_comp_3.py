#TUPLAS

print('CONSTRUA UM TUPLA CONTENDO OS SEGUINTES AMINOÁCIDOS: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y')

t = t = ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')
print('Tupla criada:',t)

print('A- CONTE E IMPRIMA O NÚMERO DE ELEMENTOS CONTIDOS NA TUPLA CRIADA:')
tupla_len = len(t)
print(tupla_len)

print('B- VERIFIQUE E IMPRIMA SE O AMINOÁCIDO SERINA (S) PERTENCE À TUPLA:')
tupla_in = 'S' in t
print(tupla_in)

print('C- CRIE UMA SEGUNDA TUPLA CONTENDO OS ELEMENTOS PROLINA (P), GLICINA (G), ASPARAGINA (N), TIROSINA (Y), VALINA (V) E TRIPTOFANO (W):')
t2 = ('P', 'G', 'N', 'Y', 'V', 'W')
print(t2)

print('D- SOME AS TUPLAS CONSTRUÍDAS E IMPRIMA O RESULTADO:')
tupla_some = t + t2
print(tupla_some)

print('E- CONTE A OCORRÊNCIA DOS ELEMENTOS GLICINA (G), ASPARAGINA (N) E CISTEÍNA (C):')
tupla_g = tupla_some.count('G')
print('Ocorrência de G', tupla_g)
tupla_n = tupla_some.count('N')
print('Ocorrência de N', tupla_n)
tupla_c = tupla_some.count('C')
print('Ocorrência de C', tupla_c)

print('F- RETORNE A POSIÇÃO DO PRIMEIRO ELEMENTO ASPARAGINA (N):')
tupla_n_1 = tupla_some.index('N')
print(tupla_n_1)

print('G- RETORNE OS 5 ÚLTIMOS ELEMENTOS DA TUPLA:')
tupla_last_five = tupla_some[-5:]
print(tupla_last_five)