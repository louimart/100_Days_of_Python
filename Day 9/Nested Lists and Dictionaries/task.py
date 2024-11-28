# Practice accessing elements in nested Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

# Practice accessing elements in nested list
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

# Practice accessing elements in dictionaries nested within a dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

travel_log["Japan"] = {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5}

print(travel_log["Germany"]["cities_visited"][2])
print(travel_log)