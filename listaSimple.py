from nodo import Nodo
class ListaSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    #METODOS PARA AGREGAR DATOS
    def insertarFinal(self, dato):
        nuevoNodo = Nodo(dato)
        self.size +=1
        #si la lista no tiene ningun dato
        if self.primero == None:
            #el apuntador primero apunta al nuevo nodo
            self.primero = nuevoNodo
            #el apuntador ultimo apunta al nuevo nodo
            self.ultimo = nuevoNodo
        #si la lista ya tiene uno o mas datos se agrega el nuevo nodo
        else: 
            #el apuntador siguiente apunta al nuevo nodo --->
            self.ultimo.siguiente = nuevoNodo
            #el apuntador ultimo apunta al nuevo nodo
            self.ultimo = nuevoNodo

    def obtenerSize(self):
        return self.size   
    
    def estaVacia(self):
        #si el primero es diferente de nulo No está vacia
        if self.primero !=None:
            return True
        #Si el primero es igual a nulo Si está vacia
        if self.primero ==None:
            return False

    def imprimir(self):
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
            print("ItemCode: ",nodoTemporal.dato.item)
            print("QuantityOnHand: ",nodoTemporal.dato.quantityOnHand)
            print("PriceLevel1: $",nodoTemporal.dato.priceLevel1)
            print("PriceLevel2: $",nodoTemporal.dato.priceLevel2)
            print("PriceLevel3: $",nodoTemporal.dato.priceLevel3)
            print("LastTotalUnitCost: $",nodoTemporal.dato.lastTotalUnitCost)
            print("MarginLevel1: ",nodoTemporal.dato.marginLevel1,"%")
            print("MarginLevel2: ",nodoTemporal.dato.marginLevel2,"%")
            print("MarginLevel3: ",nodoTemporal.dato.marginLevel3,"%")
            print("valorInventario: $",nodoTemporal.dato.valorInventario)
            print()
            nodoTemporal = nodoTemporal.siguiente
            
    def imprimirTop(self):
        print('-'*96)
        print("| {:<16} | {:<16} | {:<16} | {:<16} | {:<16} |".format('Item Code','Margin Level 1', 
                                                                    'Margin Level 2', 'Margin Level 3',
                                                                    'valor Inventario'))
        print('-'*96)
        contador = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.primero
        while nodoTemporal != None:
            contador +=1
            if contador <= 10:
                print("| {:<16} | {:<16} | {:<16} | {:<16} | {:<16} |".format(str(nodoTemporal.dato.item),
                                                                            str(nodoTemporal.dato.marginLevel1)+str(" %"),
                                                                            str(nodoTemporal.dato.marginLevel2)+str(" %"),
                                                                            str(nodoTemporal.dato.marginLevel3)+str(" %"),
                                                                            str("$ ")+str(nodoTemporal.dato.valorInventario)))
                print()
            nodoTemporal = nodoTemporal.siguiente

    def ordenamientoBurbuja(self, llave):
        #las variables hacen referencia al primer elemento de la lista
        actual = self.primero 
        aux = self.primero
        #si la lista está vacía agrega el dato a la lista
        if actual.siguiente != None and aux != None:
            #obtiene el primer dato de la lista
            i = self.primero
            while i != None:
                #obtiene el dato siguiente de la lista
                j = i.siguiente
                while j != None:
                    #compara los datos para saber cual es el mayor
                    if llave  == "valor inventario":
                        i1 =i.dato.valorInventario
                        j1 = j.dato.valorInventario
                    elif llave  == "margen level 1":
                        i1 =i.dato.marginLevel1
                        j1 = j.dato.marginLevel1
                    elif llave  == "margen level 2":
                        i1 =i.dato.marginLevel2
                        j1 = j.dato.marginLevel2
                    elif llave  == "margen level 3":
                        i1 =i.dato.marginLevel3
                        j1 = j.dato.marginLevel3

                    if i1 < j1:
                        #cambia el orden de los datos
                        temporal = i.dato
                        i.dato = j.dato
                        j.dato = temporal
                    #pasa al siguiente dato de la lista
                    j = j.siguiente
                #pasa al siguiente dato de la lista
                i = i.siguiente