import sys

def prim_delivery_network(graph, locations):
    num_locations = len(graph)
    selected_location = [False] * num_locations
    delivery_routes = []
    total_cost = 0

    selected_location[0] = True

    for _ in range(num_locations - 1):
        min_cost = sys.maxsize
        x, y = 0, 0

        for i in range(num_locations):
            if selected_location[i]:
                for j in range(num_locations):
                    if not selected_location[j] and graph[i][j]:  
                        if min_cost > graph[i][j]:
                            min_cost = graph[i][j]
                            x, y = i, j

        delivery_routes.append((locations[x], locations[y], graph[x][y]))
        total_cost += graph[x][y]
        selected_location[y] = True

    return delivery_routes, total_cost


num_locations = int(input("Enter the total number of locations (including supply center): "))
locations = []

for i in range(num_locations):
    location_name = input(f"Enter the name of location {i + 1}: ")
    locations.append(location_name)


graph = [[0] * num_locations for _ in range(num_locations)]


print("\nEnter the delivery cost between each pair of locations (enter 0 if there's no direct route):")
for i in range(num_locations):
    for j in range(i + 1, num_locations):  
        cost = int(input(f"Cost from {locations[i]} to {locations[j]}: "))
        graph[i][j] = cost
        graph[j][i] = cost  


delivery_routes, total_cost = prim_delivery_network(graph, locations)

print("\nDelivery Routes in the Minimum Cost Network:")
for route in delivery_routes:
    print(f"Route from {route[0]} to {route[1]} with cost {route[2]}")
print(f"Total cost of delivery network: {total_cost}")
