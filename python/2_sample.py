from second_code import SimpleBars
import re

bs = SimpleBars(' '*24)
bs[8] = 'T'
for i in range(30):
    print(bs.next())
