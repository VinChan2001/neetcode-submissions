class TimeMap:

    def __init__(self):
        self.store = {} # key= string, value= list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
# get is a function that fetches the value associated with the key in the dictionary and also specify a default value if that key has no value 
        values = self.store.get(key, []) 

        #these are list of values associated with the key where we have to do a binary search

        l, r = 0, len(values)-1
        while l <= r :
            m = (l+r)//2
            if values[m][1] <= timestamp:#input parameter
                res = values[m][0] # this is the closest value seen so far to the timestamp
                l = m+1 #search the right portion
            else:
                r = m-1
                #we dont assign res here because its bigger timestamp and we need <= closer aspect
        return res


                






