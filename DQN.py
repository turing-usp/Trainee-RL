#!/usr/bin/env python3


class ReplayBuffer:
    """Um buffer que armazena transições e permite a amostragem de transições aleatórias."""

    def __init__(self, max_size):
        """Cria um replay buffer.

        Args:
            max_size (int): número máximo de transições armazenadas pelo buffer.
        """
        pass

    def add_transition(self, transition):
        """Adiciona uma transição ao replay buffer.

        Args:
            transition (tuple): uma tupla representando a transição.
        """
        pass

    def sample_transitions(self, num_samples):
        """Retorna uma lista com transições amostradas aleatoriamente.

        Args:
            num_samples (int): o número de transições desejadas.
        """
        pass

    def get_size(self):
        """Retorna o número de transições armazenadas pelo buffer."""
        pass

    def get_max_size(self):
        """Retorna o número máximo de transições armazenadas pelo buffer."""
        pass


class DQNAgent:
    """Implementa um agente de RL usando Deep Q-Learning."""

    def __init__(self, state_dim, action_dim,
                 buffer_size=100_000,
                 batch_size=32,
                 gamma=0.97,
                 learning_rate=1e-3):
        """Cria um agente de DQN com os hiperparâmetros especificados

        Args:
            state_dim (int): número de variáveis de estado.
            action_dim (int): número de ações possíveis.
            buffer_size (int, optional): tamanho máximo do replay buffer.
            batch_size (int, optional): número de transições utilizadas por batch.
            gamma (float, optional): fator de desconto utilizado no calculo do retorno.
            learning_rate (float, optional): taxa de aprendizado da rede neural.
        """
        pass

    def act(self, state, epsilon=0):
        """Retorna a ação tomada pelo agente no estado `state`.

        Args:
            state: o estado do ambiente.
            epsilon (int, optional): o valor de epsilon a ser considerado
                                     na política epsilon-greedy.
        """
        pass

    def optimize(self):
        """Roda um passo de otimização da DQN.

        Obtém `self.batch_size` transições do replay buffer
        e treina a rede neural. Se o replay buffer não tiver
        transições suficientes, a função não deve fazer nada.
        """
        pass


if __name__ == '__main__':
    env = ...
    agent = DQNAgent(action_dim=..., state_dim=...,
                     batch_size=32, learning_rate=1e-3,
                     gamma=0.99)

    # Hiperparâmetros da política epsilon-greedy
    initial_eps = 1
    min_eps = 0.001
    eps_decay = .95
    eps = initial_eps

    # Número total de episódios
    num_episodes = 150

    for episode in range(num_episodes):
        # Rodar o episódio, da mesma forma que com o agente aleatório.
        pass

    env.close()
