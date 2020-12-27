#collections: Counter, namedTuple OrderedDict, defaultDict, deque
from collections import Counter
a = "aaaaaabbbbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))