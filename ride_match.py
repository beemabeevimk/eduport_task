from math import radians, sin, cos, sqrt, atan2

def haversine_distance(coord1, coord2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radius of the Earth in kilometers (approximate)
    earth_radius_km = 6371.0

    # Calculate the distance
    distance_km = earth_radius_km * c

    return distance_km

def match_rides_with_drivers(users, ride_requests, max_distance_km=5):
    matched_pairs = []

    for request in ride_requests:
        request_location = (request['latitude'], request['longitude'])

        # Find the closest available user (driver)
        closest_user = None
        min_distance = float('inf')

        for user in users:
            user_location = (user['latitude'], user['longitude'])
            distance = haversine_distance(request_location, user_location)

            if distance < min_distance and distance <= max_distance_km:
                min_distance = distance
                closest_user = user

        if closest_user:
            # Match the ride request with the closest user (driver)
            matched_pairs.append({'request_id': request['id'], 'user': closest_user})

            # Remove the matched user (driver) from the list
            users.remove(closest_user)

    return matched_pairs

# Example usage:
users_and_ride_requests = [
    {'id': 'A', 'latitude': 37.7750, 'longitude': -122.4150},
    {'id': 'B', 'latitude': 37.7760, 'longitude': -122.4200},
    # Add more users as needed
]

ride_requests = [
    {'id': 1, 'latitude': 37.7749, 'longitude': -122.4194},
    {'id': 2, 'latitude': 37.7745, 'longitude': -122.4184},
    # Add more ride requests as needed
]

matched_pairs = match_rides_with_drivers(users_and_ride_requests, ride_requests)

# print("Matched pairs:", matched_pairs)



list1 = [i for i in range(10)]
print(list1)



        