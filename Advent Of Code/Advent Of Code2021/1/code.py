# Advent of code Year 2021 Day 1 solution
# Author = David Myers
# Date = December 2020

# with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    # input = input_file.read()
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [x.rstrip() for x in input_file]


print(input)
def depth_check(input):
    num_of_incr = 0
    num_of_decr = 0 #should sum with num_of_incr to the number of measurements
    num_of_comparisons =0 #should be the number of measurements -1
    i = 0
    # while i+1 <len(input):
    for each in input[:-1]:

        if int(input[i+1])>int(input[i]): #if this depth is greater than the last one
            num_of_incr +=1 #then count it

        # if input[i+1]<=input[i]:
        #     num_of_decr +=1
        # print(i,input[i])
        # num_of_comparisons +=1
        i +=1


    return num_of_incr






print("Part One : "+ str(depth_check(input)))



print("Part Two : "+ str(None))
