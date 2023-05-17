#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
    elementos = row.strip().split(",")
    campos = elementos[0]
    column = campos.split("   ")
    letra = column[0]    
    valor = column[2]  
    sys.stdout.write("{}\t{}\n".format(letra, valor))