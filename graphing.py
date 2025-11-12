from roundsys import *
import matplotlib.pyplot as plot


def advance(inp, base, num=1):
    out = inp
    for i in range(num):
        out = round_add(out, base)
    return out

def striping(i_list, typ="dmg"):
    out = {}
    tot = 0
    key = {"dmg":1, "sp":3, "crit":5}
    for item in i_list:
        d = item.split("-")[key[typ]]
        y = i_list[item]
        tot += i_list[item]
        out.update({d:y})
    return out, tot

base = XdY(4, d(6))
sys = round_start(base, sp=11)
sys = advance(sys, base, 1)
raw_data, pri = striping(sys)
data = {}
for name in raw_data:
    data.update({int(name):raw_data[name]/pri})

data = dict(sorted(data.items()))

avgdmg = 0
for x, y in data.items():
    avgdmg += x*y
print(avgdmg)
print(pri)

plot.bar(data.keys(), data.values(), color="#bfafff")
plot.title("title")
plot.xticks(rotation=270)

plot.show()
