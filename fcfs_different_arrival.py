#COMPLETED VERSION - differing arrival time

import tabulate


def fcfs (processes):
    #this function returns a new dictionary containing new information of the processses
    
    #declare output new dictionary
    
    scheduled_processes = []
    
    #counter is to keep track of the current time that has passed for every loop
    counter = 0
    
    #looping around the dictionary
    for i in processes:
        #find the first process 
        if i['order'] == 1:
            
            #find burst_time 
            burst_time = i['burst_time']
            id = i['id']
            order = i['order']
            arrival_time = i['arrival_time']
            
            if arrival_time > counter:
                counter = arrival_time
            
            #default waiting time is equal to zero
            waiting_time = 0
            turnaround_time = burst_time - arrival_time
            counter = turnaround_time
            
            #add attributes to new dictionary
            scheduled_processes.append({
                
                'id':id,
                'order': order,
                'arrival time': arrival_time,
                'burst time': burst_time,
                'waiting time': waiting_time,
                'turnaround time': turnaround_time,
                
                
            })
            
            
        else:
            
            
            #declaring initial attributes 
            order = i['order']
            process_id = i['id']
            arrival_time = i['arrival_time']
            
            if counter < arrival_time:
                counter = arrival_time
            
            
            #find burst_time
            burst_time = i['burst_time']
            
            #calculate new attributes 
            waiting_time = counter - arrival_time
            turnaround_time = waiting_time + burst_time
            
            #update counter
            counter = turnaround_time
            
             # add attributes to new dictionary 
            scheduled_processes.append({
                
                'id':process_id,
                'order': order,
                'arrival time': arrival_time,
                'burst time': burst_time,
                'waiting time': waiting_time,
                'turnaround time': turnaround_time
                
                
                
            })
             
    return scheduled_processes

def findAverageWaitingTime(scheduled_processes):
    n = len(scheduled_processes)
    total_waiting_time = 0
    
    for i in scheduled_processes:
        waiting_time = i['waiting time']
        total_waiting_time =+ waiting_time
        
    average = (total_waiting_time)/n
    
    return average

def findAverageTurnaroundTime(scheduled_processes):
    n = len(scheduled_processes)
    total_turnaround_time = 0
    
    for i in scheduled_processes:
        turnaround_time = i['turnaround time']
        total_turnaround_time =+ turnaround_time
    
    average = (total_turnaround_time)/n
    
    
    return average

def main():
    
    
     processes = [
        
        {"order": 1,"id": "P1", "arrival_time": 1, "burst_time": 10},
        {"order": 2,"id": "P2", "arrival_time": 5, "burst_time": 5},
        {"order": 3,"id": "P3", "arrival_time": 7, "burst_time": 8},
        {"order": 4,"id": "P4", "arrival_time": 12, "burst_time": 15},
        {"order": 5,"id": "P5", "arrival_time": 14, "burst_time": 25},
        {"order": 6,"id": "P6", "arrival_time": 15, "burst_time": 13},
        {"order": 7,"id": "P7", "arrival_time": 25, "burst_time": 56},
        {"order": 8,"id": "P8", "arrival_time": 26, "burst_time": 2},
        {"order": 9,"id": "P9", "arrival_time": 30, "burst_time": 76},
        {"order": 10,"id": "P10", "arrival_time": 34, "burst_time": 45},
        {"order": 11,"id": "P11", "arrival_time": 36, "burst_time": 12}
    
    ]
     
     output = fcfs(processes)
     header = output[0].keys()
     rows = [x.values() for x in output]
     print(tabulate.tabulate(rows, header))
    
     averageWaitingTime = str(round(findAverageWaitingTime(output),2))
     averageTurnaroundTime = str(round(findAverageTurnaroundTime(output),2))
    
     print("Average Waiting Time:",averageWaitingTime)
     print("Average Turnaround Time:",averageTurnaroundTime)
    
main()
    
    
    
    
    

            
            
            
            