#REINFORCEMENT LEARNING

#is a kind of ml where an agent learns from an enviroment as it recieves rewards
#what is RL?

#key concepts
#1. Agent - the learner or decision maker
#2. Environment - the world through which the agent moves
#3. State - a situation in which the agent finds itself
#4. Action - decisions made by the agent that affect the state of the environment
#5. Reward - feedback from the environment based on the action taken by the agent
#6. Policy - the strategy that the agent employs to determine its actions
#7. Value Function - a prediction of future rewards for a given state


#key characteristics
#no labeled learning
#focus on learning from interaction
#involve exploration of the enviroment
#working throughout without delay rewards

#RL Algorithms
#1. Q -learning: a value-based method that learns the value of actions in states
#   using a Q-table to store action values.
#2. Deep Q networks: a neural network-based approach that approximates the Q-values
#   using deep learning techniques.
#3. Policy Gradient methods: a class of algorithms that optimize the policy directly
#   by adjusting the parameters of the policy network.
#4. Actor-Critic methods: a combination of value-based and policy-based methods
#   where an actor learns the policy and a critic evaluates the action taken by the actor.
#5. Proximal Policy Optimization (PPO): a policy gradient method that uses a clipped objective function
#   to ensure stable updates to the policy.
#6. Trust Region Policy Optimization (TRPO): a policy gradient method that ensures updates are within a
#   trust region to maintain stability.
#7. Deep Deterministic Policy Gradient (DDPG): an algorithm for continuous action spaces that combines




#Q-learning with policy gradients


import numpy as np
import random


#define the enviroment
position =5 #inital positions of the agent from zero to 4
action = 2 # two actions to move left and to move right

#initalize the Q table
Q = np.zeros((position,action)) 

#Define the parameters,,,, how fast is it learning
episodes =1000 #episodes fro training
leraning_rate = 0.8 
gamma = 0.9 #discoiunt factor for future rewards
epsilon = 0.3 # probability of taking a random action of exploration


#training loop
for episode in range{episodes}:
    state = random.randint(0, position - 1)
    
#action selection {episilon greedy policy}
