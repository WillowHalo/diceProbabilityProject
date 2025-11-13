from roundsys import *
import matplotlib.pyplot as plot
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
    return out

def reorganize(dic, tot): # reorganize original dict
    out = {}
    for name in raw_data:
        data.update({int(name):dic[name]/tot}) # change quantity to %
    out = dict(sorted(out.items()))
    return out

def graph_bar_stack(data_set):
    n = 0
    prior = {}
    for data in data_set:
        for name in data:
            data[name] += prior.get(name, 0)
        prior = data
    for data in reversed(data_set):
        plot.bar(data.keys(), data.values(), color=get_color(n, len(data_set)-1)) 
        n += 1
        

    plot.show()

def get_color(cur, tot, colors=[[1, 0, 1], [0, 1, 1], [1, 1, 0]]):
    cmap = [[], [], []]
    for item in colors:
        for i in range(3):
            cmap[i].append(item[i])
    r = rgb_single(cur/tot, cmap[0])
    g = rgb_single(cur/tot, cmap[1])
    b = rgb_single(cur/tot, cmap[2])
    print(r, g, b)
    return (r, g, b)

def rgb_single(per, colors):
    quan = len(colors)-1
    num = per*quan
    mf = num-(floor(num))
    mi = 1-mf
    bottom = colors[floor(num)]*mi
    top = colors[ceil(num)]*mf
    out = bottom + top
    return out

def r(v):
    return round(v, 3)

### Play Vars
base = XdY(5, d(6))
sp = 11
round_count = 4
### Play Vars ^^^

sys = round_start(base, sp)
sys = advance(sys, base, round_count-1)
data = stripper(sys)
graph_bar_stack(data)


