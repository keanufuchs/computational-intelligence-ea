
import numpy as np

SEED = 113
np.random.seed(SEED)

n = 6
start, end = sorted(np.random.choice(n, 2, replace=False))
print(f"Seed {SEED}: start={start}, end={end}")

parent1 = np.array([0, 1, 2, 3, 4, 5])
parent2 = np.array([3, 5, 4, 2, 0, 1])

child = np.full(n, -1)
child[start:end+1] = parent1[start:end+1]

segment_values = set(child[start:end+1])
remaining = [x for x in parent2 if x not in segment_values]

remaining_idx = 0
pos = (end + 1) % n
while remaining_idx < len(remaining):
    if child[pos] == -1:
        child[pos] = remaining[remaining_idx]
        remaining_idx += 1
    pos = (pos + 1) % n

print(f"Final child: {child}")
print(f"Equal to parent1? {np.array_equal(child, parent1)}")
print(f"Equal to parent2? {np.array_equal(child, parent2)}")

