#transit app

#assumption: destination, point of origin, fastest route to destination,
#real time bus and train, stations and bus stops with limited accessability
#

#feature: estimate cost for commute based on time; determine an alternate safe route
# connnect Ventra rider profile
#conditions: walking speed and fare

#parameters: city crime data, train/bus schedule,


###def walk_speed():
##    'user age determines walking speed'
##    age = eval(input('enter age: '))
##    if age > 67:
##        return 1
##    else:
##        return 2.5
##
##def missed_trx(transfer):
##    'probability of making the transfer'
##    #speed = eval(input('enter age: '))
##    return walk_speed()/time
##
##
##
##
##
##    
##def commute_fee(lst):
##    '''assuming buses only, input buses taken and time for whole commute
##        return cost for trip'''
##    print('{:4}  {:5}  {:5}  {:5}  {:5}'.format('route', 'on', 'off', 'diff','fare'))
##    bus_counter = 0
##    minute_counter = 0
##    trip_counter = 1
##    for i in range(len(lst)):
##        minutes = lst[i][2] - lst[i][1]
##        bus_counter += 1
##        minute_counter += minutes
##        fare = (bus_counter - 1)*.25 + 2.25*trip_counter
##        print('{:4}  {:5}  {:5}  {:5}  {:5}'.format(lst[i][0], lst[i][1], lst[i][2], minutes, fare)) 
##        print ('{}  {}'.format(bus_counter, minute_counter))
##        if bus_counter == 3:
##            bus_counter = 0
##            trip_counter += 1
##            print ('reset: 3 bus')
##        elif minute_counter >= 120:
##            bus_counter = 0
##            minute_counter = 0
##            trip_counter += 1
##            print('reset: minute')
##    num_bus = eval(input('number of buses: '))
##    if 1 <= num_bus <= 3:
##        cost = (num_bus - 1)*.25 + 2.25
##        return cos

##def newList(nums):
##    lst = []
##    trip = 1
##    bus = 0
##    time = 0
##    fare = 0
##    tap = nums[0]
##    i = 0
##    while i in range(len(nums)):
##        bus += 1
##        time = nums[i] - tap
##        if bus == 1 and time < 120:
##            fare += 2.25
##            print (trip,bus,time,fare)
##            i += 1
##        elif bus == 2 and time < 120:
##            fare += .25
##            print (trip,bus,time,fare)
##        
##        break

##        if time >= 120:
##            fare += 2.25
##            bus = 1
##            trip += 1
##            print('reset')
##            print('{:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, fare))
##            new_trip = lst[i+1]
##        elif bus == 1 and time < 120:
##            fare += 2.25
##            print('{:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, fare))
##        elif bus == 2 and time < 120:
##            fare += .25
##            print('{:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, fare))
##        elif (bus > 2 and time < 120):
##            fare += .25
##            print('{:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, fare))
##            print('reset')
##            bus = 0
##            trip += 1
##            new_trip = lst[i+1]
        
##def test(num):
##    i = 0
##    lst = []
##    while i in range(num):
##        lst.append([i, 10*i])
##        print (lst)
##        i += 1
    
       
        
        
        
##        elif time >= 120:
##            print('{:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, fare))
##            print('reset: time')
##            bus = 0
##            trip += 1
##            new_trip = lst[i+1]

        


# this program takes a time format such as '5:37pm' or '10:22am' and converts it into minutes since 00:00
def parse_time_2_min(s):
    l = list(s)
    return_time = 0;
    hours = 0;
    mins = 0;
    # if ':' is in 1st index, hour is 1 digit
    if (l[1] == ':'):
        # determine AM or PM and parse hour to int
        if ((l[4]) == 'a'): # am
            hours = int(l[0])
        elif ((l[4]) == 'p'): # pm
            hours = int(l[0]) + 12
        else:
            print('hour format error')
        mins = int(l[2]+l[3])
        return_time = hours*60 + mins
    # if ':' is in 2nd index, hour is 2 digits
    elif(l[2] == ':'):
        if((l[5]) == 'a'):
            hours = int(l[0]+l[1])
        elif((l[5]) == 'p'):
            hours = int(l[0]+l[1]) + 12
        else:
            print('hour format error')
        mins = int(l[3]+l[4])
    return_time = hours*60 + mins
    return return_time           


sample = (0,10,30,90,120,600,745,750)

    
        
        
        

def commute2(nums, profile):
    #print('{:5}  {:5}  {:5}  {:5}  {:5}'.format('trip', 'bus', 'diff', 'time', 'fare'))
    trip = 1
    bus = 0
    time = 0
    tap = nums[0]
    rider = (('full',2.25, .25), ('reduced', 1.10, .15), ('student', .75, .15))
    fare = 0

    if profile == 'full':
        initial = rider[0][1]
        transfer = rider [0][2]
    elif profile == 'reduced':
        initial = rider [1][1]
        transfer = rider[1][2]
    elif profile == 'student':
        initial = rider[2][1]
        transfer = rider[2][2]
    for i in range(len(nums)):
        bus += 1
        time = nums[i] - tap
        if bus == 1 and time < 120:
            fare += initial 
            #print('{:5}  {:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, nums[i],fare))
        elif bus == 2 and time < 120:
            fare += transfer
            #print('{:5}  {:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, nums[i], fare))
        elif bus > 2 and time < 120:
            fare += transfer
            #print('{:5}  {:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, nums[i], fare))
            trip += 1
            bus = 0
            tap = nums[i]
        elif time >= 120:
            fare += initial
            bus = 1
            trip += 1
            #print('{:5}  {:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, nums[i], fare))
            tap = nums[i]
    return fare


##        time = nums[i] - tap
##        bus += 1
##        if bus == 1 and time < 120:
##            fare += 2.25
##            print('{:5}  {:5}  {:5}  {:5}'.format(trip, bus, time, fare))
##        elif bus == 2 and time < 120:
##            fare += .25
##            print('{:5}  {:5}  {:5}  {:5}'.format(trip, bus, time, fare))
##        elif bus > 2 and time < 120:
##            fare += .25
##            print('{:5}  {:5}  {:5}  {:5}'.format(trip, bus, time, fare))
##            bus = 0
##            trip += 1
##            tap = nums[i + 1]
##        elif time >= 120:
##            fare += 2.25
##            bus = 1
##            trip += 1
##            print('{:5}  {:5}  {:5}  {:5}'.format(trip, bus, time, fare))
##            tap = nums[i+1]
##        
##            

