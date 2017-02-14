import json
import urllib3
from sopel import module

@module.commands('ipinfo')
def ipinfo(bot, trigger):
    if not trigger.group(2):
        return bot.say('This commands requires a hostname or IP address. \
                        e.g. "!ipinfo irc.occultus.net" or \
                        "!ipinfo 208.99.88.243"')
    http = urllib3.PoolManager()
    url = 'https://freegeoip.net/json/' + trigger.group(2)
    response = http.request('GET', url)
    ipinfo = json.loads(response.data.decode('utf8'))
    ipadd = ipinfo['ip']
    cname = ipinfo['country_name']
    ccode = ipinfo['country_code']
    region = ipinfo['region_name']
    city = ipinfo['city']
    zipcd = ipinfo['zip_code']
    tzdata = ipinfo['time_zone']
    lat = ipinfo['latitude']
    lon = ipinfo['longitude']
    metro = ipinfo['metro_code']
    bot.say('Query: ' + trigger.group(2))
    bot.say('IP Address: ' + ipadd)
    bot.say('Country Code: ' + ccode)
    bot.say('Country Name: ' + cname)
    bot.say('Region Name: ' + region)
    bot.say('City: ' + city)