def quiz():
    import random
    birthdays = {'Aimi': '25.12.1991', 'Otsuka Sae': '10.10.1995', 'Nishimoto Rimi': '25.10.1994',
                 'Ohashi Ayaka': '13.09.1994', 'Itou Ayasa': '17.08.1996', 'Aiba Aina': '17.10.1988',
                 'Kudou Haruka': '16.03.1989', 'Nakashima Yuki': '12.09.1997',
                 'Sakuragawa Megu': '24.10.1988', 'Akesaka Satomi': '02.01.1988'}
    numeral = [''] + 'один два три четыре пять шесть семь восемь девять десять'.split(' ')
    ordinal = [''] + 'первое второе третье четвёртое пятое шестое седьмое восьмое девятое десятое'.split(' ')
    ordinal += [numeral[n - 10][:-1] + (['н', 'е', 'и'][n - 11] if n < 14 else '') + 'надцатое' for n in range(11, 20)]
    ordinal += [numeral[n // 10] + 'дцать ' + ordinal[n % 10] if n % 10 else numeral[n // 10] + 'дцатое' for n in
                range(20, 32)]
    months = [''] + 'января февраля марта апреля мая июня июля августа сентября октября ноября декабря'.split(' ')
    length = len(birthdays) // 2
    bandori_birthdays = random.sample(birthdays.keys(), length)
    while True:
        errors = 0
        for girl in bandori_birthdays:
            date = input('input birthday of ' + str(girl))
            if date != birthdays[girl]:
                errors += 1
                day, month, year = birthdays[girl].split('.')
                print('неверно', ordinal[int(day)], months[int(month)], year, 'года')
        print(errors, 'wrong answers', length - errors, 'true answers', round(errors / length * 100),
              '% of wrong answers', round((length - errors) / length * 100), '% of true answers')
        again = input('wanna play again?')
        if again == 'no':
            return