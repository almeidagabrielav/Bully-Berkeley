import threading
import time

class Relogio(threading.Thread):
    def __init__(self, incremento):
        self.incremento = incremento
        self.tempo = 0
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.tempo += self.incremento
            time.sleep(1)

    def pegarTempo(self):
        return self.tempo

    def atualizarTempo(self, atualizacao):
        self.tempo = atualizacao