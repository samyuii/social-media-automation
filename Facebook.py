


import facebook


# Set up the Graph API client
access_token = "your_access_token"
graph = facebook.GraphAPI(access_token)


# Post a message
message = "Automating posts with Python! #SocialMediaAutomation"
graph.put_object("me", "feed", message=message)