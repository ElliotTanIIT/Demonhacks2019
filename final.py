from tkinter import*
import tkinter as tk
import tkinter.messagebox as m
import time
import urllib
import json
import requests
from pprint import pprint

def get_data_from_json(directions):
    departure_time_list = [];
    departure_stop_list = [];
    transit_type_list = [];
    return_list = [[]];
    for i in  range(len(directions['routes'])):
        for j in range(len(directions['routes'][i]['legs'])):
            for k in range(len(directions['routes'][i]['legs'][j]['steps'])):
                if 'transit_details' in directions['routes'][i]['legs'][j]['steps'][k]:
                    departure_time_list.append(directions['routes'][i]['legs'][j]['steps'][k]['transit_details']['departure_time']['text'])
                    #time_list.append(directions['routes'][i]['legs'][j]['steps'][k]['transit_details']['arrival_time']['text'])
                    departure_stop_list.append(directions['routes'][i]['legs'][j]['steps'][k]['transit_details']['departure_stop']['name'])
                    transit_type_list.append(directions['routes'][i]['legs'][j]['steps'][k]['transit_details']['line']['vehicle']['type'])

    #print(transit_type_list)
    #print(departure_stop_list)
    #print(departure_time_list)
    return_list = [departure_time_list,departure_stop_list,transit_type_list]
    print(return_list)
    print("success")
    return return_list

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

def commute(lst, profile):
    'compute cost of CTA commute; input list [tap time(s), location, mode(s)]'
    #print('{:5}  {:5}  {:6}  {:5}  {:5}'.format('trip', 'ride', 'mode', 'time', 'fare'))
     
    profile = profile.lower()
    trip = ''
    ride = 0
    time = 0
    tap = lst[0][0]
    rider = (('full',2.50, 2.25, .25), ('reduced', 1.25, 1.10, .15), ('student', .75, .75, .15))
    fare = 0
    firstSubway = 0
    firstBus = 0
    transfer = 0
    if profile == 'full':
        firstSubway = rider[0][1]
        firstBus = rider[0][2]
        transfer = rider [0][3]
    elif profile == 'reduced':
        firstSubway = rider[1][1]
        firstBus = rider [1][2]
        transfer = rider[1][3]
    elif profile == 'student':
        firstSubway = rider[2][1]
        firstBus = rider[2][2]
        transfer = rider[2][3]
    for i in range(len(lst[0])):
        ride += 1
        time = lst[0][i] - tap
        if ride == 1 and time < 120 and lst[2][i] == 'BUS':
            fare += firstBus
            trip = 'first'
            #print('{:10}  {:5}  {:6}  {:5}  {:5.2f}'.format(trip, ride, lst[2][i], lst[0][i],fare))
        elif ride == 1 and time < 120 and lst[2][i] == 'SUBWAY':
            fare += firstSubway
            trip = 'first'
            #print('{:10}  {:5}  {:6}  {:5}  {:5.2f}'.format(trip, ride, lst[2][i], lst[0][i],fare))
        elif ride == 2 and time < 120:
            fare += transfer
            trip = 'transfer'
            #print('{:10}  {:5}  {:6}  {:5}  {:5.2f}'.format(trip, ride, lst[2][i], lst[0][i], fare))
        elif ride > 2 and time < 120:
            fare += transfer
            #print('{:10}  {:5}  {:6}  {:5}  {:5.2f}'.format(trip, ride, lst[2][i], lst[0][i], fare))
            trip = 'transfer'
            ride = 0
            tap = lst[0][i]
        elif time >= 120 and lst[2][i] == 'BUS':
            fare += firstBus
            ride = 1
            trip = 'first'
            #print('{:10}  {:5}  {:6}  {:5}  {:5.2f}'.format(trip, ride, lst[2][i], lst[0][i], fare))
            tap = lst[0][i]
        elif time >= 120 and lst[2][i] == 'SUBWAY':
            fare += firstSubway
            ride = 1
            trip = 'first'
            #print('{:10}  {:5}  {:6}  {:5}  {:5.2f}'.format(trip, ride, lst[2][i], lst[0][i], fare))
            tap = lst[0][i]
    return fare



def run():
    global start_loc
    global end_loc
    start_loc = input_start.get()
    end_loc = input_end.get()
    profile = user_type
    print(profile)
    # api key
    api_key = 'AIzaSyA7e-VjNC3ymu_pLAv-FjshTXx2TB4Ymjw'
    # google api address
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    origin = start_loc.replace(' ', '+')
    destination = end_loc.replace(' ', '+')
    mode = 'transit'
    nav_req = "origin={}&destination={}&mode={}&key={}".format(origin, destination, mode, api_key)
    my_request = endpoint + nav_req
    response = urllib.request.urlopen(my_request)
    directions = json.load(response)
    data_list = get_data_from_json(directions)
    #first list in data_list is time list
    time_list_mins = []
    for x in data_list[0]:
        time_list_mins.append(parse_time_2_min(x))
    data_list[0] = time_list_mins
    total = commute(data_list, profile)
    print("total fare: ${}".format(total))
    


# create the application
r = tk.Tk()

#print(start_loc,end_loc,z_value)

# here are method calls to the window manager class
r.title("Chicago transit")
r.maxsize(1000, 500)
s = tk.Label(r, text="Start", width=25)
s.grid(column=0, row=0)
input_start = tk.Entry(r, bd =5)
input_start.grid(column=1, row=0)
d = tk.Label(r, text="Destination", width=25)
d.grid(column=0, row=1)
input_end = tk.Entry(r, bd =5)
input_end.grid(column=1, row=1)

def getUsertype():
    global user_type
    user_type = user_var.get()
    print(user_type)
user_var = StringVar(r)
user_var.set("Full") # default value

u_t = OptionMenu(r, user_var, "Full", "Reduced", "Student",command=lambda _: getUsertype())
u_t.grid(column=1, row=2)

user = tk.Label(r, text="User Type", width=25)
user.grid(column=0, row=2)

u= tk.Button(r, text="User Comment", width=25)
u.grid(column=0, row=4)
#saves the inputs from the entries
next=tk.Button(r, text="Next", width=25, command=run)
next.grid(column=1, row=4)

# start the program
r.mainloop()