def assign_priority(request_type):

    if request_type == "Rush":
        return 1
    elif request_type == "same day":
        return 2
    else:
        return 3
