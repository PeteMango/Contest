def solution(requests, totalSlots):
    slots = [0] * totalSlots
    ans = []

    for r in requests:
        # print(slots)
        request_type = r[0]
        start = int(r[1])
        length = int(r[2])

        if request_type == "store":
            if length > totalSlots:
                ans.append(-1)
                continue

            num_stuff = 0
            for i in range(start, start + length):
                if slots[i % totalSlots] == 1:
                    num_stuff += 1

            if num_stuff == 0:
                for i in range(start, start + length):
                    slots[i % totalSlots] = 1
                ans.append(start)
                continue

            print(num_stuff)
            new_start = start
            while num_stuff > 0 and new_start < 2 * totalSlots:
                if slots[new_start % totalSlots] == 1:
                    num_stuff -= 1

                new_start += 1
                if slots[(new_start + length - 1) % totalSlots] == 1:
                    num_stuff += 1
                print(f"{num_stuff} {new_start}")

            if new_start >= 2 * totalSlots:
                ans.append(-1)
            else:
                for i in range(new_start, new_start + length):
                    slots[i % totalSlots] = 1
                ans.append(new_start % totalSlots)
        else:
            freed = 0
            for i in range(start, start + length):
                slots[i % totalSlots] = 0

            ans.append(length)

    return ans
