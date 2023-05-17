#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    filas = []
    for line in sys.stdin:
        columnas = line.strip().split("\t")
        filas.append(columnas)

    filas_ordenadas = sorted(filas, key=lambda x: int(x[0]))

    posicion_letras = {}
    for i, columnas in enumerate(filas_ordenadas):
        letras = columnas[1].split(",")
        #print(columnas)

        for letra in letras:
            if letra not in posicion_letras:
                posicion_letras[letra] = []
            posicion_letras[letra].append(str(i))

    orden_posicion_letras = dict(sorted(posicion_letras.items()))
    for letra, posicion in orden_posicion_letras.items():
        posiciones = ",".join(posicion)
        sys.stdout.write(f"{letra}\t{posiciones}\n")