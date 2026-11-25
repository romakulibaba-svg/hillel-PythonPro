signal = input("введіть колір(red, green, yellow): ").lower().strip()
if signal == "red":
    print("зупинитися")
elif signal == "green":
    print("рух дозволено за умови безпеки")
elif signal == "yellow":
    print("очікувати або підготуватися відповідно до навчальної моделі")  
    
else:
    print("невідомий сигнал ")