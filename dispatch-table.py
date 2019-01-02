"""
A dispatch table is a better way to avoid use a chained of if and elif statements.
"""
import datetime

today = datetime.datetime.today()

def monday():
    print('Monday')

def tuesday():
    print('Tuesday')

def wednesday():
    print('Wednesday')

def thursday():
    print('Thursday')

def friday():
    print('Friday')

def saturday():
    print('Saturday')

def sunday():
    print('Sunday')

# The worse way of chained a set of if and elif statements.
# if today == 1:
#     monday()
# elif today == 2:
#     tuesday()
# ...

dispatch = {
    0: monday,
    1: tuesday,
    2: wednesday,
    3: thursday,
    4: friday,
    5: saturday,
    6: sunday,
}

# The best way of execute using a dispatch dictionary.
dispatch[today.weekday()]()