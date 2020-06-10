import gym
import numpy as np
"""
    Description:
        A pole is attached by an un-actuated joint to a cart, which moves along
        a frictionless track. The pendulum starts upright, and the goal is to
        prevent it from falling over by increasing and reducing the cart's
        velocity.

    Source:
        This environment corresponds to the version of the cart-pole problem
        described by Barto, Sutton, and Anderson

    Observation:
        Type: Box(4)
        Num   Observation               Min             Max
        0     Cart Position             -4.8            4.8
        1     Cart Velocity             -Inf            Inf
        2     Pole Angle                -24 deg         24 deg
        3     Pole Velocity At Tip      -Inf            Inf

    Actions:
        Type: Discrete(2)
        Num   Action
        0     Push cart to the left
        1     Push cart to the right

        Note: The amount the velocity that is reduced or increased is not
        fixed; it depends on the angle the pole is pointing. This is because
        the center of gravity of the pole increases the amount of energy needed
        to move the cart underneath it

    Reward:
        Reward is 1 for every step taken, including the termination step

    Starting State:
        All observations are assigned a uniform random value in [-0.05..0.05]

    Episode Termination:
        Pole Angle is more than 12 degrees.
        Cart Position is more than 2.4 (center of the cart reaches the edge of
        the display).
        Episode length is greater than 200.
        Solved Requirements:
        Considered solved when the average reward is greater than or equal to
        195.0 over 100 consecutive trials.
    """

class RL_agent():
    def __init__(self,env):
        # Discrete action sapce
        self.action_space = np.arange(env.action_space.n)
        # Continuous state space
        # Theoretical bound
        # [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38]
        # [-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38]
        # self.state_space_upperbound = env.observation_space.high
        # self.state_space_lowerbound = env.observation_space.low
        
        # Cartpole Probelm
        # Pracitcal bound: (get from many times random test)
        # high[0.21673986 1.55362511 0.20883955 2.34863741]
        # low [-0.17247946 -1.56646328 -0.20826308 -2.37250619]
        self.state_space_upperbound = np.array([2.4, 5, 0.21, 5])
        self.state_space_lowerbound = -np.array([2.4, 5, 0.21, 5])
        
        pass
    
    def random_action(self,):
        return np.random.choice(self.action_space)
    
class Q_learning_agent(RL_agent):
    def __init__(self,env, discrete_para = np.array([40,80,40,80])):
        RL_agent.__init__(self, env)

        # Cartpole Probelm
        # Pracitcal bound: (get from many times random test)
        # high[0.21673986 1.55362511 0.20883955 2.34863741]
        # low [-0.17247946 -1.56646328 -0.20826308 -2.37250619]
        # self.state_space_upperbound = np.array([0.3, 2, 0.21, 3])
        # self.state_space_lowerbound = -np.array([0.3, 2, 0.21, 3])

        self.delta_state = (self.state_space_upperbound - self.state_space_lowerbound) / discrete_para
        goal_pos = (0,0,0,0) # (0,0,0,0) if use all features
        goal_action_Q  = np.array([100.0, 100.0])
        self.Qtable = {goal_pos: goal_action_Q}
        
        self.alpha = 0.8 # step size or learnig rate
        self.gamma = 0.95 # discount factor
        self.epsilon = 0.1 # epsilon-greedy 
        
    def discretize_observation(self, observation):
        discrete_obs = observation / self.delta_state
        discrete_obs = discrete_obs.round().astype(np.int)
        # Only use cart position and pole angle
        # obs_in_table = (discrete_obs[0] , discrete_obs[2]) # tuple
        obs_in_table = tuple(discrete_obs)
        
        if obs_in_table not in self.Qtable: # if never meet this state before
            self.Qtable[obs_in_table] = np.random.rand(len(self.action_space)) # init Q in [0,10)
        
        return obs_in_table
        
    
    def generate_action(self, observation, method = "epsilon-greedy", Qtable = None):
        if Qtable == None:
            Qtable = self.Qtable
        observation = self.discretize_observation(observation)

        if method == "epsilon-greedy":
            return epsilon_greedy(Qtable, observation, self.epsilon)
        
        if method == "greedy":
            return np.argmax(Qtable[observation])
        # if method == "UCB":
        #     return UCB(observation)
        

    
    def learn(self, old_state, action, new_state, reward, termination, step_size = 0.8):
        old_state = self.discretize_observation(old_state)
        # print(old_state)
        
        # Update Q table
        if termination:
            self.Qtable[old_state][action] -= 5.0 # penalty 
            return
        
        new_state = self.discretize_observation(new_state)
        
        old_Q = self.Qtable[old_state][action]
        max_Q_of_new_state = np.max(self.Qtable[new_state])
        new_Q = old_Q + step_size * (reward + self.gamma*max_Q_of_new_state - old_Q)
        self.Qtable[old_state][action] = new_Q
        # print("old state: {} , old Q:{}, new Q:{}".format(old_state, old_Q, new_Q))
            
        return


def epsilon_greedy(ValueTable, observation, epsilon):
    if np.random.rand() < epsilon:
        action = np.random.choice(len(ValueTable[observation]))
    else:
        action = np.argmax(ValueTable[observation])
    # print(action)
    return action



if __name__ == '__main__':
    
    env = gym.make('CartPole-v1')
    agent = Q_learning_agent(env)

    total_episode = 20001
    
    for i_episode in range(total_episode):
        observation = env.reset()
        # print(agent.Qtable)
        for t in range(300):
            # env.render()
            
            # print(observation)
            old_state = observation
            action = agent.generate_action(observation, method = "epsilon-greedy")
            # print(old_state[0],old_state[2])
            # print(action)
            observation, reward, done, info = env.step(action)
            new_state = observation
            # print(new_state[0], new_state[2])
            agent.learn(old_state, action, new_state, reward, done, 1*(1 - i_episode/total_episode)) # decay step size
            # agent.learn(old_state, action, new_state, reward, done, 0.8)
            
            if done:
                # if i_episode % 2000 == 0 or t > 195:
                #     print("Episode {} finished after {} timesteps".format(i_episode, t+1))
                break
            # if t == 199:
            #     print("Episode {} finished after {} timesteps".format(i_episode, t+1))
        
        if i_episode % 1000 == 0:
            rewards_stat = []
            for test_episode in range(100):
                observation = env.reset()
                cum_reward = 0
                for tt in range(300):
                    action = agent.generate_action(observation, method = 'greedy')
                    observation, reward, done, info = env.step(action)
                    cum_reward += reward

                    if done:
                        # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                        rewards_stat.append(cum_reward)
                        break

                    if tt == 299:
                        # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                        rewards_stat.append(cum_reward)
            print("Episode {} : ".format(i_episode))
            print('Average rewards over 100 consecutive trials: ', np.mean(rewards_stat))
    
    # Test Q-learning result
    print('<-------------------------------------------->')
    print('Test the reuslt of Q-learning:')
    Learned_Qtable = agent.Qtable
    rewards_stat = []
    for test_episode in range(1000):
        observation = env.reset()
        cum_reward = 0
        for t in range(500):
            action = agent.generate_action(observation, 'greedy', Learned_Qtable)
            observation, reward, done, info = env.step(action)
            cum_reward += reward

            if done:
                # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                rewards_stat.append(cum_reward)
                break

            if t == 499:
                # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                rewards_stat.append(cum_reward)

    print('Average rewards over 1000 consecutive trials: ', np.mean(rewards_stat))
    print('Min rewards over 1000 consecutive trials: ', np.min(rewards_stat))
    print('Max rewards over 1000 consecutive trials: ', np.max(rewards_stat))

    env.close()