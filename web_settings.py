from flask import request

import util, database


def change_name(output_number):
    
   output_name = request.form['output_name']

   database.change_name(output_number, output_name)


def add_command(output_number):
    
    time = request.form['time']
    command = request.form['command']

    util.log(time + command)


    database.add_command(output_number, time, command)
   

