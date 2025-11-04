from dice import *

def calc_dmg(i_list, sp="NaN", crit_num=2):
    out = {}
    max_val = i_list[-1][-1]
    for dice in i_list:
        crit = dice.count(max_val) >= crit_num # if num of maxed dice is crit
        s = "dmg-{}-sp-{}-C-{}".format(sum(dice), sp, int(crit)) # format for labels
        out[s] = out.get(s, 0)+1 # update quantity 
    return out

