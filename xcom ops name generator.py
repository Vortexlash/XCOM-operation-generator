import random

#missionnames

rfn = random.randrange(0, 52)
fw = ["Swift", "Unceasing", "Vengeful", "Lone", "Cold", "Hot", "Purple", "Brutal", "Flying", "Driving", "Blind", "Demon", "Enduring", "Defiant", "Lost", "Dying", "Falling", "Soaring", "Twisted", "Glass", "Bleeding", "Broken", "Silent", "Red", "Black", "Dark", "Fallen", "Patient", "Burning", "Final", "Lazy", "Morbid", "Crimson", "Cursed", "Frozen", "Bloody", "Banished", "First", "Severed", "Empty", "Spectral", "Sacred", "Stone", "Shattered", "Hidden", "Rotting", "Devil's", "Forgotten", "Blinding", "Fading", "Crystal", "Secret", "Cryptic"]

rln =random.randrange(0, 75)
lw = [" Engine", " Chant", " Heart", " Justice", " Law", " Thunder", " Moon", " Heat", " Fear", " Star", " Apollo", " Prophet", " Hero", " Hydra", " Serpent", " Crown", " Thorn", " Empire", " Line", " Fall", " Summer", " Druid", " God", " Savior", " Stallion", " Hawk", " Vengeance", " Calm", " Knife", " Sword", " Dream", " Sleep", " Stroke", " Flame", " Spark", " Fist", " Dirge", " Grave", " Shroud", " Breath", " Smoke", " Giant", " Whisper", " Night", " Throne", " Pipe", " Blade", " Daze", " Pyre", " Tears", " Mother", " Crone", " King", " Father", " Priest", " Dawn", " Hammer", " Shield", " Hymn", " Vanguard", " Sentinel", " Stranger", " Bell", " Mist", " Fog", " Jester", " Scepter", " Ring", " Skull", " Paramour", " Palace", " Mountain", " Rain", " Gaze", " Future", " Gift"]

opname = (fw[rfn]) + (lw[rln])

#missiontypes

rmt = random.randrange(0, 7)
mt = ["Alien Abductions", "Alien Base Assault", "Council Mission", "Temple Ship Assault", "Alien Terror Attack", "UFO Crash Site", "UFO Landing Site", "XCOM Base Defense"]

optype = (mt[rmt])

if rmt == 3:
    opname = "Avenger"
elif rmt == 7:
    opname = "Ashes And Temples"
    
print("Operation " + '"' + (opname) + '"')

print(optype)

#missiondetails

rml = random.randrange(0, 15)
cl = ["USA", "Canada", "France", "United Kingdom", "Germany", "Nigeria", "Egypt", "South Africa", "China", "Japan", "India", "Australia", "Brazil", "Argentina", "Mexico", "Russia"]

oplocation = (cl[rml])

print(oplocation)

#missionobjectives

rcm = random.randrange(0, 24)
cm = ["Asset Recovery [1]", "Asset Recovery [2]", "Asset Recovery [3]", "Asset Recovery [4]", "Asset Recovery [5]", "Asset Recovery [6]", "Bomb Disposal [1]", "Bomb Disposal [2]", "Bomb Disposal [3]", "Bomb Disposal [4]", "Bomb Disposal [5]", "Target Escort [1]", "Target Escort [2]", "Target Escort [3]", "Target Extraction [1]", "Target Extraction [2]", "Target Extraction [3]", "Site Recon", "Portent", "Deluge", "Furies", "Friends in Low Places", "Confounding Light", "Gangplank", "Gateway"]

opbrief = None
optasks = None

if rmt == 0:
    opbrief = "Alien abduction in progress. Site is clear of civilians; collateral damage is not a concern."
    optasks = "Neutralize all hostile targets. Locate and secure any Meld canisters."
elif rmt == 1:
    opbrief = "We have gained access to an Alien Base by means of the Skeleton Key. Use extreme caution; analysis indicates the presence of a large combined enemy contingent. This mission cannot be aborted."
    optasks = "Penetrate the base's defenses. Neutralize all invader forces. Identify and capture the base commander, if possible."
