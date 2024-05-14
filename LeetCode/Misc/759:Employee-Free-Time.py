class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []

        for employee in schedule:
            for event in employee:
                events.append(event)

        events.sort(key=operator.attrgetter('start'))

        for event in events:
            print(f'{event.start} {event.end}')

        ret = []

        start, end = events[0].start, events[0].end
        n = len(events)
        for i in range(1, n):
            s, e = events[i].start, events[i].end
            if s > end:
                ret.append(Interval(end, s))
            end = max(end, e)


        return ret
