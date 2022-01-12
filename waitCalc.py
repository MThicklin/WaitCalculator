from sys import argv
import random

try:
    arrRate = argv[1]
    arrTime = argv[2]
    serRate = argv[3]
    serTime = argv[4]
    timeRangeHr = argv[5]
    line = argv[6]
    lineCap = argv[7]

except IndexError:
    arrRate = input("Enter amount of people to arrive: ")
    arrTime = input("Enter amount of time for arrival: ")
    serRate = input("Enter how many people service can work with: ")
    serTime = input("Enter amount of time for service: ")
    timeRangeHr = input("How long will the ride run: ")
    line = input("How many people in line: ")
    lineCap = input("What's the line's capacity: ")


class ride:
    def __init__(self, arrRate, arrTime, serRate, serTime, timeRangeHr, line, lineCap) -> None:
        self.arrRate = arrRate
        if self.arrRate == 'r':
            self.arrRate = random.randrange(1, 10)
        self.arrTime = arrTime
        if self.arrTime == 'r':
            self.arrTime = random.randrange(1, 10)
        self.serRate = serRate
        if self.serRate == 'r':
            self.serRate = random.randrange(1, 10)
        if int(self.serRate) < int(self.arrRate):
            answ = input(
                "Service Rate is lower then Arrival Rate. Keep(k) or Correct(c)?: "
            )
            if answ == 'r':
                self.serRate = random.randrange(1, 10)
            elif answ == 'c':
                print("Current Service Rate: ", self.serRate,
                      " - Current Arrival Rate: ", self.arrRate)
                self.serRate = input("New Service Rate: ")
            elif answ == 'k':
                pass
        self.serTime = serTime
        if self.serTime == 'r':
            self.serTime = random.randrange(1, 10)
        self.timeRangeHr = timeRangeHr
        if self.timeRangeHr == 'r':
            self.timeRangeHr = random.randrange(1, 10)
        self.line = line
        if self.line == 'r':
            self.line = int(random.randrange(1, 10))
            self.stLine = self.line
        self.cap = lineCap
        if self.cap == 'r':
            self.cap = random.randrange(1, 10)
        self.report = []

    def startRide(ride):
        lineResult = ""
        ride.report.append("Minute 0: Ride opens with " + str(ride.line) + " people.\n")
        for mins in range(int(ride.timeRangeHr * 60 + 1)):
            if (int(ride.line) > int(ride.cap)):
                lineResult = "  Line capacity met, Arrival rate to 0..."
                arrRateOld = ride.arrRate
                ride.arrRate = 0
            elif (int(ride.line) < int(ride.cap) and ride.arrRate == 0):
                ride.arrRate = arrRateOld
            else:
                pass

            if int(mins) % int(ride.arrTime) == 0:
                ride.line = int(ride.line) + int(ride.arrRate)
                arrResult = "  Arrival added " + str(ride.arrRate)
            else:
                arrResult = ""

            if int(mins) % int(ride.serTime) == 0:
                ride.line = int(ride.line) - int(ride.serRate)
                serResult = "  Service took away " + str(ride.serRate)
            else:
                serResult = ""

            if (ride.line < 0):
                lineWarning = "  Negative line length was detected."
                lineResult = lineWarning + "  Line size capped at 0."
                ride.line = 0
            elif (int(ride.line) <= 0 and int(len(lineResult)) > 1):
                  lineResult = "Line size currently capped at 0."
                  ride.line = 0
            elif (int(ride.line) > 0 and int(len(lineResult)) > 1):
                lineResult = "---Line normalized---"
            else:
                lineResult = ""

            lineSize = "  Line is " + str(ride.line) + " long."

            ride.report.append("Minute " + str(mins) + ":" + lineSize +
                               lineResult + arrResult + serResult + "\n")

            if (arrResult, serResult, lineResult != ""):
                arrResult = ""
                serResult = ""
                lineResult = ""
            else:
                pass

    def printRide(ride):
        f = open("WaitReport.txt", "w")
        
        rideStats = "Ride Stats: \n Arrival time: " + str(ride.arrTime) + " Arival rate: " + str(ride.arrTime) + "\n Service time: " + str(ride.serTime) + " Service rate: " + str(ride.serRate) + "\n Ride operating hours: " + str(ride.timeRangeHr) + " Ride starting line: " + str(ride.stLine) + " Line Capacity: " + str(ride.cap) + "\n"

        f.write("---- Start ----\n")
        f.write(rideStats)
        for index, item in enumerate(ride.report):
            f.write(ride.report[index])
        f.write(rideStats)
        f.close


x = ride(arrRate, arrTime, serRate, serTime, timeRangeHr, line, lineCap)

x.startRide()

x.printRide()
