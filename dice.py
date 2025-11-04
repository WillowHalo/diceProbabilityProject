def d(i): # i for input
    o_list = []
    for n in range(1, i+1):
        o_list.append(n)
    return o_list

def XdY(X, dY, r_lim=7776, print_spam=False): # count for dice qnty, d_name for dice type
    ### vars
    o_list = []
    dice = []
    max_dice = []
    ### vars

    for i in range(X): # set up dice lists
        dice.append(dY[0])
        max_dice.append(dY[-1])

    run = 0
    while run < r_lim or r_lim == "inf":
        if print_spam == True: # to watch creation of list step by step
            print(dice)
        
        o_list.append([]) # ready new point
        
        for n in range(X):
            o_list[run].append(dice[n]) # add values to new point           Neccisary beecause directly adding lists uses deeper memory
        
        n = 0
        for d in dice:
            if max_dice == dice:
                return o_list # return if finnished
            if d != dY[-1]:
                dice[n] += 1
                break # add to first unfull, then stop
            else:
                dice[n] = dY[0] # if max, roll over
            n += 1
        run += 1
    print("Runtime Error; runtime in excess of limit ("+str(run)+")")
    return o_list # if while loop didnt return results

def calc_dmg(i_list):
    pass

