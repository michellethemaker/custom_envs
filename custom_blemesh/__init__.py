from gym.envs.registration import register

register(
     id='customblemesh-v0',
     entry_point='customblemesh.envs:customblemeshEnv'
 )

register(
     id='customblemesh-v0.1',
     entry_point='customblemesh.envs:customblemeshEnv',
     max_episode_steps=1500,
     kwargs={'size' : 1, 'init_state' : 10., 'state_bound' : np.inf},
 )
