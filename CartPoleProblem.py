import gym
import numpy as np
from RL_methods import  Q_learning_agent, Sarsa_agent, MC_agent, generate_episode, epsilon_greedy , UCB1

def Q_learning_agent_solve(env, total_episode, EE_method = "epsilon-greedy"):
    print('<-------------------------------------------->')
    print('Q-learning agent solve Cartpole problem. Total episodes: {}, EE_method: {}'.format(total_episode, EE_method))

    agent = Q_learning_agent(env)
    # agent.ucbalpha = 50
    plot_rewards_stat = []

    for i_episode in range(total_episode):
        observation = env.reset()
        for t in range(300):
            # env.render()
            # print(observation)
            old_state = observation
            action = agent.generate_action(observation, method = EE_method ) # "epsilon-greedy" /"UCB1" / "greedy"
            observation, reward, done, info = env.step(action)
            new_state = observation
            # if i_episode < 2000:
            #     agent.learn(old_state, action, new_state, reward, done, 0.3) # decay step size
            # else:
            agent.learn(old_state, action, new_state, reward, done, 0.5*(1 - i_episode/total_episode)) # decay step size

            # agent.learn(old_state, action, new_state, reward, done, 0.95) 
            
            if done:
                # if i_episode % 100 == 0:
                    # print("Episode {} finished after {} timesteps".format(i_episode, t+1))
                break
            # if t == 249:
            #     print("Episode {} finished after {} timesteps".format(i_episode, t+1))
        
        # current triaining result
        if i_episode % 1000 == 0:
            rewards_stat = []
            for test_episode in range(100):
                observation = env.reset()
                cum_reward = 0
                tt = 0
                done = False
                while not done:
                    tt += 1
                # for tt in range(300):
                    action = agent.generate_action(observation, method = 'greedy')
                    observation, reward, done, info = env.step(action)
                    cum_reward += reward

                    if done:
                        # print("Episode {} finished after {} timesteps".format(test_episode, tt+1))
                        rewards_stat.append(cum_reward)
                        break
            plot_rewards_stat.append(np.mean(rewards_stat))
            print("Episode {} : ".format(i_episode))
            print('Average rewards over 100 consecutive trials: ', np.mean(rewards_stat))
    
    # Test Q-learning result
    print('<-------------------------------------------->')
    print('Test the reuslt of Q-learning after training {} episodes:'.format(total_episode))
    Learned_Qtable = agent.Qtable
    rewards_stat = []
    for test_episode in range(1000):
        observation = env.reset()
        cum_reward = 0
        t = 0
        done = False
        while not done:
            t += 1
            action = agent.generate_action(observation, 'greedy', Learned_Qtable)
            observation, reward, done, info = env.step(action)
            cum_reward += reward
            if done:
                # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                rewards_stat.append(cum_reward)
                break

    print('Average rewards over 1000 consecutive trials: ', np.mean(rewards_stat))
    print('Min rewards over 1000 consecutive trials: ', np.min(rewards_stat))
    print('Max rewards over 1000 consecutive trials: ', np.max(rewards_stat))
    # plot_rewards_stat.append(np.mean(rewards_stat))
    env.close()

    return agent, np.array(plot_rewards_stat)


def Sarsa_agent_solve(env, total_episode, EE_method = "epsilon-greedy"):
    print('<-------------------------------------------->')
    print('SARSA agent solve Cartpole problem. Total episodes: {}, EE_method: {}'.format(total_episode, EE_method))
    agent = Sarsa_agent(env)
    plot_rewards_stat = []

    for i_episode in range(total_episode):
        rho_state, rho_action_reward = generate_episode(env, agent, EE_method)
        agent.learn(rho_state, rho_action_reward, 0.5*(1 - i_episode/total_episode), i_episode)

        if i_episode % 1000 == 0:
            rewards_stat = []
            for test_episode in range(100):
                observation = env.reset()
                cum_reward = 0
                tt = 0
                done = False
                while not done:
                    tt += 1
                # for tt in range(300):
                    action = agent.generate_action(observation, method='greedy')
                    observation, reward, done, info = env.step(action)
                    cum_reward += reward

                    if done:
                        # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                        rewards_stat.append(cum_reward)
                        break
                    # if tt == 299:
                    #     # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                    #     rewards_stat.append(cum_reward)
            plot_rewards_stat.append(np.mean(rewards_stat))
            # print(plot_rewards_stat)
            print("Episode {} : ".format(i_episode))
            print('Average rewards over 100 consecutive trials: ', np.mean(rewards_stat))

        # file_name = 'sarsa e=0.1'
        # file_name = 'MC e=0.1'
        # np.save(file_name, np.array(plot_rewards_stat))
        if i_episode == total_episode - 1:
            print('\nLearning Finished\n')

    # Test  result
    print('<-------------------------------------------->')
    print('Test the reuslt of SARSA with epsilon greedy improvement:')
    # print('Test the reuslt of SARSA:')
    Learned_Qtable = agent.Qtable
    rewards_stat = []
    for test_episode in range(1000):
        observation = env.reset()
        cum_reward = 0
        t = 0
        done = False
        while not done:
            t += 1
        # for t in range(500):
            action = agent.generate_action(observation, 'greedy', Learned_Qtable)
            observation, reward, done, info = env.step(action)
            cum_reward += reward

            if done:
                # print("Episode {} finished after {} timesteps".format(test_episode, t))
                rewards_stat.append(cum_reward)
                break
            # if t == 499:
            #     # print("Episode {} finished after {} timesteps".format(test_episode, t))
            #     rewards_stat.append(cum_reward)

    print('Average rewards over 1000 consecutive trials: ', np.mean(rewards_stat))
    print('Min rewards over 1000 consecutive trials: ', np.min(rewards_stat))
    print('Max rewards over 1000 consecutive trials: ', np.max(rewards_stat))
    env.close()
    return agent, np.array(plot_rewards_stat)


