from house_control.model.device.code_name import incCodeNameLetter
from house_control.model.device.impl import Computer, Monitor, Light, ColorLight, BrightnessLight, \
    Fan, SpeedFan, Blower, Radio, TV, AlarClock, Shutter
from house_control.model.location import Loc

house = Loc('dom')

attic = Loc('poddasze', parent=house)
atticP1 = Loc('część pierwsza na poddaszu', parent=attic)
atticP2 = Loc('część druga na poddaszu', parent=attic)
bedroom = Loc('sypialnia', parent=house)
bathroom = Loc('łazienka', parent=house)
livingRoom = Loc('salon', parent=house)
kitchen = Loc('kuchnia', parent=house)

# ################ attic part 1 ################
curLoc = atticP1
lamps = [
    Light('oświetlenie górne', curLoc),
    Light('oświetlenie biurka', curLoc)
]
Radio('radio', curLoc)
Computer('komputer', curLoc)
Monitor('monitor', curLoc)

# ################ attic part 2 ################
curLoc = atticP2
lamps.extend([
    Light('oświetlenie górne', curLoc),
    Light('lampa nad ławą', curLoc),
    Light('lampa lewa', curLoc),
    Light('lampa prawa', curLoc),
])
TV('telewizor', curLoc)
lamps.append(Light('oświetlenie za telewizorem', curLoc, requiredNames='oświetlenie'))
Light('całe oświetlenie na poddaszu', curLoc, aggr=lamps)

# ################ bedroom ################
curLoc = bedroom
incCodeNameLetter()
lamps = [
    ColorLight('oświetlenie górne', curLoc, 'oświetlenie główne'),
    Light('lampa lewa', curLoc, requiredNames='lewa'),
    Light('lampa prawa', curLoc, requiredNames='prawa'),
    Light('lampa', curLoc, requiredNames=('!prawa', '!lewa')),
]
TV('telewizor', curLoc)
lamps.append(Light('oświetlenie za telewizorem', curLoc, requiredNames='oświetlenie'))
Light('całe oświetlenie w sypialni', curLoc, aggr=lamps)
AlarClock('budzik', curLoc)

# ################ bathroom ################
curLoc = bathroom
incCodeNameLetter()
lamps = [
    Light('oświetlenie górne', curLoc),
    Light('lampa nad lustrem', curLoc),
]
Fan('wentylator', curLoc)
Blower('dmuchawa', curLoc)
Light('całe oświetlenie w łazience', curLoc, aggr=lamps)

# ################ livingRoom ################
curLoc = livingRoom
incCodeNameLetter()
lamps = [
    Light('oświetlenie górne', curLoc),
    ColorLight('lampa lewa', curLoc),
    ColorLight('lampa prawa', curLoc),
]
Light('całe oświetlenie w salonie', curLoc, aggr=lamps)
s0 = Shutter('Roleta lewa', curLoc)
s1 = Shutter('Roleta prawa', curLoc)
Shutter('Rolety razem', curLoc, aggr=[s0, s1])

# ################ kitchen ################
curLoc = kitchen
incCodeNameLetter()
lamps = [
    Light('oświetlenie górne', curLoc),
    BrightnessLight('oświetlenie nad szafkami', curLoc),
    Light('oświetlenie pod szafkami', curLoc),
    Light('oświetlenie okapu', curLoc),
]
SpeedFan('okap', curLoc)
Fan('wentylator', curLoc)
Light('całe oświetlenie w kuchni', curLoc, aggr=lamps)
