import urllib.request, json

# Opening a web request
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=ultra&apiKey=25e1cb1220bfe92ec9d9")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
currency = data['ILS_USD']

print("Welcome to currency converter")
while True:
    try:
        amount = float(input("Please enter an amount of Shekeles to convert:"))
        break
    except ValueError as e:
        print(f"you got {e.__class__.__name__}, please enter a number")

print(amount * currency)
print("Thanks for using our currency converter")

