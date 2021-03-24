import random

NUM_TRIALS = 10

for item in range(0, NUM_TRIALS):

    # randit finds numbers between given endpoints, including both endpoints
    prize_num = random.randint(1,4)
    print(prize_num)