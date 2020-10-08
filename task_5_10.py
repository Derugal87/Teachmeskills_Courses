from datetime import datetime as dt, timedelta


def prepare_data():
    trains = []
    while True:
        should_continue = input('Enter more?')
        if should_continue == '-':
            break
        number = input('Enter train number: ')
        dep_point = input('Enter departure point: ')
        dep_time = input('Enter departure time (year,month,day,hour,minutes): ')
        arr_point = input('Enter arrival point: ')
        arr_time = input('Enter arrival time (year,month,day,hour,minutes): ')
        trains.append(
            {
                'number': number,
                'dep_point': dep_point,
                'dep_time': dep_time,
                'arr_point': arr_point,
                'arr_time': arr_time,
            }
        )
    train_operation(trains)


def train_operation(trains):
    for train in trains:
        dep_time = dt(*[int(i) for i in train['dep_time'].split(',')])
        arr_time = dt(*[int(i) for i in train['arr_time'].split(',')])
        diff = arr_time - dep_time
        if diff > time_delta:
            print(train)


if __name__ == '__main__':
    time_delta = timedelta(hours=7, minutes=20)
    prepare_data()
