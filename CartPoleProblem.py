import gym
from RL_methods import  Q_learning_agent, epsilon_greedy 


env = gym.make('CartPole-v1')

agent = Q_learning_agent(env)

for i_episode in range(50000):
    observation = env.reset()

    for t in range(150):
        # env.render()
        
        old_state = observation
        action = agent.generate_action(observation)
        observation, reward, done, info = env.step(action)
        new_state = observation
        agent.learn(old_state, action, new_state, reward, done)
        
        if done:
            if i_episode % 1000 == 0 or t > 100:
                print("Episode {} finished after {} timesteps".format(i_episode, t+1))
            break
env.close()