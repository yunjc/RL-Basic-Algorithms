import gym
import numpy as np
import math
from gym import spaces, logger
from gym.utils import seeding
from matplotlib import pyplot as plt
import cv2
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
        # goal_action_Q  = np.array([100.0, 100.0])
        goal_action_Q = np.random.rand(len(self.action_space))
        self.Qtable = {goal_pos: goal_action_Q}
        self.alpha = 0.8 # step size or learnig rate
        self.gamma = 0.95 # discount factor
        self.epsilon = 0.1 # epsilon-greedy
        self.action_taken_times = {goal_pos: np.array([1,1])} # UCB1
        self.ucbalpha = 1 # UCB1
        
    def discretize_observation(self, observation):
        discrete_obs = observation / self.delta_state
        discrete_obs = discrete_obs.round().astype(np.int)
        # Only use cart position and pole angle
        # obs_in_table = (discrete_obs[0] , discrete_obs[2]) # tuple
        obs_in_table = tuple(discrete_obs)
        if obs_in_table not in self.Qtable: # if never meet this state before
            self.Qtable[obs_in_table] = np.random.rand(len(self.action_space)) # init Q in [0,1)
            self.action_taken_times[obs_in_table] = np.array([1,1]) # init action taken times
        return obs_in_table
        
    
    def generate_action(self, observation, method = "epsilon-greedy", Qtable = None):
        if Qtable == None:
            Qtable = self.Qtable
        observation = self.discretize_observation(observation)

        if method == "epsilon-greedy":
            return epsilon_greedy(Qtable, observation, epsilon = self.epsilon)
        
        if method == "greedy":
            return np.argmax(Qtable[observation])

        if method == "UCB1":
            action, self.action_taken_times = UCB1(Qtable, self.action_taken_times, observation, ucbalpha = self.ucbalpha)
            return action
        
    def learn(self, old_state, action, new_state, reward, termination, step_size = 0.8):
        old_state = self.discretize_observation(old_state)
        # Update Q table
        if termination:
            self.Qtable[old_state][action] -= 5.0 # penalty 
            return
        new_state = self.discretize_observation(new_state)  
        old_Q = self.Qtable[old_state][action]
        max_Q_of_new_state = np.max(self.Qtable[new_state])
        new_Q = old_Q + step_size * (reward + self.gamma*max_Q_of_new_state - old_Q)
        self.Qtable[old_state][action] = new_Q  
        return


class Sarsa_agent(RL_agent):
    def __init__(self, env, discrete_para=np.array([40, 80, 40, 80])):
        RL_agent.__init__(self, env)

        # Cartpole Probelm
        # Practical bound: (get from many times random test)
        # high[0.21673986 1.55362511 0.20883955 2.34863741]
        # low [-0.17247946 -1.56646328 -0.20826308 -2.37250619]
        # self.state_space_upperbound = np.array([0.3, 2, 0.21, 3])
        # self.state_space_lowerbound = -np.array([0.3, 2, 0.21, 3])

        self.delta_state = (self.state_space_upperbound - self.state_space_lowerbound) / discrete_para
        goal_pos = (0, 0, 0, 0)  # (0,0,0,0) if use all features
        goal_action_Q = np.array([100.0, 100.0])
        self.Qtable = {goal_pos: goal_action_Q}

        self.alpha = 0.8  # step size or learning rate
        self.gamma = 0.95  # discount factor
        self.epsilon = 0.1  # epsilon-greedy
        self.action_taken_times = {goal_pos: np.array([1,1])} # UCB1
        self.ucbalpha = 1 # UCB1

    def discretize_observation(self, observation):
        discrete_obs = observation / self.delta_state
        discrete_obs = discrete_obs.round().astype(np.int)
        # Only use cart position and pole angle
        # obs_in_table = (discrete_obs[0] , discrete_obs[2]) # tuple
        obs_in_table = tuple(discrete_obs)

        if obs_in_table not in self.Qtable:  # if never meet this state before
            self.Qtable[obs_in_table] = np.random.rand(len(self.action_space)) # init Q in [0,1)
            self.action_taken_times[obs_in_table] = np.array([1,1]) # init action taken times
        return obs_in_table

    def generate_action(self, observation, method="epsilon-greedy", Qtable=None):
        if Qtable == None:
            Qtable = self.Qtable
        observation = self.discretize_observation(observation)

        if method == "epsilon-greedy":
            return epsilon_greedy(Qtable, observation, epsilon = self.epsilon)
        
        if method == "greedy":
            return np.argmax(Qtable[observation])

        if method == "UCB1":
            action, self.action_taken_times = UCB1(Qtable, self.action_taken_times, observation, ucbalpha = self.ucbalpha)
            return action

    def learn(self, rho_state, rho_action_reward, step_size, iter):
        if iter > 15000:
            self.epsilon = 0.1 / (iter - 15000) # epsilon decay
        for t in range(len(rho_action_reward)-1):
            # get state & action pair
            state = rho_state[t]
            action, reward = rho_action_reward[t]
            next_state = rho_state[t+1]
            next_action, next_reward = rho_action_reward[t+1]
            # update Q
            old_Q = self.Qtable[state][action]
            next_Q = self.Qtable[next_state][next_action]
            new_Q = old_Q + step_size * (reward + self.gamma * next_Q - old_Q)
            self.Qtable[state][action] = new_Q
        if len(rho_action_reward) < 300:  # penalty
            self.Qtable[rho_state[-2]][rho_action_reward[-1][0]] -= 5.0
        return


