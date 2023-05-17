#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
  elementos = row.split(",")
  campos = elementos[3:5]
  linea = "\t".join(campos)
  sys.stdout.write(linea+"\n")