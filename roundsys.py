from dice import *

def round_start(i_list, sp=11, abl=1, crit_num=2, crit_dmg=5):
    out = {}
    max_val = i_list[-1][-1]
    for dice in i_list:
        crit = int(dice.count(max_val) >= crit_num) # if num of maxed dice is crit
        dmg = max(sum(dice)-sp, 0)
        s = "dmg-{}".format( dmg + (crit_dmg * crit) ) # damage plus crit
        s += "-sp-{}".format( sp - (abl*int(dmg!=0)) ) # check remaining SP with abblation
        s += "-C-{}".format(crit) # count num of crits
        out[s] = out.get(s, 0)+1 # update quantity 
    return out

def deform(i): # remove data formating
    i = i.split("-")
    return int(i[1]), int(i[3]), int(i[5]) # return the numbers

def round_add(i_prior, i_list, abl=1, crit_num=2, crit_dmg=5):
    out = {}
    max_val = i_list[-1][-1]
    for base in i_prior:
        for dice in i_list:
            p_dmg, sp, c = deform(base) # find base stats
            crit = int(dice.count(max_val) >= crit_num)
            dmg = max(sum(dice)-sp, 0)
            s = "dmg-{}".format(dmg + (crit_dmg * crit) + p_dmg) # damage plus crit plus prior damage
            s += "-sp-{}".format(sp - (abl*int(dmg!=0))) # check remaining SP with abblation
            s += "-C-{}".format(crit+c) # count num of crits
            out[s] = out.get(s, 0)+1
    return out
