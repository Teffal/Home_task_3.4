import osa


def open_file(file_name_path=''):
    with open(file_name_path, encoding='utf8') as f:
        line = f.readline()
        returned_list = []
        while line:
            returned_list.append(line.strip().split(' '))
            line = f.readline()
    return returned_list


# Task 1
def convert_temperature(file):
    url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    our_client = osa.client.Client(url)
    list_temp = open_file('Homework\\' + file)
    sum_temp = 0
    for i in list_temp:
        response_temp = our_client.service.ConvertTemp(Temperature=i[0], FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
        sum_temp = sum_temp + response_temp
    print('{:.2f}'.format(sum_temp/list_temp.__len__()))


# Task 2
def convert_currency(file):
    url = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    our_client = osa.client.Client(url)
    list_currency = open_file('Homework\\' + file)
    for i in list_currency:
        response_currency = our_client.service.ConvertToNum(toCurrency='RUB', fromCurrency=i[2], amount=i[1], rounding=True)
        print('{} {:.0f} RUB'.format(i[0], float(response_currency)))


# Task 3
def convert_length(file):
    url = 'http://www.webservicex.net/length.asmx?WSDL'
    our_client = osa.client.Client(url)
    list_length = open_file('Homework\\' + file)
    for i in list_length:
        length = float(i[1].replace(',', ''))
        response_length = our_client.service.ChangeLengthUnit(LengthValue=length, fromLengthUnit='Miles', toLengthUnit='Kilometers')
        print('{} {:,.2f} km'.format(i[0], float(response_length)))


def main():
    file = input('Please, enter file\'s name: ')
    if file.lower() == 'temps.txt':
        convert_temperature(file)
    elif file.lower() == 'currencies.txt':
        convert_currency(file)
    elif file.lower() == 'travel.txt':
        convert_length(file)
    else:
        print('File name does not exist.')

if __name__ == "__main__":
    main()