class MC_agent(RL_agent):
    def __init__(self, env, discrete_para=np.array([40, 80, 40, 80])):
        RL_agent.__init__(self, env)

        # Cartpole Probelm
        # Practical bound: (get from many times random test)
        # high[0.21673986 1.55362511 0.20883955 2.34863741]
        # low [-0.17247946 -1.56646328 -0.20826308 -2.37250619]
        # self.state_space_upperbound = np.array([0.3, 2, 0.21, 3])
        # self.state_space_lowerbound = -np.array([0.3, 2, 0.21, 3])

        self.delta_state = (self.state_space_upperbound - self.state_space_lowerbound) / discrete_para
        goal_pos = (0, 0, 0, 0)  # (0,0,0,0) if use all features
        goal_action_Q = np.array([100.0, 100.0])
        self.Qtable = {goal_pos: goal_action_Q}

        self.alpha = 0.8  # step size or learning rate
        self.gamma = 1  # discount factor
        self.epsilon = 0.3  # epsilon-greedy
        self.action_taken_times = {goal_pos: np.array([1,1])} # UCB1
        self.ucbalpha = 10 # UCB1

    def discretize_observation(self, observation):
        discrete_obs = observation / self.delta_state
        discrete_obs = discrete_obs.round().astype(np.int)
        # Only use cart position and pole angle
        # obs_in_table = (discrete_obs[0] , discrete_obs[2]) # tuple
        obs_in_table = tuple(discrete_obs)

        if obs_in_table not in self.Qtable:  # if never meet this state before
            self.Qtable[obs_in_table] = np.random.rand(len(self.action_space))  # init Q in [0,1)
            self.action_taken_times[obs_in_table] = np.array([1,1]) # init action taken times

        return obs_in_table

    def generate_action(self, observation, method="epsilon-greedy", Qtable=None):
        if Qtable == None:
            Qtable = self.Qtable
        observation = self.discretize_observation(observation)

        if method == "epsilon-greedy":
            return epsilon_greedy(Qtable, observation, self.epsilon)

        if method == "greedy":
            return np.argmax(Qtable[observation])

        if method == "UCB1":
            action, self.action_taken_times = UCB1(Qtable, self.action_taken_times, observation, ucbalpha = self.ucbalpha)
            return action

    def learn(self, rho_state, rho_action_reward, step_size , iter):
        if iter > 5000:
            self.epsilon = 0.3 / (iter - 5000) # epsilon decay
        closed_set = []  # to tell first visit
        for t in range(len(rho_action_reward)):
            # get state & action pair
            state = rho_state[t]
            action, reward = rho_action_reward[t]
            if [state, action] in closed_set:
                continue
            closed_set.append([state, action])  # add visited state & action pair into closed set
            # calculate L
            L = 0
            for i in range(t,len(rho_action_reward)):
                L += self.gamma ** (i-t) * rho_action_reward[i][1]
            # update Q
            old_Q = self.Qtable[state][action]
            new_Q = old_Q + step_size * (L - old_Q)
            self.Qtable[state][action] = new_Q
        if len(rho_action_reward) < 300:  # penalty
            self.Qtable[rho_state[-2]][rho_action_reward[-1][0]] -= 5.0
        return


def generate_episode(env, agent, EE_method = "epsilon-greedy"):
    observation = env.reset()
    rho_state = [agent.discretize_observation(observation)] # using to store the episode
    rho_action_reward = []
    for t in range(300):
        action = agent.generate_action(observation, method= EE_method)
        observation, reward, done, info = env.step(action)
        rho_action_reward.append([action, reward])
        rho_state.append(agent.discretize_observation(observation))
        if done:
            break
    # print(rho_state)
    # print(rho_action)
    return rho_state, rho_action_reward


# Explore-Exploit methods:

def epsilon_greedy(ValueTable, observation, epsilon):
    if np.random.rand() < epsilon:
        action = np.random.choice(len(ValueTable[observation]))
    else:
        action = np.argmax(ValueTable[observation])
    return action

def UCB1(ValueTable, action_times_table, observation, ucbalpha = 1):
    values = ValueTable[observation]
    action_times = action_times_table[observation]
    total_times = np.sum(action_times)
    ucbs = values + np.sqrt(ucbalpha * np.log(total_times) / (2*action_times))
    action_chosen = np.argmax(ucbs)
    action_times_table[observation][action_chosen] += 1
    return action_chosen, action_times_table






if __name__ == '__main__':
    pass

