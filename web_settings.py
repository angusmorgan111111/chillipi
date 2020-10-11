from flask import request

import util, database


def change_name(output_number):
    
   output_name = request.form['output_name']

   database.change_name(output_number, output_name)


def add_command(day, output_number):
    
   time = request.form['time']
   command = request.form['command']

   time_on = '-'
   time_off = '-'

   if command =='periodic':
      time_on = request.form['time_on']
      time_off = request.form['time_off']
      
      try:                 #these 2 trys are to check time input was a number
         int(time_on)
      except ValueError:
         time_on = ''
         
      try:
         int(time_off)
      except ValueError:
         time_off = ''

      #util.log(time_on)    
         
   if not len(time)==0:
      if not len(time_on)==0: 
         if not len(time_off)==0:          
            database.add_command(output_number, day, time, command, time_on, time_off)

   

def clear_commands(day, output_number):
    
   if 'clear_all' in request.form: 
      util.log('clear')
      database.clear_commands(output_number, day)
     
