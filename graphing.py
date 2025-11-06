from roundsys import *
import matplotlib.pyplot as plot


def advance(inp, base, num=1):
    out = inp
    for i in range(num):
        out = round_add(out, base)
    return out

def striping(i_list, typ="dmg"):
    out = []
    y = []
    tot = 0
    key = {"dmg":1, "sp":3, "crit":5}
    for item in i_list:
        d = item.split("-")[key[typ]]
        y.append(i_list[item])
        tot += i_list[item]
        out.append(d)
    return out, y, tot

base = XdY(5, d(6))
sys = round_start(base, sp=11)
sys = advance(sys, base, 0)
data, y, pri = striping(sys)
real_y = []
for val in y:
    real_y.append(val/pri)

print(pri)

plot.bar(data, real_y, color="#bfafff")
plot.title("title")
plot.xticks(rotation=270)

plot.show()
