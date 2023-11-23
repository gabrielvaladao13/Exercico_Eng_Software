class MRU:
    def __init__(self, distancia=None, tempo=None, velocidade=None):
        self.distancia = distancia
        self.tempo = tempo
        self.velocidade = velocidade

    def calcular_velocidade(self):
        if self.tempo is not None and self.velocidade is not None and self.distancia is None:
            self.distancia = self.tempo * self.velocidade
            return self.velocidade

    def calcular_tempo(self):
        if self.distancia is not None and self.velocidade is not None and self.tempo is None:
            self.tempo = self.distancia / self.velocidade
            return self.tempo

    def calcular_distancia(self):
        if self.tempo is not None and self.velocidade is not None and self.distancia is None:
            self.distancia = self.tempo * self.velocidade
            return self.distancia
        
    def converter_para_metros_por_segundo(self):
        if self.velocidade is not None:
            return self.velocidade * 1000 / 3600
        else:
            raise ValueError("A velocidade deve ser calculada antes de converter para metros por segundo.")

    def converter_para_kilometros_por_hora(self):
        if self.velocidade is not None:
            return self.velocidade * 3600 / 1000
        else:
            raise ValueError("A velocidade deve ser calculada antes de converter para quilômetros por hora.")

    def imprimir_resultados(self):
        print(f'Distancia: {self.distancia} km')
        print(f'Tempo: {self.tempo} horas')
        print(f'Velocidade: {self.velocidade} km/h')
        print(f'Velocidade em metros por segundo: {self.converter_para_metros_por_segundo()} m/s')

