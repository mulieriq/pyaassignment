"""
Name: Peter Mark Kaiganaine
Reg No: F21/136578/2019
"""


def get_data_list(FILE_NAME):
    # dataList to hold extracted data
    dataList = []
    file = open(FILE_NAME, 'r')
    for line in file.readlines()[1:]:
        dataList.append(list(line.replace('\n', '').split(',')))
    file.close()
    return dataList


def get_monthly_averages(data_list):
    months = list(range(1, 13))
    monthAverages = []
    volumes = 0

    for month in months:
        for line in data_list:
            if (int(line[0].split('-')[1]) == month):
                volumeClosesTotal += (float(line[5]) * float(line[4]))
                volumes += float(line[5])
                monthAverages.append(
                    tuple([(volumeClosesTotal / volumes), line[0].split('-')[1] + "-" + line[0].split('-')[0]]))
            else:
                volumeClosesTotal = 0
                volumes = 0
    return monthAverages


def print_info(monthly_average_list):
    monthly_average_list.sort()
    print('6 worst months:')
    for (stock, year) in monthly_average_list[0:6]:
        print(year, ',', stock)

    print('\n6 best months:')
    monthly_average_list.reverse()
    for (stock, year) in monthly_average_list[0:6]:
        print(year, ',', stock)
