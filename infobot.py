from sopel import module

@module.rule('.*(groot).*good bo(t|y).*')
def thanks(bot, trigger):
	bot.say('thank you, ' + trigger.nick)

@module.rule('pets groot')
def smile(bot, trigger):
	bot.action('smiles at ' + trigger.nick)

@module.rule('kicks groot')
def fall(bot, trigger):
	bot.action('falls down, sadly, with a hollow clang')

@module.rule('.*(groot).*bad bo(t|y).*')
def badbot(bot, trigger):
	bot.action('goes to the Corner of Shame and starts taking himself apart')

@module.rule('.*canada.*')
def canada(bot, trigger):
	bot.say('“Canada is a myth people made up to entertain children, like the Tooth Fairy. There’s no such place.” -- Christopher Moore')