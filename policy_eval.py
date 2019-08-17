from gridworld_env import GridWorldEnv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

env = GridWorldEnv()

def policy_eval(policy, env, discount_factor=1.0, epsilon= 0.0001):

    v_old = np.zeros(env.nS)
    while True:
        v_new = np.zeros(env.nS)

        delta = 0

        for state in range(env.nS):
            v_fn = 0

            action_probs = policy[state]
            
            for action in range(env.nA):
                [prob, next_state, reward, done] = env.P[state][action]
                v_fn += action_probs[action] * (reward + discount_factor*v_old[next_state[0]*4 + next_state[1]])
            
            delta = max(delta, abs(v_fn - v_old[state]))

            v_new[state] = v_fn
        
        v_old = v_new
        
        if delta < epsilon:
            break
        
    return np.reshape(v_old, (4,4))

def plots(v, title):
    matplotlib.use('TkAgg')

    ax = plt.gca()

    plt.title(title)

    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])

    im = ax.imshow(v)

    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('Value', rotation=-90, va='bottom')

    plt.show()

random_policy = np.ones([env.nS, env.nA]) / env.nA
v = policy_eval(random_policy, env)

plots(v, 'Value map')

print(v)