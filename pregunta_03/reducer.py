#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    result = []
    max_val = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #

    for line in sys.stdin: 
             
      key, val = line.split(",")
      val = int(val)       

      if curkey is None:
            curkey = key
            val_max = val
      elif curkey != key:
            result.append((curkey, val_max))
            curkey = key
            val_max = val
      else:
            if val > val_max:
                val_max = val

    result.append((curkey, val_max))           

    sorted_result = sorted(result, key=lambda x: x[1])

    for key, val in sorted_result:
      sys.stdout.write("{},{}\n".format(key, val))