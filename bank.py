def bank():
    balance = 0
    history = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            balance += int(input('введите сумму на сколько пополнить счет'))
        elif choice == '2':
            price = int(input('введите сумму покупки'))
            if balance < price:
                print('денег не хватает')
            else:
                goods = input('введите название покупки')
                balance -= price
                history.append((goods, price))
        elif choice == '3':
            print(history)
        elif choice == '4':
            return
        else:
            print('Неверный пункт меню')