import threading
import collections
import time
import random

# Recursos compartilhados
buffer = collections.deque()
mutex = threading.Lock()
items = threading.Semaphore(0)
buffer_size = 10
spaces = threading.Semaphore(buffer_size)

# Configuração do experimento
num_producers = 2
num_consumers = 2
items_to_produce = 5

# Produz os itens e adiciona ao buffer
def producer(producer_id):
    for i in range(items_to_produce):
        item = f"Item-{producer_id}-{i}"
        time.sleep(random.uniform(0.01, 0.1))  # Simulando trabalho NÃO-ASSÍNCRONO

        spaces.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Producer {producer_id} produced {item}")
        mutex.release()
        items.release()

# Consome os itens adicionados ao buffer pelo produtor
def consumer(consumer_id):
    while True:
        items.acquire()
        mutex.acquire()
        if not buffer:
            mutex.release()
            # Aqui existe um possivel problema de lógica, mas para simplificação, vamos apenas
            # assumir que isso indica que os produtores terminaram.
            break
        item = buffer.popleft()
        print(f"Consumer {consumer_id} consumed {item}")
        mutex.release()
        spaces.release()
        time.sleep(random.uniform(0.05, 0.15)) # Simulando trabalho NÃO-ASSÍNCRONO

if __name__ == "__main__":
    start_time = time.time()

    producers = []
    consumers = []

    # Cria e inicia produtores e consumidores
    for i in range(num_producers):
        p = threading.Thread(target=producer, args=(i,))
        producers.append(p)
        p.start()
    for i in range(num_consumers):
        c = threading.Thread(target=consumer, args=(i,))
        consumers.append(c)
        c.start()

    # Espera os produtores produzirem os items
    for p in producers:
        p.join()

    # Sinaliza os consumidores para que a produção acabou
    # Esta é uma maneira mais simples de finalizar o serviço dos consumidores.
    # Uma solução mais robusta poderia usar uma flag por exemplo.
    for _ in range(num_consumers):
        items.release() # Chama os consumidores que estiverem esperando

    # Espera os consumidores terminarem
    for c in consumers:
        c.join()

    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time:.4f} seconds")
