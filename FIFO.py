# importa a biblioteca random para randomizar as bursts
import random
# importa o deque para implementar a fila
from collections import deque

tempo_atual = 0
soma_espera = 0
total_processos = 0

class Queue:
    def __init__(self): # inicia
        self.items = deque()

    def isEmpty(self): # verifica se a fila está vazia
        return len(self.items) == 0

    def inQueue(self, item): #adiciona
        self.items.append(item)

    def outQueue(self): # remove
        return self.items.popleft()

    def size(self): # tamanho da fila
        return len(self.items)

    def printQueue(self): # printa a fila
        for item in self.items:
            print(f"P{item['pid']}", end=" -> ")
        print("FIM\n")


# cria a fila
q = Queue()

# lista de processos (pid = Process ID, arrival = tempo de chegada, burst = tempo de execução)
p1 = {'pid': 1, 'arrival': 0, 'burst': random.randint(1, 20)}
p2 = {'pid': 2, 'arrival': 2, 'burst': random.randint(1, 20)}
p3 = {'pid': 3, 'arrival': 4, 'burst': random.randint(1, 20)}
p4 = {'pid': 4, 'arrival': 6, 'burst': random.randint(1, 20)}
p5 = {'pid': 5, 'arrival': 8, 'burst': random.randint(1, 20)}
p6 = {'pid': 6, 'arrival': 10, 'burst': random.randint(1, 20)}
p7 = {'pid': 7, 'arrival': 12, 'burst': random.randint(1, 20)}
p8 = {'pid': 8, 'arrival': 14, 'burst': random.randint(1, 20)}
p9 = {'pid': 9, 'arrival': 16, 'burst': random.randint(1, 20)}
p10 = {'pid': 10, 'arrival': 18, 'burst': random.randint(1, 20)}

# ordem de chegada dos processos
processos = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
for proc in processos:
    q.inQueue(proc)


# printa o tamanho e os itens da fila
print(f"\nTotal de processos: {len(q.items)}")
q.printQueue()

print("Execução dos processos:")
while not q.isEmpty():
    proc = q.outQueue()
    total_processos += 1

    # atualiza o tempo atual se  for menor que o arrival do processo
    if tempo_atual < proc['arrival']:
        tempo_atual = proc['arrival']

    # tempo de espera (tempo atual - arrival do processo)
    espera = tempo_atual - proc['arrival']

    # printa o processo em execução e o tempo de espera (utilizei ajuda para deixar o texto da saída bonitinho)
    print(f"> P{proc['pid']} executando de {tempo_atual} até {tempo_atual + proc['burst']} (tempo de execução = {proc['burst']})")
    print(f"--- Tempo de espera do P{proc['pid']}: {espera}\n")


    # soma o tempo de espera e atualiza o tempo atual
    soma_espera = soma_espera + espera
    tempo_atual = tempo_atual + proc['burst']

# calcula o tempo médio e printa o resultado
media_espera = soma_espera / total_processos
print(f"Tempo médio de espera = {media_espera}\n")
