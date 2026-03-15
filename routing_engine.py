import pandas as pd

def assign_request(request, users, training):

    category = request["category"]

    # Step 1: Find users trained for this category
    trained_users = training[
        (training["category"] == category) &
        (training["readiness"] == "Y")
    ]

    # Step 2: Merge with available users
    eligible = users.merge(trained_users, on="employee")

    if eligible.empty:
        return None

    # Step 3: Select user with lowest workload
    assigned_user = eligible.sort_values("no of cases").iloc[0]["employee"]

    return assigned_user