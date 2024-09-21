class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] # (speed, position, time to destination)
        for pos, spd in zip(position,  speed):
            cars.append((pos, spd))
        
        cars.sort()
        st = []

        for i in range(len(position) - 1, -1, -1):
            print(f'st[{i}] = {st}')
            pos, spd = cars[i][0], cars[i][1]
            if not st:
                st.append((pos, spd, (target - pos) / spd))
                continue
            
            # will catch up
            if st and spd > st[-1][1] and (st[-1][0] - pos) / (spd - st[-1][1]) <= st[-1][2]:
                continue

            st.append((pos, spd, (target - pos) / spd)) 

        return len(st)                                                                                                                      