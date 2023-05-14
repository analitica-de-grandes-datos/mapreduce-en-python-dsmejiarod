#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
for row in sys.stdin:
  elementos = row.strip()
  elementos = elementos.split("   ")
  
  
  linea = ";".join(elementos)
  sys.stdout.write(linea+"\n")