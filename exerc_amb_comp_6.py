#VARIÁVEIS - DICIONÁRIOS

print("1. O Protein Data Bank (PDB) é uma base de dados de estruturas de proteínas. Cada entrada da base de dados é identificada de por um id de 4 letras / dígitos como por exemplo “1ABC”. Abaixo são apresentados ids de estruturas PDBs, juntamente com a a contagem de aminoácidos presentes nessas estruturas.")

print("1A8M - 471, 1TNR - 283, 2AZ5 - 592, 1TNF - 471, 2TNF - 468, 2TUN - 942, 4TSV - 150, 5TSW - 900, 2E7A - 471, 6RMJ - 489")

print("a) Construa um dicionário onde os ids PDB sejam as chaves e o número de resíduos de aminoácidos sejam o valor.")
pdb = {"1A8M" : "471",
"1TNR" : "283",
"2AZ5" : "592",
"1TNF" : "471",
"2TNF" : "468",
"2TUN" : "942",
"4TSV" : "150",
"5TSW" : "900",
"2E7A" : "471",
"6RMJ" : "489" 
}
print (pdb)

print("b) Imprima os valores contidos nos ids 2TNF e 2E7A.")
id2TNF = pdb["2TNF"]
print(id2TNF)

id2E7A = pdb["2E7A"]
print(id2E7A)

print("c) Verifique e imprima o tamanho do dicionário construído.")
print(len(pdb))

print("d) Obtenha e imprima a lista de todas as chaves do dicionário.")
print(pdb.keys())

for chave in pdb:
    print(chave)

print("e) Obtenha e imprima a lista de todos os valores do dicionário.")
print(pdb.values())

for chave in pdb:
    id = pdb[chave]
    print(id)

print("f) Obtenha e imprima uma lista de tuplas com todos os pares chave-valor. Cada dupla será um par ordenado (chave, valor).")
print(pdb.items())