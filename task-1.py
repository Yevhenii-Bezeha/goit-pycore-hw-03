from datetime import datetime


def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.today().date()
        result = (today_date - input_date).days
        return result
    except ValueError:
        raise ValueError("Wrong date format use: 'YYYY-MM-DD'.")


try:
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("invalid-date"))
except ValueError as e:
    print(e)
