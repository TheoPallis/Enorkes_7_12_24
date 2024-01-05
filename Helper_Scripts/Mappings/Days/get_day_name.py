def get_day_name(date_string, date_format='%d/%m/%Y'):

    date_object = datetime.datetime.strptime(date_string, date_format)
    return date_object.strftime('%A')
