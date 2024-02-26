class Marca:
    def __init__(self, nombre, marca):
        self.nombre = nombre 
        self.marca = marca

        def getNombre (self):
            return self.nombre
        
        def setNombre(self, nombre):
            self.nombre = nombre 

        def getMarca (self):
            return self.marca
        
        def setMarca(self,marca):
            self.marca = marca 

class TV:
    def __init__(self, marca, canal, precio, estado, volumen, control):
        self.marca = marca
        self.canal = canal
        self.precio = precio
        self.estado = estado
        self.volumen = volumen
        self.control = control
        numTV = 0

        def __init__(self, marca, estado):
            self.marca = marca
            self.estado = estado
            canal = 1
            volumen = 1
            precio = 500

            def setMarca(self, marca):
                self.marca = marca 

            def getMarca(self):
                return self.marca
            
            def setCanal(self, canal):
                self.canal = canal

            def getCanal(self):
                return self.canal
            
            def setPrecio(self, precio):
                self.precio = precio
            
            def getPrecio(self):
                self.precio = precio

            def setVolumen(self, volumen):
                self.volumen = volumen

            def getVolumen(self):
                return self.volumen
            
            def setControl(self, control):
                self.control = control

            def getControl(self):
                return self.control
            
        def turnOn(self, estado):
                self.estado = True
            
        def turnOff(self, estado):
                self.estado = False
            
        def getEstado(self):
            return self.estado

        def canalUp(self, canal):
            self.canal += 1

        def canalDown(self, canal):
            self.canal -= 1

        def volumenUp(self, volumen):
            self.volumen += 1

        def volumenDown(self, volumen):
            self.volumen -= 1

        def setCanal(self, canal):
            if (self.canal and canal >=1) and (canal<=120) and self.estado == True:
               self.canal = canal 
            return self.canal 
        
        def setVolumen(self, volumen):
            if (self.volumen and volumen >= 0) and (volumen<= 7) and self.estado == True:
                self.volumen = volumen
            return self.volumen
        

class Control:
    def __init__(self, tv):
        self.tv = tv

    def enlazar(self, TV, tv):
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
        if (self.canal and canal >=1) and (canal<=120) and self.estado == True:
            self.canal = canal 
            return self.canal 
        
    def setVolumen(self, volumen):
        if (self.volumen and volumen >= 0) and (volumen<= 7) and self.estado == True:
            self.volumen = volumen
            return self.volumen

    



    

        


    

        
