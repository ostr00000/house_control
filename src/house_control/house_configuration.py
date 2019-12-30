from house_control.model.device.impl import Computer, Monitor, Light, ColorLight, BrightnessLight, \
    Fan, SpeedFan, Blower, Radio, TV, AlarClock, Shutter
from house_control.model.location import Loc

house = Loc('dom')

attic = Loc('poddasze', parent=house)
atticP1 = Loc('cześć pierwsza', parent=attic)
atticP2 = Loc('cześć druga', parent=attic)
bedroom = Loc('sypialnia', parent=house)
bathroom = Loc('łazienka', parent=house)
livingRoom = Loc('salon', parent=house)
kitchen = Loc('kuchnia', parent=house)

# attic part 1
Light('oświetlenie górne', atticP1)
Light('oświetlenie biurka', atticP1)
Radio('radio', atticP1)
Computer('komputer', atticP1)
Monitor('monitor', atticP1)

# attic part 2
Light('oświetlenie górne', atticP2)
Light('lampa nad ławą', atticP2)
Light('lampa lewa', atticP2)
Light('lampa prawa', atticP2)
Light('lampa', atticP2)
TV('telewizor', atticP2)
Light('oświetlenie za telewizorem', atticP2)
Light('całe oświetlenie na poddaszu', atticP2)

# bedroom
ColorLight('oświetlenie górne', bedroom)
Light('lampa lewa', bedroom)
Light('lampa prawa', bedroom)
Light('lampa', bedroom)
TV('telewizor', bedroom)
Light('oświetlenie za telewizorem', bedroom)
Light('całe oświetlenie w sypialni', bedroom)
AlarClock('budzik', atticP2)

# bathroom
Light('oświetlenie górne', bathroom)
Light('lampa nad lustrem', bathroom)
Fan('wentylator', bathroom)
Blower('dmuchawa', bathroom)
Light('całe oświetlenie w łazience', bathroom)

# living room
Light('oświetlenie górne', livingRoom)
ColorLight('lampa lewa', livingRoom)
ColorLight('lampa prawa', livingRoom)
Light('całe oświetlenie w salonie', livingRoom)
Shutter('Roleta lewa', livingRoom)
Shutter('Roleta prawa', livingRoom)  # TODO default should be 'razem'
Shutter('Rolety razem', livingRoom)

# kitchen
Light('oświetlenie górne', kitchen)
BrightnessLight('oświetlenie nad szafkami', kitchen)
Light('oświetlenie pod szafkami', kitchen)
Light('oświetlenie okapu', kitchen)
SpeedFan('okap', kitchen)
Fan('wentylator', kitchen)
Light('całe oświetlenie w kuchni', livingRoom)
