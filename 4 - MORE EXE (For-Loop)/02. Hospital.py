period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
for day in range(1, period + 1):
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    count_patients_per_day = int(input())
    if count_patients_per_day <= doctors:
        treated_patients += count_patients_per_day
    else:
        untreated_patients += abs(count_patients_per_day - doctors)
        treated_patients += doctors
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
