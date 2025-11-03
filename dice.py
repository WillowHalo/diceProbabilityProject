from random import randrange



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

    for i in range(X):
        dice.append(dY[0])
        max_dice.append(dY[-1])

    run = 0
    while run < r_lim or r_lim == "inf":
        if print_spam == True:
            print(dice)
        
        o_list.append([]) # ready new point

        for n in range(X):
            o_list[run].append(dice[n]) # add values to new point

        n = 0
        for d in dice:
            n += 1

            if max_dice == dice:
                return o_list

            if d != dY[-1]:
                dice[n-1] += 1
                break
            else:
                dice[n-1] = dY[0]
            
        run += 1
    print("Runtime Error; runtime in excess of limit ("+str(run)+")")
    return o_list

    

print( XdY(16, d(4)) )
