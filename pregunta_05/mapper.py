#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
    elementos = row.strip().split(",")
    campos = elementos[0]
    column = campos.split("   ")
    linea = column[1]
    fecha = linea.split("-")
    dia = fecha[1]
    sys.stdout.write((dia+"\t1\n"))