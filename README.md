# Task Assigning System

This project implements a rule-based task assignment that automatically assigns incoming operational requests to employees based on multiple decision criteria.
The system evaluates:
- Current workload (number of active cases per employee)
- Employee availability (break status)
- Training eligibility for the request category
- Request priority based on SLA requirements

Requests are assigned to the most suitable employee with the lowest workload among those eligible to handle the task.
The project demonstrates how Python and pandas can be used to design operational decision systems commonly used in banking and operations teams.
