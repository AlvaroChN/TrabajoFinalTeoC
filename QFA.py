from qiskit import QuantumCircuit, execute, Aer

def crear_qfa(cadena_binaria):
    # Crea un circuito cuántico con 1 qubit y 1 bit clásico
    circuito = QuantumCircuit(1, 1)

    # Aplica una puerta X si el último bit es 1
    if cadena_binaria[-1] == '1':
        circuito.x(0)

    # Aplica una puerta Hadamard para poner el qubit en superposición
    circuito.h(0)

    # Mide el qubit
    circuito.measure(0, 0)

    return circuito

def ejecutar_qfa(circuito):
    # Ejecuta el circuito en un simulador
    resultado = execute(circuito, Aer.get_backend('qasm_simulator')).result()

    # Obtiene los conteos de los resultados de la medición
    conteos = resultado.get_counts()

    # El QFA acepta la cadena si la mayoría de las mediciones dan 0
    return conteos.get('0', 0) > conteos.get('1', 0)

# Solicita al usuario que ingrese las cadenas binarias
cadenas_binarias = input("Por favor, ingresa las cadenas binarias separadas por comas: ").split(',')

# Prueba el QFA con las cadenas binarias ingresadas por el usuario
for cadena_binaria in cadenas_binarias:
    qfa = crear_qfa(cadena_binaria.strip())
    print(f"La cadena {cadena_binaria.strip()} es aceptada: {ejecutar_qfa(qfa)}")
# Este automata tiene un 50% de posibilidad de aceptar la cadena. Aun esta en proceso de poder llegar a un 100% de posibilidad, al ser un tema no tan investigado, no se tiene aun cierto algoritmo que tenga al 100% de posibilidad de aceptar la cadena