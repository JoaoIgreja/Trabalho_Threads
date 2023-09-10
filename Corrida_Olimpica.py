import threading  # Importa a biblioteca threading para trabalhar com threads.
import random  # Importa a biblioteca random para gerar números aleatórios.
import time  # Importa a biblioteca  time para controlar intervalos de tempo.

# Função para simular a corrida de um corredor


def corredor(numero, distancia_percorrida):
    while distancia_percorrida[numero - 1] < 100:
        # Gera um valor aleatório entre 1 e 10 para simular o avanço do corredor.
        avanco = random.randint(1, 5)
        # Atualiza a distância percorrida pelo corredor.
        distancia_percorrida[numero - 1] += avanco
        print(
            f"Corredor {numero} percorreu {distancia_percorrida[numero - 1]} metros.")
        # time.sleep(0.1)  # Aguarda 0.1 segundos antes da próxima iteração.
    print(f"Corredor {numero} terminou a corrida!")


# Número de corredores na corrida
num_corredores = 4

# Inicializa a lista de distâncias percorridas por cada corredor
distancia_percorrida = [0] * num_corredores

# Cria threads para os corredores
threads_corredores = []  # Criando lista para corredores
for i in range(1, num_corredores + 1):  # For que itera de 1 até o número de corredores
    # Passando argumentos para a função corredor e a definindo como alvo da Thread
    t = threading.Thread(target=corredor, args=(i, distancia_percorrida))
    # Adicionaa Thread criada a lista thread corredores
    threads_corredores.append(t)
    t.start()  # Inicia a Thread

# Aguarda todas as threads terminarem
for t in threads_corredores:  # Loop para percorrer a lista
    t.join()  # Bloqueia o resto do programa executar até que a thread_corredores seja finalizada

# Determina o vencedor após a thread_corredores ser finalizada
vencedor = distancia_percorrida.index(max(distancia_percorrida)) + 1

print(f"O Corredor {vencedor} venceu a corrida olimpica!")
