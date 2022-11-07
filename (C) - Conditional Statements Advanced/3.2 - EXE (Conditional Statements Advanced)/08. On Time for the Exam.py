hour_of_the_exam = int(input())
minutes_of_the_exam = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
time_of_the_exam_in_minutes = (hour_of_the_exam * 60) + minutes_of_the_exam
arrival_time_in_minutes = (arrival_hour * 60) + arrival_minutes
if arrival_time_in_minutes > time_of_the_exam_in_minutes:
    print("Late")
    diff_in_minutes = abs(arrival_time_in_minutes - time_of_the_exam_in_minutes)
    hour = diff_in_minutes // 60
    minutes = diff_in_minutes % 60
    if hour != 0:
        if minutes < 10:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")
    else:
        print(f"{minutes} minutes after the start")
elif (arrival_time_in_minutes + 30) < time_of_the_exam_in_minutes:
    print("Early")
    diff_in_minutes = abs(arrival_time_in_minutes - time_of_the_exam_in_minutes)
    hour = diff_in_minutes // 60
    minutes = diff_in_minutes % 60
    if hour != 0:
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")
    else:
        print(f"{minutes} minutes before the start")
elif arrival_time_in_minutes == time_of_the_exam_in_minutes:
    print("On time")
else:
    print("On time")
    diff_in_minutes = abs(arrival_time_in_minutes - time_of_the_exam_in_minutes)
    hour = diff_in_minutes // 60
    minutes = diff_in_minutes % 60
    if hour != 0:
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")
    else:
        print(f"{minutes} minutes before the start")
