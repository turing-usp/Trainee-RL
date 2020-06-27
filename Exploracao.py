import gym

# Essa funcao deve rodar um episodio do ambiente escolhendo acoes aleatorias
def rodar_ambiente():
    # Crie o ambiente 'pong:turing-easy-v0'
    env = ...

    # Receba a observacao do primeiro estado
    state = ...

    # Inicializando done como false
    done = False

    # Loop de treino
    while not done:
        # Escolha uma acao aleatoria
        action = ...

        # Tome essa acao e receba as informacoes do estado seguinte
        next_state, reward, done, info = ...

        # Renderize o ambiente
        ...

        # Atualizando o estado
        state = next_state

    # Fechando o ambiente
    env.close()

if __name__ == '__main__':
    rodar_ambiente()
