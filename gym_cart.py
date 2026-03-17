import gymnasium as gym
import time

scores = []
times = []

def average(list):
    avg = 0
    for x in list:
        avg += x
    return avg / len(list)

for x in range(15):
    episode_over = False
    total_reward = 0
    env = gym.make("CartPole-v1", render_mode="human")

    observation, info = env.reset()
    print(f"Starting observation:  {observation}")
    time_s = time.perf_counter()

    while not episode_over:
        action = env.action_space.sample()

        observation, reward, terminated, truncated,  info = env.step(action)

        total_reward += reward
        episode_over = terminated or truncated

    time_e = time.perf_counter()
    scores.append(total_reward)
    times.append(time_e - time_s)

    print(f"Elapsed time: {time_e - time_s:.4f}")
    print(f"Cycle over! Total Reward: {total_reward}")

    env.reset()

env.close()

print(f"Average elapsed time: {average(times)}")
print(f"Maximum elapsed time: {max(times)}")
print(f"Minimum elapsed time: {min(times)}")

print(f"Average score: {average(scores)}")
print(f"Maximum score: {max(scores)}")
print(f"Minimum score: {min(scores)}")