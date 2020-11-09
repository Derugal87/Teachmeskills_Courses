import argparse
import datetime
import time

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('-hour', '--hours', required=True)
parser.add_argument('-minute', '--minutes', required=True)
parser.add_argument('-second', '--seconds', required=True)

args = parser.parse_args()

fn = args.first_name
ln = args.last_name
hour = int(args.hours)
minute = int(args.minutes)
second = int(args.seconds)

time_now = str(datetime.datetime.now())


def timer(first_name, last_name, hours, minutes, seconds):
    with open('file.txt', 'a') as file:
        file.write(f'{first_name} {last_name} {datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        file.write('\n')
    seconds += hours * 3600 + minutes * 60
    for second in range(seconds, 0, -1):
        yield second
        time.sleep(1)
        if second == 1:
            print('ALARM')


if __name__ == '__main__':
    my_timer = timer(fn, ln, hour, minute, second)
    for sec in my_timer:
        print(f'{sec // (60 * 60)}:{(sec - ((sec // (60 * 60)) * 60 * 60)) // 60}:'
              f'{(sec - ((sec // (60 * 60)) * 60 * 60)) % 60}')
