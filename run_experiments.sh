#!/bin/bash

mkdir -p results

> results/threads_times.csv
> results/coroutines_times.csv

echo "Executando Experimento de Threads..."
for i in {1..5}
do
    python3 threads/producer_consumer.py | grep "Tempo de execucao" | awk '{print $4}' >> results/threads_times.csv
done

echo "Executando Experimento de Coroutines..."
for i in {1..5}
do
    python3 coroutines/producer_consumer.py | grep "Tempo de execucao" | awk '{print $4}' >> results/coroutines_times.csv
done

echo "Fim da Execução."

echo "Gerando Gráfico de Resultados..."

python3 plot_results.py
 
echo "Gráfico gerado em results/comparacao_performance.png"
