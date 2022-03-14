import sys
import random

class Demon():
    def __init__(self, S_c, T_r, S_r, N_a, N_a_LIST):
        self.S_c = S_c              # stamina consumed
        self.T_r = T_r              # After T_r turns you recover...
        self.S_r = S_r              # ... S_r stamina points
        self.N_a = N_a              # You'll earn points for N_a rounds
        self.N_a_LIST = N_a_LIST    # list of fragments

S_i = None      # Initial stamina
S_max = None    # Max stamina
T = None        # Turns
D = None        # Demons number
Demons = []

data = ["00-example.txt", "01-the-cloud-abyss.txt", "02-iot-island-of-terror.txt", "03-etheryum.txt", "04-the-desert-of-autonomous-machines.txt", "05-androids-armageddon.txt"]
data_ID = 0
with open("./data/" + data[data_ID], "r") as f:
    lines = []
    
    for line in f:
        lines.append(line)

    S_i = int(lines[0].split(" ")[0])
    S_max = int(lines[0].split(" ")[1])
    T = int(lines[0].split(" ")[2])
    D = int(lines[0].split(" ")[3])
        
    for i in range(D):
        new_d = lines[1+i].strip().split(" ")
        fragments = []
        
        for j in range(len(new_d)-4):
            fragments.append(int(new_d[4+j]))
        
        demon = Demon(int(new_d[0]), int(new_d[1]), int(new_d[2]), int(new_d[3]), fragments)
        Demons.append(demon)
        
########################################
#           PARSING DONE               #
########################################

defeated = {}       # Dictionary of demon id and fight time
score = 0

for step in range(T):

    for id_demon in defeated:
        this_id = step-defeated[id_demon]

        if this_id == Demons[id_demon].T_r:
            S_i += Demons[id_demon].S_r

            if S_i > S_max:
                S_i = S_max

    ##### Stamina recharged

    # Take the available demons
    possible = []
    for demon_idx in range(len(Demons)):
        # Demon was not defeated
        if demon_idx not in defeated:
            # Actual stamina is enough to defeat
            if S_i >= Demons[demon_idx].S_c:
                possible.append(demon_idx)
    '''
    ################################################    
    ##### First metric - minimum stamina used: #####
    _minimumStamina = sys.maxsize
    _chosenDemonID = None

    for p in possible:
        if Demons[p].S_c < _minimumStamina:
            _minimumStamina = Demons[p].S_c
            _chosenDemonID = p
    
    if _chosenDemonID != None:
        defeated[_chosenDemonID] = step

    ################################################    
    ############ Second metric - random: ###########
    random_index = random.randint(0, (len(possible)-1))
    defeated[random_index] = step

    ################################################    
    #### Third metric - minimum recovery steps: ####

    _minimumRecovery = sys.maxsize
    _chosenDemonID = None

    for p in possible:
        if Demons[p].T_r < _minimumRecovery:
            _minimumRecovery = Demons[p].T_r
            _chosenDemonID = p
    
    if _chosenDemonID != None:
        defeated[_chosenDemonID] = step

    ################################################    
    ## Fourth metric - best average of fragments: ##

    _maximum_average = -1
    _chosenDemonID = None
    
    for p in possible:
        if Demons[p].N_a == 0:
            this_average = -1
        else:
            this_average = sum(Demons[p].N_a_LIST)/Demons[p].N_a
        
        if this_average > _maximum_average:
            _maximum_average = this_average
            _chosenDemonID = p
    
    if _chosenDemonID != None:
        defeated[_chosenDemonID] = step

    ################################################    
    ## Fifth metric - getting points for as long as I can ##

    _maximum_rounds = -1
    _chosenDemonID = None
    
    for p in possible:
        if Demons[p].N_a > _maximum_rounds:
            _maximum_rounds = Demons[p].N_a
            _chosenDemonID = p
    
    if _chosenDemonID != None:
        defeated[_chosenDemonID] = step

    ################################################    
    # Sixth metric - minimum stamina used and some gain: #
    
    _minimumStamina = sys.maxsize
    _chosenDemonID = None

    for p in possible:
        if Demons[p].S_c < _minimumStamina:
            if sum(Demons[p].N_a_LIST) > 0:
                _minimumStamina = Demons[p].S_c
                _chosenDemonID = p
    
    if _chosenDemonID != None:
        defeated[_chosenDemonID] = step

    ################################################    
    ##### Seventh metric - sum of points / N_a #####
    
    _maximum_metric = 0
    _chosenDemonID = None

    for p in possible:
        if Demons[p].N_a != 0:
            this_metric = sum(Demons[p].N_a_LIST) / Demons[p].N_a

            if this_metric > _maximum_metric:
                _maximum_metric = this_metric
                _chosenDemonID = p
    
    if _chosenDemonID != None:
        defeated[_chosenDemonID] = step
'''
    ################################################    
    ##### Third metric update #####
    _minimumRecovery = sys.maxsize
    _chosenDemonID = None

    for p in possible:
        if sum(Demons[p].N_a_LIST) > 0:
            if Demons[p].T_r < _minimumRecovery:
                _minimumRecovery = Demons[p].T_r
                _chosenDemonID = p
    
    if _chosenDemonID != None:
        defeated[_chosenDemonID] = step


    ##### Enemy faced(or not)

    for id_demon in defeated:
        this_id = step-defeated[id_demon]

        # If the value can still be collected, do it
        if this_id < Demons[id_demon].N_a:
            score += Demons[id_demon].N_a_LIST[this_id]

    ##### Fragments collected

########################################
#          ALGORITHM DONE              #
########################################

with open("./" + data[data_ID], "w+") as f:
    for id_demon in defeated:
        f.write(str(id_demon) + "\n")

########################################
#            OUTPUT DONE               #
########################################
