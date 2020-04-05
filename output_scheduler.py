import datetime
import pinset

def apply_outputs(schedule, pin):   
    time = datetime.datetime.now()
    current_day = time.weekday()
    current_time = time.strftime('%H:%M:%S')  

    s = ''

    command_list = schedule.fetchall()

    for i in range(len(command_list)):
        if current_day < command_list[i]['day'] or (current_day == command_list[i]['day'] and current_time < command_list[i]['time']):

            if i == 0:
                row = command_list[len(command_list) - 1]
            else:
                row = command_list[i - 1]

            if row['command'] == 'on':
                pinset.pin_on(pin)

            if row['command'] == 'off':
                pinset.pin_off(pin)

            for element in row:
                s += str(element)

            return str(s)