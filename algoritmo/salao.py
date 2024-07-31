class Salao:
    def __init__(self, largura, altura, obstaculos):
        self.largura = largura
        self.altura = altura
        self.obstaculos = obstaculos

    def valido(self, x, y):
        # Verifica se a posição é válida e não é um obstáculo
        if not (0 <= x < self.largura and 0 <= y < self.altura):
            return False
        if self.obstaculos[y][x]:
            return False
        
        # Verifica se a posição é adjacente a um obstáculo
        adjacentes = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x + 1, y + 1)
        ]
        for adj_x, adj_y in adjacentes:
            if 0 <= adj_x < self.largura and 0 <= adj_y < self.altura and self.obstaculos[adj_y][adj_x]:
                return False
        return True

    def custo_total(self, estado, objetivo):
        return 1  # Custo base é sempre 1 para simplificar

    def heuristica(self, estado, objetivo):
        dx = abs(estado.x - objetivo.x)
        dy = abs(estado.y - objetivo.y)
        return dx + dy  # Heurística de Manhattan
