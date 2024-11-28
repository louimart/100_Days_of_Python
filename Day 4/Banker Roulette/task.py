friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random

# Method 1
# number_of_friends = len(friends)
# print(number_of_friends)
#
# friend_selected = random.randint(0, number_of_friends-1)
# print(friends[friend_selected])

# Method 2
# random choice from this list
print(random.choice(friends))