'''
Your task in order to complete this Kata is to write a function which formats a duration,
 given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. 
If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:
  format_duration(62)    # returns "1 minute and 2 seconds"
  format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. 
In general, a positive integer and one of the valid units of time, separated by a space. 
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). 
Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. 
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. 
So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. 
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". 
It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

For the purpose of this Kata, a year is 365 days and a day is 24 hours.
'''

def format_duration(seconds):
    if seconds == 0:
        return 'now'
        
    sec_year = 31536000
    sec_day = 86400
    sec_hour = 3600
    sec_minute = 60

    years, seconds = get_unit(seconds,sec_year)
    days, seconds = get_unit(seconds,sec_day)
    hours, seconds = get_unit(seconds,sec_hour)
    minutes, seconds = get_unit(seconds,sec_minute)

    duration = [years,days,hours,minutes,seconds]
    unit_str = ['year','day','hour','minute','second']
    time = []
    for i,val in enumerate(duration):
        if val > 0:
            unit = '{0} {1}'.format(val,unit_str[i])
            if val > 1:
                unit += 's'
            time.append(unit)

    last = time.pop()    
    return ', '.join(time) + ' and ' + last if time else last     

def get_unit(seconds, unit):
    res = 0
    if seconds >= unit:
        res,m = divmod(seconds,unit)
        seconds = m
    return res, seconds


# Cleaner solution
# times = [("year", 365 * 24 * 60 * 60), 
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]

# def format_duration(seconds):

#     if not seconds:
#         return "now"

#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)

#         seconds = seconds % secs
#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]   


 