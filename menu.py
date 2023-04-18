import sys
from tkinter import filedialog
import xml.etree.cElementTree as ET
from listaSimple import ListaSimple
from item import Item

item_List = ListaSimple()

def cargarArchivo():
    try:
        #usando element tree
        
        # abre ventana para seleccionar archivo
        urlarchivo = filedialog.askopenfilename(initialdir="./", title="Seleccione un Archivo", filetypes=(("xml", "*.xml"), ("all files", "*.*")))
        # urlarchivo = input()
        if urlarchivo != "":
            documento = ET.parse(urlarchivo)
            #Obtiene la raíz CONFIG
            root = documento.getroot() 
            #dentro de la raíz recorre los hijos
            for item in root: 
                if item.tag == "Item":
                    for item2 in item:
                        if item2.tag == "ItemCode":
                            item2_ItemCode = item2.text
                        elif item2.tag == "QuantityOnHand":
                            item2_QuantityOnHand = item2.text
                        elif item2.tag == "PriceLevel1":
                            item2_PriceLevel1 = item2.text
                        elif item2.tag == "PriceLevel2":
                            item2_PriceLevel2 = item2.text
                        elif item2.tag == "PriceLevel3":
                            item2_PriceLevel3 = item2.text
                        elif item2.tag == "LastTotalUnitCost":
                            item2_LastTotalUnitCost = item2.text
                    #Aca se envia al objeto listaElementos elemento
                    objetoItem = Item(str(item2_ItemCode).strip(),int(item2_QuantityOnHand),float(item2_PriceLevel1),float(item2_PriceLevel2),float(item2_PriceLevel3),float(item2_LastTotalUnitCost))
                    #enviando objeto a la lista
                    item_List.insertarFinal(objetoItem)
                
            print("Archivo leído exitosamente\n")
        else :
            print("Opcion cancelada.")
    except Exception as e:
        print("Ha ocurrido un error.")

def topMargenPorNivel():
    print("Top 10 de productos con mayor margen de ganancia\n")
#Agregar que solamente se impriman los primeros 10
    print("**********Nivel 1**********")
    item_List.ordenamientoBurbujaCompuesto("margen level 1")
    item_List.imprimirTop()

    print("\n**********Nivel 2**********")
    item_List.ordenamientoBurbujaCompuesto("margen level 2")
    item_List.imprimirTop()
    print("\n**********Nivel 3**********")
    item_List.ordenamientoBurbujaCompuesto("margen level 3")
    item_List.imprimirTop()

def topValor():
    #Imprimir por  mayor valor del inventario
    item_List.ordenamientoBurbujaCompuesto("valor inventario")
    item_List.imprimirTop()

def opciones():
    opcionesMenu = '''
    ------- Menu Principal --------
    1. Cargar archivo xml
    2. Top 10 de productos con mayor margen de ganancia.
    3. Top 10 de productos con mayor valor del inventario.
    4. Imprimir datos.
    5. Salir.
    '''
    print(opcionesMenu)

if __name__ == '__main__':
    while True:
        try:
            opciones()
            # recibe la opcion ingresada y la guarda como entero
            opcion = int(input("Ingrese una opcion: "))
            print()
            if opcion == 1:
                cargarArchivo()
            elif opcion == 2:
                validarVacia = item_List.estaVacia()
                if validarVacia == True:
                    topMargenPorNivel()
                elif validarVacia == False:
                    print(
                        "Por favor cargue un archivo ya que no hay datos para procesar")
            elif opcion == 3:
                validarVacia1 = item_List.estaVacia()
                if validarVacia1 == True:
                    topValor()
                elif validarVacia1 == False:
                    print("Por favor cargue un archivo ya que no hay datos para procesar")
            elif opcion == 4:
                validarVacia1 = item_List.estaVacia()
                if validarVacia1 == True:
                    item_List.imprimir()
                elif validarVacia1 == False:
                    print("Por favor cargue un archivo ya que no hay datos para procesar")
            elif opcion == 5:
                sys.exit()
            else:
                print("Ingrese una opcion correcta")
        except ValueError:
            print("\nPor favor ingrese solo numeros")
