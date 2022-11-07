# Simulation

import random

hospitals = {"Alberta Children's Hospital": None, "South Health Campus": None}

resources = {"Ventilators": None, "Oxygen Tanks": None, "Nurses": None, "Doctors": None, "Beds": None}

capactiy = {
    "Emergency" : None,
    "Anesthetics" : None,
    "Burn Center" : None,
    "Cardiology" : None,
    "Critical Care" : None,
    "Diagnostic Imaging" : None,
    "Gasteroenterology" : None,
    "General Surgery" : None,
    "Gynecology" : None,
    "Haematology" : None,
    "Intensive Care Unit" : None,
    "Infection Control" : None,
    "Nephrology" : None,
    "Neurology" : None,
    "Oncology" : None,
    "Ophthalmology" : None,
    "Orthopedics" : None,
    "Otolaryngology" : None,
    "Physiotherapy" : None,
    "Rheumatology" : None,
    "Urology" : None,
}

def randomize_capacity():
    for key in capactiy:
        capactiy[key] = random.randint(0, 99)
    return capactiy

def randomize_resources():
    for key in resources:
        resources[key] = random.randint(0, 99)
    return resources



def sim():

    for hospital in hospitals:
        hospitals[hospital] = [randomize_capacity(), randomize_resources()]

    return hospitals

if __name__ ==   "__main__":
    print(sim())