import json


class Patients:
    def __init__(self):
        with open("Patients.json") as json_file:
            self.patients = json.load(json_file)

    def search(self, typeOfSearch, specialization):
        for patient_info in self.patients["Patients"]:
            if patient_info[typeOfSearch] == specialization:
                print(patient_info)

    def take_appointment(self, date, doctor_id, patient_id):
        for patient_info in self.patients["Patients"]:
            if patient_info["Id"] == patient_id:
                patient_info["Appointments"].append((date, doctor_id))
                return True
        return False

    def save(self):
        with open("Patients.json", "w") as json_file:
            json.dump(self.patients, json_file, indent=4)
