#!/usr/bin/python3
from functools import reduce
print(reduce(lambda x, y: x + chr(y), range(65, 91), ""))
