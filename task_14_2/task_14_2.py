import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('-t', '--task', required=True)
parser.add_argument('-ft', '--focus_time', default=25, required=False)
parser.add_argument('-bt', '--break_time', default=5, required=False)
parser.add_argument('-c', '--cycle', default=4, required=False)

args = parser.parse_args()

fn = args.first_name
ln = args.last_name
t = args.task
ft = int(args.focus_time)
bt = int(args.break_time)
c = int(args.cycle)


def timer(first_name, last_name, task, focus_time, break_time, cycle):
    with open('file_2.txt', 'w') as file:
        file.write(f'"{task}" reported by {first_name} {last_name}')
        file.write('\n')
        for i in range(1, cycle + 1):
            print(f'Cycle {i}: {focus_time} minutes')
            file.write(f'Cycle: {i}: {focus_time} minutes')
            file.write('\n')
            for minute in range(focus_time, 0, -1):
                yield minute
                time.sleep(1)
                if minute == 1:
                    if i == cycle:
                        print('Happy End!')
                        break
                    elif not (i % 4):
                        print(f'Break time: {break_time * 3} minutes')
                        file.write(f'Break time: {break_time * 3} minutes')
                        file.write('\n')
                        time.sleep(break_time * 3)
                    else:
                        print(f'Break time: {break_time} minutes')
                        file.write(f'Break time: {break_time} minutes')
                        file.write('\n')
                        time.sleep(break_time)


if __name__ == '__main__':
    my_timer = timer(fn, ln, t, ft, bt, c)
    for i in my_timer:
        print(i)
