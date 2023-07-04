
class Nodo():
    def __init__(self,dato=None,prox=None):
        self.dato=dato
        self.prox=prox
    def __str__(self) -> str:
        return self.dato.__str__() # Especificas como queres que se printee
    
class Lista():
    def __init__(self):
        self.head=None
        self.len=0
    def __str__(self):
        nodo = Nodo()
        nodo=self.head
        lista = []
        while nodo is not None:
            lista.append(str(nodo.dato))
            nodo = nodo.prox
        return "\n".join(lista)
    
    def append(self,nodo:Nodo):
        if(self.len==0):
            self.head=nodo
        else:
            nodomov=Nodo()
            nodomov=self.head
            while(nodomov.prox!=None):
                nodomov=nodomov.prox
            nodomov.prox=nodo   #muy bueno
        self.len+=1
        
    def pop(self,input_principal,atributo_principal):  #INPUT PRINCIPAL: VARIABLE QUE INGRESA EL USUARIO   ATRIBUTO_PRINCIPAL "DNI"
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len-1):
            if i==0 and getattr(nodo.dato,atributo_principal)==input_principal:
                self.head=nodo.prox
                self.len-=1
                return True
            elif getattr(nodo.prox.dato,atributo_principal)==input_principal:
                nodo.prox=nodo.prox.prox
                self.len-=1
                return True
            nodo=nodo.prox
        return False
    
    def buscar_inst(self,input_principal, atributo_principal):
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len):
            if getattr(nodo.dato,atributo_principal)==input_principal:
                return nodo.dato
            nodo=nodo.prox
        return False

    def buscar_attr(self,input_principal, atributo_principal,atributo_a_buscar):
        dato = self.buscar_inst(input_principal, atributo_principal)
        if dato:
            return getattr(dato,atributo_a_buscar)
        return False 
        
    def actualizar_le(self,input_principal, atributo_principal,atributo_a_buscar,nuevo_input):
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len):
            
            if getattr(nodo.dato,atributo_principal)==input_principal:
                setattr(nodo.dato, atributo_a_buscar,nuevo_input)
        
                return True
            nodo=nodo.prox
        
        return False