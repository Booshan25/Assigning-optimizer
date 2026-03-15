import pandas as pd

from load_data import load_data
from sla_engine import calculate_deadline
from priority_queue import assign_priority
from routing_engine import assign_request


file = "project sample db.xlsx"

number_cases, break_flag, user_trained, request_queue = load_data(file)

users = number_cases.merge(break_flag, on="employee")

users = users[users["On Break"] == "N"]

request_queue["priority"] = request_queue["request type"].apply(assign_priority)

request_queue = request_queue.sort_values("priority")

assignments = []

for _, request in request_queue.iterrows():

    assigned_user = assign_request(request, users, user_trained)

    assignments.append({
        "request_id": request["Task"],
        "assigned_to": assigned_user
    })

result = pd.DataFrame(assignments)


print(result)