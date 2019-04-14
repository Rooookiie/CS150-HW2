# copy and paste your answers into each of the below variables 
# NOTE: do NOT rename variables
# Modify the return statements to return the relevant values
# Include 1-2 sentences (as a python comment) above each answer explaining your reasoning.

import math

#Q1ai 
io_split_sort = 680
# split the files into runs of size 40, so we have 8 runs.
# for each runs, size 40 means 5 IO cost for read, 80 IO cost for write.
# So total IO is (80+5)*8 = 680

#Q1aii
merge_arity =4
# one page in buffer are supposed to left to output, so B = 39.
# reads are always read in 8 -page chunks
# so the max pages of buffer we can use is 8*4= 32.
# the max n is 4, where 4 * 8 =32 < B = 39.

#Q1aiii 
merge_passes = 2
# after initial split and sort, we have 8 runs of size 40.
# accoring n = 4, we can know that we can merge at most 4 runs into 1 once.
# So the total pass is 2.

#Q1aiv 
merge_pass_1 = 680
# cost of read is 320 / 8 =40.
# cost of write is 320 * 2 = 640.
# total cost is 640 + 40 = 680.

#Q1av
total_io = 2040
# initial split and sort : 680 IO costs.
# two passes : 680 * 2 = 1360 IO costs.
# total costs : 1360 +680 = 2040

#Q1bi 
def cost_initial_runs(B, N, P):
    # BEGIN YOUR CODE 
    r = N / P
    w = 2 * N
    return r + w
    # END YOUR CODE 

#Q1bii 
def cost_per_pass(B, N, P):
    # BEGIN YOUR CODE 
    r = N / P
    w = 2 * N
    return r + w
    #END YOUR CODE

#Q1biii
def num_passes(B, N, P):
    # BEGIN YOUR CODE 
    arity = math.floor( (B+1-1) / P )
    runs = N / (B+1)
    passes = math.ceil( math.log(runs, arity) )
    return passes
    # END YOUR CODE

#Q1c 
# Save the optimal value here
P = 11

# Save a list of tuples of (P, io_cost) here, for all feasible P's
points = [(1, 5400.0), (2, 4500.0), (3, 4200.0), (4, 4050.0), (5, 3960.0), (6, 3900.0), (7, 3857.1428571428573), (8, 3825.0), (9, 3800.0), (10, 3780.0), (11, 3763.6363636363635), (12, 5625.0), (13, 5607.692307692308), (14, 5592.857142857143), (15, 5580.0), (16, 5568.75), (17, 5558.823529411765), (18, 5550.0), (19, 5542.105263157895), (20, 5535.0), (21, 5528.571428571428), (22, 5522.727272727273), (23, 5517.391304347826), (24, 5512.5), (25, 5508.0), (26, 5503.846153846153), (27, 5500.0), (28, 5496.428571428572), (29, 5493.103448275862), (30, 5490.0), (31, 5487.096774193548), (32, 5484.375), (33, 5481.818181818182), (34, 9132.35294117647), (35, 9128.57142857143), (36, 9125.0), (37, 9121.621621621622), (38, 9118.42105263158), (39, 9115.384615384615), (40, 9112.5), (41, 9109.756097560976), (42, 9107.142857142857), (43, 9104.651162790698), (44, 9102.272727272728), (45, 9100.0), (46, 9097.826086956522), (47, 9095.744680851063), (48, 9093.75), (49, 9091.836734693878)]


#Q2a 
IO_Cost_HJ_1 = 7560
# Hashing R and S needs 2(P_R+P_S)IO costs.
# Matching R and S needs (P_R+P_S+P_RS)IO costs.
# Hashing RS and T needs 2(P_RS+P_T)IO costs.
# Matching RS and T needs (P_RS+P_T+P_RST)IO costs. Total 7560 IO.
IO_Cost_HJ_2 = 11160
# Hashing R and S needs 2(P_T+P_S)IO costs.
# Matching R and S needs (P_R+P_S+P_ST)IO costs.
# Hashing RS and T needs 2(P_ST+P_R)IO costs.
# Matching RS and T needs (P_ST+P_R+P_RST)IO costs. Total 11160 IO.
IO_Cost_SMJ_1 = 16160
#Split & Sort R and S costs 2P_R + 4P_S IO. 
#Scanning R and S costs (P_R+P_S+P_TS) IO.
#Split & Sort RS and T costs 4P_RS + 6P_T IO. 
#Scanning RS and T costs (P_RS+P_T+P_RST) IO.
IO_Cost_SMJ_2 = 21560
#Split & Sort R and S costs 2P_T + 4P_S IO. 
#Scanning R and S costs (P_T+P_S+P_ST) IO.
#Split & Sort RS and T costs 4P_ST + 6P_R IO. 
#Scanning RS and T costs (P_ST+P_R+P_RST) IO.
IO_Cost_BNLJ_1 = 8920
#joint1 costs P_R+ceil(P_R/(B-2))*P_S+P_RS IO.
#joint2 costs P_RS+ceil(P_RS/(B-2))*P_T+P_RST IO.
IO_Cost_BNLJ_2 = 18580
#joint1 costs P_S+ceil(P_S/(B-2))*P_T+P_ST IO.
#joint2 costs P_ST+ceil(P_ST/(B-2))*P_T+P_RST IO.

