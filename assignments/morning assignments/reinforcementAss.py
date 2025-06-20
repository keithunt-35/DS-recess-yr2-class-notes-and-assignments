import numpy as np
import random

# Environment setup
road_length = 5  # Positions 0 to 4
actions = ['left', 'right']

# Q-table initialization
Q = np.zeros((road_length, len(actions)))

# Hyperparameters
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3
episodes = 1000

# Training loop
for episode in range(episodes):
    state = random.randint(0, road_length - 1)
    done = False
    
    while not done:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = actions[np.argmax(Q[state])]
        
        # Environment dynamics
        if action == 'right':
            next_state = min(state + 1, road_length - 1)
            reward = 1 if next_state == road_length - 1 else 0
        else:
            next_state = max(state - 1, 0)
            reward = 0
        
        # Q-learning update
        Q[state, actions.index(action)] = (1 - learning_rate) * Q[state, actions.index(action)] + \
                                        learning_rate * (reward + gamma * np.max(Q[next_state]))
        
        state = next_state
        done = (state == road_length - 1)

print("Learned Q-table:")
for i in range(road_length):
    print(f"State {i}: {Q[i]}")

print("\nLearned Policy:")
for i in range(road_length):
    print(f"State {i}: {actions[np.argmax(Q[i])]}")