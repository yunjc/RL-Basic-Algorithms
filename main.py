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
        # self.state_space_upperbound = env.observation_space.high
        # self.state_space_lowerbound = env.observation_space.low
        
        # Cartpole Probelm
        # Pracitcal bound: (get from many times random test)
        # high[0.21673986 1.55362511 0.20883955 2.34863741]
        # low [-0.17247946 -1.56646328 -0.20826308 -2.37250619]
        self.state_space_upperbound = np.array([0.3, 2, 0.21, 3])
        self.state_space_lowerbound = -np.array([0.3, 2, 0.21, 3])
        
        pass
    
    def random_action(self,):
        return np.random.choice(self.action_space)
    
class Q_learning_agent(RL_agent):
    def __init__(self,env, discrete_para = np.array([20,20,30,20])):
        RL_agent.__init__(self, env)
        self.delta_state = (self.state_space_upperbound - self.state_space_lowerbound) / discrete_para
        goal_pos = (0,0,0,0) # (0,0,0,0) if use all features
        goal_action_Q  = np.array([0.0,0.0])
        self.Qtable = {goal_pos: goal_action_Q}
        
        self.alpha = 0.5 # step size or learnig rate
        self.gamma = 0.8 # discount factor
        self.epsilon = 0.05 # epsilon-greedy 
        
    def discretize_observation(self, observation):
        discrete_obs = observation / self.delta_state
        discrete_obs = discrete_obs.round().astype(np.int)
        # Only use cart position and pole angle
        # obs_in_table = (discrete_obs[0] , discrete_obs[2]) # tuple
        obs_in_table = tuple(discrete_obs)
        
        if obs_in_table not in self.Qtable: # if never meet this state before
            self.Qtable[obs_in_table] = np.random.rand(len(self.action_space)) # init Q in [0,10)
        
        return obs_in_table
        
    
    def generate_action(self, observation, method = "epsilon-greedy"):
        observation = self.discretize_observation(observation)
        if method == "epsilon-greedy":
            return epsilon_greedy(self.Qtable, observation, self.epsilon)
        
        # if method == "UCB":
        #     return UCB(observation)
        

    
    def learn(self, old_state, action, new_state, reward, termination):
        old_state = self.discretize_observation(old_state)
        # print(old_state)
        
        # Update Q table
        # if termination:
        #     self.Qtable[old_state][action] -= 1 # penalty 
        #     return
        
        new_state = self.discretize_observation(new_state)
        
        old_Q = self.Qtable[old_state][action]
        max_Q_of_new_state = np.max(self.Qtable[new_state])
        new_Q = old_Q + self.alpha * (reward + self.gamma*max_Q_of_new_state - old_Q)
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
    
    for i_episode in range(50000):
        observation = env.reset()
        # print(agent.Qtable)
        for t in range(200):
            # env.render()
            
            # print(observation)
            old_state = observation
            action = agent.generate_action(observation)
            # print(old_state[0],old_state[2])
            # print(action)
            observation, reward, done, info = env.step(action)
            new_state = observation
            # print(new_state[0], new_state[2])
            agent.learn(old_state, action, new_state, reward, done)
            
            if done:
                if i_episode % 1000 == 0 or t > 100:
                    print("Episode {} finished after {} timesteps".format(i_episode, t+1))
                break
    env.close()