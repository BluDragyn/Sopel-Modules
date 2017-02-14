'''

A simple module for Sopel (http://sopel.chat) to get horoscope
information from a JSON API and put it back into chat

All orignal code written by: BluDragyn. (www.bludragyn.net)

This module is released under the terms of the GPLv3
(https://www.gnu.org/licenses/gpl-3.0.en.html)

If you use and like this module, please send me an email
(dragyn@bludragyn.net) or drop in to see me on Occultus IRC
(irc.occultus.net), I hang out in #sacredpaths

'''

import json
import urllib3
from sopel import module

@module.commands('hs', 'horoscope')
def horoscope(bot, trigger):
    signs = set(['aquarius', 'Aquarius',
                 'pisces', 'Pisces',
                 'aries', 'Aries',
                 'taurus', 'Taurus',
                 'gemini', 'Gemini',
                 'cancer', 'Cancer',
                 'leo', 'Leo',
                 'virgo', 'Virgo',
                 'libra', 'Libra',
                 'scorpio', 'Scorpio',
                 'sagittarius', 'Sagittarius',
                 'capricorn', 'Capricorn'])
    sign = trigger.group(2)
    nick = trigger.nick
    if sign in signs:
        sign = sign.lower()
        hs = get_hs(sign)
        sign = sign.capitalize()
        bot.say('Today\'s horoscope for ' + sign + ' is: ' + hs)
    else:
        bot.say(nick + ', please use a valid zodiac sign and try again.')
        
def get_hs(sunsign):
    http = urllib3.PoolManager()
    url = 'http://sandipbgt.com/theastrologer/api/horoscope/' \
           + sunsign + '/today/'
    response = http.request('GET', url)
    raw = json.loads(response.data.decode('utf8'))
    hscope = raw['horoscope']
    if not hscope:
        hscope = 'There was an error getting the horoscope right now.\
                  Please try again later.'
        return hscope
    else:
        hscope = hscope[:-59]
        return hscope