#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
    #elementos = row.split(" ")
    #campos = elementos[0]
    column = row.strip().split(" ")
    letra = column[0] 
    fecha = column[3]   
    valor = column[6]  
    sys.stdout.write("{}\t{}\t{}\n".format(letra, fecha, valor))