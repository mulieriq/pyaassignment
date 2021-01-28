"""
Name: Kanyari Peter Muriithi
Reg No: F21/2242/2019
Project04
Version: First Attempt
Date: 15/01/2021
"""

import math


def read_body(file_name, bmi_age=False):
    data = []
    try:
        fh = open(file_name, 'r')
        for line in fh.readlines():
            if bmi_age:
                data.append(tuple(line.replace('  ', ' ').split(' ')[21:24]))
            else:
                # 2, 3, 4, 19, 20
                _data = line.replace('  ', ' ').split(' ')
                data.append(tuple([_data[2], _data[3], _data[4], _data[19], _data[20], _data[22], _data[23]]))

    except FileExistsError:
        print(FileExistsError)
    return data


def linear_reg_bmi_age(data):
    _x = []
    _y = []
    for (age, weight, height) in data:
        _x.append(float(age))
        _y.append(round(calc_bmi(float(weight), float(height)), 2))
    return [_x, _y]


def linear_reg_cpa_age(data):
    _x = []
    _y = []
    for (brio_diameter, chest_depth, chest_diameter, ankle_girth, wrist_girth, weight, height) in data:
        _x.append(float(weight))
        _y.append(round(calc_cpa(float(brio_diameter), float(chest_depth), float(chest_diameter), float(ankle_girth),
                                 float(wrist_girth), float(height)), 2))
    return [_x, _y]


def calc_bmi(weight, height):
    return weight / pow((height / 100), 2)


def calc_cpa(brio_diameter, chest_depth, chest_diameter, ankle_girth, wrist_girth, height):
    return -110 + (1.34 * (chest_diameter / 100) + 1.54 * (chest_depth / 100) + 1.20 * (brio_diameter / 100) + 1.11 * (
                wrist_girth / 100) + 1.15 * (ankle_girth / 100) + 0.177 * (height / 100))


def calc_intercept(sum_y, sum_x, slope, _n):
    return (sum_y - (slope * sum_x)) / _n


def calc_slope(sum_x, sum_y, sum_x_squared, sum_xy, _n):
    return (_n * sum_xy - (sum_x * sum_y)) / (_n * sum_x_squared - pow(sum_x, 2))


def calc_correlation(_n, sum_xy, sum_x, sum_y, sum_xsq, sum_ysq):
    return (_n * sum_xy - (sum_x * sum_y)) / math.sqrt((_n * sum_xsq) * pow(sum_x, 2) * (_n * sum_ysq) - pow(sum_y, 2))


if __name__ == '__main__':
    x = 0
    y = 1


    def prod(a):
        xy = []
        for i in range(len(a[x])):
            xy.append(a[x][i] * a[y][i])
        return xy


    def pow_2(i):
        return pow(i, 2)


    _data_bmi_age = linear_reg_bmi_age(read_body('body.dat', True))
    _sum_xsq_bmi_age = sum(list(map(pow_2, _data_bmi_age[x])))
    _sum_ysq_bmi_age = sum(list(map(pow_2, _data_bmi_age[y])))
    _sum_xy_bmi_age = round(sum(prod(_data_bmi_age)), 2)
    _sum_x_bmi_age = sum(_data_bmi_age[x])
    _sum_y_bmi_age = sum(_data_bmi_age[y])
    _n_bmi_age = len(_data_bmi_age[x])
    _slope_bmi_age = round(calc_slope(_sum_x_bmi_age, _sum_y_bmi_age, _sum_xsq_bmi_age, _sum_xy_bmi_age, _n_bmi_age), 2)
    _intercept_bmi_age = round(calc_intercept(_sum_y_bmi_age, _sum_x_bmi_age, _slope_bmi_age, _n_bmi_age), 2)
    _correlation_bmi_age = round(
        calc_correlation(_n_bmi_age, _sum_xy_bmi_age, _sum_x_bmi_age, _sum_y_bmi_age, _sum_xsq_bmi_age,
                         _sum_ysq_bmi_age), 2)

    _data_cpa_wt = linear_reg_cpa_age(read_body('body.dat'))
    _sum_xsq_cpa_wt = sum(list(map(pow_2, _data_cpa_wt[x])))
    _sum_ysq_cpa_wt = sum(list(map(pow_2, _data_cpa_wt[y])))
    _sum_xy_cpa_wt = round(sum(prod(_data_cpa_wt)), 2)
    _sum_x_cpa_wt = sum(_data_cpa_wt[x])
    _sum_y_cpa_wt = sum(_data_cpa_wt[y])
    _n_cpa_wt = len(_data_cpa_wt[x])
    _slope_cpa_wt = round(calc_slope(_sum_x_cpa_wt, _sum_y_cpa_wt, _sum_xsq_cpa_wt, _sum_xy_cpa_wt, _n_cpa_wt), 2)
    _intercept_cpa_wt = round(calc_intercept(_sum_y_cpa_wt, _sum_x_cpa_wt, _slope_cpa_wt, _n_cpa_wt), 2)
    _correlation_cpa_wt = round(
        calc_correlation(_n_cpa_wt, _sum_xy_cpa_wt, _sum_x_cpa_wt, _sum_y_cpa_wt, _sum_xsq_cpa_wt, _sum_ysq_cpa_wt), 2)

    print('x = Weight, y = CPA')
    print('slope\tintercept\tcorrelation')
    print(_slope_cpa_wt, '\t', _intercept_cpa_wt, '\t\t', _correlation_cpa_wt, '\n')

    print('\nx = Age, y = BMI')
    print('slope\tintercept\tcorrelation')
    print(_slope_bmi_age, '\t', _intercept_bmi_age, '\t\t\t', _correlation_bmi_age, '\n')
