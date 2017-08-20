import osa


def get_travel_list():
    with open('travel.txt', encoding='utf-8-sig') as file:
        travel_list = []
        for l in file:
            tempstr = l.strip()
            if 'mi' in tempstr:
                travel_dist = tempstr.split()[1]
                travel_distance = travel_dist.replace(",", "")
                travel_list.append(travel_distance)
    return travel_list


def add(a, b):
    # client = osa.Client('http://www.dneonline.com/calculator.asmx?WSDL')
    # return client.service.Add(
    #     intA=a,
    #     intB=b
    # )
    return a + b


def distance_unit_convertor(dist_value, from_len_unit, tu_len_unit):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    return client.service.ChangeLengthUnit(
        LengthValue=dist_value,
        fromLengthUnit=from_len_unit,
        toLengthUnit=tu_len_unit
    )


def distance_unit_kilometers(distance):
    from_len_unit = 'Miles'
    tu_len_unit = 'Kilometers'
    distance_kilometers = distance_unit_convertor(distance, from_len_unit, tu_len_unit)
    num_round = 2
    distance_kilometers = round(distance_kilometers, num_round)
    return distance_kilometers


def get_sum_dist():
    travel_list = get_travel_list()
    dist_a = 0
    for distance in travel_list:
        dist_b = distance_unit_kilometers(distance)
        add(dist_a, dist_b)
        dist_a = (add(dist_a, dist_b))
        # print(dist_a)
    return dist_a


def get_result():
    distance_kilometers = get_sum_dist()
    print("Суммарное расстояние пути в километрах: {}.".format(distance_kilometers))


get_result()
