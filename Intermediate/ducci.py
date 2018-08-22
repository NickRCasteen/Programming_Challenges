#Okay, so we're looking to make a Ducci

#We'll take an array. Any array will do. Of integers.

def Ducci(duclist):
    #So the idea is thatWe start at i=0, do abs(duclist[i]-duclist[i+1]) for every item, unless i = len(duclist)-1, then abs(duclist[i] - duclist[0])
    #So how to check? Well, the check can do this:
    #Every loop, increment a counter
    #if all zeroes, return counter
    #How to see we're in a stable repeating pattern? It's law that a stable binary pattern has only 2 numbers.
        #Thusly, you need to store what those 2 numbers are. Make a copy of the first array where there's only 2 numbers. Change context to repeat pattern mode.
        #So long as RPM = 1, repeat sequence and check. If there's still the same 2 numbers stored, good. If not, change RPM to 0.

        #So, there'll be 3 checks, basically.
        #if RPM=1: {binary pattern check 01. Trying to be given a reason to set RPM to 0. If any number other than the 2 stored, RPM=0.}
        #if RPM=1: {Full Tuple check. See if the current binary pattern tuple matches the stored binary tuple to see if we're REALLY in a stable loop.}
        #if RPM=0: {Binary pattern check 02. See if there's only 2 unique numbers. If yes, store the current iteration number, the tuple and the two numbers. set RPM=1}
        #if RPM=0: {Zero check. Checks to see if every entry is 0.}

        #Both states have a 'termination loop'. Loop #2 and Loop #4 can both cancel the iterations and give the final iteration count.
    #Let's have the checks first then run the Ducci. The iterator will be here.

    RunnerList = duclist

    iterations = 0

    binary_x = None
    binary_y = None
    binary_START_TUPLE = None
    binary_START_ITERATION = None

    RPM = 0

    while true:
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #BINARY PATTERN CHECK 01 GOES HERE=================================================================================================================
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #BINARY PATTERN CHECK 01 GOES HERE=================================================================================================================
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #FULL TUPLE CHECK GOES HERE========================================================================================================================
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #FULL TUPLE CHECK GOES HERE========================================================================================================================
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #BINARY PATTERN CHECK 02 GOES HERE=================================================================================================================
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        helper_binx = None #This is a checker, temp while the binary_x and binary_y are for each epoch
        helper_biny = None
        helper_bin = 0 #This is a binary flag. It's set to 1 once we have 2 unique numbers. Set to 0 if we find >2.

        if binary_START_TUPLE != None:

        #bin_x and bin_y have to be checked against.
        #Check to see if there's only two numbers. If yes, store in binary_x and binary_y
        for x in RunnerList:

            if helper_binx == None:
                helper_binx = x

            elif helper_biny == None and helper_binx != None and x != helper_binx:
                #So, we have an x that doesn't match helper_binx, which has been taken. So helper_biny gets this one.
                helper_biny = x
                helper_bin = 1

            if helper_biny != None and helper_binx != None and x != helper_biny and y != helper_binx:
                #Now we have a number that doesn't match either helper while we've already got values for the helpers. >2 numbers, trash.
                helper_bin = 0
                break #break out.

        #After the loop, we can see if we have a 0 tuple easily. If helper_biny is *still* None and helper_binx is 0, then they're all 0.
        if helper_biny == None and helper_binx == 0:
            break #break out of the while loop.

        if helper_bin == 1:
            #Here we go. Sets all these permenate values that'll last after this epoch. If we survived the for loop with helper_bin still at 1, do this.
            binary_x = helper_binx
            binary_y = helper_biny
            binary_START_TUPLE = RunnerList
            binary_START_ITERATION = iterations
            RPM = 1
            #THIS IS HOW WE CHANGE THE START TUPLE

        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #BINARY PATTERN CHECK 02 GOES HERE=================================================================================================================
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        #SET UP NEXT LOOP
        RunnerList = RunDucci(RunnerList)
        iteration += 1
        #BEGIN NEW LOOP

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #FINAL PRINT
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def RunDucci(runlist):
    #Here's where we make and send a new Ducci list. Also PRINT the line.

