signal = input("введіть колір(red, green, yellow): ").lower().strip()

match signal:
    case "red":
        print("зупинитися")
    case "green":
        print("рух дозволено за умови безпеки")
    case "yellow":
        print("очікувати або підготуватися відповідно до навчальної моделі")
    case _:
        print("невідомий сигнал")