from MRU import MRU
import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
import io  
class TestMRU(unittest.TestCase):
    def setUp(self):
        self.mru = MRU()

    def test_calcular_velocidade(self):
        self.mru.tempo = 2
        self.mru.velocidade = 5
        self.assertEqual(self.mru.calcular_velocidade(), 5)
        self.assertEqual(self.mru.distancia, 10)

    def test_calcular_tempo(self):
        self.mru.distancia = 15
        self.mru.velocidade = 3
        self.assertEqual(self.mru.calcular_tempo(), 5)
        self.assertEqual(self.mru.tempo, 5)

    def test_calcular_distancia(self):
        self.mru.tempo = 4
        self.mru.velocidade = 6
        self.assertEqual(self.mru.calcular_distancia(), 24)
        self.assertEqual(self.mru.distancia, 24)

    def test_converter_para_metros_por_segundo(self):
        self.mru.velocidade = 10
        self.assertEqual(self.mru.converter_para_metros_por_segundo(), 10/3.6)

    def test_converter_para_kilometros_por_hora(self):
        self.mru.velocidade = 5
        self.assertEqual(self.mru.converter_para_kilometros_por_hora(), 5*3600/1000)

    def test_imprimir_resultados(self):
        self.mru.distancia = 20
        self.mru.tempo = 2
        self.mru.velocidade = 10
        expected_output = (
            f'Distancia: 20 km\n'
            f'Tempo: 2 horas\n'
            f'Velocidade: 10 km/h\n'
            f'Velocidade em metros por segundo: {10 * 1000 / 3600} m/s'
        )
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.mru.imprimir_resultados()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()