class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """

        
        formula = (celsius * 9/5) +32
        return formula;
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        formula = (fahrenheit-32)*5/9;
        return formula;
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        f = metros / 0.3048;
        return f;
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        f = (pies/3.2808399);
        
        return f;
    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """

        mod = [];
        if(decimal == 0):
            return "0";

        while(decimal != 0):
            bit = decimal % 2; 
            
            cos = decimal // 2;
            
            mod.append(bit);
            
            decimal = cos;
        
        # invert = [];

        # for i in range(1, len(mod)+1,1):
        #     invert.append(mod[-i])

        # modS = "";
        # for i in invert:
        #     modS = modS + str(i)

        bin = "".join(str(bit) for bit in mod[::-1]);

        return bin;

    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        s = 0;
        
        i = 0;
        bin = int(binario);

        while(bin >= 1):
            d = bin%10;
            bin=int(bin/10);
            s = s + d * pow(2,i);
            i = i + 1; 

        
 
        return s;
    
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
        numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'];
    
        romanNumeral = '';
        i = 0;
        while numero > 0:
            for _ in range(numero // nums[i]):
                romanNumeral = romanNumeral + numerals[i];
                numero = numero - nums[i];

            i = i + 1;
        return romanNumeral;
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        pass
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        pass
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        pass


show = Conversion();

print("Result:",show.decimal_a_romano(9),"\n data Type:",type(show.decimal_a_romano(9)));
