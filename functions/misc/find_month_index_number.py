# import pprint
# pp=pprint.PrettyPrinter(indent=2)
# import sys
import datetime

def find_month_index_number(month_number):
    # the purpose of this function is to give an index number to a month
    # number. The reason an index number is needed is for display purposes. If
    # month data ranges from May 2019 to November 2018, the months should be
    # displayed from top to bottom like this: may, april, march, february,
    # january, december, november. 

    # in the month_index_lookup, key is month number, value is its index (1 is the current month, 2 is the
    # last month, ect)
    month_index_lookup = {}    


    previous_year_lookup = {0: 12,
                        -1: 11,
                        -2: 10,
                        -3: 9,
                        -4: 8,
                        -5: 7,
                        -6: 6,
                        -7: 5, 
                        -8: 4, 
                        -9: 3,
                        -10: 2}


    current_month = int(datetime.datetime.now().strftime("%m"))

    counter = 1 
    while counter <= 12:
        if current_month > 0:
            month_index_lookup[current_month] = counter
            counter += 1
            current_month -= 1
        else:
            month_index_lookup[previous_year_lookup[current_month]] = counter
            counter += 1
            current_month -= 1

    return month_index_lookup[month_number]
   


# pp.pprint(find_month_index_number(5))


     
    
