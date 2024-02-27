

class Control:
    def __init__(self, tv):
        self.tv = tv

    def enlazar(self, tv):
        tv.setControl(self) 

    def turnOn(self, estado):
        self.estado = True

    def turnOff(self, estado):
        self.estado = False
    
    def canalUp(self, canal):
        self.canal += 1

    def canalDown(self, canal):
         self.canal -= 1
    
    def volumenUp(self, volumen):
        self.volumen += 1
    
    def volumenDown(self, volumen):
        self.volumen -= 1

    def setCanal(self, canal):
        if self.estado == True:
            if (self.canal and canal >=1) and (canal<=120):
                self.canal = canal
                return self.canal
        
    def setVolumen(self, volumen):
        if self.estado == True:
            if (self.volumen and volumen >= 0) and (volumen<= 7):
                self.volumen = volumen
                return self.volumen

    def setTv(self, tv):
        self.tv = tv    

    def getTv(self):
        return self.tv
    
    def getVolumen(self):
        return self.volumen
    
    def getCanal(self):
        return self.canal



    

        


    

        