def MC_agent_solve(env, total_episode, EE_method):
    print('<-------------------------------------------->')
    print('MC agent solve Cartpole problem. Total episodes: {}, EE_method: {}'.format(total_episode, EE_method))
    agent = MC_agent(env)
    plot_rewards_stat = []

    for i_episode in range(total_episode):
        rho_state, rho_action_reward = generate_episode(env, agent, EE_method)
        if i_episode < 5000:
             agent.learn(rho_state, rho_action_reward, 0.3, i_episode)
        else:
            # agent.epsilon = 0.1 / (iter - 15000+1)
            agent.learn(rho_state, rho_action_reward, 0.5*(1 - i_episode/total_episode), i_episode)

        if i_episode % 1000 == 0:
            rewards_stat = []
            for test_episode in range(100):
                observation = env.reset()
                cum_reward = 0
                tt = 0
                done = False
                while not done:
                    tt += 1
                # for tt in range(300):
                    action = agent.generate_action(observation, method='greedy')
                    observation, reward, done, info = env.step(action)
                    cum_reward += reward

                    if done:
                        # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                        rewards_stat.append(cum_reward)
                        break
                    # if tt == 299:
                    #     # print("Episode {} finished after {} timesteps".format(test_episode, t+1))
                    #     rewards_stat.append(cum_reward)
            plot_rewards_stat.append(np.mean(rewards_stat))
            # print(plot_rewards_stat)
            print("Episode {} : ".format(i_episode))
            print('Average rewards over 100 consecutive trials: ', np.mean(rewards_stat))

        # file_name = 'sarsa e=0.1'
        # file_name = 'MC e=0.1'
        # np.save(file_name, np.array(plot_rewards_stat))
        if i_episode == total_episode - 1:
            print('\nLearning Finished\n')

    # Test  result
    print('<-------------------------------------------->')
    print('Test the reuslt of firs-visit MC with epsilon greedy improvement:')
    # print('Test the reuslt of SARSA:')
    Learned_Qtable = agent.Qtable
    rewards_stat = []
    for test_episode in range(1000):
        observation = env.reset()
        cum_reward = 0
        t = 0
        done = False
        while not done:
            t += 1
        # for t in range(500):
            action = agent.generate_action(observation, 'greedy', Learned_Qtable)
            observation, reward, done, info = env.step(action)
            cum_reward += reward

            if done:
                # print("Episode {} finished after {} timesteps".format(test_episode, t))
                rewards_stat.append(cum_reward)
                break
            # if t == 499:
            #     # print("Episode {} finished after {} timesteps".format(test_episode, t))
            #     rewards_stat.append(cum_reward)

    print('Average rewards over 1000 consecutive trials: ', np.mean(rewards_stat))
    print('Min rewards over 1000 consecutive trials: ', np.min(rewards_stat))
    print('Max rewards over 1000 consecutive trials: ', np.max(rewards_stat))
    env.close()
    return agent, np.array(plot_rewards_stat)


if __name__ == '__main__':
    
    env = gym.make('CartPole-v1')
    total_episode = 20001
    
    # "epsilon-greedy" /"UCB1"
    EE_method = "epsilon-greedy"
    # EE_method = "UCB1"

    # Q_learning_agent, plot_rewards_stat = Q_learning_agent_solve(env, total_episode, EE_method)
    # # np.save('./result/Q learning e=0.1.npy', plot_rewards_stat)
    # print(plot_rewards_stat)

    Sarsa_agent, plot_rewards_stat = Sarsa_agent_solve(env,total_episode, EE_method)
    # np.save('./result/sarsa e=0.1.npy', plot_rewards_stat)
    print(plot_rewards_stat)
    
    MC_agent, plot_rewards_stat = MC_agent_solve(env, total_episode, EE_method)
    # np.save('./result/MC e=0.1.npy', plot_rewards_stat)
    print(plot_rewards_stat)

    print('Solution Ends.')
