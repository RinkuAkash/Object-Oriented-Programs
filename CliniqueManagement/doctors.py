import json


class Doctors:
    def __init__(self):
        with open("Doctors.json") as json_file:
            self.doctors = json.load(json_file)

    def search(self, typeOfSearch, specialization):
        for doctor_info in self.doctors["Doctors"]:
            if doctor_info[typeOfSearch] == specialization:
                print(doctor_info)

    def set_appointment(self, date, doctor_id, patient_id):

        for doctor_info in self.doctors["Doctors"]:
            if doctor_info["Id"] == doctor_id:
                if date in doctor_info["Appointments"]:
                    if doctor_info["Appointments"][date] < 5:
                        doctor_info["Appointments"][date] += 1
                        doctor_info["Appointments"]["total"] += 1
                        return True
                    else:
                        return False
                else:
                    doctor_info["Appointments"][date] = 1
                    doctor_info["Appointments"]["total"] += 1
                    return True

        return False

    def report(self, doctor_name):

        for doctor_info in self.doctors["Doctors"]:
            if doctor_info["Name"] == doctor_name:
                print("Name :", doctor_info["Name"])
                print("Id :", doctor_info["Id"])
                print("Specialization :", doctor_info["Specialization"])
                print("Availability :", doctor_info["Availability"])
                print("Appointments :")
                print(doctor_info["Appointments"])
                return

        print("Not found")

    def popular_doctor(self):
        maximum = 0
        for doctor_info in self.doctors["Doctors"]:
            if doctor_info["Appointments"]["total"] > maximum:
                name = doctor_info["Name"]
                maximum = doctor_info["Appointments"]["total"]

        if maximum != 0:
            print("Popular doctor :", name)

    def popular_specialization(self):
        physician = cardiologist = neurologist = 0

        for doctor_info in self.doctors["Doctors"]:
            if doctor_info["Specialization"] is "Neurologist":
                neurologist += doctor_info["Appointments"]["total"]
            elif doctor_info["Specialization"] is "Cardiologist":
                cardiologist += doctor_info["Appointments"]["total"]
            elif doctor_info["Specialization"] is "Physician":
                physician += doctor_info["Appointments"]["total"]

        if physician == max(physician, cardiologist, neurologist):
            print("Physician")
        elif cardiologist == max(neurologist, physician, cardiologist):
            print("Neurologist")
        else:
            print("Cardiologist")

    def save(self):
        with open("Doctors.json", "w") as json_file:
            json.dump(self.doctors, json_file, indent=4)
