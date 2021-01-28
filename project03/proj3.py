"""
Name: Gesora Ian Maranga
Reg No: F21/2253/2019

"""


def get_crater_tuple(line_str):
    return tuple(line_str.split('\t')[0:5])


def read_craters(filename):
    tuple = []
    fh = open(filename, 'r')
    try:
        for line in fh.readlines()[3:]:
            tuple.append(get_crater_tuple(line))
        fh.close()
    except [FileExistsError, FileNotFoundError]:
        print('File Not Found!\n')
        _file = input('Please Enter File Name: ')
        read_craters(_file)
    finally:
        fh.close()

    return tuple


def get_eligible_craters(crater_list):
    eligible_craters = []
    for (_id, name, lat, lng, d) in crater_list:
        if -40 < float(lat) < 50 and 40 < float(lng) < 135 and float(d) >= 60:
            eligible_craters.append(tuple([_id, name, lat, lng, d]))

    return eligible_craters


def write_craters(eligible_crater_list):
    fh = open('crater.txt', 'a')
    try:
        fh.write("reference\tnumber\tName\tlat\tlon\tdiameter\n#\tName\tLat\tLon\tD\n")
        for (_id, name, lat, lng, d) in eligible_crater_list:
            fh.write(_id + "\t" + name + "\t" + lat + "\t" + lng + "\t" + d + "\n")
    except IOError:
        print('File IO error ', IOError.errno)
    finally:
        fh.close()


if __name__ == '__main__':
    write_craters(get_eligible_craters(read_craters('rel3main.txt')))
