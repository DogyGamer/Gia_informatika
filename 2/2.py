from itertools import permutations

sled = lambda a, b: False if a and not b else True

F = lambda dict: (sled(dict["w"], (dict["y"] == dict["z"])) and (dict["y"] == sled(dict["z"],dict["x"])))

def compare(labels, values: list):
    result = values.pop()
    return F(dict(zip(labels, values))) == result

for perm in permutations("xyzw", 4):
    for x1 in [True, False]:
        for x2 in [True, False]:
            
            a = [
                [x1, False, False, False, True],
                [False, x2, True, True, True],
                [False, False, False, True, False],
            ]
            res = []
            for aa in a:
                res.append(compare(perm, aa))
            # print(res)
            if all(res):
                print(perm)
            # dict(zip("yxzw", [1,2,3,4]))


# print(list(permutations("xyzw", 4)))
