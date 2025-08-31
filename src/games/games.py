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
        if numero_secreto == intento :
            return "correcto";
        elif numero_secreto < intento:
            return "muy alto";
        elif numero_secreto > intento:
            return "muy bajo"
    
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
        print(tablero);
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
                return tablero[i][0];
        for i in range(3):
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
                return tablero[0][i];
    
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
            return tablero[0][0];
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
            return tablero[0][2];
            
        for i in tablero:
            if ' ' in i:
                return 'continua';
        
        # Test juego continúa (tablero incompleto sin ganador)
        # tablero_continua = [["X", "O", " "], [" ", "X", "O"], ["O", " ", "X"]]
        # assert self.games.ta_te_ti_ganador(tablero_continua) == "continua"
        return "empate";

        
        
        
    
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
        mix = [];

        for i in range(longitud):
            color = colores_disponibles[0];
            mix.append(color);
        return mix;
            



    
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
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila <8 and 0<= hasta_col < 8):
            # fuera de tablero
            return False;
    
        if desde_fila == hasta_fila and desde_col == hasta_col:
            # no es correcto movimiento en la misma casilla
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            print("no es movimiento lineal-primer condicional evaluado-");
            return False;


        if desde_fila == hasta_fila:
            aux = 0;
            if hasta_col > desde_col:
                aux = 1;
            else:
                aux = -1;

            for c in range(desde_col + aux, hasta_col, aux):
                print(f"watch space in {desde_fila}, {c}");
                if tablero[desde_fila][c] != ' ':
                    
                    return False
        else:
            if hasta_col > desde_col:
                aux = 1;
            else:
                aux = -1;
            for f in range(desde_fila + aux, hasta_fila,aux):
                print(f"watch space in {desde_fila}, {f}");
                if tablero[f][desde_col] != ' ':
                    
                    return False;
        
        print("valid movement");
        return True;

        

show = Games();

# print(show.piedra_papel_tijera("Tijera","papel"));
# tablero_continua = [["X", "O", " "], [" ", "X", "O"], ["O", " ", "X"]];


# print(show.ta_te_ti_ganador(tablero_continua));
# print(type(show.ta_te_ti_ganador(tablero_continua)));

# colores = ["rojo", "azul", "verde", "amarillo"];

# print(show.generar_combinacion_mastermind( 4 , colores ));

# print(show.adivinar_numero_pista(-10, -5));
tablero_vacio = [[" " for _ in range(8)] for _ in range(8)];

for i in tablero_vacio:
    print(i);

print(show.validar_movimiento_torre_ajedrez(0,0,1,1,tablero_vacio));
print(type(show.validar_movimiento_torre_ajedrez(0,0,1,1,tablero_vacio)));
