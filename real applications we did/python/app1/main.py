import pandas as pd
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer


#Our main aim is on here to train machine learning project based on animals and their features 


yapay zekaya kullanıcının belirttiği konuda eğitim seti oluşturmak için hazır yapay zekalar kullanılacak

Önce kullanıcının girdiği konuyla ilgili ana başlıklar alınacak 
sonra ana başlıklarla ilgili detaylar alınacak


data = {
    "red fox": {
        "species": "vulpes vulpes",
        "genius": "vulpes",
        "family": "canidae",
        "order": "carnivora",
        "class": "mammalia",
        "phylum": "chordata",
        "kingdom": "animalia",
        "domain": "eukaryota",
        "averageWeight": "5.5",
        "averageBodyLength": "75",
        "averageShoulderHeight": "42",
        "mainColor": "red-brown with white underside",
        "howToBreed": "Sexual reproduction; mating season in winter",
        "scientificName": "Vulpes vulpes",
        "habitat": ["Forests", "grasslands", "urban areas", "tundra"],
        "lifeTime": "3-6 years in the wild, up to 14 years in captivity",
        "habitsOfFeeding": ["small mammals", "birds", "fruits", "insects"],
        "differencesBetweenMaleAndFemale": "Males are typically larger than females",
        "dailyActivity": "Mostly nocturnal, active during the night",
        "socialStructure": "Solitary or small family groups",
        "communicationTypes": ["Vocalizations (barks, screams)", "body language", "scent marking"],
        "distributionOfGeographical": ["Found across Europe", "Asia", "North America","parts of Australia"],
        "balanceOfHunterHunting": "Predator and scavenger, balances predator-prey dynamics",
        "naturalThreats": ["large predators", "diseases"],#
        "threatsCausedByHumanity": ["habitat destruction", "roadkill", "poaching"],
        "situationOfProtection": "Least Concern (IUCN Red List)",
        "specialAbilities": ["Sharp senses (hearing, sight)", "adaptable diet"],
        "turkishName": "Kızıl Tilki"
    },
    "arctic fox": {
        "species": "vulpes lagopus",
        "genius": "vulpes",
        "family": "canidae",
        "order": "carnivora",
        "class": "mammalia",
        "phylum": "chordata",
        "kingdom": "animalia",
        "domain": "eukaryota",
        "averageWeight": "3.5",
        "averageBodyLength": "50",
        "averageShoulderHeight": "35",
         "mainColor": "white fur with seasonal changes to brown or gray in summer",
        "howToBreed": "Sexual reproduction; mating season in winter",
        "scientificName": "Vulpes lagopus",
        "habitat":["Arctic regions", "tundra","icy plains"] ,#
        "lifeTime": "3-6 years in the wild, up to 10 years in captivity",
        "habitsOfFeeding": ["small mammals", "birds", "fish", "berries", "insects"],#
        "differencesBetweenMaleAndFemale": "Males and females are similar in size, though males are slightly larger",
        "dailyActivity": "Primarily nocturnal or crepuscular, active at night and dusk",
        "socialStructure": "Solitary or small family groups",
        "communicationTypes": ["Vocalizations (screams, barks)", "body language", "scent marking"],#
        "distributionOfGeographical": "Found in Arctic regions across the Northern Hemisphere",
        "balanceOfHunterHunting": "Predator and scavenger, plays a role in controlling small prey populations",
        "naturalThreats": ["large predators (such as wolves, polar bears)", "extreme weather conditions"],#
        "threatsCausedByHumanity": ["habitat loss due to climate change", "hunting", "roadkill"],#
        "situationOfProtection": "Least Concern (IUCN Red List), but affected by climate change",
        "specialAbilities": "Thick fur for insulation, excellent hearing and smell, adapts to extreme cold",
        "turkishName": "Kutup Tilkisi"
    }
}

df = pd.DataFrame(data) 

#habitat and habitsOfFeeding is list values
habitat = []
binarizedHabitat = None
habitsOfFeedingperAnimal = []
binarizedhabitsOfFeedingperAnimal = None
communicationTypes = []
binarizedcommunicationTypes = None

for column in df.columns:
    for key2,value2 in data[column].items():

        if data[column][key2] == data[column]["habitat"]:
            habitat.append(value2)
        elif data[column][key2] == data[column]["habitsOfFeeding"]:
            habitsOfFeedingperAnimal.append(value2)
        elif data[column][key2] == data[column]["communicationTypes"]:
            communicationTypes.append(value2)
            

print(habitat)
multiLabel = MultiLabelBinarizer()
binarizedHabitat = multiLabel.fit_transform(habitat)
binarizedhabitsOfFeedingperAnimal = multiLabel.fit_transform(habitsOfFeedingperAnimal)
binarizedcommunicationTypes = multiLabel.fit_transform(communicationTypes)
multiLabel.classes_




df.to_csv("animal.csv", index = False)


