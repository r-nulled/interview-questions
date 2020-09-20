class Gateway(self):
    def __init__(self, throttles):
        # throttles: List [ Tuple(Timeframe int, Capacity int) ]
        self.throttles = sorted(throttles, key=(lambda x: x[0]), reverse=true)
        self.data = []
        self.dropped = []

    def update(self, data):
        now = data
        temp =  self.data
        temp.insert(0, data)
        for time_frame, capacity in self.throttles:
            temp2 = [x for x in temp if x > (now - time_frame)]
            if len(temp2) > capacity:
                self.dropped.append(data)
                return
        self.data = temp

    def get_num_dropped(self):
        return len(self.dropped)

    def get_dropped(self):
        return self.dropped
