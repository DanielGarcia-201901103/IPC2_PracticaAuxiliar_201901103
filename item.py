class Item():
    item: str
    quantityOnHand: int
    priceLevel1: float
    priceLevel2: float
    priceLevel3: float
    lastTotalUnitCost: float
    marginLevel1: float
    marginLevel2: float
    marginLevel3: float
    valorInventario : float

    def __init__(self, item, quantityOnHand,priceLevel1,priceLevel2,priceLevel3,lastTotalUnitCost):
        self.item = item
        self.quantityOnHand = quantityOnHand
        self.priceLevel1 = priceLevel1
        self.priceLevel2 = priceLevel2
        self.priceLevel3 = priceLevel3
        self.lastTotalUnitCost = lastTotalUnitCost
        self.marginLevel1 = self.__calcularMargenes(self.priceLevel1,self.lastTotalUnitCost)
        self.marginLevel2 = self.__calcularMargenes(self.priceLevel2,self.lastTotalUnitCost)
        self.marginLevel3 = self.__calcularMargenes(self.priceLevel3,self.lastTotalUnitCost)
        self.valorInventario = self.__calcularValorInventario()

    def __calcularMargenes(self, precio, costo):
        if costo !=0:
            margen = ((precio - costo)/costo) * 100 
            resultado = round(margen, 2)
            return resultado

    def __calcularValorInventario(self):
        valor = self.lastTotalUnitCost * self.quantityOnHand
        resultado = round(valor, 2)
        return resultado