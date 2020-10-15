def main():
    while (choose := input('Enter the appropriate variant of converting:\n'
                           '1. Convert inch to cm\n'
                           '2. Convert cm to inch\n'
                           '3. Convert mile to km\n'
                           '4. Convert km to mile\n'
                           '5. Convert lb to kg\n'
                           '6. Convert kg to lb\n'
                           '7. Convert oz to g\n'
                           '8. Convert g to oz\n'
                           '9. Convert gal(USA) to litre\n'
                           '10. Convert litre to gal(USA)\n'
                           '11. Convert pt(USA) to litre\n'
                           '12. Convert litre to pt(USA)\n'
                           '0. EXIT\n')) != '0':

        number = input('Enter number:\n')
        if number.isdigit():
            number = int(number)
        elif number.replace('.', '').isdigit():
            number = float(number)

        if choose == '1':
            print(f'Convert {number} inch to cm: {round((lambda x: x / 0.39370)(number), 2)}\n')
        elif choose == '2':
            print(f'Convert {number} cm to inch: {round((lambda x: x * 0.39370)(number), 2)}\n')
        elif choose == '3':
            print(f'Convert {number} mile to km: {round((lambda x: x / 0.62137)(number), 2)}\n')
        elif choose == '4':
            print(f'Convert {number} km to mile: {round((lambda x: x * 0.62137)(number), 2)}\n')
        elif choose == '5':
            print(f'Convert {number} lb to kg: {round((lambda x: x / 2.2046)(number), 2)}\n')
        elif choose == '6':
            print(f'Convert {number} kg to lb: {round((lambda x: x * 2.2046)(number), 2)}\n')
        elif choose == '7':
            print(f'Convert {number} oz to g: {round((lambda x: x / 0.035274)(number), 2)}\n')
        elif choose == '8':
            print(f'Convert {number} g to oz: {round((lambda x: x * 0.035274)(number), 2)}\n')
        elif choose == '9':
            print(f'Convert {number} gal(USA) to litre: {round((lambda x: x / 0.26417)(number), 2)}\n')
        elif choose == '10':
            print(f'Convert {number} litre to gal(USA): {round((lambda x: x * 0.26417)(number), 2)}\n')
        elif choose == '11':
            print(f'Convert {number} pt(USA) to litre: {round((lambda x: x / 2.1134)(number), 2)}\n')
        elif choose == '12':
            print(f'Convert {number} litre to pt(USA): {round((lambda x: x * 2.1134)(number), 2)}\n')


if __name__ == '__main__':
    main()
