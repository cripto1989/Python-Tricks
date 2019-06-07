import datetime 


def get_init_end_date(date=None):
    """
    This function return two dates base on a date set or the current date(today)
    Monday(0) - Sunday(6)
    return dict: init and end date of the week
    """    
    if not date:
        date = datetime.date.today()  
    day_of_week = date.weekday()  # Number of day of the week
    day_init_week = date - datetime.timedelta(day_of_week)  # Get the init day of the week
    day_end_week = day_init_week + datetime.timedelta(6)  # Get the end day of the week    
    return {'init': day_init_week, 'end': day_end_week}

# print(get_init_end_date(date=datetime.date(2019,05,01)))
# print(get_init_end_date())