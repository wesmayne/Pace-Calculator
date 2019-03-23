km = float(input("How far did you run in km?\n"))
time = str(input("What was your time in hh:mm:ss?\n"))

def pace_calc():
    #To calculate mins/km you must convert hrs & secs to dec. format, then divide by distance then reconvert secs to time format
    hours1 = int(time[:2])
    minutes = int(time[3:5])
    secs1 = int(time[6:])

    secs2 = (secs1/60)
    hours2 = (hours1*60)
    minutes2 = minutes
    total = (hours2 + minutes2 + secs2)/km

    secs3 = str(total).partition(".")[2]
    secs3 = "." + secs3
    secs3 = float(secs3)*.6
    secs3 = round(secs3, 2)
    secs3 = str(secs3).partition(".")[2]
    if secs3 == '6':
        secs3 = "59"

    pace = "Your pace was " + str(total).partition(".")[0] + ":" + secs3 + "/km"

    print(pace)
def speed():
    #To calculate km/hr it is distance/time(in dec. format)
    hours = int(time[:2])
    minutes = int(time[3:5])
    secs = int(time[6:])

    minutes = minutes/60
    secs = secs/60/60
    total = hours + minutes + secs
    speeed = round(km/total, 2)

    print("Your speed was " + str(speeed) + " km/h")
while True:
    try:
        pace_calc()
        speed()
        break
    except ValueError:
        print("Invalid Response, Try Again!\n")
        time = str(input("What was your time in hh:mm:ss?\n"))


input("\n\nPress Enter to Esc")