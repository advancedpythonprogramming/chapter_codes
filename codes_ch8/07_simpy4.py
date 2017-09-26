# 07_simpy4.py
import simpy
import random


def moderator(env):
    discussion_proc = env.process(discussion(env))
    yield env.timeout(random.randint(8, 15))
    # if this randon number is higher than the minimum in the randint of
    # 'discussion method' will try to interrupt a process already ended
    discussion_proc.interrupt("Time is over {}".format(env.now))


def discussion(env):
    try:
        yield env.timeout(random.randint(15, 25))
    except simpy.Interrupt as interr:
        print(interr.cause)
    print("Discussion terminated..", env.now)


maximum_time = 100
env = simpy.Environment()
env.process(moderator(env))
env.run(until=maximum_time)
