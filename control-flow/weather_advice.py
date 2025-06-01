#Based on the user’s input, your program will recommend different types of clothing:
#If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
#If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
#If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
#Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.

weather_input = input("What's the weather like today? (sunny/rainy/cold): ")

if weather_input == 'sunny':
    print("Wear a t-shirt and sunglasses.")
elif weather_input == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather_input == 'cold':
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
