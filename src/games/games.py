class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        weapons = ['piedra','papel','tijera']
        
        jugador1 = jugador1.lower();
        
        jugador2 = jugador2.lower();
        if jugador1 not in weapons or jugador2 not in weapons:
            return "invalid";
    
        if jugador1 == jugador2:
            return "empate";

        rules = {
            'piedra':'tijera',
            'tijera':'papel',
            'papel': 'piedra'
        }
        if rules[jugador1] == jugador2:
            return 'jugador1';
        else:
            return 'jugador2';

        # elif jugador1 == "piedra":
        #     if jugador2 == "papel":
        #         return "jugador2";
        #     if jugador2 == "tijera":
        #         return "jugador1";
        # elif jugador1 == "papel":
        #     if jugador2 == "tijera":
        #         return "jugador2";
        #     if jugador2== "tijera":
        #         return "jugador1";
        # elif jugador1 == "tijera":
        #     if jugador2 == "piedra":
        #         return "jugador2";
        #     if jugador2 == "papel":
        #         return "jugador1";
           


            

    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        pass
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        pass
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        pass
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        pass

show = Games();
print(show.piedra_papel_tijera("Tijera","papel"));