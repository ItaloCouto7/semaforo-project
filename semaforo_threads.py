import threading
import time

class Semaforo:
    def __init__(self, verde, amarelo, vermelho):
        self.verde = verde
        self.amarelo = amarelo
        self.vermelho = vermelho

    def iniciar(self):
        while True:
            print("🟢 Verde - Siga")
            time.sleep(self.verde)

            print("🟡 Amarelo - Atenção")
            time.sleep(self.amarelo)

            print("🔴 Vermelho - Pare")
            time.sleep(self.vermelho)

tempo_verde = 5
tempo_amarelo = 2
tempo_vermelho = 7

semaforo = Semaforo(tempo_verde, tempo_amarelo, tempo_vermelho)

thread = threading.Thread(target=semaforo.iniciar)
thread.start()
