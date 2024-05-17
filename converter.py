import converters

usage_count = 0


def get_choice():
    choice_map = {
        1: {
            'main': 'Celsius',
            'to': 'Fahrenheit',
            'converter': converters.celsius_to_fahrenheit_converter
        },
        2: {
            'main': 'Fahrenheit',
            'to': 'Celsius',
            'converter': converters.fahrenheit_to_celsius_converter
        },
        3: {
            'main': 'Celsius',
            'to': 'Kelvin',
            'converter': converters.celsius_to_kelvin_converter
        },
        4: {
            'main': 'Fahrenheit',
            'to': 'Kelvin',
            'converter': converters.fahrenheit_to_kelvin_converter
        }
    }

    while True:
        try:
            choice = int(input('Enter your choice:'))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    if choice not in choice_map.keys():
        print('Invalid choice. Please enter a valid choice.')
        return get_choice()
    return choice_map[choice]


def convert_temperature(choice):
    while True:
        try:
            temperature = float(input('Enter the temperature in {}:'.format(choice['main'])))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    result = choice['converter'](temperature)
    print('The temperature in {} is:'.format(choice['to']), result)


def convert():
    global usage_count
    if usage_count == 0:
        print('***This is a small temperature conversion program***')

    print('Enter 1 for Celsius to Fahrenheit conversion')
    print('Enter 2 for Fahrenheit to Celsius conversion')
    print('Enter 3 for Celsius to Kelvin conversion')
    print('Enter 4 for Fahrenheit to Kelvin conversion')

    usage_count = usage_count + 1

    choice = get_choice()
    convert_temperature(choice)

    response = input('Would you like to make another conversion? Y/n')

    if response.lower() == 'y':
        convert()
        usage_count = usage_count + 1
    else:
        print('Goodbye!')
        exit()


if __name__ == "__main__":
    convert()
