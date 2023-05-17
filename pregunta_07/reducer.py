#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
datos = []
for line in sys.stdin:
  columnas = line.strip().split("\t")
  datos.append(columnas)
organizar = sorted(datos, key=lambda x: (x[0], float(x[2])))
for item in organizar:
  sys.stdout.write(f"{item[0]}\t{item[1]}\t{item[2]}\n")