elif rmt == 2:
    if rcm == 0:
        opbrief = "Alien forces have infiltrated the site and will actively oppose our efforts."
        optasks = "Sweep the area of operations. Eliminate all opposition."
    elif rcm == 1:
        opbrief = "Alien forces have infiltrated the site and will actively oppose our efforts."
        optasks = "Sweep the area of operations. Eliminate all opposition."
    elif rcm == 2:
        opbrief = "Alien forces have infiltrated the site and will actively oppose our efforts."
        optasks = "Sweep the area of operations. Eliminate all opposition."
    elif rcm == 3:
        opbrief = "Alien forces have infiltrated the site and will actively oppose our efforts."
        optasks = "Sweep the area of operations. Eliminate all opposition."
    elif rcm == 4:
        opbrief = "Alien forces have infiltrated the site and will actively oppose our efforts."
        optasks = "Sweep the area of operations. Eliminate all opposition."
    elif rcm == 5:
        opbrief = "Alien forces have infiltrated the site and will actively oppose our efforts."
        optasks = "Sweep the area of operations. Eliminate all opposition."
    elif rcm == 6:
        opbrief = "The invaders have placed a bomb in the area of operations to inflict maximum destruction and panic."
        optasks = "Deactivate the bomb before it goes off. Delay the detonation countdown by deactivating the bomb's power sources. Prevent reactivation by eliminating all remaining opposition."
    elif rcm == 7:
        opbrief = "The invaders have placed a bomb in the area of operations to inflict maximum destruction and panic."
        optasks = "Deactivate the bomb before it goes off. Delay the detonation countdown by deactivating the bomb's power sources. Prevent reactivation by eliminating all remaining opposition."
    elif rcm == 8:
        opbrief = "The invaders have placed a bomb in the area of operations to inflict maximum destruction and panic."
        optasks = "Deactivate the bomb before it goes off. Delay the detonation countdown by deactivating the bomb's power sources. Prevent reactivation by eliminating all remaining opposition."
    elif rcm == 9:
        opbrief = "The invaders have placed a bomb in the area of operations to inflict maximum destruction and panic."
        optasks = "Deactivate the bomb before it goes off. Delay the detonation countdown by deactivating the bomb's power sources. Prevent reactivation by eliminating all remaining opposition."
    elif rcm == 10:
        opbrief = "The invaders have placed a bomb in the area of operations to inflict maximum destruction and panic."
        optasks = "Deactivate the bomb before it goes off. Delay the detonation countdown by deactivating the bomb's power sources. Prevent reactivation by eliminating all remaining opposition."
    elif rcm == 11:
        opbrief = "A high value target requires an escort for evacuation to XCOM HQ. However, hostile units in the area are on high alert, and will attempt to counter our extraction team."
        optasks = "Escort the target safely to the extraction point. Protect the target at all costs."
    elif rcm == 12:
        opbrief = "A high value target is in position for evacuation to XCOM HQ. However, hostile units in the area are on high alert, and will attempt to counter our extraction team."
        optasks = "Escort the target to the extraction point. Protect the target at all costs."
    elif rcm == 13:
        opbrief = "A high value target is in position for evacuation to XCOM HQ. However, hostile units in the area are on high alert, and will attempt to counter our extraction team."
        optasks = "Escort the target to the extraction point. Protect the target at all costs."
    elif rcm == 14:
        opbrief = "A high value target requires an escort for evacuation to XCOM HQ. However, hostile units in the area are on high alert, and will attempt to counter our extraction team."
        optasks = "Find the Target. Escort the target safely to the extraction point. Protect the target at all costs."
    elif rcm == 15:
        opbrief = "A high value target requires an escort for evacuation to XCOM HQ. However, hostile units in the area are on high alert, and will attempt to counter our extraction team."
        optasks = "Find the target. Escort the target safely to the extraction point. Protect the target at all costs."
    elif rcm == 16:
        opbrief = "Intel indicates a high value civilian asset somewhere at site; exact location unknown. The enemy is present in unknown numbers."
        optasks = "Locate the VIP. Protect the VIP at all costs."
    elif rcm == 17:
        opbrief = "The fishing village still shows no signs of life. The nature of the aliens' involvement is unknown, as is the type and level of resistance. Extreme caution is warranted."
        optasks = "Investigate the site. Identify and eliminate all opposition."
    elif rcm == 18:
        opbrief = "A French military convoy was caught in an ambush. The convoy's current status is unknown. Be prepared for anything."
        optasks = "Investigate the area of operations. Locate and secure any survivors as well as the convoy's cargo. Eliminate any remaining opposition."
    elif rcm == 19:
        opbrief = "The transport is stopped on a dam in France; it's likely the aliens have sabotaged the structure. They clearly consider this transport to be high value. Expect substantial opposition."
        optasks = "Secure the dam by any means necessary. Locate and secure the convoy and its contents."
    elif rcm == 20:
        opbrief = "The aliens are holding Annette's fellow abductees on their ship and will not easily let them go. Secure the captives as quickly as possible."
        optasks = "Locate and rescue the other abductees. Eliminate all opposition."
    elif rcm == 21:
        opbrief = "If the contact's device is genuine, as we suspect it is, it'll be of high value. Stay sharp, as the aliens may make an effort to recover it."
        optasks = "Escort VIP and the alien artifact to the extraction point. Eliminate any resistance. VIP must survive."
    elif rcm == 22:
        opbrief = "A battleship is closing on the city. The squad must place the transponders in time to divert the attack. Aliens will likely deploy scouts to seek out any human resistance. Enemy contact likely."
        optasks = "Plant the transponders on the train. Once the transponders are in place, activate the train's drive control system."
    elif rcm == 23:
        opbrief = "The battleship is crippled but still active, and the aliens aboard won't be happy to see us. Expect maximum resistance."
        optasks = "Destroying or disabling the power conduits will enable us to bring down the Battleship without damaging it. Eliminate all alien defenders."
    elif rcm == 24:
        opbrief = "Alien forces are in the area; witnesses report seeing multiple canisters of unknown purpose. Civilians have been evacuated."
        optasks = "Neutralize all hostile targets. Locate and secure the canisters for analysis at HQ."
