# Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random

lottery_tickets_list = []
print("creating 100 random lottery tickets")

for i in range(100):
    # ticket number must be 10 digit (1000000000, 9999999999)
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))

winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)
