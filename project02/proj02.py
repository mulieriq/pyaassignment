
if __name__ == '__main__':
    def get_data_list(FILE_NAME):
        f = open(FILE_NAME, "r")
        print(f.read().split(" "))


    get_data_list('table.csv')
