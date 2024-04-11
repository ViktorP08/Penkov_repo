#Penguin Olympics: Swimming Race Disaster
#The situation...
#The fastest penguins in the world have just swum for the ultimate prize in professional penguin swimming.
#The cameras that were capturing the race stopped recording half way through.
#The athletes, and the fans are in disarray waiting for the results.
#The challenge...
#Given the last recorded frame of the race, and an array of penguin athletes, work out the gold, silver and bronze medal positions.
#The rules...
#Assume all penguins swim at the same speed, when swimming through the same kind of water (waves or smooth water).
#Waves (~) take twice as long to swim through as smooth water (-).
#Penguins (p or P) are racing from left to right.
#There can be any number of lanes, and the race can be any length.
#All Lanes in a single race will be the same length.
#Penguin names are in the same order as the lanes.
#Return a string in this format: "GOLD: <name-1>, SILVER: <name-2>, BRONZE: <name-3>"
#There will always be an equal amount of penguins and lanes.
#There will always be a top three (no draws).

def penguin_olympics(photo, penguins):
    times = []

    for lane, penguin in zip(photo, penguins):
        time = lane.count("-") + 2 * lane.count("~")
        times.append(time)

    timess = sorted(times)
    gold = times.index(timess[0])
    silver = times.index(timess[1])
    bronze = times.index(timess[2])

    gold_name = penguins[gold]
    silver_name = penguins[silver]
    bronze_name = penguins[bronze]

    return f"GOLD: {gold_name}, SILVER: {silver_name}, BRONZE: {bronze_name}"
photo1 = ["|----p---~---------|", "|----p---~~--------|", "|----p---~~~-------|"]
penguins1 = ["Derek", "Francis", "Bob"]
print(penguin_olympics(photo1, penguins1))

photo2 = ["|-~~---------~--P-------|", "|~~--~P----------~-------|", "|--------~-P---------------|", "|--------~-P----~~~------|"]
penguins2 = ["Joline", "Abigail", "Jane", "Gerry"]
print(penguin_olympics(photo2, penguins2))