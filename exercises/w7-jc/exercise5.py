"""

@author: Jiahao Chen
@since: 21/10/2021
@version: 1.0

Create three dictionaries: maria, peter, and mike. Give each dictionary the keys ’name’,
’weeklyExercises’ and ’weeklyTests. Have the ’name’ key be the name of the student
(that is, maria’s name should be ’Maria’ and so on). The other keys should be an empty list.
Print the dictionaries on the screen. Next populate each list with 10 random numbers in the
range 0 to 10. For each of the dictionaries create a new key named exam and fill it with a
random value in the range 0 to 10.

"""

import random

maria = {"name": "Maria","weeklyExercises": [], "weeklyTests": []}
peter = {"name": "Peter","weeklyExercises": [],"weeklyTests": []}
mike = {"name": "Mike","weeklyExercises": [],"weeklyTests": []}

for i in range(10):
  maria["weeklyExercises"].append(random.randint(0,10))
  maria["weeklyTests"].append(random.randint(0,10))
  peter["weeklyExercises"].append(random.randint(0,10))
  peter["weeklyTests"].append(random.randint(0,10))
  mike["weeklyExercises"].append(random.randint(0,10))
  mike["weeklyTests"].append(random.randint(0,10))

maria["exam"] = []
peter["exam"] = []
mike["exam"] = []

for i in range(10):
  maria["exam"].append(random.randint(0,10))
  peter["exam"].append(random.randint(0,10))
  mike["exam"].append(random.randint(0,10))

print(maria)
print(peter)
print(mike)