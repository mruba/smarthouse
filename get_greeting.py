#!/bin/python
# -*- coding: utf-8 -*-
import time
import better_spoken_numbers as bsn
import ConfigParser
import locale

#Spanish version
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

day_of_month=str(bsn.d2w(int(time.strftime("%d"))))

now = time.strftime("%A ") + day_of_month +' de '+time.strftime("%B") + ', y son las' + time.strftime(" %I %M %p")
# print now es_ES.utf8


if int(time.strftime("%H")) < 12:
  period = 'dias'
if int(time.strftime("%H")) >= 12:
  period = 'tardes'
if int(time.strftime("%H")) >= 17:
  period = 'noches'

#print time.strftime("%H")
#print period

# reads out good morning + my name
gmt = 'Buenos ' + period + ', '

# reads date and time
day = ' Hoy es ' + now + '.  '

greeting = gmt + Config.get('greeting','name') + day

if Config.get('main','debug') == str(1):
  print greeting
