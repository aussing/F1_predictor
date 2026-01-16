import fastf1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

year=2025 ## There's heaps of data available, just starting with last year

session_list = ['Session1','Session2','Session3','Session4','Session5'] 
## FastF1 session naming scheme
## Normal Weekend: Practice 1, Practice 2, Practice 3, Qualifying, Race
## Sprint Weekend: Practice 1, Spring Qualifying, Sprint, Qualifying, Race

def create_season_folder_structure(schedule):
    """
    This function just checks that folders for each round exist, and if not creates them
    It doesn't neet to run everytime but easier than handwriting every folder
    
    schedule: The data object with all the event information for the year
    """

    if not os.path.exists(f'./{year}'):
        os.makedirs(f'./{year}')
    
    total_rounds = len(schedule)
    round_names = schedule['EventName']
    list_of_round_names = []

    for current_round_number in range(total_rounds):
        ## Might get rid of testing - check later
        # if current_round_number == 0:
        #     continue
        
        current_round_name = f"{current_round_number}" + "_" + f"{round_names[current_round_number].replace(' ', '_')}"

        if not os.path.exists(f'./{year}/{current_round_name}'):
            os.makedirs(f'./{year}/{current_round_name}')

        list_of_round_names.append(f'{current_round_name}')

    return list_of_round_names

def create_round_folder_structure(list_of_round_names):
    """
    Same thing as above but checks every round and creates the folders for each session
    
    :param list_of_round_names: Description
    """

    for round_number, round_name in enumerate(list_of_round_names):
        for session_number, session_name in enumerate(session_list):
            if not os.path.exists(f'./{year}/{round_name}/{session_name}'):
                os.makedirs(f'./{year}/{round_name}/{session_name}')



if __name__ == "__main__":
    schedule = fastf1.get_event_schedule(year)
    list_of_round_names = create_season_folder_structure(schedule)
    create_round_folder_structure(list_of_round_names)
    
