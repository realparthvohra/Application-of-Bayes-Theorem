# Here I will show how conditional probability works using Python.
# P(A|B) = P(A and B) / P(B)


# Simulated data: (is_cloudy, is_rainy)
data = [
    (True, True),
    (True, False),
    (False, False),
    (True, True),
    (False, False),
    (True, True),
    (False, True),
    (True, False),
]

def calculate_conditinal_probability(data, event_a , event_b):
    intersection_count = 0
    event_b_count = 0

    for outcome in data:
        if outcome[event_b]:
            event_b_count += 1
            if outcome[event_a]:
                intersection_count += 1
    
    if event_b_count == 0:
        return 0
    
    return intersection_count / event_b_count

probability_of_rain_given_cloudy = calculate_conditinal_probability(data, 1, 0)
print(f"P(Rain | Cloudy) = {probability_of_rain_given_cloudy:.2f}")
probability_of_cloudy_given_rain = calculate_conditinal_probability(data, 0, 1)
print(f"P(Cloudy | Rain) = {probability_of_cloudy_given_rain:.2f}")
# In this example, we have a dataset of weather conditions represented as tuples.