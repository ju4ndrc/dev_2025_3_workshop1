
class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La media aritmética de los números
            
        Ejemplo:
            promedio([1, 2, 3, 4, 5]) -> 3.0
        """
        sum = 0;
        for i in numeros:
            sum = sum + i;
        if sum == 0:
            return 0;
        else:
            result = sum / len(numeros) 
            return result
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: El valor mediano
             
        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        if numeros == []:
            return 0;
        orderedList = sorted(numeros);
        n = len(numeros)
        if n % 2 != 0:
            central_index = n // 2;
            mediana = orderedList[central_index];
        else:
            index1 = (n//2)-1
            index2 = n//2
            value1 = orderedList[index1]
            value2 = orderedList[index2]
            mediana = (value1 + value2)/2
        return mediana
        
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        frecuenci = {}
        if numeros == []:
            return None;
        for i in numeros:
            frecuenci[i] = frecuenci.get(i, 0) + 1
        max_frecuenci = 0
        moda_value = 0
        for i in frecuenci:
            if frecuenci[i] > max_frecuenci:
                max_frecuenci = frecuenci[i]
                moda_value = i
        return moda_value
        
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        if numeros == []:
            return 0;
        n = len(numeros)
        sum = 0
        for i in numeros:
            sum = sum + i;
        media = sum / n

        square_sum = 0
        for i in numeros:
            diference = i - media;
            square_sum = square_sum + diference ** 2

        variance = square_sum /n
        desviacion = variance ** 0.5
        return desviacion
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        if numeros == []:
            return 0;
        n = len(numeros)
        sum = 0
        for i in numeros:
            sum = sum + i;
        media = sum / n

        square_sum = 0
        for i in numeros:
            diference = i - media;
            square_sum = square_sum + diference ** 2

        variance = square_sum /n
        
        return variance
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        if numeros == []:
            return 0;
        max = numeros[0]
        min = numeros[0]
        for i in numeros:
            if i > max:
                max = i
            if i < min:
                min = i
        return max - min;
        

show = Stats()
print(show.desviacion_estandar([1, 2, 3, 4, 5]))