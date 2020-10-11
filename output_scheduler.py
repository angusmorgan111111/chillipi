import datetime
import pinset
import util
import database



def apply_outputs(schedule, pin):   
    time = datetime.datetime.now()
    current_day = time.weekday()
    current_time = time.strftime('%H:%M:%S')  

    s = ''

    
     

    if len(schedule) == 0:
        pinset.pin_off(pin)
        util.log(str(pin)+' off')     
    else:

        for i in range(len(schedule)):

            
            if current_day < schedule[i]['day'] or (current_day == schedule[i]['day'] and current_time < schedule[i]['time']):
                
                        
                if i == 0:
                    row = schedule[len(schedule) - 1]
                    
                else:
                    row = schedule[i - 1]

                if row['command'] == 'on':
                    pinset.pin_on(pin)
                    util.log(str(pin) + ' on')
                
                if row['command'] == 'off':
                    pinset.pin_off(pin)
                    util.log(str(pin)+' off')
                
                
                return


            
