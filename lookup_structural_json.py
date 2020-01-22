import sys
import json
          
check_keys = ['profile', 'time_start', 'max_speed', 'score_new',
              'duration2force', 'session_id', 'file_powerRange',
              'distance_km', 'duration', 'elapsed_ts', 'score']

with open(sys.argv[1], 'r') as d:
    session_data_dict = json.load(d)
#print(len(workout_data_dict.keys()))
session_data_new_dict = session_data_dict.copy()#possible lookup
session_count_dict = {"user": "session count"}
count_workout = 0 
for key in session_data_new_dict:
    count_session = 0 #reset count
#check userid digit for uniform 8-digit userid
#    if len(key) != 8: 
    for value in session_data_new_dict[key]:
        count_session = count_session + 1
#check keys for each workout data
        if value.keys() != check_keys:
            print(value.keys())
    session_count_dict[key] = count_session
with open('writeFile1.txt', 'w') as c:
    json.dump(session_count_dict, c)
