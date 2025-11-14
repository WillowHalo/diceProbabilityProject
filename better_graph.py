from roundsys import *
import matplotlib.pyplot as plot
import matplotlib.ticker as mticker
from math import ceil, floor


def advance(inp, base, num=1):
    out = inp
    for i in range(num):
        out = round_add(out, base)
    return out

def stripper(i_list, typ="dmg", second="crit"):
    out = []
    tot = 0
    key = {"dmg":1, "sp":3, "crit":5}
    
    for item, count in i_list.items():
        item_set = item.split("-")
        
        val = int(item_set[key[typ]]) # pull dmg
        graph_num = int(item_set[key[second]])

        while len(out)-1 < graph_num: # force
            out.append({})
        
        tot += count
        out[graph_num].update({val:count})
    pre = out
    out = []
    for dic in pre:
        out.append(reorganize(dic, tot))
    return out

def reorganize(dic, tot): # reorganize original dict
    out = {}
    for name in dic:
        out.update({int(name):dic[name]/tot}) # change quantity to %
    out = dict(sorted(out.items()))
    return out

def graph_bar_stack(data_set, color=[[0.9, 0, 0.9], [0, 0.9, 0.9], [0.9, 0.9, 0]]):
    n = 0
    prior = {}
    for data in data_set:
        for name in data:
            data[name] += prior.get(name, 0)
        prior = data
    for data in reversed(data_set):
        plot.bar(data.keys(), data.values(), color=get_color(n, len(data_set)-1, color), width=0.9, label="{} crits".format(len(data_set)-n-1)) 
        n += 1
    ax = plot.subplot() # pulls axis?
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0, decimals=2)) # formats y axis as percent
    ax.legend(title="crit count")

    plot.title("Dmg Average Graph")
    plot.xlabel("Damage")
    plot.ylabel("Percent of Outcome")
    
    
    plot.show()

def get_color(cur, tot, colors=[[0, 0, 0]]):
    cmap = [[], [], []]
    for item in colors:
        for i in range(3):
            cmap[i].append(item[i])

    tot = max(tot, 1)
    
    r = rgb_single(cur/tot, cmap[0])
    g = rgb_single(cur/tot, cmap[1])
    b = rgb_single(cur/tot, cmap[2])
    return (r, g, b)

def rgb_single(per, colors):
    quan = len(colors)-1
    num = per*quan
    mf = num-(floor(num)) # remove full num for mult of final
    mi = 1-mf # mult for initial
    bottom = colors[floor(num)]*mi
    top = colors[ceil(num)]*mf
    out = bottom + top
    return out

def r(v):
    return round(v, 3)

### Play Vars
base = XdY(5, d(6))
sp = 11
round_count = 2
coloring = [[0.9, 0, 0.9], [0, 0.9, 0.9], [0.9, 0.9, 0]] # Triadic
##coloring = [[1, 0, 0], [0.5, 1, 0], [0, 1, 1], [0, 1, 0.5]] # Tetradic
### Play Vars ^^^

sys = round_start(base, sp)
sys = advance(sys, base, round_count-1)
data = stripper(sys)
graph_bar_stack(data, coloring)

avg = 0
for dmg, count in data[-1].items():
    avg += dmg*count
print("avg dmg:", r(avg))

