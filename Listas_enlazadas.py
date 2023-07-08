
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
        #Nos paramos en el 1er nodo de la lista
        nodo = Nodo()
        nodo=self.head

        #Lista para poner los nodos pasados a string
        lista = []

        #Recorremos la lista enlazada
        while nodo is not None:
            #Agregamos el nodo actual a la lista en formato str
            lista.append(str(nodo.dato))
            nodo = nodo.prox
        return "\n".join(lista)
    
    def append(self,nodo:Nodo):
        if(self.len==0):
            #Si la lista está vacía, el nodo ingresado será el head
            self.head=nodo
        else:
            #Nos movemos hasta el final de la lista
            nodomov=Nodo()
            nodomov=self.head
            while(nodomov.prox!=None):
                nodomov=nodomov.prox
            #Ahora el último de la lista será el ingresado
            nodomov.prox=nodo

        #Ahora la lista es más larga
        self.len+=1
    
    #ORDENA EL NUEVO OBJETO
    def ordenar(self):
        #Nos paramos en el 1er elemento
        nodo_mov1=Nodo()
        nodo_mov1=self.head
        
        if nodo_mov1.prox==None:
            return self
        
        #Nos movemos al siguiente nodo hasta el final de la lista
        while nodo_mov1.prox.prox is not None:
            nodo_mov1 = nodo_mov1.prox
        nuevo_nodo=nodo_mov1.prox
        nodo_mov1.prox=None
        
        #Volveremos a recorrer la lista desde el principio con un nuevo nodo
        nodo_mov2=self.head

        #Ahora comparamos el nodo actual con el próximo para ver cómo ordenar
        while nodo_mov2.prox!=None and nodo_mov2.prox.dato.posicion < nuevo_nodo.dato.posicion :
            nodo_mov2 = nodo_mov2.prox

        #Ponemos al nodo en la posición adecuada
        nuevo_nodo.prox=nodo_mov2.prox
        nodo_mov2.prox=nuevo_nodo
        #Devolvemos la lista ordenada
        return self
    
    def pop_ints(self,dato_a_eliminar: int):
        nodo=Nodo()
        nodo=self.head

        #Recorremos la lista
        while nodo.prox is not None:
            #Si encontramos el nodo que queremos eliminar
            if nodo.dato==dato_a_eliminar:
                #Cambiamos el enlace para desprendernos el nodo elegido
                nodo.prox=nodo.prox.prox
                print(f'Se ha eliminado correctamente {dato_a_eliminar}')
            nodo = nodo.prox

        #Devolvemos la lista                 
        return self
    
    def pop(self,input_principal,atributo_principal):  #INPUT PRINCIPAL: VARIABLE QUE INGRESA EL USUARIO   ATRIBUTO_PRINCIPAL "POSICION"
        nodo=Nodo()
        nodo=self.head

        #Recorremos la lista
        for i in range(self.len-1):
            if i==0 and getattr(nodo.dato,atributo_principal)==input_principal:
                #Si el nodo a eliminar es el Head
                self.head=nodo.prox
                self.len-=1
                return True
            elif getattr(nodo.prox.dato,atributo_principal)==input_principal:
                #Caso contrario, cambiamos el enlace para desprendernos el nodo elegido
                nodo.prox=nodo.prox.prox
                self.len-=1
                return True
            nodo=nodo.prox

        #Si no se pudo eliminar correctamente
        return False

    def buscar_inst_anterior(self,input_principal, atributo_principal):
        nodo=Nodo()
        nodo=self.head

        #Recorremos la lista desde el head
        for i in range(self.len-1):
            if getattr(nodo.prox.dato,atributo_principal)==input_principal:
                #Si encontramos el nodo (viendo cuál es el próximo), lo devolvemos
                return nodo
            nodo=nodo.prox
        return False
    
    def buscar_inst(self,input_principal, atributo_principal):
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len):
            if getattr(nodo.dato,atributo_principal)==input_principal:
                #Si encontramos el nodo, lo devolvemos
                return nodo
            nodo=nodo.prox
        return False