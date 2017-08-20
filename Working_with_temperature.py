import osa


def get_temperature_list():
    with open('temps.txt', encoding='utf-8-sig') as file:
        temperature_list = []
        for l in file:
            tempstr = l.strip()
            if 'F' in tempstr:
                temperature = tempstr.split()[0]
                temperature_list.append(temperature)
    return temperature_list


def add(a, b):
    client = osa.Client('http://www.dneonline.com/calculator.asmx?WSDL')
    return client.service.Add(
        intA=a,
        intB=b
    )


def get_sum_temperature():
    temperature_list = get_temperature_list()
    temperature_a = 0
    for temperature_b in temperature_list:
        add(temperature_a, temperature_b)
        temperature_a = (add(temperature_a, temperature_b))
    return temperature_a


def divide(a, b):
    client = osa.Client('http://www.dneonline.com/calculator.asmx?WSDL')
    return client.service.Divide(
        intA=a,
        intB=b
    )


def get_average_temperature():
    sum_temperature = get_sum_temperature()
    number_of_values = len(get_temperature_list())
    divide(sum_temperature, number_of_values)
    average_temperature = divide(sum_temperature, number_of_values)
    return average_temperature


def temperature_unit_convertor(temper, from_u, tu_u):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(
        Temperature=temper,
        FromUnit=from_u,
        ToUnit=tu_u
    )


def temperature_degree_celsius():
    average_temperature = get_average_temperature()
    from_unit = 'degreeFahrenheit'
    to_unit = 'degreeCelsius'
    num_round = 2
    temperature_celsius = round(temperature_unit_convertor(average_temperature, from_unit, to_unit), num_round)
    return temperature_celsius


def get_result():
    result_temperature = temperature_degree_celsius()
    print("Средняя за неделю арифметическая температура по Цельсию: {} градуса.".format(result_temperature))


get_result()
