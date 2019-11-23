def format_price(price):
    if not isinstance(price, (int, float)):
        print("Введите число")
    elif price*100 % 100 > 44:
        price = int(price)+1
    else: price = int(price)
    return "Цена: " +str(price)+ " руб."

price=56.24 
final_price = format_price(price)
print(final_price)

price=57.46
final_price = format_price(price)
print(final_price)

price="asd"
final_price = format_price(price)
print(final_price)