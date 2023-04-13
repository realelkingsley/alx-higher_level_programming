# Import required libraries
import random

# Create a dictionary of users with their information
users = {
    "user1": {
        "name": "John Smith",
        "address": "123 Main St",
        "items": ["milk", "bread", "eggs"]
    },
    "user2": {
        "name": "Jane Doe",
        "address": "456 Elm St",
        "items": ["apples", "oranges", "bananas"]
    }
}

# Create a list of helpers with their information
helpers = [
    {
        "name": "Samantha",
        "fee": 10,
        "max_distance": 5,
        "availability": ["Mon", "Wed", "Fri"]
    },
    {
        "name": "Tom",
        "fee": 5,
        "max_distance": 10,
        "availability": ["Tue", "Thu", "Sat"]
    }
]

# Define a function to match a user with a helper
def match_helper(user):
    # Create an empty list to store potential helpers
    potential_helpers = []
    
    # Loop through the list of helpers
    for helper in helpers:
        # Check if the helper is available on the day the user needs help
        if user["day"] in helper["availability"]:
            # Calculate the distance between the user and the helper
            distance = random.randint(1, 20)
            
            # Check if the helper is within the maximum distance from the user
            if distance <= helper["max_distance"]:
                # Add the helper to the list of potential helpers
                potential_helpers.append((helper, distance))
    
    # Check if any potential helpers were found
    if len(potential_helpers) > 0:
        # Sort the potential helpers by distance
        potential_helpers.sort(key=lambda x: x[1])
        
        # Return the helper with the lowest distance
        return potential_helpers[0][0]
    else:
        # Return None if no helpers were found
        return None

# Define a function to match all users with helpers
def match_all_users():
    # Loop through the users
    for user_id, user_info in users.items():
        # Call the match_helper function for each user
        helper = match_helper(user_info)
        
        # Print the match result
        if helper is not None:
            print(f"{user_info['name']} is matched with {helper['name']} (fee: {helper['fee']}, distance: {random.randint(1, 20)} miles)")
        else:
            print(f"No match found for {user_info['name']}")

# Call the match_all_users function to match all users with helpers
match_all_users()

