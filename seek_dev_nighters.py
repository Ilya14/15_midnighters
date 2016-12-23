import requests
import pytz
import argparse

from datetime import datetime, time


def load_attempts():
    first_page = 1
    attempts, number_of_pages = get_page(first_page)
    for attempt in attempts:
        yield attempt

    for page in range(first_page + 1, number_of_pages + 1):
        attempts_index = 0
        for attempt in get_page(page)[attempts_index]:
            yield attempt


def get_page(page_num):
    url = 'https://devman.org/api/challenges/solution_attempts'
    params = {'page': str(page_num)}
    response = requests.get(url, params)
    page_json_content = response.json()
    return page_json_content['records'], page_json_content['number_of_pages']


def get_midnighters(attempts_list, midnight_period):
    datetime_format = '%Y-%m-%d %H:%M:%S %Z%z'
    midnighters = []

    for attempt in attempts_list:
        timestamp = attempt['timestamp']
        if timestamp is not None:
            timezone_localize = get_timezone_localize(timestamp, attempt['timezone'])
            if timezone_localize.time() <= time(hour=midnight_period):
                midnighters.append(
                    {
                        'username': attempt['username'],
                        'datetime': timezone_localize.strftime(datetime_format)
                    }
                )

    return midnighters


def get_timezone_localize(timestamp, timezone):
    utc_localize = pytz.utc.localize(datetime.utcfromtimestamp(timestamp))
    timezone = pytz.timezone(timezone)
    return utc_localize.astimezone(timezone)


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

    midnighters = get_midnighters(list(load_attempts()), midnight_period)

    print(
        'Devman midnighters in the range [00:00:00, {0}] (total quantity: {1}):'.format(
            time(hour=midnight_period).strftime('%H:%M:%S'),
            len(midnighters)
        )
    )
    for midnighter in midnighters:
        print('{0[username]:20}{0[datetime]}'.format(midnighter))
