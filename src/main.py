import gfootball.env as football_env
import logging

if __name__ == '__main__':
    env = football_env.create_environment(
        env_name='academy_empty_goal_close',
        stacked=False,  # solo estado, no pixeles
        representation='simple115',  # solo estado, no pixeles
        rewards="scoring,checkpoints",  # recompensas intermedias, no solo al marcar
        render=True)  # mostrar graficamente

    logging.disable(logging.WARNING)

    for i in range(1, 10):
        env.reset()
        acc_reward = 0

        while True:
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            acc_reward += reward

            if done:
                break

        print("Recomensa episodio {:d}: {:.2f}".format(i, acc_reward))

    env.close()




