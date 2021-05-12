import datetime
import operator
import pinset
import util
import database


""" Appy the appropriate pin outputs for the current time

This function works out the correct state the pins should be in by iterating
through the list of commands. It finds the most recent command before the
current time, and because that indicates the current state the pins should be
in, applies the output from that command.
"""
def apply_outputs(schedule, pin):   
    time = datetime.datetime.now()
    current_day = time.weekday()
    current_time = time.strftime('%H:%M:%S')

    # Turn the pin off if no schedule is set
    if len(schedule) == 0:
        pinset.pin_off(pin)
        # util.log(str(pin)+' off')     
    else:

        # Sort the schedule into chronological order for the week
        schedule.sort(key=operator.itemgetter('time'))
        schedule.sort(key=operator.itemgetter('day'))

        # For each index i in the schedule list
        for i in range(len(schedule)):

            

            # Find the first command after the current time
            if current_day < schedule[i]['day'] or (current_day == schedule[i]['day'] and current_time < schedule[i]['time']):
               
                # Then apply the command before that i.e. the
                # most recent command before the current time
                if i == 0:
                    row = schedule[len(schedule) - 1]

                else:
                    row = schedule[i - 1]
                             
                apply_output(row, pin)
                return

        apply_output(schedule[len(schedule)-1], pin)


def apply_output(row, pin):

    if row['command'] == 'on':
        pinset.pin_on(pin)
        #util.log(str(pin) + ' on')

    if row['command'] == 'off':
        pinset.pin_off(pin)
        #util.log(str(pin)+' off')

