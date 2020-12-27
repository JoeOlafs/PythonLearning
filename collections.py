#collections: Counter, namedTuple OrderedDict, defaultDict, deque
from collections import Counter
a = "aaaaaabbbbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(2,3)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

from collections import defaultdict
default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
default_dict['c'] = 3
print(default_dict['a'])
print(default_dict['d'])

from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop()
print(d)
d.popleft()
print(d)

d.extend([2,3,4])
d.extendleft([7,6,5])
print(d)

d.rotate(4)
print(d)