import numpy as np


reaction_times = np.array([
    248, 231, 276, 219, 254,
    243, 225, 198, 284, 212,
    267, 236, 271, 301, 222
])


average_reaction_time = np.mean(reaction_times)
fastest_reaction_time = np.min(reaction_times)
slowest_reaction_time = np.max(reaction_times)
standard_deviation = np.std(reaction_times)

under_240 = reaction_times[reaction_times < 240]
under_240_count = len(under_240)

first_five = reaction_times[:5]


print(f"Average reaction time: {average_reaction_time:.2f} ms")
print(f"Fastest reaction time: {fastest_reaction_time} ms")
print(f"Slowest reaction time: {slowest_reaction_time} ms")
print(f"Standard deviation: {standard_deviation:.2f} ms")

print(f"Reaction times below 240 ms: {under_240}")
print(f"Number below 240 ms: {under_240_count}")

print(f"First 5 reaction times: {first_five}")