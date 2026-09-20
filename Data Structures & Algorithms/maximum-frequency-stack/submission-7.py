class FreqStack:

    def __init__(self):
        # Keeps track of the CURRENT frequency of each value.
        # Example:
        # {5: 3, 7: 2, 4: 1}
        self.freq = {}

        # Maps a frequency -> stack of values that reached that frequency.
        # Example:
        # 1 -> [5, 7, 4]
        # 2 -> [5, 7]
        # 3 -> [5]
        #
        # The stack order also remembers recency.
        self.group = {}

        # Highest frequency currently present.
        self.maxFreq = 0

    def push(self, val: int) -> None:

        # Increase the frequency of val by 1.
        # If val has never appeared before, start from 0.
        self.freq[val] = self.freq.get(val, 0) + 1

        # Store its new frequency.
        f = self.freq[val]

        # If nobody has reached this frequency before,
        # create a new stack for this frequency.
        if f not in self.group:
            self.group[f] = []

        # Put val into the stack for its NEW frequency.
        # Since we append, the most recently pushed value
        # at this frequency will always be on top.
        self.group[f].append(val)

        # Update the highest frequency if necessary.
        self.maxFreq = max(self.maxFreq, f)

    def pop(self) -> int:

        # Go directly to the highest-frequency stack
        # and pop the most recent value from it.
        val = self.group[self.maxFreq].pop()

        # One copy of val was removed,
        # so decrease its current frequency.
        self.freq[val] -= 1

        # If there are no values left in the current
        # maximum-frequency stack, then the new maximum
        # frequency must be one less.
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        # Return the value we removed.
        return val