from roundsys import *
import matplotlib.pyplot as plot


def advance(inp, base, num=1):
    out = inp
    for i in range(num):
        out = round_add(out, base)
    return out

def striper(i_list, typ="dmg"):
    out = {}
    tot = 0
    key = {"dmg":1, "sp":3, "crit":5}
    
    for item in i_list:
        val = item.split("-")[key[typ]]

def reorganize(dic, tot): # reorganize original dict
    out = {}
    for name in raw_data:
        data.update({int(name):dic[name]/tot}) # change quantity to %
    out = dict(sorted(out.items()))
    return out

### Play Vars
base = XdY(5, d(6))
sp = 11
round_count = 1
### Play Vars ^^^

sys = round_start(base, sp)
sys = advance(sys, base, round_count-1)
