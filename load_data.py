import pandas as pd

def load_data(file):

    number_cases = pd.read_excel(file, sheet_name="number_cases")
    break_flag = pd.read_excel(file, sheet_name="break Flag")
    user_trained = pd.read_excel(file, sheet_name="user_trained")
    request_queue = pd.read_excel(file, sheet_name="request_time")

    return number_cases, break_flag, user_trained, request_queue