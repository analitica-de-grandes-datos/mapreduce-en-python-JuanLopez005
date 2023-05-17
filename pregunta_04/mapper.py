#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
    elementos = row.strip().split(",")
    campos = elementos[0]
    column = campos.split("   ")
    linea = column[0]
    #linea = ",".join(column)
    sys.stdout.write((linea+"\t1\n"))