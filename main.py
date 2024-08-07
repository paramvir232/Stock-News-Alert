import requests
from twilio.rest import Client
import datetime
from os import environ

STOCK = 'RELIANCE.BSE'
COMPANY_NAME = "Reliance Industries Ltd"
TODAY_DATE = datetime.date.today()

account_sid = environ.get('account_sid')
auth_token = environ.get('auth_token')
api_key = environ.get('api_key')
client = Client(account_sid, auth_token)

to_phone = environ.get('to_phone')
from_phone = environ.get('from_phone')
## Using Stock API
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday .

stock_api = 'ZFOARZH3BP2G5KE7'
stock_paramerters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': stock_api
}

stock_response = requests.get(url='https://www.alphavantage.co/query', params=stock_paramerters)
stock_data = stock_response.json()
closing_price = stock_data['Time Series (Daily)']
previous_days = [key for key in closing_price.items()][:2]
closings_values = [float(item[1]['4. close']) for item in previous_days]

# 0 -> today || 1 -> Yesterday 

is_up_down = False
emoji = ''
highest_price = max(closings_values)
change_in_price = closings_values[0] - closings_values[1]
percentage_up_down = round((change_in_price / highest_price) * 100, 2)

if percentage_up_down >= 1:
    emoji = '▲🟢'
    is_up_down = True
elif percentage_up_down <= -1:
    emoji = '▼🔴'
    is_up_down = True

## Using https://newsapi.org
# Getting news from news API for the given stock.

news_api = '13bd100d08c34537892c4923f2885630'
news_parameters = {
    'q': COMPANY_NAME,
    'apiKey': news_api
}
news_response = requests.get(url='https://newsapi.org/v2/everything', params=news_parameters)
news_data = news_response.json()['articles']

## Using Messeage API to send message with the percentage change and each article's title and description to your phone number.
if is_up_down:
    for item_index in range(1):
        news_title = news_data[item_index]['title']
        news_desciption = news_data[item_index]['description']
        message = client.messages.create(
            from_=from_phone,
            body=f'{STOCK} : {emoji} {percentage_up_down}%\n\nHeadline : {news_title}\n\nBreif : {news_desciption}',
            to=to_phone
        )
