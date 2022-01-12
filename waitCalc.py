from sys import argv

try:
    arrRate = argv[1]
    arrTime = argv[2]
    serRate = argv[3]
    serTime = argv[4]
    timeRangeHr = argv[5]
    line = argv[6]
except IndexError:
    arrRate = input("Enter amount of people to arrive: ")
    arrTime = input("Enter amount of time for arrival: ")
    serRate = input("Enter how many people service can work with: ")
    serTime = input("Enter amount of time for service: ")
    timeRangeHr = input("How long will the ride run: ")
    line = input("How many people in line: ")

class ride:
    def __init__(self, arrRate, arrTime, serRate, serTime, timeRangeHr, line) -> None:
        self.arrRate = arrRate
        self.arrTime = arrTime
        self.serRate = serRate
        self.serTime = serTime
        self.timeRangeHr = timeRangeHr
        self.line = line
        self.report = []

    def printRideStats(self):
        print("Arrival Rate: ", self.arrRate, "Arrival Time: ", self.arrTime, "Service Rate: ", self.serRate, "Service Time: ", self.serTime, "Hours: ",timeRangeHr, "Line: ", line)
        
    def startRide(ride):
        for index, seconds in enumerate((ride.timeRangeHr*60)*60, start=1):

            if int(index) % int(ride.arrTime) == 0:
                ride.line = int(ride.line) + int(ride.arrRate)

            if int(index) % int(ride.serTime) == 0:
                ride.line = int(ride.line) - int(ride.serRate)
            
            ride.report.append("Second "+str(index)+": Line is "+str(ride.line)+" long.  Arrival added "+str(ride.arrRate)+ " - Service took away "+str(ride.serRate)+"\n")     

    def printRide(ride):
        f=open("WaitReport.txt", "w")
        f.write("---- Start ----\n")
        f.write(str(ride.printRideStats()))
        for index,item in enumerate(ride.report):
            f.write(ride.report[index]+"\n")
                
        f.write("Ride Stats: \n Arrival time: "+ str(ride.arrTime) + " Arrival rate: " + str(ride.arrTime) + "\n Service time: " + str(ride.serTime) + " Service rate: " + str(ride.serRate) + "\n Ride operating hours: " + str(ride.timeRangeHr) + " Ride starting line: " + str () + "\n")
        f.close

x = ride(arrRate, arrTime, serRate, serTime, timeRangeHr, line)

x.startRide()

x.printRide()