elif rmt == 3:
    opbrief = "We finally have the strength to face the Ethereals on their own ship. The future of humanity is at stake. Expect extreme resistance."
    optasks = "Force entry to the Temple Ship's bridge. The Volunteer must survive."
elif rmt == 4:
    opbrief = "Alien terror attack in progress. Strong civilian presence; every civilian casualty will sharply increase panic in this country. Failure will have severe political consequences for XCOM."
    optasks = "Approach civilians to enable evacuations. Minimize civilian casualties. Neutralize all hostile targets"
elif rmt == 5:
    opbrief = "XCOM Interceptors have splashed a UFO. Intel indicates some surviving crew. Exercise caution when engaging the enemy; the craft may contain usable salvage."
    optasks = "Locate the crashed UFO. Sweep the area for surviving crew and neutralize them. Locate and secure any Meld canisters. Avoid additional damage to the craft if possible; some components may be recoverable."
elif rmt == 6:
    opbrief = "Satellite data indicates a UFO has touched down; high probability of enemy operation in progress. Expect to face a full complement of enemy crew."
    optasks = "Gain entry to the UFO and neutralize all enemy forces. Locate and secure any Meld canisters."
elif rmt == 7:
    opbrief = "The invaders have infiltrated XCOM in unknown numbers. Limited reinforcements, including XCOM Base Security personnel, are available. Failure will mean a massive setback for XCOM."
    optasks = "Defend our base by all necessary means. If all soldiers in the combat area are killed, XCOM HQ will suffer massive damage and loss of resources."

print("MISSION BRIEF: " + (opbrief))
print("MISSION OBJECTIVES: " + (optasks))

#tacticaltips

rt =random.randrange(0, 31)
tt = [" Always move to flank enemies if possible. They are easier to hit and to score critical hits against.", " Be on the lookout for ladders and drain pipes. Gaining a height advantage over an enemy increases your chance to hit them.", " Grenades and rockets will render unusable any artifacts other than corpses.", " You can increase the number of soldiers you bring on combat missions by purchasing tactical upgrades in the Officer Training School.", " A unit performing a dash move has a defensive bonus against enemy reaction fire.", " Poison can be cured using a Medikit. Advanced armor types can also protect against it entirely.", " A soldier who has survived a critical wound can recover, but suffers a permanent reduction to Will.", " Your soldiers can kick in doors and jump through windows, but the resulting noise will alert any nearby aliens to your presence.", " Opening a door won't cost an action, so take cover beside one and open it from the side to avoid attracting enemy attention.", " Switching to pistol is a good alternative when a soldier's primary weapon is out of ammo or otherwise unavailable.", " When facing an enemy at long range and armed with a shotgun, consider switching to a pistol for reduced damage but increased aim.", " Staying in cover is the key to staying alive.", " Think carefully about taking a low-percentage shot. It may be better to use Overwatch instead.", " If you have no enemies in sight, consider Overwatch to guard against ambush.", " Reaction fire from overwatch carries an Aim penalty, but is still dangerous.", " On outdoor missions, pay attention to your surroundings. Flames and debris can help you locate crashed UFOs.", " Critically wounded soldiers have only a few turns before bleeding out and dying. Stabilize them quickly with a Medikit.", " Panicking soldiers will lose their next turn, and can act unpredictably.", " Civilian VIPs can improve their defense by taking cover and using the Head Down ability.", " Pistols never run out of ammunition, and they can be heavily upgraded in the Foundry if the right research is pursued.", " Be careful when facing enemies that use grenades; clustering your squad together can result in disaster.", " The Arc Thrower has a limited range, so using it can be risky.", " Robotic units are immune to panic, but cannot receive training.", " Flying enemies can be hard to hit if they have the Evasion ability. Take care to avoid being flanked.", " Close combat attacks never miss, so be especially careful when fighting enemies that use them.", " Smoke protects both sides. When you deploy smoke grenades, be careful not to help the enemy as well as your own squad.", " Many objects on the battlefield are volatile, and can cause devastating explosions if set off with explosive weapons.", " By using Hunker Down, squad members can improve the value of cover and become immune to critical hits, at the cost of visibility.", " Snipers cannot fire after moving, unless they've had special training. They rely on their pistols more than any other class does.", " If a unit is suppressed after going on overwatch, it loses its reaction fire opportunity.", " Soldiers will not incur wound recovery time if the damage they take is less than the health their armor grants.", " Medikits will save a soldier from death, but they are just a temporary measure, and the soldier will still need infirmary time if any damage got through the soldier's armor."]

print("TIP:" + (tt[rt]))
