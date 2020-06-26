from ambiente.objects import Environment

# Essa funcao deve rodar um episodio do ambiente escolhendo acoes aleatorias
def rodar_ambiente():
    # Crie o ambiente
    env = Environment()

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

if __name__ == '__main__':
    rodar_ambiente()
