#!/usr/bin/env python
''' Towing capacity calculator, takes user inputs for vehicle and trailer data, then determines if the vehicle is over payload or under gross combined vehicle weight rating. Proof of concept before turning this into a web app.

    Disclaimer: If you use this, double-check using your own math, too. This has not gone through a formal validation process, and I don't want my code to cause any accidents. -jmf '''

# Check if over/under payload
def payloadcheck(availablepayload):
    if availablepayload >= 0:
        print("Available payload: {}".format(availablepayload))
        return True
    else:
        print("Exceeded Payload! Over payload capacity by {}".format(availablepayload))
        return False

# check if over/under GCVWR
def gcvwcheck(towcapacity, newgcvw):
    if newgcvw >= towcapacity:
        print("Acceptable! With combined weight of {}".format(newgcvw))
        print("You are under your GCVWR by {}".format(towcapacity - newgcvw))
        return True
    else:
        print("Exceeded GCVWR! Over capacity by {}".format(newgcvw - towcapacity))
        return False

def getdata():
    vehicle = input("What vehicle will be doing the towing? ")

    # dry weight, or curb weight = unloaded vehicle weight, WITHOUT driver, passengers, or cargo
    truckdrywt = int(input("Curb weight: "))

    # gvwr = maximum allowed weight of a fully loaded vehicle (dry wt + driver + passengers + cargo)
    gvwr = int(input("Gross Vehicle Weight Rating (GVWR): "))

    # gcvw = curb weight + allowable payload + passenger weight + trailer weight
    gcvwr = int(input("Gross Combined Vehicle Weight Rating (GCVWR): "))

    # payload = maximum allowed weight of passengers + cargo + hitch
    payload = int(input("Payload: "))

    # tow capacity = defined by manufacturer, listed in owners manual or a manufacturer's tow guide
    towcapacity = int(input("Tow capacity: "))

    # passenger weight = driver + all human and non-human riders
    passengerwt = int(input("Combined driver and passenger weight: "))

    # cargo = everything in the vehicle that isn't sentient
    cargo = int(input("Cargo weight inside the vehicle: "))


    trailer = input("What trailer are you towing? ")

    # trailer dry weight, or curb weight = unloaded weight, can be determined by a sticker on the trailer or by taking an unloaded trailer to a truck scale. Published unloaded weights may or may not include water/waste/propane
    trailerdrywt = int(input("Trailer curb weight: "))

    # trailer gcvw = dry weight + everything inside it
    trailergvwr = int(input("Trailer Gross Vehicle Weight Rating (GVWR): "))

    # hitch weight = defined by manufacturer, listed in manual or sticker on the trailer
    hitchwt = int(input("Trailer hitch weight: "))

    availablepayload = payload - (passengerwt + cargo + hitchwt)
    newgvw = truckdrywt + hitchwt + passengerwt + cargo
    newgcvw = trailergvwr - hitchwt + newgvw

    print("\nWith the {} towing the {}: ".format(vehicle, trailer))

    payloadcheck(availablepayload)
    gcvwcheck(towcapacity, newgcvw)


def main():
    print("==================================================")
    print("Towing calculator.")
    print("It does not matter if you use pounds or kilograms, just be consistent. \n")

    getdata()

    print("\nDon't forget to check the capacity of your tires and gross axle weight ratings (GAWR).")
    print("==================================================")

main()


''' inspiration for this came from Marc Leach's Excel worksheet here: http://www.keepyourdaydream.com/payload/ '''
