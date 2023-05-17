#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
n = 6
registros = []
for line in sys.stdin:
  columnas = line.strip().split("\t")
  registros.append(columnas)
    
registros.sort(key=lambda x: int(x[2]))
   
for i in range(min(n,len(registros))):
  sys.stdout.write("   ".join(registros[i])+"\n")