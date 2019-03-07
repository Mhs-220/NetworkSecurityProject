import datetime

def convert_to_tehran(created_date: str) -> str:
    datetime_object = datetime.datetime.strptime(created_date, '%Y-%m-%d %H:%M:%S')
    datetime_object_date = datetime_object.date()
    now = datetime.datetime.now()
    now_date = now.date()
    ASIA_TEHRAN_UTC = 3.5
    tehran_time_delta = datetime.timedelta(hours = ASIA_TEHRAN_UTC)
    tehran_date_time = datetime_object + tehran_time_delta
    if datetime_object_date == now_date:
        return '{} | {}'.format('Today', datetime.datetime.strftime(tehran_date_time, '%H:%M'))
    else:
        return '{}'.format(datetime.datetime.strftime(tehran_date_time, '%b %d %Y | %H:%M'))