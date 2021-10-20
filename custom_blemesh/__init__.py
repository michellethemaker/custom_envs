from gym.envs.registration import register
import numpy 

register(
     id='customblemesh-v0',
     entry_point='customblemesh.envs:customblemeshEnv'
 )


