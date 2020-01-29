from Doctors import Doctors
from Patients import Patients

if __name__ == "__main__":

    print("Clinique Management")
    while True:
        print("Select your role")
        print("1. User\n2. Patient\n0. exit")
        role = int(input())

        doctor = Doctors()
        patient = Patients()
        # User role
        if role == 1:
            while True:
                print("Enter")
                print("1. Search for patient")
                print("2. Search for doctor")
                print("3. Print doctor report")
                print("4. Search for popular doctor")
                print("5. Search for popular specialization")
                print("0. exit")

                option = int(input())
                if option == 2:
                    typeOfSearch = input("Enter specific type to search : ")
                    specialization = input("Enter specialization : ")
                    doctor.search(typeOfSearch, specialization)
                elif option == 3:
                    name = input("Enter doctor name : ")
                    doctor.report(name)
                elif option == 1:
                    typeOfSearch = input("Enter specific type to search : ")
                    specialization = input("Enter specialization : ")
                    patient.search(typeOfSearch, specialization)
                elif option == 4:
                    doctor.popularDoctor()
                elif option == 5:
                    doctor.popularSpecialization()
                elif option == 0:
                    doctor.save()
                    patient.save()
                    break
                else:
                    print("invalid input")
        # patient role
        elif role == 2:

            while True:
                print("1 to search for doctor")
                print("2 to get appointment")
                print("0 to exit")
                option = int(input())

                if option == 1:
                    typeOfSearch = input("Enter specific type to search : ")
                    specialization = input("Enter specialization : ")
                    doctor.search(typeOfSearch, specialization)

                elif option == 2:
                    while True:
                        patient_id = input("Enter your id : ")
                        doctor_id = input("Enter doctor id : ")
                        date = input("enter date (dd/mm/yyyy) :")
                        if doctor.set_appointment(date, doctor_id, patient_id):
                            if patient.takeAppointment(
                                date, doctor_id, patient_id
                                  ):
                                print("Appoinment successful")
                            else:
                                print("Appointment unsuccessful")
                            break
                        else:
                            print("Sorry, doctor not available on that day")

                elif option == 0:
                    doctor.save()
                    patient.save()
                    break

                else:
                    print("invalid input")

        elif role == 0:
            doctor.save()
            patient.save()
            break

        else:
            print("Invalid input")
