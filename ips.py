import sys

def validarIp(ip):
    octetos = ip.split('.')
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        if not octeto.isdigit():
            return False
        if int(octeto) < 0 or int(octeto) > 255:
            return False
    return True

def determinarClase(ip):
    primerOcteto = int(ip.split('.')[0])
    if 0 <= primerOcteto <= 127:
        return 'A'
    elif 128 <= primerOcteto <= 191:
        return 'B'
    elif 192 <= primerOcteto <= 223:
        return 'C'
    elif 224 <= primerOcteto <= 239:
        return 'D'
    elif 240 <= primerOcteto <= 255:
        return 'E'

def main():
    if len(sys.argv) != 2:
        print("La ip no debe contener espacios en sus octetos")
        sys.exit(1)

    direccionIp = sys.argv[1]

    if validarIp(direccionIp):
        clase = determinarClase(direccionIp)
        print(f"La dirección IP {direccionIp} es de clase {clase}.")
    else:
        print("La dirección IP ingresada no es válida, debe contener 4 octetos con numeros comprendidos entre 0 y 255.")

if __name__ == "__main__":
    main()