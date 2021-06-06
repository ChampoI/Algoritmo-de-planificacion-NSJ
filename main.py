# Algoritmos de Planificacion de Procesos
# Plantilla Diego Fernando Marin 
# Universidad Libre
# CodigoNombre
 

# - Imports  
import sys, copy
 
# - Modifique SOLO esta funcion  
# El planificador debe devolver un apuntador
# al proceso que le corresponde el turno, 
# el proceso actual se encuentra en activo
def menos_duracion(cola)
  menor = 999999

  for proceso in cola
    if proceso.D - proceso.i = menor
      menor = proceso.D - proceso.i
      proceso_mas_corto = proceso
  return proceso_mas_corto     


def planificador(activo, cola, terminados)
    if activo == None      # La primera vez
        activo = menos_duracion(cola)    # hace activo al primero
    # print(activo)
    if activo.i  activo.D # si ya termino
        copia = copy.copy(activo)
        terminados.append(copia)
        cola.remove(activo)
        
    if cola != []
            activo = menos_duracion(cola) # retorne el proximo
    return activo            # no retorna el mismo
 
# - NO modifique NADA de aqui en adelante

# - Programa Principal  
def main()
    archivo = input(nombre del archivo )
 
    procesos = []      # Procesos de la 'A' a la 'Z'
    cola = []          # Cola de Procesos
    terminados = []    # Procesos Terminados
    proceso = None     # Proceso Activo
    CPU = 0            # Unidad de Tiempo
   
    procesos = cargar(archivo)
   
    # para ver la tabla de procesos
    imprimir(procesos)
 
    adicionar(CPU, cola, procesos)
    # Ciclo Infinito
    while cola != []
        # Adiciona los procesos nuevos
        adicionar(CPU, cola, procesos)
        # Selecciona el proximo proceso
        proceso = planificador(proceso, cola, terminados)
        if cola != []
            # Ejecuta el proceso seleccionado
            activador(CPU, proceso)
        # siguiente Unidad de Tiempo, tick del reloj de la CPU
        CPU += 1
 
    # Si desea ver la tabla de resultados
    resultados(terminados)
 
# - Clases
 
class Proceso()
    # Constructor
    def __init__(self, nombre, To, D, Pr)
        # Atributos - BCP Bloque de Control de Proceso
        self.nombre = nombre
        self.To = To    # Tiempo de Llegada
        self.D = D      # Duracion
        self.Pr = Pr    # Prioridad
        self.i = 1      # Process Counter (index)
        self.age = 10   # Envejecimiento
        self.Tw = 0     # Tiempo de Espera
        self.Ts = 0     # Tiempo de Servicio
        self.activo = False
    # Metodos
    def __str__(self)
        return { %c  %d  %d } % (self.nombre, self.i, self.D)
    def imprimir(self)
        return %ct%dt%dt%d % (self.nombre, self.To, self.D, self.Pr)
    def resultados(self)
        return %ct%dt%d % (self.nombre, self.Tw, self.Ts)
 
# - Funciones 

# Carga los procesos de un archivo, 
# y verifica que no hay errores!
def cargar(nombreArchivo)
    lista = []
    To = 0
    To2 = 0
    archivo = open(nombreArchivo, r)
    if archivo == None
        print(Error imposible abrir archivo '%s'n % (nombreArchivo));
    for linea in archivo.readlines()
        valores = linea.split()
        nombre = valores[0]
        To = int(valores[1])
        D = int(valores[2])
        Pr = int(valores[3])
        if To  To2      # To solo puede aumentar
            print(Error [%s] Tiempo de Llegada (%d) inferior al anterior (%d) en '%c'n % (nombreArchivo, To, To2, nombre))
            sys.exit(101)
        if D1 or D9    # Duracion solo entre 1 y 9
            print(Error [%s] Duracion (%d) fuera de rango en '%c'n % (nombreArchivo, D, nombre))
            sys.exit(102)
        if Pr!=0 and Pr!=1 # Prioridad solo 0 o 1
            print(Error [%s] Prioridad (%d) fuera de rango en '%c'n % (nombreArchivo, Pr, nombre))
            sys.exit(103)
        proceso = Proceso(nombre, To, D, Pr)
        lista.append(proceso)
        To2 = To;
    return lista
 
def adicionar(CPU, cola,  procesos)
    salir = False
    while not salir
        mover = None
        for proceso in procesos
            if proceso.To = CPU
                # Si quiere ver en que momento se adicionan los procesos
                # Quite los comentarios del siguiente print
                # print(t+%c[%d,%d,%d] % (proceso.nombre, proceso.To, proceso.D, proceso.Pr))
                mover = proceso
                break
        if mover != None
            copia = copy.copy(mover)
            cola.append(copia)
            procesos.remove(mover)
        else
            salir = True
 
# El activador solo imprime la tajada de proceso
# que esta Ejecutando, e incrementa el contador q[].i
def activador(CPU, proceso)
    # Imprime la unidad de tiempo, en que se encuentra
    print(%d % (CPU), end='')
    # la primera vez que le toca el turno
    # registra la espera
    if proceso.i == 1 
      # cuando entra, menos cuando llego
      proceso.Tw = CPU - proceso.To
    # la ultima vez que le toca el turno
    if proceso.i == proceso.D   
      # cuando sale, menos cuando llego
      # +1, porque inicia desde zero
      proceso.Ts = CPU - proceso.To + 1 
    # Ejecuta el proceso
    print(t%c%d % (proceso.nombre, proceso.i))
    proceso.i += 1
 
# Imprime todos los procesos
def imprimir(procesos)
    print(nTabla de Procesosn)
    print(PtTotDtprn--t---t--t--)
    for proceso in procesos
        print(proceso.imprimir())
    print()
 
# Imprime todos los resultados
def resultados(procesos)
    print(nTabla de Resultadosn)
    print(PtTwtTsn--t---t---)
    for proceso in procesos
        print(proceso.resultados())
 
if __name__ == __main__
    main()
