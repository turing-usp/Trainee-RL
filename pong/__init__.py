import os
from gym.envs.registration import register

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

register(
    id='turing-easy-v0',
    entry_point='pong.objects:PongEnv',
    max_episode_steps=10_000,
)

register(
    id='turing-normal-v0',
    entry_point='pong.objects:EasyPongEnv',
    max_episode_steps=10_000,
)
