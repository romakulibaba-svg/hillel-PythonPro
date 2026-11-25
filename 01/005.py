from decimal import Decimal


raw = input("Введіть суму: ").replace(",", ".").strip()

cents = int(Decimal(raw) * 100)

banknotes_counts = 0
coins_counts = 0
breakdown = []

banknotes = [
    (50000, "500"),
    (20000, "200"),
    (10000, "100"),
    (5000, "50"),
    (2000, "20"),
    (1000, "10"),
    (500, "5"),
]

coins = [
    (200, "2"),
    (100, "1"),
    (50, "0.5"),
    (20, "0.2"),
    (10, "0.1"),
    (5, "0.05"),
    (2, "0.02"),
    (1, "0.01"),
]

for value_cents, label in banknotes:
    count = cents // value_cents
    if count > 0:
        banknotes_counts += count
        breakdown.append(f"{count} x {label}")
        cents %= value_cents

for value_cents, label in coins:
    count = cents // value_cents
    if count > 0:
        coins_counts += count
        breakdown.append(f"{count} x {label}")
        cents %= value_cents

print(f"Кількість банкнот: {banknotes_counts}")
print(f"Кількість монет: {coins_counts}")
print("Склад суми:")
for item in breakdown:
    print(item)