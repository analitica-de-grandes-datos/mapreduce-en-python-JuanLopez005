#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
  elementos = row.split(",")
  campos = elementos[0:2]
  linea = ",".join(campos)
  sys.stdout.write(linea)