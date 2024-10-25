print('EXERCÍCIO 1')

TNF='VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
print(TNF)

print('A- RETORNE O TAMANHO DA SEQUÊNCIA:')
size_TNF = len(TNF)
print(size_TNF)

print('B- REALIZE A CONTAGEM DA OCORRÊNCIA DE UMA SEQUÊNCIA DE LEUCINAS (LL):')
leu_TNF = TNF.count('LL')
print(leu_TNF)

print('C- ENCONTRE NA SEQUÊNCIA AS POSIÇÕES OCUPADAS POR DUAS GLICINAS (GG) E DUAS ARGININAS (RR):')
gly_TNF = TNF.find('GG')
print("Posição Glicinas", gly_TNF)

arg_TNF = TNF.find('RR')
print("Posição Argininas", arg_TNF)

print('D- RETORNE OS 100 PRIMEIROS AMINOÁCIDOS DA SEQUÊNCIA:')
ami_TNF = TNF[0:100]
print(ami_TNF)

print('E- SUBSTITUA O TRECHO DA SEQUÊNCIA COM A OCORRÊNCIA DE 3 SERINAS E 1 ARGININA (SSSR) POR ALANINAS:')
arg_ser_TNF = TNF.replace('SSSR','AAAA')
print(arg_ser_TNF)

print('F- QUEBRE A SEQUÊNCIA NO LOCAL ONDE A SUBSTITUIÇÃO FOI REALIZADA:')
split_TNF= arg_ser_TNF.split('AAAA')
print(split_TNF)

print('EXERCÍCIO 2')

texto = "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome."
print(texto)

print('A- PASSE O TEXTO PARA LETRAS MAIÚSCULAS:')
texto_ma = texto.upper()
print(texto_ma)

print('B- PASSE O TEXTO PARA LETRAS MINÚSCULAS:')
texto_mi = texto.lower()
print(texto_mi)

print('C- PASSE CADA PRIMEIRA LETRA DE PALAVRA EM MAIÚSCULO:')
texto_title = texto.title()
print(texto_title)

print('D- TRANSFORME AS LETRAS MAIÚSCULAS EM MINÚSCULAS E VICE-VERSA:')
texto_inv = texto.swapcase()
print(texto_inv)

print('EXERCÍCIO 3')

insulin_signal = 'MALWMRLLPLLALLALWGPDPAAA'
print(insulin_signal)

print('A- RETORNE O TAMANHO DA SEQUÊNCIA APRESENTADA:')
size_insulin_signal = len(insulin_signal)
print(size_insulin_signal)

print('B- QUEBRE A SEQUÊNCIA NO TRECHO “LLALLALWG": ')
split_insulin_signal = insulin_signal.split('LLALLALWG')
print(split_insulin_signal)

print('C- CONCATENE AS SEQUÊNCIAS RESULTANTES OBTENDO A SEGUINTE SEQUÊNCIA FINAL MALWMRLLPPDPAAA:')
join_insulin_signal = ''.join(split_insulin_signal)
print(join_insulin_signal)

print('D- SUBSTITUA O TRECHO "DPAAA" POR “LLALL”: ')
replace_insulin_signal = insulin_signal.replace('DPAAA','LLALL')
print(replace_insulin_signal)

print('EXERCÍCIO 4')
print('COM BASE NA SEQUÊNCIA DE DNA GATGGAACTTGACGTAAACCTATATT RETORNE A SEQUÊNCIA DE RNA CORRESPONDENTE:')

DNA = 'GATGGAACTTGACGTAAACCTATATT'
RNA = DNA.replace('T', 'U')
print(RNA)