import sys 

def log(s):
    print(s)
    sys.stdout.flush()

    
def log_iterable(iterable):
    
    for row in iterable:
        print('=======')

        for k, v in dict(zip(row.keys(),row)).items():
            print(k, v)
    
    sys.stdout.flush()







