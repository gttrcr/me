from collections import defaultdict


def simple_hash(x):
    return hash(x) % 100


def find_collisions(hash_func, input_space):
    hash_table = defaultdict(list)
    collisions = {}

    for x in input_space:
        h = hash_func(x)
        hash_table[h].append(x)

    for h, values in hash_table.items():
        if len(values) > 1:
            collisions[h] = values

    return collisions


input_space = [str(i) for i in range(1000000)]
collisions = find_collisions(simple_hash, input_space)
collisions = dict(sorted(collisions.items()))
for h, values in collisions.items():
    print(f"Hash {h}: Colliding values -> {len(values)}")
