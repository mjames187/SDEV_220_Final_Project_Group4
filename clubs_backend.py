class Club:
    name = "UNDEFINED"
    poster = "Jane Doe"
    location = "UNDEFINED"
    startTimeHours = 0
    startTimeMins = 0
    endTimeHours = 0
    endTimeMins = 0
    sponsor = "UNDEFINED"
    description = "This is a club that doesn't quite have an identity just yet!"
    interest = 0
    def __init__(self, name, poster, location, startTime1, startTime2, endTime1, endTime2, sponsor, description):   
        self.name = name
        self.poster = poster
        self.location = location
        self.startTimeHours = startTime1
        self.startTimeMins = startTime2
        self.endTimeHours = endTime1
        self.endTimeMins = endTime2
        self.sponsor = sponsor
        self.description = description

def interestQuery(club):
    if input("Are you interested in this club? y/n ") == "y":
        club.interest += 1


def userClubInput():
    nameInput = input("Name of club: ")
    posterInput = input("Name of club founder: ")
    locInput = input("Location: ")
    startHourInput = int(input("Time activity starts: "))
    startMinInput = int(input(":"))
    endHourInput = int(input("Time activity ends: "))
    endMinInput = int(input(":"))
    sponsorInput = input("First and last name of club's faculty sponsor: ")
    descInput = input("Description: ")
    return Club(nameInput,posterInput,locInput,startHourInput,startMinInput,endHourInput,endMinInput,sponsorInput,descInput)

def clubDisplay():
    print("Name:", selected.name)
    print("Founder:", selected.poster)
    print("Location:", selected.location)
    print("Time:", selected.startTimeHours, ":", selected.startTimeMins, "-", selected.endTimeHours, ":", selected.endTimeMins)
    print("Sponsor:", selected.sponsor)
    print("Interest:", selected.interest)
    print("Description:", selected.description)

club1 = userClubInput()

selected = club1

clubDisplay()

interestQuery(selected)

clubDisplay()