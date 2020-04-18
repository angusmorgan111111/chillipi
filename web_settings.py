from flask import request

import util, database


def change_name(output_number):
    
   output_name = request.form['output_name']

   database.change_name(output_number, output_name)


    

