from network import Network
from relogio import Relogio
import sys
import getopt

def main(argv):
    r = Relogio(incremento = 1)
    r.start()
    coord = False

    if len(argv) != 0 and argv[0] == 'coord':
        coord = True

    if coord:
        print('Eu sou o coordenador')
        while True:
            p.send(data = str.encode('pegarTempo'))
            clientes = []
            try:
                while True:
                    msg, cliente = p.recv()
                    print(msg.decode(), cliente) 

                    if cliente[0] == p.DEFAULT_HOST:
                        msg = str.encode(str(r.pegarTempo()))

                    clientes.append((msg, cliente))
            except:
                print('Tempo esgotado, calculando novo valor do relogio...\n\n')
                tempo = 0
                qtd = 0
                for linha in clientes:
                    msg, _ = linha
                    tempo += int(msg.decode())
                    qtd += 1
                
                if qtd != 0:
                    final = tempo/qtd
                    p.send(data = str.encode('atualizar:'+str(int(final))))
                
                msg, cliente = p.recv()
                print(msg.decode(), cliente)

                comando = msg.decode().split(':')
                r.atualizarTempo(int(comando[1]))
                print('Tempo atualizado para: ', r.pegarTempo())
                print('\n\n')
    else:
        while True:
            try:
                msg, cliente = p.recv()
                print(msg.decode(), cliente)

                comando = msg.decode().split(':')

                if comando[0] == 'pegarTempo':
                    p.send(data = str.encode(str(r.pegarTempo())), address = cliente)
                elif comando[0] == 'atualizar':
                    r.atualizarTempo(int(comando[1]))
            except:
                print("Aguardando...\n")

if __name__ == "__main__":
   main(sys.argv[1:])