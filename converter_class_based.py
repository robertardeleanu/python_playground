import converters


class TemperatureConverter:
    def __init__(self):
        self.usage_count = 0

    def get_choice(self):
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
            return self.get_choice()
        return choice_map[choice]

    def convert_temperature(self, choice):
        while True:
            try:
                temperature = float(input(f'Enter the temperature in {choice["main"]}:'))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        result = choice['converter'](temperature)
        print(f'The temperature in {choice["to"]} is:', result)

    def do(self):
        if self.usage_count == 0:
            print('***This is a small temperature conversion program***')

        print('Enter 1 for Celsius to Fahrenheit conversion')
        print('Enter 2 for Fahrenheit to Celsius conversion')
        print('Enter 3 for Celsius to Kelvin conversion')
        print('Enter 4 for Fahrenheit to Kelvin conversion')

        self.usage_count = self.usage_count + 1

        choice = self.get_choice()
        self.convert_temperature(choice)

        response = input('Would you like to make another conversion? Y/n')

        if response.lower() == 'y':
            self.do()
            self.usage_count = self.usage_count + 1
        else:
            print('Goodbye!')
            exit()


def main():
    converter = TemperatureConverter()
    converter.do()


if __name__ == "__main__":
    main()
