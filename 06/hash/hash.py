import sys
import hashlib


def mostrar_ayuda():
    print("Uso: python hash.py <operación> <tipo_entrada> <archivo_o_texto_entrada>")
    print()
    print("Hashea un texto o un archivo con md5, sha1 o sha256.")
    print()
    print("Argumentos:")
    print("  operación          -md5 | -sha1 | -sha256")
    print("  texto o archivo    -t si es texto | -f si es fichero")
    print("  archivo_entrada    Archivo de texto que se va a procesar")
    print()
    print("Ejemplos:")
    print("  python hash.py -md5 -t texto")
    print("  python hash.py -sha256 -f secreto.txt")

def hash(entrada, hashing):
    if hashing == "-sha256":
        hash_obj = hashlib.sha256()
        hash_obj.update(entrada)
        resultado = hash_obj.hexdigest()

    if hashing == "-sha1":
        hash_obj = hashlib.sha1()
        hash_obj.update(entrada)
        resultado = hash_obj.hexdigest()

    if hashing == "-md5":
        hash_obj = hashlib.md5()
        hash_obj.update(entrada)
        resultado = hash_obj.hexdigest()

    print(hashing, ":",resultado)
    


def main():
    if '--help' in sys.argv:
        mostrar_ayuda()
        sys.exit()
    
    if len(sys.argv) < 4:
        mostrar_ayuda()
        sys.exit()
        
    hashing = sys.argv[1]
    t_o_f = sys.argv[2]
    archivo_entrada = sys.argv[3]

    if t_o_f == "-f":
        with open(archivo_entrada, "rb") as entrada:
            texto_original = entrada.read()

    if t_o_f == "-t":
        texto_original = archivo_entrada

    if hashing == "-md5":
        hash(texto_original, hashing)
    elif hashing == "-sha1":
        hash(texto_original, hashing)
    elif hashing == "-sha256":
        hash(texto_original, hashing)
    else:
        print("-md5 | -sha1 | -sha256")
        sys.exit()
    

    print()
    print("Operación finalizada con éxito")
        
if __name__ == "__main__":
    main()
