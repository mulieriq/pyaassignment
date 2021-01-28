"""
Name: Peter Mark Kaiganaine
Reg No: F21/136578/2019
"""



def get_crater_tuple(line_str):
    return tuple(line_str.split('\t')[0:5])


def read_craters(filename):
    tuple = []
    file = open(filename, 'r')
    try:
        for line in file.readlines()[3:]:
            tuple.append(get_crater_tuple(line))
        file.close()
    except [FileExistsError, FileNotFoundError]:       
        _file = input('Please Enter File Name: ')
        read_craters(_file)
    finally:
        file.close()

    return tuple


def get_eligible_craters(crater_list):
    creators = []
    for (id, name, lat, lng, d) in crater_list:
        if -40 < float(lat) < 50 and 40 < float(lng) < 135 and float(d) >= 60:
            creators.append(tuple([id, name, lat, lng, d]))

    return creators


def write_craters(eligible_crater_list):
    file = open('crater.txt', 'a')
    try:
        file.write("reference\tnumber\tName\tlat\tlon\tdiameter\n#\tName\tLat\tLon\tD\n")
        for (id, name, lat, lng, d) in eligible_crater_list:
            file.write(id + "\t" + name + "\t" + lat + "\t" + lng + "\t" + d + "\n")
    except IOError:
        print('File IO error ', IOError.errno)
    finally:
        file.close()


if __name__ == '__main__':
    write_craters(get_eligible_craters(read_craters('rel3main.txt')))
