from itertools import chain
class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        result = 0;
        num = 0;
        a = 1;

        if n == 0 :
            return 0;
        else:
    
            for _ in range(n):
            
                result = num + a;
                
                num = a;
                a = result;
            
            return num;
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        
        result = 0;
        num = 0;
        a = 1;
        sec = [0];

        if n == 1 :
            return  [0];
        else:
    
            for _ in range(n-1):
            
                result = num + a;
                
                num = a;

                a = result;
                sec.append(num);
            
            return sec;
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
            return False;
        else:
            for i in range(2,n):
                if n % i == 0:
                    return False;
        return True;
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """

        cousins = [];
        if n <= 1:
            return [];
        else:
            for i in range(2,n+1):

                is_p = True;
                for j in range(2,i):
                    if i % j == 0:
                        is_p = False;
                        break
                if is_p:
                    cousins.append(i);

            return cousins; 
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        i = 2;
        sum = 0;
        while i <= n:
            if n % i == 0:
                sum = sum + n //i;
            i = i+1;
        if n <= 1:
            return False;
        if sum == n:
            return True;
        else:
            return False;

    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        row = [1]
        result = []
        for _ in range(filas):
            result.append(row);
            row = [i + j for i, j in zip([0] + row , row + [0])]
   
        return result;

    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        aux = 1;

        for i in range(1, n + 1):
        
            aux = aux * i;   
        
        return aux;        
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        mcd = 1;

        if a % b == 0 :
            return b;
        for i in range(int(b/2), 0 ,-1):
            if a % i == 0 and b % i == 0:
                mcd = i   
                break         
        return mcd;
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if b == 0:
            return b; 
        if a > b:
            max = a
        else:
            max = b
        while(True):
            if((max % a == 0) and (max % b == 0)):
                mcm = max
                break
            max = max + 1;
        return mcm;

    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        sum = 0;
        while n > 0:
            digit = n % 10
            sum = sum + digit
            n = n // 10
        return sum;
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        conv = str(n);
        acum = 0;
        for i in range(len(conv)):
            acum = acum + (int(conv[i])**len(conv))
        if acum == n:
            return True;
        else:
            return False;
    


    def es_cuadrado_magico(self, matriz):
        def diferentElemnets(matriz):
            num = list(chain(*matriz))
            return len(set(num)) == len(num)

        if len(matriz) != len(matriz[0]):
            return False  # No es cuadrada

        if not diferentElemnets(matriz):
            return False  # Elementos repetidos

        target_sum = sum(matriz[0])

        # Verificar filas
        for fila in matriz:
            if sum(fila) != target_sum:
                return False

        # Verificar columnas
        for j in range(len(matriz[0])):
            columna = [matriz[i][j] for i in range(len(matriz))]
            if sum(columna) != target_sum:
                return False

        # Verificar diagonal principal
        diagonalP = [matriz[i][i] for i in range(len(matriz))]
        if sum(diagonalP) != target_sum:
            return False

        # Verificar diagonal secundaria
        diagonalS = [matriz[i][len(matriz)-1-i] for i in range(len(matriz))]
        if sum(diagonalS) != target_sum:
            return False

        return True



        

show = Magic();
# print(show.secuencia_fibonacci(2));
# print(show.es_numero_perfecto(28));
print(show.factorial(5));