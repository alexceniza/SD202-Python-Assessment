# Task 1: Detective 
# Works out which murder scenario is most likely
# Score for each scenario = room value + tool value, then sorted in descending order


# Value of each room
rooms = {"Ball": 0.5, "Dining": 0.9, "Kitchen": 0.1, "Master bedroom": 0.3, "Bathroom": 0.3}

# Value of each tool 
tools = {"Dagger":0.4, "Revolver": 0.7, "Lead pipe": 0.1, "Hammer": 0.8}

# One dictionary for each scenario
# I only store names here, not numbers, so the values are not hard coded
# The numbers are looked up from the dictionaries above

scenarios = [
    {"suspect": "John", "room": "Bathroom", "tool": "Lead pipe"}, 
    {"suspect": "Cathy", "room": "Dining", "tool": "Revolver"}, 
    {"suspect": "Cathy", "room": "Ball", "tool": "Dagger"}, 
    {"suspect": "Samuel", "room": "Master bedroom", "tool": "Revolver"}, 
    {"suspect": "John", "room": "Kitchen", "tool": "Dagger"},
    {"suspect": "Cathy", "room": "Master bedroom", "tool": "Hammer"}
]


# This function is used by sorted() to know which value to sort on 
def get_score(scenario): 
    return scenario["value"]


# Work out the total for every scenario and store it in its dictionary
for scenario in scenarios: 
    scenario["value"] = round(rooms[scenario["room"]] + tools[scenario["tool"]], 2)


# Sort from biggest total to smallest. reverse=True gives descending order
sorted_scenarios = sorted(scenarios, key=get_score, reverse=True)


# Display the results 
print("Prioritized scenarios (most likely first):")
print()


rank = 1 
for scenario in sorted_scenarios: 
    suspect = scenario["suspect"]
    room = scenario["room"]
    tool = scenario["tool"]
    value = scenario["value"]

    print(f"{rank}. {suspect}, {room}, {tool} = {value}")
    rank = rank + 1 

print()
print("The most likely scenario is:", sorted_scenarios[0]["suspect"],
        "in the", sorted_scenarios[0]["room"],
        "with the", sorted_scenarios[0]["tool"])