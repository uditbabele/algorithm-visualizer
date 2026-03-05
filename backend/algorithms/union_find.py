def union_find_steps(ops):

    parent = {}
    steps = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a,b):

        pa = find(a)
        pb = find(b)

        if pa != pb:
            parent[pb] = pa

    for op in ops:

        if op[0] == "make":

            parent[op[1]] = op[1]

            steps.append({
                "action":"create",
                "node":op[1]
            })

        if op[0] == "union":

            union(op[1],op[2])

            steps.append({
                "action":"union",
                "a":op[1],
                "b":op[2]
            })

    return steps