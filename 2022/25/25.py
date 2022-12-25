import re
snafu = [x.strip() for x in open('input.txt').readlines()]

t = '=-012'

def from_snafu(s):
    f = 0
    l = len(s)
    for i, n in enumerate(re.findall("[\-\=\d]{1}", s)):
        f += pow(5, l-i-1) * (t.find(n)-2)
    return f

def to_snafu(x):
    snafu_x = ''
    for i in range(20,-1,-1):
        s = pow(5, i)
        y = x/s
        if -2.5 < y < 2.5:
            f = round(y)
            x = x - f*s
            snafu_x += t[f+2]
    return snafu_x.lstrip('0')

u = 0
for s in snafu:
    u += from_snafu(s)

print(u)

print(to_snafu(u))