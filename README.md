# Problema de Sincronização Produtor-Consumidor

Este projeto implementa e compara duas abordagens para resolver o clássico problema de sincronização Produtor-Consumidor em Python:

* **Concorrência Preemptiva:** Usando o módulo threading
* **Concorrência Cooperativa:** Usando o módulo asyncio com corrotinas

## Pré-requisitos

* Python 3.7+ (Desenvolvi utilizando o 3.13.5)
* Um ambiente tipo Linux para rodar o script `.sh` (ou você pode executar os comandos manualmente).
* Bibliotecas Python listadas em `requirements.txt`.

# Guia de Execução

## 1. Instale as Dependências

Primeiro, instale as bibliotecas Python necessárias:
```bash
pip install -r requirements.txt
```

## 2. Execução

### 2.1 Execute cada implementação diretamente para ver a saída

**Threads:**
```bash
python3 threads/producer_consumer.py
```

**Coroutines:**
```bash
python3 coroutines/producer_consumer.py
```

### 2.2 Executando os Experimentos de Performance

Para executar os experimentos de performance execute o script run_experiments.sh.

O mesmo irá:
* Executar os códigos
* Guardar seus tempos de execução
* Plotar um gráfico comparando os dois resultados dos códigos na pasta results

```bash
bash run_experiments.sh
```

### 4. Gerando o Gráfico

Após rodar os experimentos, você pode gerar o gráfico comparativo executando:

```bash
python3 plot_results.py
```

O script irá criar um arquivo de imagem chamado `comparacao_performance.png` no diretório `results/`.

### Configuração
Para alterar os parâmetros do experimento basta alterar as variáveis:

*   `num_producers`: O número de threads/tasks produtoras.
*   `num_consumers`: O número de threads/tasks consumidoras.
*   `items_to_produce`: O número de itens que cada produtor irá criar.
*   `buffer_size`: O tamanho máximo do buffer/fila compartilhada.