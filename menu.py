import sys
from tkinter import filedialog
import xml.etree.cElementTree as ET
from listaSimple import ListaSimple
from item import Item
import colorama
from colorama import Fore
from colorama import Style
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
                
            print(Fore.GREEN +"Archivo leído exitosamente\n"+ Style.RESET_ALL)
        else :
            print(Fore.RED+"Opcion cancelada."+ Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + Style.DIM +"Ha ocurrido un error."+ Style.RESET_ALL)

def topMargenPorNivel():
    print(Fore.GREEN + Style.BRIGHT +"Top 10 de productos con mayor margen de ganancia.\n"+ Style.RESET_ALL)
#Agregar que solamente se impriman los primeros 10
    print(Fore.BLUE + Style.BRIGHT +"**********Nivel 1**********"+ Style.RESET_ALL)
    item_List.ordenamientoBurbujaCompuesto("margen level 1")
    item_List.imprimirTop()

    print(Fore.BLUE + Style.BRIGHT +"\n**********Nivel 2**********"+ Style.RESET_ALL)
    item_List.ordenamientoBurbujaCompuesto("margen level 2")
    item_List.imprimirTop()
    print(Fore.BLUE + Style.BRIGHT +"\n**********Nivel 3**********"+ Style.RESET_ALL)
    item_List.ordenamientoBurbujaCompuesto("margen level 3")
    item_List.imprimirTop()

def topValor():
    #Imprimir por  mayor valor del inventario
    print(Fore.GREEN + Style.BRIGHT +"\nTop 10 de productos con mayor valor del inventario."+ Style.RESET_ALL)
    item_List.ordenamientoBurbujaCompuesto("valor inventario")
    item_List.imprimirTop()

def opciones():
    opcionesMenu = '''
==========================================================
    -------------- Menu Principal ---------------
    1. Cargar archivo xml
    2. Top 10 de productos con mayor margen de ganancia.
    3. Top 10 de productos con mayor valor del inventario.
    4. Imprimir datos.
    5. Salir.
==========================================================
    '''
    print(Fore.YELLOW +opcionesMenu+Style.RESET_ALL)

if __name__ == '__main__':
    while True:
        try:
            colorama.init()
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
                    print(Fore.RED + Style.DIM +
                        "Por favor cargue un archivo ya que no hay datos para procesar"+ Style.RESET_ALL)
            elif opcion == 3:
                validarVacia1 = item_List.estaVacia()
                if validarVacia1 == True:
                    topValor()
                elif validarVacia1 == False:
                    print(Fore.RED + Style.DIM +"Por favor cargue un archivo ya que no hay datos para procesar"+ Style.RESET_ALL)
            elif opcion == 4:
                validarVacia1 = item_List.estaVacia()
                if validarVacia1 == True:
                    item_List.imprimir()
                elif validarVacia1 == False:
                    print(Fore.RED + Style.DIM +"Por favor cargue un archivo ya que no hay datos para procesar"+ Style.RESET_ALL)
            elif opcion == 5:
                sys.exit()
            else:
                print(Fore.RED + Style.DIM +"Ingrese una opcion correcta"+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + Style.DIM +"\nPor favor ingrese solo numeros"+ Style.RESET_ALL)
