
class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        """
        Calcula el área de un rectángulo.
        
        Args:
            base (float): Longitud de la base del rectángulo
            altura (float): Altura del rectángulo
            
        Returns:
            float: Área del rectángulo
        """
        return base*altura
    
    def perimetro_rectangulo(self, base, altura):
        """
        Calcula el perímetro de un rectángulo.
        
        Args:
            base (float): Longitud de la base del rectángulo
            altura (float): Altura del rectángulo
            
        Returns:
            float: Perímetro del rectángulo
        """
        return 2*(base+altura);
    
    def area_circulo(self, radio):
        """
        Calcula el área de un círculo.
        
        Args:
            radio (float): Radio del círculo
            
        Returns:
            float: Área del círculo
        """
        return 3.14159*(radio*radio);
    
    def perimetro_circulo(self, radio):
        """
        Calcula el perímetro (circunferencia) de un círculo.
        
        Args:
            radio (float): Radio del círculo
            
        Returns:
            float: Perímetro del círculo
        """
        return ((2*3.14159)*(radio));
    
    def area_triangulo(self, base, altura):
        """
        Calcula el área de un triángulo.
        
        Args:
            base (float): Longitud de la base del triángulo
            altura (float): Altura del triángulo
            
        Returns:
            float: Área del triángulo
        """
        return ((base*altura)/2);
        
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        """
        Calcula el perímetro de un triángulo.
        
        Args:
            lado1 (float): Longitud del primer lado
            lado2 (float): Longitud del segundo lado
            lado3 (float): Longitud del tercer lado
            
        Returns:
            float: Perímetro del triángulo
        """
        return (lado1 + lado2 + lado3);
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        """
        Verifica si tres longitudes pueden formar un triángulo válido.
        Un triángulo es válido si la suma de las longitudes de dos lados
        es mayor que la longitud del tercer lado, para todos los lados.
        
        Args:
            lado1 (float): Longitud del primer lado
            lado2 (float): Longitud del segundo lado
            lado3 (float): Longitud del tercer lado
            
        Returns:
            bool: True si los lados pueden formar un triángulo, False en caso contrario
        """
        if (lado1 + lado2) > lado3 :
            return True;
        
        return False;
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        """
        Calcula el área de un trapecio.
        
        Args:
            base_mayor (float): Longitud de la base mayor
            base_menor (float): Longitud de la base menor
            altura (float): Altura del trapecio
            
        Returns:
            float: Área del trapecio
        """
        result = (((base_mayor + base_menor)/2)*(altura));
        
        return result;
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        """
        Calcula el área de un rombo usando sus diagonales.
        
        Args:
            diagonal_mayor (float): Longitud de la diagonal mayor
            diagonal_menor (float): Longitud de la diagonal menor
            
        Returns:
            float: Área del rombo
        """
        result = ((diagonal_mayor * diagonal_menor )/ 2);
        return result;
    
    def area_pentagono_regular(self, lado, apotema):
        """
        Calcula el área de un pentágono regular.
        
        Args:
            lado (float): Longitud del lado del pentágono
            apotema (float): Longitud de la apotema (distancia del centro al punto medio de un lado)
            
        Returns:
            float: Área del pentágono regular
        """
        perimeter = 5 * lado;
        return ((perimeter * apotema)/2);
    
    def perimetro_pentagono_regular(self, lado):
        """
        Calcula el perímetro de un pentágono regular.
        
        Args:
            lado (float): Longitud del lado del pentágono
            
        Returns:
            float: Perímetro del pentágono regular
        """
        return 5*lado;
    
    def area_hexagono_regular(self, lado, apotema):
        """
        Calcula el área de un hexágono regular.
        
        Args:
            lado (float): Longitud del lado del hexágono
            apotema (float): Longitud de la apotema (distancia del centro al punto medio de un lado)
            
        Returns:
            float: Área del hexágono regular
        """
        perimeter = 6 * lado;
        return (perimeter * apotema / 2);
        
    
    def perimetro_hexagono_regular(self, lado):
        """
        Calcula el perímetro de un hexágono regular.
        
        Args:
            lado (float): Longitud del lado del hexágono
            
        Returns:
            float: Perímetro del hexágono regular
        """
        return 6 * lado;
    
    def volumen_cubo(self, lado):
        """
        Calcula el volumen de un cubo.
        
        Args:
            lado (float): Longitud del lado del cubo
            
        Returns:
            float: Volumen del cubo
        """
        return lado *lado *lado;
    
    def area_superficie_cubo(self, lado):
        """
        Calcula el área de la superficie de un cubo.
        
        Args:
            lado (float): Longitud del lado del cubo
            
        Returns:
            float: Área de la superficie del cubo
        """
        l = lado ** 2;
        return 6* l;
    
    def volumen_esfera(self, radio):
        """
        Calcula el volumen de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Volumen de la esfera
        """
        return (4/3*3.141592653589793*radio**3);
    
    def area_superficie_esfera(self, radio):
        """
        Calcula el área de la superficie de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Área de la superficie de la esfera
        """
        return 4*3.141592653589793*radio**2;
    
    def volumen_cilindro(self, radio, altura):
        """
        Calcula el volumen de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Volumen del cilindro
        """
        return 3.141592653589793*radio**2*altura;
    
    def area_superficie_cilindro(self, radio, altura):
        """
        Calcula el área de la superficie de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Área de la superficie del cilindro
        """
        area = (3.141592653589793*radio**2)*2;
        lateralArea = ((2*(3.141592653589793)*radio)*altura);
        return area + lateralArea;
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        """
        Calcula la distancia euclidiana entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Distancia entre los dos puntos
        """
        abscisas = (x2 - x1)**2 ;
        ordered = (y2 - y1)**2;
        sum = abscisas + ordered;
        raiz = sum ** 0.5;
        return raiz;


    
    def punto_medio(self, x1, y1, x2, y2):
        """
        Calcula el punto medio entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coordenadas (x, y) del punto medio
        """
        abscisa = (x1 + x2)/2;
        ordered = (y1 + y2)/2;
        return (abscisa,ordered);
    
    def pendiente_recta(self, x1, y1, x2, y2):
        """
        Calcula la pendiente de una recta que pasa por dos puntos.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Pendiente de la recta
        """
        abscisa = (x2 - x1);
        ordered = (y2 - y1);
        return ordered/abscisa;
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coeficientes (A, B, C) de la ecuación de la recta
        """
        a = y2 - y1;
        b = x1 - x2;
        c = ((x2 * y1) - (x1 * y2));
        if a == 0:
            return(0,1,-y1);
        return (a,b,c);

        
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el área de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            apotema (float): Longitud de la apotema
            
        Returns:
            float: Área del polígono regular
        """
        pass
    
    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            
        Returns:
            float: Perímetro del polígono regular
        """
        pass

show = Geometria()

print(show.es_triangulo_valido(1, 2, 10));