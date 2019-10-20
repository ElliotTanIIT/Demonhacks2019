full_list = [['10:12am', '10:41am', '11:00am', '5:40am', '6:10am'], ['State & 30th Street', 'Washington', 'Megabus Stop on W Polk St. Between S Clinton St and S Canal St', '10th & P Street', "Gold's - 11th Street"], ['BUS', 'SUBWAY', 'BUS', 'BUS', 'BUS']]

def commute(full_list, profile):
    #first list in data_list is time list
    time_list_mins = []
    for x in full_list[0]:
        time_list_mins.append(parse_time_2_min(x))
    profile = profile.lower()
    trip = 1
    bus = 0
    time = 0
    tap = time_list_mins[0]
    rider = (('full',2.25, .25), ('reduced', 1.10, .15), ('student', .75, .15))
    fare = 0
    initial = 0
    transfer = 0

    if profile == 'full':
        initial = rider[0][1]
        transfer = rider [0][2]
    elif profile == 'reduced':
        initial = rider [1][1]
        transfer = rider[1][2]
    elif profile == 'student':
        initial = rider[2][1]
        transfer = rider[2][2]
    else:
        if initial == 0:
            print('error: no initial fair')
        if transfer == 0:
            print('error: no transfer fair')
    for i in range(len(time_list_mins)):
        bus += 1
        time = time_list_mins[i] - tap
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
            tap = time_list_mins[i]
        elif time >= 120:
            fare += initial
            bus = 1
            trip += 1
            #print('{:5}  {:5}  {:5}  {:5}  {:5.2f}'.format(trip, bus, time, nums[i], fare))
            tap = time_list_mins[i]
    return fare