#Build a SF story
#
import random




Systems = ["Proxima Centauri#", "4.2465", "Wolf 359#", "7.856", "Lalande 21185", "8.304", "Epsilon Eridani", "10.489", "Lacaille 9352#", "10.724", "Ross 128", "11.007", "Struve 2398 B#", "11.491", "Groombridge 34 A#", "11.619", "Epsilon Indi A", "11.867", "Tau Ceti#", "11.912"]
#ships = ["The Enterprise", "The Millenium Falcon", "Solar Sail Rembrandt"]
ships = ["Gamma XR3", "Brave Flyer", "USS Piranha", "Leviathan", "The Nova Siren", 
"The EAS Dilhan", "HMS Turin", "The Real Warrior", "The Nova Fortune", 
"The JMC Law", "The JMC Nebulon", "Perseus", "Aegean", 
"Pearce", "The White Corsair", "Mermaid", "Giant Nobel", 
"HMS Welshman", "USS Pantheon", "The Scrap Matador", "Gamma Intrepid", 
"USS Wyoming", "Patriotic Manoa", "The Starlight Goole", "The IKS Venture", 
"JMC Rimward XL5", "The Scrap Condor", "Royal Argo", "The Flying Lexington", 
"Slim Chekov", "USS Anubis"]

travel = ["travels to", "returns from"]
solution =  ["is repaired by automated systems.", " and tumbles out of control till emergency crews reach them", "and just barely reaches destination stardock."]
purpose = ["with supplies", "carrying passengers", "with ancient artifacts", "escaping a battle", "pursuing an enemy"]
problem = ["and is damaged in an explosion", "and loses power", "and runs out of fuel"]
solution =  ["and is repaired by automated systems.", " and tumbles out of control till emergency crews reach them", "and just barely reaches destination stardock."]
twist = ["And then a mysterious message arrives from {alien} {place}.",
         "Suddenly a ship appears from {place} warning of imminent {alien} attack.",
         "An urgent emergency message from {place} arrives. The {alien} planet is experiencing an epidemic.",
         "Word comes that the {alien} ambassador has just died on {place}."]
 
aliens = ["Stezets",
    "Scuns",
    "Cuds",
    "Vrucuins",
    "Bhisih",
    "Ahleath",
    "Dandaeds",
    "Qat'iet",
    "Gad",
    "Nahrins"]

planets = ["Mageinope",
    "Thotreatune",
    "Zolinda",
    "Nilreron",
    "Uclite",
    "Notania",
    "Guapra",
    "Brozalea",
    "Gerth NYV",
    "Strilia Q5OV"]

def nm(index):
    name = Systems[index*2]
    return(name)

def dist(index):
    dst = Systems[1+(index*2)]
    dst = eval(dst)
    return (dst)

def story():
    ind = random.randrange(10)
    SFStory = ""
    
    SFStory = SFStory + "Star System: " + nm(ind) + "\n"
    SFStory = SFStory + "Distance: " + str(dist(ind))+ " light years" + "\n-----\n"
    SFStory = SFStory + random.choice(ships)+ "\n"
    SFStory = SFStory + random.choice(travel)+ "\n"
    SFStory = SFStory + nm(ind)+ "\n"
    SFStory = SFStory + random.choice(purpose)+ "\n"
    SFStory = SFStory + random.choice(problem)+ "\n"
    SFStory = SFStory + random.choice(solution)+ "\n"
    SFStory = SFStory + random.choice(twist).format(place=random.choice(planets), alien = random.choice(aliens))
#return story
    return(SFStory)+ "\n"

