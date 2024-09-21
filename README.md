# Cartographic Telegram Bot
##This project is a Telegram bot that interacts with users, allowing them to display cities on a map and manage their personal list of cities.

## Key Features
- Map Display: The bot can display selected cities on a map using Cartopy and Matplotlib.
- City Saving: Users can save cities of interest to their personal list.
- Viewing Saved Cities: The bot provides a list of all cities saved by the user.
  
## Technologies
- Python 3: Programming language.
- SQLite: Database for storing user and city information.
- Matplotlib and Cartopy: Libraries for creating graphical data representations.
- Telebot: Library for creating and managing Telegram bots.
  
## Clone the repository:
```Bash
git clone <url_to_repository>
cd <repository_name>
```

## Install dependencies:
```Bash
pip install -r requirements.txt
```

## Set up environment variables:
Open the config.py file in the root directory of the project and specify the required variables:

```Bash
TOKEN=<your_telegram_bot_token>
```

## Run the bot:
```Bash
python bot.py
Используйте код с осторожностью.
```

## Usage
- /start - start working with the bot and get a welcome message.
- /help - get a list of available commands.
- /show_city <city_name> - display the specified city on the map.
- /remember_city <city_name> - save the city to the favorites list.
- /show_my_cities - show all saved cities.
- Note: Ensure that you replace <url_to_repository> with the actual URL of your GitHub repository and <your_telegram_bot_token> with the token you obtain from the BotFather.

## Additional Considerations:

- Error Handling: Consider adding error handling for cases like invalid city names, API rate limits, or database issues.
- User Interface: Explore ways to improve the user interface, perhaps using inline keyboards or custom keyboards.
- Map Customization: Allow users to customize the map, such as choosing different map styles or projections.
- Data Sources: Consider using different data sources for city information, such as OpenStreetMap or Geocoding APIs.

