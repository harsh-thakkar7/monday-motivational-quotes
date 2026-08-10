import datetime as dt
import random
now=dt.datetime.now()
weekday=now.weekday()

if weekday==0:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)

        print(quote)

else:
    today_is_not_monday=input(f"sorry today is not monday, but still you want the quote then insert yes or no on this line")
    if today_is_not_monday=="yes":
        with open("quotes.txt") as quote_file:
            all_quotes=quote_file.readlines()
            quote=random.choice(all_quotes)

        print(f"still its not monday here is your quote\n{quote}")