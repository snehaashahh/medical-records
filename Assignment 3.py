from typing import List, Dict, Optional

def readPatientsFromFile(fileName):
        # Read the contents of the file into a list
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """

    patients = {}
    fileName = "patients.txt"
    try:
        with open("patients.txt") as file:
            for line_num, line in enumerate(file, start=1):
                try:
                    fields = line.strip().split(',')
                    if len(fields) != 8:
                        print(f"Invalid number of fields ({len(fields)}) in line: {line}")
                        continue
                    patient_id = int(fields[0])
                    date = fields[1]
                    temperature = float(fields[2])
                    if not (35 <= temperature <= 42):
                        print(f"Invalid temperature value ({temperature}) in line: {line}")
                        continue
                    heart_rate = int(fields[3])
                    if not (30 <= heart_rate <= 180):
                        print(f"Invalid heart rate value ({heart_rate}) in line: {line}")
                        continue
                    respiratory_rate = int(fields[4])
                    if not (5 <= respiratory_rate <= 40):
                        print(f"Invalid respiratory rate value ({respiratory_rate}) in line: {line}")
                        continue
                    systolic_blood_pressure = int(fields[5])
                    if not (70 <= systolic_blood_pressure <= 200):
                        print(f"Invalid systolic blood pressure value ({systolic_blood_pressure}) in line: {line}")
                        continue
                    diastolic_blood_pressure = int(fields[6])
                    if not (40 <= diastolic_blood_pressure <= 120):
                        print(f"Invalid diastolic blood pressure value ({diastolic_blood_pressure}) in line: {line}")
                        continue
                    oxygen_saturation = int(fields[7])
                    if not (70 <= oxygen_saturation <= 100):
                        print(f"Invalid oxygen saturation value ({oxygen_saturation}) in line: {line}")
                        continue
                    if patient_id not in patients:
                        patients[patient_id] = []
                    patients[patient_id].append([date, temperature, heart_rate, respiratory_rate, systolic_blood_pressure, diastolic_blood_pressure, oxygen_saturation])
                except ValueError:
                    print(f"Invalid data type in line: {line}")
                    continue
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
    except:
        print("An unexpected error occurred while reading the file.")

    return(patients)


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    if not isinstance(patients, dict):
            print("Error: patients must be a dictionary.")
            return
    if patientId != 0 and (not isinstance(patientId, int) or patientId < 0):
            print("Error: patientId must be a non-negative integer or 0.")
            return
    found_patient = False
    for patient_id, visits in patients.items():
        if patientId == 0 or patient_id == patientId:
            found_patient = True
            print(f"Patient ID: {patient_id}")
            for visit in visits:
                print(" ", end="")
                print("Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % visit[1], "C")
                print("  Heart Rate:", visit[2], "bpm")
                print("  Respiratory Rate:", visit[3], "bpm")
                print("  Systolic Blood Pressure:", visit[4], "mmHg")
                print("  Diastolic Blood Pressure:", visit[5], "mmHg")
                print("  Oxygen Saturation:", visit[6], "%")
    if not found_patient and patientId != 0:
        print(f"Patient with ID {patientId} not found.")  


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    
    # Check if patients parameter is a dictionary
    if not isinstance(patients, dict):
        print("Error: 'patients' should be a dictionary.")
        return
       
    # Check if patientId is an integer
    if patientId.isdigit() == False:
        print("Error: 'patientId' should be an integer.")
        return
    temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = os_sum = num_visits = 0
    # Check if patientId is specified
    if int(patientId) == 0:
        print("Vital Signs for All Patients:")
    # calculate averages for all patients
        
        for patient in patients:
            for visit in patients[patient]:
                temp_sum += float(visit[1])
                hr_sum += int(visit[2])
                rr_sum += int(visit[3])
                sbp_sum += int(visit[4])
                dbp_sum += int(visit[5])
                os_sum += int(visit[6])
                num_visits += 1
        if num_visits == 0:
            print("No data found for any patient.")
        else:    
            print("Average temperature: %.2f Â°C" % (temp_sum / num_visits))
            print("Average heart rate: %.2f bpm" % (hr_sum / num_visits))
            print("Average respiratory rate: %.2f bpm" % (rr_sum / num_visits))
            print("Average systolic blood pressure: %.2f mmHg" % (sbp_sum / num_visits))
            print("Average diastolic blood pressure: %.2f mmHg" % (dbp_sum / num_visits))
            print("Average oxygen saturation: %.2f %%" % (os_sum / num_visits))
    elif int(patientId) in patients:
        # calculate averages for specified patient
        
        for visit in patients[int(patientId)]:
            temp_sum += float(visit[1])
            hr_sum += int(visit[2])
            rr_sum += int(visit[3])
            sbp_sum += int(visit[4])
            dbp_sum += int(visit[5])
            os_sum += int(visit[6])
            num_visits += 1
        
        else:
            print(f"Vital Signs for Patient {patientId}:")
            print("Average temperature: %.2f Â°C" % (temp_sum / num_visits))
            print("Average heart rate: %.2f bpm" % (hr_sum / num_visits))
            print("Average respiratory rate: %.2f bpm" % (rr_sum / num_visits))
            print("Average systolic blood pressure: %.2f mmHg" % (sbp_sum / num_visits))
            print("Average diastolic blood pressure: %.2f mmHg" % (dbp_sum / num_visits))
            print("Average oxygen saturation: %.2f %%" % (os_sum / num_visits))
    else:
        if num_visits == 0:
            print(f"No data found for patient with ID {patientId}.")
    



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """

    try:
        from datetime import datetime

        # Validate date format
        datetime.strptime(date, '%Y-%m-%d')

        # Validate date existence
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date. Please enter a valid date.")
            return

        # Validate temperature
        if not (35.0 <= temp <= 42.0):
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
            return

        # Validate heart rate
        if not (30 <= hr <= 180):
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
            return

        # Validate respiratory rate
        if not (5 <= rr <= 40):
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
            return

        # Validate systolic blood pressure
        if not (70 <= sbp <= 200):
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
            return

        # Validate diastolic blood pressure
        if not (40 <= dbp <= 120):
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
            return

        # Validate oxygen saturation level
        if not (70 <= spo2 <= 100):
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
            return

        # Add new data to patient dictionary
        if patientId not in patients:
            patients[patientId] = []
        patients[patientId].append({
            "date": date,
            "temp": temp,
            "hr": hr,
            "rr": rr,
            "sbp": sbp,
            "dbp": dbp,
            "spo2": spo2
        })

        # Add new data to text file
        with open(fileName, 'a') as file:
            file.write(f"{patientId}, {date}, {temp}, {hr}, {rr}, {sbp}, {dbp}, {spo2}\n")

        # Display success message
        print(f"Visit saved for Patient # {patientId}")
    except ValueError:
        print("Invalid date. Please enter date a valid date.")
    except Exception:
        print("An unexpected error occurred while adding new data.")




