# 15_midnighters

## Описание

Скрипт выводит список тех пользователей Devman, кто отправлял задачи
на проверку после 24:00

## Использование

Скрипт имеет следующие опциональные параметры:

* -h, --help - помощь
* --hour - момент времени после полуночи, задающий интересующий интервал
[00:00:00, hour:00:00]. Может принимать значения из интервала [1, 6].
По умолчению равен 6.

## Пример

Отображение справки:

```sh
$ python3.5 ./seek_dev_nighters.py -h
usage: seek_dev_nighters.py [-h] [--hour {1,2,3,4,5,6}]

Script for midnighters search on the Devman

optional arguments:
  -h, --help            show this help message and exit
  --hour {1,2,3,4,5,6}  The interesting time period after midnight: [00:00:00,
                        hour:00:00], where hour in [1, 6]
```

Пример использования:

```sh
$ python3.5 ./seek_dev_nighters.py --hour 3
Devman midnighters in the range [00:00:00, 03:00:00] (total quantity: 24):
id54808965          2016-12-21 01:53:39 +07+0700
m_amador            2016-12-20 02:04:02 MSK+0300
m_amador            2016-12-20 01:36:38 MSK+0300
mr.kushnirov        2016-12-20 00:07:57 MSK+0300
IvanKumeyko         2016-12-19 01:35:40 MSK+0300
IvanKumeyko         2016-12-19 01:05:49 MSK+0300
IvanKumeyko         2016-12-19 00:42:11 MSK+0300
IvanKumeyko         2016-12-19 00:39:47 MSK+0300
sereschenka         2016-12-19 00:37:12 MSK+0300
IvanKumeyko         2016-12-19 00:34:01 MSK+0300
IvanKumeyko         2016-12-19 00:26:42 MSK+0300
id20889227          2016-12-18 00:28:56 MSK+0300
id54808965          2016-12-18 02:06:52 +07+0700
id213445897         2016-12-14 02:11:02 MSK+0300
MontyNumpy          2016-12-14 00:23:30 MSK+0300
id213445897         2016-12-13 02:59:14 MSK+0300
komarovv            2016-12-13 02:54:14 MSK+0300
komarovv            2016-12-13 02:23:20 MSK+0300
id93321377          2016-12-13 00:33:18 MSK+0300
id54808965          2016-12-13 02:11:49 +07+0700
MontyNumpy          2016-12-12 01:55:49 MSK+0300
id54808965          2016-12-12 00:51:38 +07+0700
id54808965          2016-12-12 00:00:23 +07+0700
id1505766           2016-12-11 00:04:45 MSK+0300
```