#Q2b 
P_R = 20
P_S = 200
P_T = 20
P_RS = 50
P_RST = 200
B = 32

HJ_IO_Cost_join1 = 710
SMJ_IO_Cost_join2 = 590

SMJ_IO_Cost_join1 = 1110
HJ_IO_Cost_join2 = 410

#Q3ai
def lru_cost(N, M, B):
    # BEGIN YOUR CODE 
    if (N>B+1):
        return N * M
    else:
        return N
    #END YOUR CODE

#Q3aii 
def mru_cost(N, M, B):
    #BEGIN YOUR CODE 
    if (N>B+1):
        B+=1
        cost = 0
        index_now = 0
        buffer = [-1 for i in range(B)]
        for i in range(M):
            for j in range(N):
                if j not in buffer:
                    if -1 in buffer:
                        index_now = buffer.index(-1)
                    buffer[index_now] = j
                    cost += 1
                else:
                    index_now = buffer.index(j)
        return cost
    else:
        return N
    #END YOUR CODE

#Q3aiii
# Provide a list of tuple (m, difference between LRU and MRU in terms of IO cost) here:
p3_lru_points = [(1, 0), (2, 5), (3, 10), (4, 15), (5, 20), (6, 24), (7, 28), (8, 33), (9, 38), (10, 43), (11, 48), (12, 52), (13, 56), (14, 61), (15, 66), (16, 71), (17, 76), (18, 80), (19, 84), (20, 89)]

#Q3bi 
def clock_cost(N, M, B):
    #BEGIN YOUR CODE
     if N <= B+1:
        return N
    else:
        B += 1
        cost = 0
        second_bit = [0 for i in range(B)]
        buffer = [-1 for i in range(B)]
        for i in range(M):
            for j in range(N):
                if j not in buffer:
                    cost += 1
                    if -1 in buffer:
                        buffer [buffer.index(-1)] = j
                    else:
                        for x in range(B):
                            if second_bit[x] == 1:
                                second_bit[x] = 0
                            else :
                                buffer [x] = j
                else:
                    second_bit[ buffer.index(j) ] = 1
        return cost
    #END YOUR CODE

#Q3bii 
# Provide a list of tuple (m vs the absolute value of the difference between LRU and CLOCK in terms of IO cost) here:
p3_clock_points = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0)]

'''
EXPLANATION GOES HERE
No. It does not prevent sequential flooding.
It works like LRU. 
In this problem, the second_change bit will never be set to 1, which means there is no reference.
So CLOCK policy works just like LRU.
'''

#Q4ai
def hashJoin(table1, table2, hashfunction,buckets):
    # Parition phase 
    t1Partition = partitionTable(table1,hashfunction,buckets)
    t2Partition = partitionTable(table2,hashfunction,buckets)
    # Merge phase
    result = []
    
    # ANSWER GOES HERE
    for i in range(buckets):
        for x in t1Partition[i]:
            for y in t2Partition[i]:
                if (x.playername == y.playername):
                    result.append((x.teamname, y.playername, y.collegename))
    # To populate your output you should use the following code(t1Entry and t2Entry are possible var names for tuples)
    # result.append((t1Entry.teamname, t1Entry.playername, t2Entry.collegename))
    return result

#Q4aii
'''
Explanation here:
'''

#Q4bi 
# partition- a table partition as returned by method partitionTable
# return value - a float representing the skew of hash function (i.e. stdev of chefs assigned to each restaurant)
def calculateSkew(partition):
    # ANSWER STARTS HERE
    count = 0
    for i in range(len(partition)):
        count += len(partition[i])
    ave = count/ len(partition)
    re = 0
    for i in range(len(partition)):
        re += (len(partition[i]) - ave)**2
    skew = math.sqrt(re /len(partition))
    # ANSWER ENDS HERE
    return skew

#Q4bii 
# Design a better hash function and print the skew difference for 
def hBetter(x,buckets):
    rawKey = hash(x)
    return rawKey % buckets

#Q4biii 
res1 = hashJoin(teams, colleges, hBetter, buckets)

# WRITE DOWN THE SPEED UP
#T he join took 147.34 ms and returned 12740 tuples in total
# it is faster than before, speed-up is 4104.60%

#Q4c
flocco_elite = True
