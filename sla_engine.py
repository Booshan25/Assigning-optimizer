from datetime import timedelta

def calculate_deadline(request_time, request_type):

    if request_type == "Rush":
        return request_time + timedelta(hours=1)

    elif request_type == "same day":
        return request_time.replace(hour=17, minute=0, second=0)

    else:
        return request_time + timedelta(hours=48)