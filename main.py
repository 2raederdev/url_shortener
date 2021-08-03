import pyshorteners
import inquirer
import pyperclip

from constants import BITLY_API_KEY

question = [
  inquirer.List('type',
                message="To continue please select the shortener method you would like to use",
                choices=['Bitly', 'Tinyurl'],
            )
]

shortener_type = inquirer.prompt(question)['type']
print(f'Great! You have selected {shortener_type}')

url = input("Now, please enter your url: ")

if shortener_type == 'Bitly':
    s = pyshorteners.Shortener(api_key=BITLY_API_KEY)
    new_url = s.bitly.short(url)
else:
    new_url = pyshorteners.Shortener().tinyurl.short(url)

print(f'Your url: {new_url}')

pyperclip.copy(new_url)
