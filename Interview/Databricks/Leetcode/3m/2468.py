class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        if limit <= 5:
            return []

        def do(num_words: int):
            real_limit = limit - len(str(num_words)) - 3
            cur_idx, word_idx = 1, 0
            ret = []
            while word_idx < n:
                cur_limit = real_limit - len(str(cur_idx))
                if word_idx + cur_limit >= n:
                    ret.append(message[word_idx:] + f'<{cur_idx}/{num_words}>')
                    return ret

                ret.append(message[word_idx:word_idx+cur_limit] + f'<{cur_idx}/{num_words}>')
                word_idx += cur_limit
                cur_idx += 1

            return ret
        
        def trydo(num_words: int):
            length = sum(limit - len(str(i)) - len(str(num_words)) - 3 for i in range(1, num_words + 1))
            return length >= len(message)

        ceil = 9
        if not trydo(ceil):
            ceil = 99
        if not trydo(ceil):
            ceil = 999
        if not trydo(ceil):
            ceil = 9999
        if not trydo(ceil):
            return []
        
        l, r, mid = 1, ceil, -1
        res = []
        while l <= r:
            mid = (l+r) // 2
            if trydo(mid):
                r = mid - 1
            else:
                l = mid + 1

        if not trydo(mid):
            return do(mid+1)
        
        return do(mid)
        
