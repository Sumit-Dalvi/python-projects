# whatToWear.py

rainy = input("how's is the weather today? Is It raining (y/n)? ") . lower()
cold = input("is it cold today? (y/n)? ") . lower()
if (rainy == 'y' and cold == 'y'):
    print("u better wear a raincoat.")
elif (rainy == 'y' and cold != 'y'):
    print("carry an umbrella with you")
elif (rainy != 'y' and cold == 'y'):
    print("put on jacket, it's cold outside")
elif (rainy != 'y' and cold !='y'):
    print("wear whatever you want, it's beautiful outside")
