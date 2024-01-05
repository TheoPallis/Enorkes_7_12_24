
import datetime

def get_day_name(date_string, date_format='%Y-%m-%d %H:%M:%S'):
    date_object = datetime.datetime.strptime(date_string, date_format)
    day_name=  date_object.strftime('%A')
    # Convert the day name to Greek
    greek_day_names = {
        'Monday': 'Δευτέρα',
        'Tuesday': 'Τρίτη',
        'Wednesday': 'Τετάρτη',
        'Thursday': 'Πέμπτη',
        'Friday': 'Παρασκευή',
        'Saturday': 'Σάββατο',
        'Sunday': 'Κυριακή'
    }
    
    return greek_day_names.get(day_name, day_name)


def map_day_name (anathesi_df) :
    anathesi_df['ΗΜΕΡΑ ΕΝΟΡΚΗΣ'] = anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'].apply(get_day_name)
    return anathesi_df