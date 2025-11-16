import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_results():
    results_directory = 'results'
    threads_file = os.path.join(results_directory, 'threads_times.csv')
    coroutines_file = os.path.join(results_directory, 'coroutines_times.csv')

    if not os.path.exists(threads_file) or not os.path.exists(coroutines_file):
        print("Erro: Arquivos de resultados não encontrados.")
        print("Por favor, execute './run_experiments.sh' primeiro para gerar os dados.")
        return

    try:
        threads_times = pd.read_csv(threads_file, header=None, names=['time'])
        coroutines_times = pd.read_csv(coroutines_file, header=None, names=['time'])
    except pd.errors.EmptyDataError:
        print("Erro: Um ou ambos os arquivos de resultados estão vazios.")
        print("Por favor, verifique a saída do './run_experiments.sh'.")
        return

    executions = range(1, len(threads_times) + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(executions, threads_times['time'], marker='o', linestyle='-', label='Threads (Preemptive)')
    plt.plot(executions, coroutines_times['time'], marker='x', linestyle='--', label='Coroutines (Cooperative)')

    plt.xlabel('Execução do Experimento')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação de Performance: Threads vs. Coroutines')
    plt.legend()
    plt.grid(True)
    plt.xticks(executions)

    output_path = os.path.join(results_directory, 'comparacao_performance.png')
    plt.savefig(output_path)

if __name__ == "__main__":
    plot_results()