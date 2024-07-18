# Task 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
our_unique_destinations = our_routes.difference(competitor_routes)
# assuming "destinations neither airline shares" means the union of unique destinations
union_unique_destinations = our_routes.symmetric_difference(competitor_routes)

print(common_destinations)
print(our_unique_destinations)
print(union_unique_destinations)