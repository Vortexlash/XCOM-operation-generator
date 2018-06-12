import random

#missionnames

rfn = random.randrange(0, 52)
fw = ["Swift", "Unceasing", "Vengeful", "Lone", "Cold", "Hot", "Purple", "Brutal", "Flying", "Driving", "Blind", "Demon", "Enduring", "Defiant", "Lost", "Dying", "Falling", "Soaring", "Twisted", "Glass", "Bleeding", "Broken", "Silent", "Red", "Black", "Dark", "Fallen", "Patient", "Burning", "Final", "Lazy", "Morbid", "Crimson", "Cursed", "Frozen", "Bloody", "Banished", "First", "Severed", "Empty", "Spectral", "Sacred", "Stone", "Shattered", "Hidden", "Rotting", "Devil's", "Forgotten", "Blinding", "Fading", "Crystal", "Secret", "Cryptic"]

rln =random.randrange(0, 75)
lw = [" Engine", " Chant", " Heart", " Justice", " Law", " Thunder", " Moon", " Heat", " Fear", " Star", " Apollo", " Prophet", " Hero", " Hydra", " Serpent", " Crown", " Thorn", " Empire", " Line", " Fall", " Summer", " Druid", " God", " Savior", " Stallion", " Hawk", " Vengeance", " Calm", " Knife", " Sword", " Dream", " Sleep", " Stroke", " Flame", " Spark", " Fist", " Dirge", " Grave", " Shroud", " Breath", " Smoke", " Giant", " Whisper", " Night", " Throne", " Pipe", " Blade", " Daze", " Pyre", " Tears", " Mother", " Crone", " King", " Father", " Priest", " Dawn", " Hammer", " Shield", " Hymn", " Vanguard", " Sentinel", " Stranger", " Bell", " Mist", " Fog", " Jester", " Scepter", " Ring", " Skull", " Paramour", " Palace", " Mountain", " Rain", " Gaze", " Future", " Gift"]

opname = (fw[rfn]) + (lw[rln])

#missiontypes

rmt = random.randrange(0, 7)
mt = ["Alien Abductions", "Alien Base Assault", "Council Mission", "Temple Ship Assault", "Alien Terror Attack", "UFO Crash Site", "UFO Landing Site"]

optype = (mt[rmt])

if rmt == 3:
    opname = "Avenger"
    
print("Operation " + '"' + (opname) + '"')

print(optype)

#missiondetails

rml = random.randrange(0, 15)
cl = ["USA", "Canada", "France", "United Kingdom", "Germany", "Nigeria", "Egypt", "South Africa", "China", "Japan", "India", "Australia", "Brazil", "Argentina", "Mexico", "Russia"]

rpl = random.randrange(0, 4) #paniclevel

oplocation = (cl[rml])

print(oplocation)

#tacticaltips

rt =random.randrange(0, 31)
tt = [" Always move to flank enemies if possible. They are easier to hit and to score critical hits against.", " Be on the lookout for ladders and drain pipes. Gaining a height advantage over an enemy increases your chance to hit them.", " Grenades and rockets will render unusable any artifacts other than corpses.", " You can increase the number of soldiers you bring on combat missions by purchasing tactical upgrades in the Officer Training School.", " A unit performing a dash move has a defensive bonus against enemy reaction fire.", " Poison can be cured using a Medikit. Advanced armor types can also protect against it entirely.", " A soldier who has survived a critical wound can recover, but suffers a permanent reduction to Will.", " Your soldiers can kick in doors and jump through windows, but the resulting noise will alert any nearby aliens to your presence.", " Opening a door won't cost an action, so take cover beside one and open it from the side to avoid attracting enemy attention.", " Switching to pistol is a good alternative when a soldier's primary weapon is out of ammo or otherwise unavailable.", " When facing an enemy at long range and armed with a shotgun, consider switching to a pistol for reduced damage but increased aim.", " Staying in cover is the key to staying alive.", " Think carefully about taking a low-percentage shot. It may be better to use Overwatch instead.", " If you have no enemies in sight, consider Overwatch to guard against ambush.", " Reaction fire from overwatch carries an Aim penalty, but is still dangerous.", " On outdoor missions, pay attention to your surroundings. Flames and debris can help you locate crashed UFOs.", " Critically wounded soldiers have only a few turns before bleeding out and dying. Stabilize them quickly with a Medikit.", " Panicking soldiers will lose their next turn, and can act unpredictably.", " Civilian VIPs can improve their defense by taking cover and using the Head Down ability.", " Pistols never run out of ammunition, and they can be heavily upgraded in the Foundry if the right research is pursued.", " Be careful when facing enemies that use grenades; clustering your squad together can result in disaster.", " The Arc Thrower has a limited range, so using it can be risky.", " Robotic units are immune to panic, but cannot receive training.", " Flying enemies can be hard to hit if they have the Evasion ability. Take care to avoid being flanked.", " Close combat attacks never miss, so be especially careful when fighting enemies that use them.", " Smoke protects both sides. When you deploy smoke grenades, be careful not to help the enemy as well as your own squad.", " Many objects on the battlefield are volatile, and can cause devastating explosions if set off with explosive weapons.", " By using Hunker Down, squad members can improve the value of cover and become immune to critical hits, at the cost of visibility.", " Snipers cannot fire after moving, unless they've had special training. They rely on their pistols more than any other class does.", " If a unit is suppressed after going on overwatch, it loses its reaction fire opportunity.", " Soldiers will not incur wound recovery time if the damage they take is less than the health their armor grants.", " Medikits will save a soldier from death, but they are just a temporary measure, and the soldier will still need infirmary time if any damage got through the soldier's armor."]

print("TIP:" + (tt[rt]))