def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    
    
 
    if year is not None and (not isinstance(year, int) or year <= 0):
        return []  # invalid year value
    
    if month is not None and (not isinstance(month, int) or month < 1 or month > 12):
        return []  # invalid month value
    
    visits = []
    
    for patient_id, patient_visits in patients.items():
        for visit in patient_visits:
            if not all(visit[:6]):  # check if date information is complete and valid
                continue
            
            visit_year, visit_month, visit_day = map(int, visit[0].split('-'))
            if (year is None or year == visit_year) and (month is None or month == visit_month):
                visit_info = [visit[0], *visit[1:]]
                visits.append((patient_id, visit_info))
    
    if not visits:
        return []  # no visits found
    
    return visits    
    


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    
    for patient_id, visits in patients.items():
        for visit in visits:
            # Check if any of the vital signs are abnormal
            if (visit[2] > 100 or visit[2] < 60 or 
                visit[4] > 140 or visit[5] > 90 or 
                visit[6] < 90):
                # Add patient ID to follow-up list
                followup_patients.append(int(patient_id))
                # No need to check more visits for this patient
                break
    
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, fileName):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    
    # Read in the current data from the file
    with open(fileName, 'r') as f:
        data = f.readlines()

    # Remove all visits for the specified patientId from the patients dictionary
    if patientId in patients:
        patients[patientId] = []

    # Create a new list of lines that does not include any rows for the specified patientId
    new_data = []
    for line in data:
        if not line.startswith(str(patientId)):
            new_data.append(line)

    # Overwrite the file with the new data
    with open(fileName, 'w') as f:
        f.writelines(new_data)

    # Print output message if data for the patient has been deleted
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}.")
    else:
        print(f"Data for patient {patientId} has been deleted.")
    




###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()