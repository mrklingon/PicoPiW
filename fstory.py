#Build a random fantasy story

import random

races = ["human", "elf", "dwarf", "hobbit"]
classes = ["wizard", "burglar",  "healer", "warrior"]
names = [
    "Krargrouk Honorgrog",
    "Kargroun Shadowbrew",
    "Vomdoick Emberminer",
    "Polo Littlefoot",
    "Leutfrid Baggins",
    "Fastolph Gardner",
    "Alen Tormyar",
    "Ascal Perbanise",
    "Felaern Tortoris",
    "Crestiennet of the Night",
    "Thilrern Derorvo",
    "Bheksomu Dreinzul",
    "Khondui Bhugazel",
    "Averitt the Heroic",
    "Heimeri of the South",
]

destination = [
    "Alterwood Palace",
    "Corftey Fortress",
    "Clarn Castle",
    "Wringcaster Citadel",
    "The Eternal Haunt",
    "The Buried Burrows",
    "The Ethereal Cells  ",
    "Water Leopard Woods",
    "Baxpool Covert",
    "Kirkasing Woodland",
]

weapons = [
    "Soulsliver",
    "Cryptic",
    "Blackout",
    "Doomguard",
    "Windsong Idol",
    "Thirsting Slicer",
    "Isolated Copper Sabre",
    "Pride's Steel Protector",
    "Aetherius, Quickblade of Eternal Bloodlust",
    "Treachery, Spine of Justice",
    "Stinger, Claymore of the Burning Sun",
    "Barbarian Iron Deflector",
    "Mournblade, Gift of Ancient Power",
]

enemy = [
    "Phasething",
    "Chaosling",
    "Rottingstep",
    "Boulderfang",
    "Phantomman",
    "Dreadcrackle",
    "Soilserpent",
    "Mornlich",
    "The Lanky Statue",
    "The Feathered Bane Jackal",
    "The Black-Eyed Cinder Spider",
    "The Tusked Venom Drake",
]


travel = [" travels to", " returns from", " explores within", " gets lost at"]
treasure = [
    "Fortune's Horn",
    "Worship Mirror",
    "Insanity Boots",
    "Sanctifying Ark",
    "Roaring Scepter",
    "Misty Satchel",
    "Hailstorm Charm",
]

forest = [
    "Misty Bluff Wilds",
    "Pleasant Brook Grove",
    "Huge Wilds",
    "Majestic Wilds",
    "Short-Tailed Snail Woodland",
    "Speckled Squirrel Grove",
    "Faint Wood",
    "Jagged Covert",
    "Short-Tailed Treefrog Grove",
    "Imperial Spider Covert",
    "Mannear Wilds",
    "Shipsons Wood",
    "Alberboia Grove",
    "Bois de la Camris",
    "Fort du Bouluon",
    "Fort de la Carcaveil",
    "Fort de la Sarmont",
]

problem = [
    "Suddenly out of {frst} appears a {monster}",
    "{name} is surprised when {monster} attacks from {frst}",
    "A battle begins. The deadly {monster} attacks {name} after leaping out of {frst}!",
    "Alarm! {monster} materializes from the edge of {frst}!",
]

solution = [
    "Stumbling badly, {name} somehow manages to find the {weapon} and dispatch them!",
    "Heroicly, {name} quickly banishes the creature to {forest} with the {weapon}.",
    "Even though {name} fails to find a weapon like {weapon}, the monster shuffles away to {forest}",
]


purpose = ["seeking", "discovering", "losing", "finding"]


def player():
    nm = random.choice(names)
    rc = random.choice(races)
    cl = random.choice(classes)
    return [nm, rc, cl]


 
def story():
    #get a new character
    Player = player()

    Fstory = ""

#Construct a story
    Fstory = Fstory +"The " + Player[1] + " " + Player[2] + " " + Player[0]+ "\n"
    Fstory = Fstory +random.choice(travel)+ "\n"
    Fstory = Fstory +random.choice(destination)+ "\n"
    Fstory = Fstory +random.choice(purpose) + " " + random.choice(treasure)+ "\n"
    Fstory = Fstory + random.choice(problem).format(name=Player[0], frst=random.choice(forest), monster=random.choice(enemy))+ "\n"
    Fstory = Fstory + random.choice(solution).format(name=Player[0],forest=random.choice(forest),monster=random.choice(enemy),weapon=random.choice(weapons),)+ "\n"
#Return story
    return Fstory
