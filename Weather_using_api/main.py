import telebot
import pyowm

# create a Telegram bot object
bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN")

# create an OWM object
owm = pyowm.OWM("YOUR_OPENWEATHERMAP_API_KEY")


# define a handler function for the "/weather" command
@bot.message_handler(commands=['weather'])
def get_weather(message):
    # get the city name from the message text
    city = message.text.split()[1]

    # get the current weather for the city
    observation = owm.weather_at_place(city)
    w = observation.get_weather()

    # send the weather data to the user
    weather_data = f"Current weather in {city}: {w.get_detailed_status()}, temperature: {w.get_temperature('celsius')['temp']}°C"
    bot.send_message(message.chat.id, weather_data)


if __name__ == '__main__':
    bot.infinity_polling()
