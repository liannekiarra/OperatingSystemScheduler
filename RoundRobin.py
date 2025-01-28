# Round Robin - Different Arrival Times 

import array 
import tabulate

# Building a class so processes can be expressed as objects and not as a list of dictionaries.
# Having all attrivuts initiated at the beginning and to store useful boolean attributes for the Process objects.

class Process:
    #object contructor
    def __init__(self):
        self.complete = False
        self.insideQueue = False
        self.identifier = 0
        self.arrivalTime = 0
        self.burstTime = 0
        self.remainingBurstTime = 0
        self.completionTime = 0
        self.turnaroundTime = 0
        self.waitingTime = 0
        

#declaring processes

def declare_processes(id: list, arrival_time: list, burst_time: list):
    initial_processes = []
    
    identification = id
    arrival = arrival_time
    burstTime = burst_time
    
    c = 0
    for x in identification:
        id = identification[c]
        arrival_time = arrival[c]
        burst_time = burstTime[c]
        
        initial_processes.append({
            'Process ID': id,
            'Arrival Time': arrival_time,
            'Burst Time': burst_time

        }) 
        c = c+1
    
    return initial_processes

#building process objects from the declared processes

def makeProcesses(initial_processes: list):
    #process object list
    liveProcesses = [] #store process objects inside here
    
    
    for i in initial_processes:
        #extract information back
        id = i['Process ID']
        arrival_time = i['Arrival Time']
        burst_time = i["Burst Time"]
        
        # build object of Process class for each process
        process = Process()
        process.identifier = id
        process.arrivalTime = arrival_time
        process.burstTime = burst_time
        
        liveProcesses.append(process)
    return liveProcesses


def find_new_arrivals(liveProcesses: list, n: int, current_time: int, readystate:int):

    currentTime = current_time
    #finding the number of processes declared by user - using the id list 
    
    
    for i in range(n):
        process = liveProcesses[i]
        # if condition to find new arrivals by checking their arrival time against current time
        # and checking if they are inside the queue and that they havent been terminated (not Completed yet)
        if process.arrivalTime <= currentTime and not process.insideQueue and not process.complete:
            liveProcesses[i].insideQueue = True
            readystate.append(i) #adding Process object intp the queue

#this function updates the ready queue
def turnOn(liveProcesses: list, n: int ,quantum: int, readystate: list,current_time:int, terminatedProcesses: int ):
    
    #findind first element in the ready queue
    x = readystate[0]
    #deleteing first element
    readystate.pop(0)
    #finding remaining burst time 
    rbt = liveProcesses[x].remainingBurstTime 
    #finding complete status
    isComplete = liveProcesses[x].complete
    #finding arrival time
    arrivalTime = liveProcesses[x].arrivalTime
    
        
    
    #Comparing Remaining Brust Time against Quantum Value
    if liveProcesses[x].remainingBurstTime <= quantum: 
        liveProcesses[x].complete = True
        current_time += liveProcesses[x].remainingBurstTime
        liveProcesses[x].completionTime = current_time
        liveProcesses[x].waitingTime = liveProcesses[x].completionTime - liveProcesses[x].arrivalTime - liveProcesses[x].burstTime
        liveProcesses[x].turnaroundTime = liveProcesses[x].waitingTime + liveProcesses[x].burstTime
        #if waiting time becomes negative
        if liveProcesses[x].waitingTime < 0:
            liveProcesses[x].waitingTime = 0
 
        liveProcesses[x].burstTimeRemaining = 0
 
        #if not all processes are in the ready state queue, find new arrivals 
        if terminatedProcesses != n:
            find_new_arrivals(liveProcesses, n, current_time, readystate)
    else:
        #Process hasnt completed
        
        liveProcesses[x].burstTimeRemaining -= quantum
        current_time += quantum
 
        # if not all processes are in the ready state queue, find new arrivals
        # t
        if terminatedProcesses != n:
            find_new_arrivals(liveProcesses, n, current_time, readystate)
        # inserting the unfinished process back into the ready state queue
        readystate.append(x)
       
    
    return

def display (liveProcesses:list, n:int):
    
    
    averagewaitingtime = 0
    averageturnaroundtime = 0
    # sort the processes array by processes.PID
    liveProcesses.sort(key=lambda x: x.identifier)
 
    for i in range(n):
        print("Process ", liveProcesses[i].identifier, ": Waiting Time: ", liveProcesses[i].waitingTime,
              " Turnaround Time: ", liveProcesses[i].turnaroundTime, sep="")
        averagewaitingtime += liveProcesses[i].waitingTime
        averageturnaroundtime += liveProcesses[i].turnaroundTime
    print("Average Waiting Time: ", averagewaitingtime / n)
    print("Average Turnaround Time: ", averageturnaroundtime / n)
    
    return


def RoundRobin(liveProcesses: list, n:int, quantum: int):
    
    #making a queue for all the ready processes
    readystate = []
    readystate.append(0)#pushing first ready process
    
    liveProcesses[0].insideQueue = True #indicate the process is inside the queue
    
    currentTime = 0 #current time set 
    
    terminatedProcesses = 0
    
    while len(readystate) != 0:
        turnOn(liveProcesses, n, quantum, readystate, currentTime, terminatedProcesses)


if __name__ == "__main__":
    
    #enter preferred quantum
    quantum = 3

    
    # example values for round robin scheduling
    id = [1,2,3,4,5]
    arrival_time = [5,2,7,3,1]
    burst_time = [34,12,40,8,13]
    
    #find n
    n = len(id)
    
    #Step One: Declare Processes
    processDict = declare_processes(id,arrival_time,burst_time)
    
    #Step Two: Build Process objects and store them in a list
    liveProcesses = makeProcesses(processDict) #list of objects
    
    #Step Three: Sort out Process Objects based on arrival time
    liveProcesses.sort(key=lambda x: x.arrivalTime)
    
    #Step Four - run round robin function
    
    RoundRobin(liveProcesses, n, quantum)
    
    #Step Five - display the results from round robin
    display(liveProcesses, n)
    
    
    
        
    
    
    
    
    
    
    
    

    
    
    
    
    
    