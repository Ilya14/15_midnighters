import requests
import pytz
import argparse

from datetime import datetime, time


def load_attempts():
    def get_page(page_number=1):
        url = 'https://devman.org/api/challenges/solution_attempts'
        params = {'page': str(page_number)}
        response = requests.get(url, params)
        return response.json()

    for page in range(get_page()['number_of_pages']):
        attempts = get_page(page + 1)['records']
        for attempt in attempts:
            yield attempt


def get_midnighters(attempts_list, midnight_period):
    datetime_format = '%Y-%m-%d %H:%M:%S %Z%z'
    midnighters = []

    for attempt in attempts_list:
        timestamp = attempt['timestamp']
        if timestamp is not None:
            utc_localize = pytz.utc.localize(datetime.utcfromtimestamp(timestamp))
            timezone = pytz.timezone(attempt['timezone'])
            timezone_localize = utc_localize.astimezone(timezone)
            if timezone_localize.time() <= time(hour=midnight_period):
                midnighters.append(
                    {
                        'username': attempt['username'],
                        'datetime': timezone_localize.strftime(datetime_format)
                    }
                )

    return midnighters


def get_args():
    parser = argparse.ArgumentParser(description='Script for midnighters search on the Devman')
    default_hour = 6
    parser.add_argument(
        '--hour',
        type=int,
        choices=range(1, default_hour + 1),
        default=default_hour,
        help='The interesting time period after midnight: [00:00:00, hour:00:00], where hour in [1, {0}]'.format(
            default_hour
        )
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    midnight_period = args.hour

    attempts_list = [attempt for attempt in load_attempts()]
    midnighters = get_midnighters(attempts_list, midnight_period)

    print(
        'Devman midnighters in the range [00:00:00, {0}] (total quantity: {1}):'.format(
            time(hour=midnight_period).strftime('%H:%M:%S'),
            len(midnighters)
        )
    )
    for midnighter in midnighters:
        print('{0[username]:20}{0[datetime]}'.format(midnighter))
