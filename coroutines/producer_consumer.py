import asyncio
import time
import random

# Configuração do experimento
num_producers = 2
num_consumers = 2
items_to_produce = 5
buffer_size = 10

# Produz os itens e adiciona ao buffer
async def producer(producer_id, queue):
    for i in range(items_to_produce):
        item = f"Item-{producer_id}-{i}"
        await asyncio.sleep(random.uniform(0.01, 0.1))  # Simulando trabalho assincrono
        await queue.put(item)
        print(f"Produtor {producer_id} produziu {item}")

# Consome os itens adicionados ao buffer pelo produtor
async def consumer(consumer_id, queue):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        print(f"Consumer {consumer_id} consumed {item}")
        await asyncio.sleep(random.uniform(0.05, 0.15)) # Simulando trabalho assincrono
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=buffer_size)
    start_time = time.time()

    # Cria e inicia produtores e consumidores
    producers = [
        asyncio.create_task(producer(i, queue))
        for i in range(num_producers)
    ]
    consumers = [
        asyncio.create_task(consumer(i, queue))
        for i in range(num_consumers)
    ]

    # Espera os produtores produzirem os items
    await asyncio.gather(*producers)

    # Sinaliza os consumidores para que a produção acabou
    for _ in range(num_consumers):
        await queue.put(None)

    # Espera os consumidores consumirem os items
    await queue.join()

    # Finaliza as tarefas dos consumidores
    for c in consumers:
        c.cancel()

    # Por fim printa o tempo de execução em segundos
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time:.4f} seg")

if __name__ == "__main__":
    asyncio.run(main())
