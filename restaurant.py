print("<---મિત્રો માં તમારું હાર્દિક સ્વાગત છે.--->")

all_items = []  # To store all ordered items
order_total = 0  

while True:
    print("\n1. Chinese")
    print("2. Punjabi")
    print("3. Gujarati")
    print("4. Italian")
    print("5. Coffee")
    print("6. Cold drinks")
    print("7. Final Bill (Exit)")

    ch1 = int(input("Enter your choice according to what you want to eat (1 to 7): "))

    if ch1 == 1:
        chinees = {
            'Dry Manchurian': 120,
            'Half Dry Manchurian': 70,
            'Manchau Soup': 50,
            'Chinese Bhel': 100,
            'Chinese Noodles': 105,
            'Fried Fries': 110
        }
        print("<<---Chinese Menu--->>")
        print("\nDry Manchurian: 120Rs\nHalf Dry Manchurian: 70Rs\nManchau Soup: 50Rs\nChinese Bhel: 100Rs\nChinese Noodles: 105Rs\nFried Fries: 110Rs")  
        item1 = input("Enter the name of the item you want to order: ")
        if item1 in chinees:
            quantity = int(input("Enter quantity: "))
            all_items.append(f"{item1} x{quantity} - {chinees[item1]*quantity}Rs")
            order_total += chinees[item1] * quantity
            print(f"Your item {item1} (x{quantity}) has been added to your order")
        else:
            print(f"Order item {item1} is not available yet")

    elif ch1 == 2:
        punjabi = {
            "Sabji": {
                "Kaju Masala": 250,
                "Kaju Butter Masala": 280,
                "Veg Tufani": 275,
                "Veg Kolhapuri": 250,
                "Kaju Kofta": 300
            },
            "Paneer": {
                'Veg Paneer': 210,
                'Butter Paneer': 220,
                'Chiz Paneer': 240,
                'Matka Paneer': 250,
                'Kofta Paneer': 260
            },
            "Roti": {
                'Naan': 50,
                'Butter Roti': 35,
                'Regular Roti': 20
            },
            'Mitro Special Sabji': 320
        }
        print("<<----Punjabi Menu---->>")
        ch2 = input("\n--Please choose according to your menu requirement--\n S--> Kaju Veg Sabji\nP--> Paneer Sabji\nR--> Roti\nM--> Mitro Special Sabji: ")
        
        if ch2 == 'S':
            print("\n****Kaju Veg Sabji****")
            print("\nKaju Masala = 250Rs..\nVeg Kolhapuri = 250Rs..\nVeg Tufani = 275Rs..\nKaju Butter Masala = 280Rs..\nKaju Kofta = 300Rs..")
            item3 = input("Enter the name of the item you want to order: ")
            if item3 in punjabi["Sabji"]:
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item3} x{quantity} - {punjabi['Sabji'][item3]*quantity}Rs")
                order_total += punjabi["Sabji"][item3] * quantity
                print(f"Your item {item3} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item3} is not available yet")
        
        elif ch2 == 'P':
            print("\n****Paneer Sabji****")
            print("\nVeg Paneer = 210Rs..\nButter Paneer = 220Rs..\nChiz Paneer = 240Rs..\nMatka Paneer = 250Rs..\nKofta Paneer = 260Rs..")
            item4 = input("Enter the name of the item you want to order: ")
            if item4 in punjabi["Paneer"]:
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item4} x{quantity} - {punjabi['Paneer'][item4]*quantity}Rs")
                order_total += punjabi["Paneer"][item4] * quantity
                print(f"Your item {item4} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item4} is not available yet")
        
        elif ch2 == 'R':
            print("\n****Roti****")
            print("\nNaan = 50Rs..\nButter Roti = 35Rs..\nRegular Roti = 20Rs..")
            item5 = input("Enter the name of the item you want to order: ")
            if item5 in punjabi["Roti"]:
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item5} x{quantity} - {punjabi['Roti'][item5]*quantity}Rs")
                order_total += punjabi["Roti"][item5] * quantity
                print(f"Your item {item5} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item5} is not available yet")
        
        elif ch2 == 'M':
            print("\n****Mitro Special Sabji****")
            print("\nMitro Special Sabji = 320Rs..")
            item6 = input("Enter the name of the item you want to order: ")
            if item6 == 'Mitro Special Sabji':
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item6} x{quantity} - {punjabi[item6]*quantity}Rs")
                order_total += punjabi[item6] * quantity
                print(f"Your item {item6} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item6} is not available yet")

    elif ch1 == 3:
        gujarati = {
            'Sabji': {
                'Dhokla': 60,
                'Khandvi': 80,
                'Patra': 90,
                'Undhiyu': 150
            },
            'Rice': {
                'Plain Rice': 80,
                'Jeera Rice': 100,
                'Biryani': 150
            },
            'Roti': {
                'Thepla': 40,
                'Phulka': 30
            },
            'Mitro Special Gujarati Thali': 250
        }
        print("<<----Gujarati Menu---->>")
        ch3 = input("\n--Please choose according to your menu requirement--\n S--> Gujarati Sabji\nR--> Rice\nT--> Roti\nM--> Mitro Special Gujarati Thali: ")
        
        if ch3 == 'S':
            print("\n****Gujarati Sabji****")
            print("\nDhokla = 60Rs..\nKhandvi = 80Rs..\nPatra = 90Rs..\nUndhiyu = 150Rs..")
            item7 = input("Enter the name of the item you want to order: ")
            if item7 in gujarati['Sabji']:
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item7} x{quantity} - {gujarati['Sabji'][item7]*quantity}Rs")
                order_total += gujarati['Sabji'][item7] * quantity
                print(f"Your item {item7} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item7} is not available yet")
        
        elif ch3 == 'R':
            print("\n****Rice Menu****")
            print("\nPlain Rice = 80Rs..\nJeera Rice = 100Rs..\nBiryani = 150Rs..")
            item8 = input("Enter the name of the item you want to order: ")
            if item8 in gujarati['Rice']:
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item8} x{quantity} - {gujarati['Rice'][item8]*quantity}Rs")
                order_total += gujarati['Rice'][item8] * quantity
                print(f"Your item {item8} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item8} is not available yet")
        
        elif ch3 == 'T':
            print("\n****Roti Menu****")
            print("\nThepla = 40Rs..\nPhulka = 30Rs..")
            item9 = input("Enter the name of the item you want to order: ")
            if item9 in gujarati['Roti']:
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item9} x{quantity} - {gujarati['Roti'][item9]*quantity}Rs")
                order_total += gujarati['Roti'][item9] * quantity
                print(f"Your item {item9} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item9} is not available yet")
        
        elif ch3 == 'M':
            print("\n****Mitro Special Gujarati Thali****")
            print("\nMitro Special Gujarati Thali = 250Rs..")
            item10 = input("Enter the name of the item you want to order: ")
            if item10 == 'Mitro Special Gujarati Thali':
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item10} x{quantity} - {gujarati[item10]*quantity}Rs")
                order_total += gujarati[item10] * quantity
                print(f"Your item {item10} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item10} is not available yet")

    elif ch1 == 4:
        italian = {
            'Pizza': {
                'Margherita': 250,
                'Pepperoni': 280,
                'Veggie Supreme': 300,
                'Cheese Burst': 350
            },
            'Pasta': {
                'Spaghetti Aglio Olio': 200,
                'Penne Arrabbiata': 220,
                'Mac and Cheese': 240
            }
        }
        print("<<----Italian Menu---->>")
        ch4 = input("\n--Please choose according to your menu requirement--\n P--> Pizza\nA--> Pasta: ")
        
        if ch4 == 'P':
            print("\n****Pizza Menu****")
            print("\nMargherita = 250Rs..\nPepperoni = 280Rs..\nVeggie Supreme = 300Rs..\nCheese Burst = 350Rs..")
            item11 = input("Enter the name of the item you want to order: ")
            if item11 in italian['Pizza']:
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item11} x{quantity} - {italian['Pizza'][item11]*quantity}Rs")
                order_total += italian['Pizza'][item11] * quantity
                print(f"Your item {item11} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item11} is not available yet")
        
        elif ch4 == 'A':
            print("\n****Pasta Menu****")
            print("\nSpaghetti Aglio Olio = 200Rs..\nPenne Arrabbiata = 220Rs..\nMac and Cheese = 240Rs..")
            item12 = input("Enter the name of the item you want to order: ")
            if item12 in italian['Pasta']:
                quantity = int(input("Enter quantity: "))
                all_items.append(f"{item12} x{quantity} - {italian['Pasta'][item12]*quantity}Rs")
                order_total += italian['Pasta'][item12] * quantity
                print(f"Your item {item12} (x{quantity}) has been added to your order")
            else:
                print(f"Order item {item12} is not available yet")

    elif ch1 == 5:
        coffee = {
            'Espresso': 80,
            'Cappuccino': 120,
            'Latte': 130,
            'Mocha': 140
        }
        print("<<----Coffee Menu---->>")
        print("\nEspresso = 80Rs..\nCappuccino = 120Rs..\nLatte = 130Rs..\nMocha = 140Rs..")
        item13 = input("Enter the name of the item you want to order: ")
        if item13 in coffee:
            quantity = int(input("Enter quantity: "))
            all_items.append(f"{item13} x{quantity} - {coffee[item13]*quantity}Rs")
            order_total += coffee[item13] * quantity
            print(f"Your item {item13} (x{quantity}) has been added to your order")
        else:
            print(f"Order item {item13} is not available yet")

    elif ch1 == 6:
        cold_drinks = {
            'Coke': 50,
            'Pepsi': 50,
            'Sprite': 50,
            'Fanta': 50
        }
        print("<<----Cold Drinks Menu---->>")
        print("\nCoke = 50Rs..\nPepsi = 50Rs..\nSprite = 50Rs..\nFanta = 50Rs..")
        item14 = input("Enter the name of the item you want to order: ")
        if item14 in cold_drinks:
            quantity = int(input("Enter quantity: "))
            all_items.append(f"{item14} x{quantity} - {cold_drinks[item14]*quantity}Rs")
            order_total += cold_drinks[item14] * quantity
            print(f"Your item {item14} (x{quantity}) has been added to your order")
        else:
            print(f"Order item {item14} is not available yet")
    
    elif ch1 == 7:
        print("\n<<---Final Bill--->>")
        for item in all_items:
            print(item)
        print(f"Total Bill: {order_total}Rs")
        print("************************************************")
        print("Bill Payment Successful...")
        print("<<------Thank you for visiting Mitro Restaurant!------>>")
        print ("<<--***પુનઃ પધારજો***-->>")
        break
