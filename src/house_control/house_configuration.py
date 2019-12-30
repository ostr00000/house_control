from house_control.model.device.impl import Computer, Monitor, Light, ColorLight, BrightnessLight, \
    Fan, SpeedFan, Blower, Radio, TV, AlarClock, Shutter
from house_control.model.location import Loc

lamps = []
house = Loc('dom')

attic = Loc('poddasze', parent=house)
atticP1 = Loc('cześć pierwsza', parent=attic)
atticP2 = Loc('cześć druga', parent=attic)
bedroom = Loc('sypialnia', parent=house)
bathroom = Loc('łazienka', parent=house)
livingRoom = Loc('salon', parent=house)
kitchen = Loc('kuchnia', parent=house)

# ################ attic part 1 ################
curLoc = atticP1
lamps.extend([
    Light('oświetlenie górne', curLoc),
    Light('oświetlenie biurka', curLoc)
])
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
    Light('lampa', curLoc),
])
TV('telewizor', curLoc)
lamp5 = Light('oświetlenie za telewizorem', curLoc)
Light('całe oświetlenie na poddaszu', curLoc, aggr=lamps)
lamps.clear()

# ################ bedroom ################
curLoc = bedroom
lamps.extend([
    ColorLight('oświetlenie górne', curLoc),
    Light('lampa lewa', curLoc),
    Light('lampa prawa', curLoc),
    Light('lampa', curLoc),
    Light('oświetlenie za telewizorem', curLoc),
])

TV('telewizor', curLoc)
Light('całe oświetlenie w sypialni', curLoc, aggr=lamps)
AlarClock('budzik', curLoc)
lamps.clear()

# ################ bathroom ################
curLoc = bathroom
lamps.extend([
    Light('oświetlenie górne', curLoc),
    Light('lampa nad lustrem', curLoc),
])
Fan('wentylator', curLoc)
Blower('dmuchawa', curLoc)
Light('całe oświetlenie w łazience', curLoc, aggr=lamps)
lamps.clear()

# ################ livingRoom ################
curLoc = livingRoom
lamps.extend([
    Light('oświetlenie górne', curLoc),
    ColorLight('lampa lewa', curLoc),
    ColorLight('lampa prawa', curLoc),
])
Light('całe oświetlenie w salonie', curLoc, aggr=lamps)
lamps.clear()
s0 = Shutter('Roleta lewa', curLoc)
s1 = Shutter('Roleta prawa', curLoc)
Shutter('Rolety razem', curLoc, aggr=[s0, s1])

# ################ kitchen ################
curLoc = kitchen
lamps.extend([
    Light('oświetlenie górne', curLoc),
    BrightnessLight('oświetlenie nad szafkami', curLoc),
    Light('oświetlenie pod szafkami', curLoc),
    Light('oświetlenie okapu', curLoc),
])
SpeedFan('okap', curLoc)
Fan('wentylator', curLoc)
Light('całe oświetlenie w kuchni', curLoc, aggr=lamps)
