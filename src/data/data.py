class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        size = len(lista);

        invert = [];
        for i in range(1, size+1 , 1):
            invert.append(lista[-i]);

        for i in invert:

            print (i);
        return invert;

    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        i = 0;
        for indx in lista:

            if indx == elemento:

                return i;
            i = i +1;        

        return -1;
        
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        unicElements = [];

        for i in range(len(lista)):
            if not any(lista[i] is x for x in unicElements):
                unicElements.append(lista[i]);
        return unicElements;
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        # def listMix(list1,list2):
        #     return sorted(list1+list2)
        def orderedList(list):
            n = len(list)
            for i in range(n):
                for j in range(0,n-i-1):
                    if list[j] > list[j+1]:
                        list[j], list[j+1] = list[j+1], list[j];
            return list;

        orList1 = orderedList(lista1);
        orList2 = orderedList(lista2);
        result = orList1 + orList2;
        orResult = orderedList(result); 
        return orResult;

    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        size = (len(lista));
        # aux = [];
        # for i in range(size):
        #     value = (lista[i]+k)%size+1;
        #     aux.append(value);
        # lista = aux;
        try:
            k = k % size;
            return lista[-k:] + lista[:-k];
        except:
            return [];

    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        
        def sum(lista):    
            sum = 0;
            for i in lista:
                sum = sum  +  i; 
            return sum;
        sumTi = sum(lista);
        size = len(lista)+1;
        def sumT(size):
            return ((size * (size + 1))//2);

        result = - sum(lista) + sumT(size);
        return result;


    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for i in conjunto1:
            if i not in conjunto2:
                return False;
        return True;
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass


show = Data();



lis1 = [1,2,3,5,6,7];
k = 3;

print(type(show.encuentra_numero_faltante(lis1)));
print(show.encuentra_numero_faltante(lis1));