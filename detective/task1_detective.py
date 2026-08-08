# Task 1: Detective 
# This program works out which murder scenario is most likely
# The score for each scenario = value of the room + value of the tool
# The scenarios are then sorted from highest score to lowest score


# Dictionary that hols the value of each room 
room_values = {
    "Ball": 0.5, 
    "Dining": 0.9,
    "Kitchen": 0.1, 
    "Master bedroom": 0.3, 
    "Bathroom": 0.3
}

# Dictionary that hold the value of each tool 
tool_values = {
    "Dagger": 0.4, 
    "Revolver": 0.7, 
    "Lead pipe": 0.1,
    "Hammer": 0.8
}

# List of dictionaries, one dictionary for each scenario
# I only store the names here, not numbers, so the values are not hard coded
# The numbers are looked up from the dictionaries above

scenarios = [
    {"suspect": "John", "room": "Bathroom", "tool": "Lead pipe"}, 
    {"suspect": "Cathy", "room": "Dining", "tool": "Revolver"}, 
    {"suspect": "Cathy", "room": "Ball", "tool": "Dagger"}, 
    {"suspect": "Samuel", "room": "Master bedroom", "tool": "Revolver"}, 
    {"suspect": "John", "room": "Kitchen", "tool": "Dagger"},
    {"suspect": "Cathy", "room": "Master bedroom", "tool": "Hammer"}
]


# This function adds the room value and the tool value together
def get_total(scenario): 
    room_name = scenario["room"]
    tool_name = scenario["tool"]

    room_score = room_values[room_name]
    tool_score = tool_values[tool_name]

    total = room_score + tool_score

    # round() is used because Python sometimes shows numbers like 0.4000000000000001 when adding decimals
    return round(total, 2)


# This function is used by sorted() to know which value to sore on 
def get_score(scenario): 
    return scenario["total"]


# Work out the total for every scenario and save it inside the dictionary 
for scenario in scenarios: 
    scenario["total"] = get_total(scenario)


# Sort the list from the biggest total to the smallest total 
# reverse=True means descending order 
sorted_scenarios = sorted(scenarios, key=get_score, reverse=True)


# Display the results 
print("Prioritized scenarios (most likely first):")
print()

rank = 1 
for scenario in sorted_scenarios: 
    suspect = scenario["suspect"]
    room = scenario["room"]
    tool = scenario["tool"]
    total = scenario["total"]

    print(f"{rank}. {suspect}, {room}, {tool} = {total}")
    rank = rank + 1 

print()
print("The most likely scenario is:", sorted_scenarios[0]["suspect"],
        "in the", sorted_scenarios[0]["room"],
        "with the", sorted_scenarios[0]["tool"])