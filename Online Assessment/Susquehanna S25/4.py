from collections import defaultdict


def solution(a, b, queries):
    d = defaultdict(int)
    for num in a:
        d[num] += 1

    b_d = defaultdict(int)
    for num in b:
        b_d[num] += 1

    ans = []
    for q in queries:
        # print(f'd: {d.items()}')
        # print(f'b_d: {b_d.items()}')
        q_type = int(q[0])
        if q_type == 0:
            idx = int(q[1])
            val = int(q[2])
            old_b = b[idx]
            b[idx] += val
            b_d[old_b] -= 1

            b_d[old_b + val] += 1
        else:
            goal = int(q[1])
            ret = 0
            for key, val in d.items():
                if goal - key in b_d:
                    ret += b_d[goal - key] * val

            ans.append(ret)
    return ans
