



from instabot import Bot


# Initialize the bot
bot = Bot()
bot.login(username="your_username", password="your_password")


# Upload a photo and add a caption
photo_path = "path_to_your_photo.jpg"
caption = "Check out this amazing photo! #PythonAutomation"
bot.upload_photo(photo_path, caption=caption)