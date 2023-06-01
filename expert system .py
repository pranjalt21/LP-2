# Define the patient class to hold information about a patient
class Patient:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.symptoms = ""

# Define the hospital class to hold information about a hospital
class Hospital:
    def __init__(self, name, location, services):
        self.name = name
        self.location = location
        self.services = services

# Define the expert system class to handle reasoning about patient symptoms
class ExpertSystem:
    def __init__(self):
        # Initialize hospitals with example data
        self.hospitals = [
            Hospital("St. Mary's Hospital", "New York", ["Emergency Room", "Cardiology", "Neurology"]),
            Hospital("Johns Hopkins Hospital", "Baltimore", ["Emergency Room", "Cancer Center", "Pediatrics"]),
            Hospital("Mayo Clinic", "Rochester", ["Emergency Room", "Gastroenterology", "Psychiatry"])
        ]

    # Function to get a list of hospitals that offer the required services
    def get_hospitals(self, services):
        result = []
        for hospital in self.hospitals:
            if self.hospital_has_services(hospital, services):
                result.append(hospital)
        return result

    # Function to determine if a hospital has all the required services
    def hospital_has_services(self, hospital, services):
        required_services = services.split(",")
        for service in required_services:
            if service not in hospital.services:
                return False
        return True

# Function to prompt the user for patient information and return a Patient instance
def get_patient_info():
    patient = Patient()
    print("Please enter patient information:")
    patient.name = input("Name: ")
    patient.age = int(input("Age: "))
    patient.gender = input("Gender: ")
    patient.symptoms = input("Symptoms: ")
    return patient

# Function to print a list of hospitals
def print_hospitals(hospitals):
    if not hospitals:
        print("No hospitals found.")
    else:
        print("Hospitals found:")
        for hospital in hospitals:
            print(f"{hospital.name} in {hospital.location}")

# Initialize the expert system
expert_system = ExpertSystem()

# Prompt the user for patient information
patient = get_patient_info()

# Get a list of hospitals that offer the required services
hospitals = expert_system.get_hospitals(patient.symptoms)

# Print the list of hospitals
print_hospitals(hospitals)
'''
Please enter patient information:
Name: fc
Age: 54
Gender: male
Symptoms: Cardiology
Hospitals found:
St. Mary's Hospital in New York
'''