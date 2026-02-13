# knowledge_base.py: Basis Pengetahuan HoK - Diupdate 2026

hero_roles = {
    # Assassin
    "Arke": "Assassin", "Athena": "Assassin", "Cirrus": "Assassin", "Feyd": "Assassin",
    "Gao Changgong": "Assassin", "Han Xin": "Assassin", "Jing": "Assassin", "Lam": "Assassin",
    "Li Bai": "Assassin", "Luna": "Assassin", "Mai Shiranui": "Assassin", "Mi Yue": "Assassin",
    "Mulan": "Assassin", "Pei": "Assassin", "Prince Of Lanling": "Assassin", "Shangguan": "Assassin",
    "Sima Yi": "Assassin", "Ukyo Tachibana": "Assassin", "Wukong": "Assassin", "Ying": "Assassin",
    "Zilong": "Assassin", "Butterfly": "Assassin", "Diaochan": "Assassin",

    # Fighter
    "Allain": "Fighter", "Arthur": "Fighter", "Biron": "Fighter", "Cao Cao": "Fighter",
    "Charlotte": "Fighter", "Dharma": "Fighter", "Dian Wei": "Fighter", "Dun": "Fighter",
    "Guan Yu": "Fighter", "Li Xin": "Fighter", "Liu Bei": "Fighter", "Lu Bu": "Fighter",
    "Mayene": "Fighter", "Sun Ce": "Fighter", "Xiang Yu": "Fighter", "Yang Jian": "Fighter",
    "Bai Qi": "Fighter", "Nezha": "Fighter", "Umbrosa": "Fighter",

    # Mage
    "Angela": "Mage", "Cai Yan": "Mage", "Chang'e": "Mage", "Daji": "Mage", "Da Qiao": "Mage",
    "Dolia": "Mage", "Dr Bian": "Mage", "Gan & Mo": "Mage", "Heino": "Mage", "Kongming": "Mage",
    "Lady Zhen": "Mage", "Milady": "Mage", "Nuwa": "Mage", "Wang Zhaojun": "Mage",
    "Xiao Qiao": "Mage", "Yuhuan": "Mage", "Zhou Yu": "Mage", "Yixing": "Mage",

    # Marksman
    "Alessio": "Marksman", "Arli": "Marksman", "Consort Yu": "Marksman", "Di Renjie": "Marksman",
    "Garo": "Marksman", "Hou Yi": "Marksman", "Huang Zhong": "Marksman", "Lady Sun": "Marksman",
    "Luban No.7": "Marksman", "Marco Polo": "Marksman", "Loong": "Marksman",

    # Support
    "Da Qiao": "Support", "Sun Bin": "Support", "Yaria": "Support", "Lapulapu": "Support",

    # Tank
    "Ata": "Tank", "Lian Po": "Tank", "Xiang Yu": "Tank", "Flowborn": "Tank", "Zhang Fei": "Tank"
    # Tambah lebih banyak jika perlu dari tier list terbaru
}

# Sort keys untuk select option (alfabetis)
all_heroes = sorted(hero_roles.keys())

physical_roles = ["Assassin", "Fighter", "Marksman"]

role_base_items = {
    "Assassin": ["Shadow Ripper", "Eternity Blade", "Bloodweeper"],
    "Fighter": ["Axe of Torment", "Master Sword", "Daybreaker"],
    "Mage": ["Scepter of Reverberation", "Savant’s Wrath", "Void Staff"],
    "Marksman": ["Boots of Dexterity", "Shadow Ripper", "Bloodweeper"],
    "Support": ["Holy Grail", "Splendor", "Dawnlight"],
    "Tank": ["Boots of Resistance", "Glacial Buckler", "Axe of Torment"],
    "Unknown": ["Boots of Fortitude", "Default Sword"]
}

counter_items = {
    "magic_def": ["Boots of Resistance", "Mask of Agony", "Succubus Cloak"],
    "phys_def": ["Glacial Buckler", "Axe of Torment", "Ominous Premonition"],
    "anti_tank": ["Starbreaker", "Void Staff", "Siege Breaker"],
    "anti_heal": ["Mortal Punisher", "Venomous Staff", "Doomsday"]
}

rules = [
    {"cond": lambda c: c["magic"] >= 2, "need": "magic_def", "exp": "Banyak mage musuh → Butuh Magic Defense tinggi."},
    {"cond": lambda c: c["phys"] >= 3, "need": "phys_def", "exp": "Banyak physical dealer → Butuh Phys Defense."},
    {"cond": lambda c: c["tank"] >= 2, "need": "anti_tank", "exp": "Banyak tank musuh → Butuh Anti-Tank penetration."},
    {"cond": lambda c: c["support"] >= 1, "need": "anti_heal", "exp": "Ada support/healer → Butuh Anti-Heal items."}
]

item_details = {
    "Axe of Torment": {
        "category": "Physical",
        "stats": {"Physical Attack": 80, "Cooldown Reduction": 0.10, "Max Health": 500},
        "passive": "Great against squishy targets",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/axe-of-torment.jpg"  # Dari search, pilih yang clear
    },
    "Eternity Blade": {
        "category": "Physical",
        "stats": {"Physical Attack": 120, "Critical Rate": 0.20},
        "passive": "Grants high critical damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/eternity-blade.jpg"
    },
    "Shadow Ripper": {
        "category": "Physical",
        "stats": {"Physical Attack": 45, "Attack Speed": 0.35, "Critical Rate": 0.20, "Movement Speed": 0.075},
        "passive": "Critical hits boosts Attack Speed",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/shadow-ripper.jpg"
    },
    "Doomsday": {
        "category": "Physical",
        "stats": {"Physical Attack": 40, "Attack Speed": 0.20, "Physical Lifesteal": 0.20, "Max Health": 500},
        "passive": "Boosts Basic Attack’s damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/doomsday.jpg"
    },
    "Sparkforged Dagger": {
        "category": "Physical",
        "stats": {"Physical Attack": 40, "Attack Speed": 0.35, "Movement Speed": 0.075},
        "passive": "Gives Chain Lighting effect to Basic Attack",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/sparkforged-dagger.jpg"
    },
    "Bloodweeper": {
        "category": "Physical",
        "stats": {"Physical Attack": 85, "Physical Lifesteal": 0.25, "Max Health": 500},
        "passive": "Physical Skill Lifesteal item",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/bloodweeper.jpg"
    },
    "Daybreaker": {
        "category": "Physical",
        "stats": {"Physical Attack": 75, "Attack Speed": 0.30, "Critical Rate": 0.15},
        "passive": "Great for Marksmen heroes",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/daybreaker.jpg"
    },
    "Destiny": {
        "category": "Physical",
        "stats": {"Physical Attack": 75, "Attack Speed": 0.15, "Max Health": 500},
        "passive": "Nullifies fatal damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/destiny.jpg"
    },
    "Master Sword": {
        "category": "Physical",
        "stats": {"Physical Attack": 55, "Attack Speed": 0.15, "Critical Rate": 0.20, "Max Health": 600},
        "passive": "Boosts Basic Attack",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/master-sword.jpg"
    },
    "Starbreaker": {
        "category": "Physical",
        "stats": {"Physical Attack": 90, "Max Health": 700, "Movement Speed": 0.075},
        "passive": "Anti-tank item",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/starbreaker.jpg"
    },
    "Siege Breaker": {
        "category": "Physical",
        "stats": {"Physical Attack": 150, "Cooldown Reduction": 0.05},
        "passive": "High damage attack",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/siege-breaker.jpg"
    },
    "Tempest": {
        "category": "Physical",
        "stats": {"Physical Attack": 50, "Attack Speed": 0.30, "Max Health": 600},
        "passive": "BA stacks Attack Speed, Movement Speed and Damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/tempest.jpg"
    },
    "Mortal Punisher": {
        "category": "Physical",
        "stats": {"Physical Attack": 100, "Attack Speed": 0.20, "Physical Lifesteal": 0.20},
        "passive": "Lowers enemies’ HP regeneration",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/mortal-punisher.jpg"
    },
    "Runic Blade": {
        "category": "Physical",
        "stats": {"Physical Attack": 90, "Magical Defense": 150, "Max Health": 600},
        "passive": "Boosts Magical defense",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/runic-blade.jpg"
    },
    "Pure Sky": {
        "category": "Physical",
        "stats": {"Physical Attack": 80, "Cooldown Reduction": 0.10, "Physical Defense": 150},
        "passive": "Temporary damage reduction",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/pure-sky.jpg"
    },
    # Magical Items
    "Scepter of Reverberation": {
        "category": "Magical",
        "stats": {"Magical Attack": 210, "Movement Speed": 0.075},
        "passive": "Heroes’ skills hits explode upon impact",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/scepter-of-reverberation.jpg"
    },
    "Savant’s Wrath": {
        "category": "Magical",
        "stats": {"Magical Attack": 210},
        "passive": "Boosts Magic Attack",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/savants-wrath.jpg"
    },
    "Mask of Agony": {
        "category": "Magical",
        "stats": {"Magical Attack": 100, "Cooldown Reduction": 0.075, "Max Health": 900},
        "passive": "Boosts skill’s damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/mask-of-agony.jpg"
    },
    "Twilight Stream": {
        "category": "Magical",
        "stats": {"Magical Attack": 160, "Cooldown Reduction": 0.10, "Max Health": 500},
        "passive": "Boosts Magical Pierce",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/twilight-stream.jpg"
    },
    "Void Staff": {
        "category": "Magical",
        "stats": {"Magical Attack": 210, "Cooldown Reduction": 0.05, "Max Health": 500},
        "passive": "Anti-tank item",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/void-staff.jpg"
    },
    "Insatiable Tome": {
        "category": "Magical",
        "stats": {"Magical Lifesteal": 0.24, "Magical Attack": 160, "Max Health": 750},
        "passive": "Magical Lifesteal",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/insatiable-tome.jpg"
    },
    "Sage's Tome": {
        "category": "Magical",
        "stats": {"Magical Attack": 350, "Cooldown Reduction": 0.10},
        "passive": "Great item for Mages",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/sages-tome.jpg"
    },
    "Splendor": {
        "category": "Magical",
        "stats": {"Magical Lifesteal": 0.12, "Magical Attack": 160, "Cooldown Reduction": 0.075},
        "passive": "Temporary Invincibility",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/splendor.jpg"
    },
    "Holy Grail": {
        "category": "Magical",
        "stats": {"Magical Attack": 150, "Cooldown Reduction": 0.15, "Max Health": 500},
        "passive": "Rapidly regenerates HP and Mana",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/holy-grail.jpg"
    },
    "Golden Blade": {
        "category": "Magical",
        "stats": {"Attack Speed": 0.20, "Magical Attack": 150, "Movement Speed": 0.075},
        "passive": "Enhances Basic Attack overtime",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/golden-blade.jpg"
    },
    "Staves of Sorcery": {
        "category": "Magical",
        "stats": {"Magical Attack": 180, "Max Mana": 300, "Max Health": 600, "Movement Speed": 0.075},
        "passive": "Boosts Basic Attack",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/staves-of-sorcery.jpg"
    },
    "Augur’s Word": {
        "category": "Magical",
        "stats": {"Magical Attack": 140, "Max Mana": 450, "Max Health": 900},
        "passive": "Offense and Defense item",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/augurs-word.jpg"
    },
    "Ardent Dominator": {
        "category": "Magical",
        "stats": {"Magical Lifesteal": 0.12, "Magical Attack": 160, "Movement Speed": 0.075},
        "passive": "Grants a shield when HP drops below 30%",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/ardent-dominator.jpg"
    },
    "Breakthrough Robe": {
        "category": "Magical",
        "stats": {"Magical Attack": 120, "Max Health": 900},
        "passive": "HP converts into Magical Pierce",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/breakthrough-robe.jpg"
    },
    "Frozen Breath": {
        "category": "Magical",
        "stats": {"Magical Attack": 180, "Cooldown Reduction": 0.075, "Max Health": 500},
        "passive": "Skills hits slows down enemies",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/frozen-breath.jpg"
    },
    "Venomous Staff": {
        "category": "Magical",
        "stats": {"Magical Attack": 240, "Cooldown Reduction": 0.075, "Movement Speed": 0.075},
        "passive": "Lowers enemies’ HP regeneration",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/venomous-staff.jpg"
    },
    "Moon Goddess": {
        "category": "Magical",
        "stats": {"Magical Lifesteal": 0.12, "Magical Attack": 160, "Cooldown Reduction": 0.075},
        "passive": "Temporary Invincibility",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/moon-goddess.jpg"
    },
    # Defense Items
    "Dawnlight": {
        "category": "Defense",
        "stats": {"Cooldown Reduction": 0.10, "Physical Defense": 240, "Health per second": 150},
        "passive": "Grants shield while dealing damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/dawnlight.jpg"
    },
    "Blazing Cape": {
        "category": "Defense",
        "stats": {"Physical Defense": 240, "Max Health": 1000},
        "passive": "Burns nearby enemies",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/blazing-cape.jpg"
    },
    "Ominous Premonition": {
        "category": "Defense",
        "stats": {"Physical Defense": 270, "Max Health": 1200},
        "passive": "Slows attackers",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/ominous-premonition.jpg"
    },
    "Glacial Buckler": {
        "category": "Defense",
        "stats": {"Cooldown Reduction": 0.20, "Max Mana": 500, "Physical Defense": 360},
        "passive": "Boosts damage and slows enemies",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/glacial-buckler.jpg"
    },
    "Spikemail": {
        "category": "Defense",
        "stats": {"Physical Attack": 300, "Physical Defense": 360},
        "passive": "Reflects Physical damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/spikemail.jpg"
    },
    "Succubus Cloak": {
        "category": "Defense",
        "stats": {"Magical Defense": 200, "Max Health": 1000, "Health per second": 100},
        "passive": "Nullifies magical damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/succubus-cloak.jpg"
    },
    "Cuirass of Savagery": {
        "category": "Defense",
        "stats": {"Physical Attack": 30, "Physical Defense": 220, "Max Health": 900, "Movement Speed": 0.05},
        "passive": "Offense and Defense item",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/cuirass-of-savagery.jpg"
    },
    "Longnight Guardian": {
        "category": "Defense",
        "stats": {"Magical Defense": 360, "Max Health": 1000},
        "passive": "Resists burst damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/longnight-guardian.jpg"
    },
    "Sage’s Sanctuary": {
        "category": "Defense",
        "stats": {"Physical Defense": 140, "Magical Defense": 140},
        "passive": "Resurrect on the Spot (Can be triggered two times per match)",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/sages-sanctuary.jpg"
    },
    "Eye of the Phoenix": {
        "category": "Defense",
        "stats": {"Magical Defense": 240, "Max Health": 1200, "Health per 5 seconds": 100},
        "passive": "Boosts HP regen",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/eye-of-the-phoenix.jpg"
    },
    "Overlord’s Platemail": {
        "category": "Defense",
        "stats": {"Max Health": 2000},
        "passive": "Healing item",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/overlords-platemail.jpg"
    },
    "Frostscar’s Embrace": {
        "category": "Defense",
        "stats": {"Physical Attack": 40, "Cooldown Reduction": 0.10, "Max Mana": 500, "Physical Defense": 240, "Max Health": 500},
        "passive": "Basic Attack slows enemies",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/frostscars-embrace.jpg"
    },
    "Blood Rage": {
        "category": "Defense",
        "stats": {"Physical Attack": 40, "Max Health": 1000},
        "passive": "Grants temporary shield and boosts basic attack",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/blood-rage.jpg"
    },
    "Frigid Charge": {
        "category": "Defense",
        "stats": {"Physical Defense": 240, "Max Health": 1000},
        "passive": "Group Crowd Control",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/frigid-charge.jpg"
    },
    # Movement Items
    "Boots of Fortitude": {
        "category": "Movement",
        "stats": {"Physical Defense": 120},
        "passive": "Reduces Physical damage",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/boots-of-fortitude.jpg"
    },
    "Boots of Resistance": {
        "category": "Movement",
        "stats": {"Magical Defense": 120},
        "passive": "Shortens Crowd Control by granting 30% resistance",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/boots-of-resistance.jpg"
    },
    "Boots of Tranquility": {
        "category": "Movement",
        "stats": {"Cooldown Reduction": 0.15},
        "passive": "Speeds Skills cooldown reduction",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/boots-of-tranquility.jpg"
    },
    "Boots of the Arcane": {
        "category": "Movement",
        "stats": {"Mana/5 seconds": 25},
        "passive": "Magical Pierce",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/boots-of-the-arcane.jpg"
    },
    "Boots of Dexterity": {
        "category": "Movement",
        "stats": {"Attack Speed": 0.20},
        "passive": "Boosts Attack Speed",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/boots-of-dexterity.jpg"
    },
    "Boots of Deftness": {
        "category": "Movement",
        "stats": {"Max Health": 300},
        "passive": "Grants Movement Speed",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/boots-of-deftness.jpg"
    },
    # Jungling Items
    "Runeblade": {
        "category": "Jungling",
        "stats": {"Magical Attack": 150, "Cooldown Reduction": 0.05, "Movement Speed": 0.07},
        "passive": "Killing monsters boosts Magical Attack",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/runeblade.jpg"
    },
    "Rapacious Bite": {
        "category": "Jungling",
        "stats": {"Physical Attack": 90, "Cooldown Reduction": 0.05, "Movement Speed": 0.08},
        "passive": "Killing monster boosts attack",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/rapacious-bite.jpg"
    },
    "Giant’s Grip": {
        "category": "Jungling",
        "stats": {"Cooldown Reduction": 0.05, "Max Health": 1200, "Movement Speed": 0.06},
        "passive": "Killing monsters boosts HP",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/giants-grip.jpg"
    },
    # Roaming Items
    "Guardian": {
        "category": "Roaming",
        "stats": {"Max Health": 500, "Movement Speed": 0.06},
        "passive": "Grants 32-60 Physical and Magical defense to allies within the range of 800",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/guardian.jpg"
    },
    "Crimson Shadow": {
        "category": "Roaming",
        "stats": {"Max Health": 500, "Movement Speed": 0.06},
        "passive": "Grants 8% Attack Speed and Cooldown Reduction, and 10 Mana every 5 seconds to all allies within the range of 800",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/crimson-shadow.jpg"
    },
    "Stormchaser": {
        "category": "Roaming",
        "stats": {"Max Health": 500, "Movement Speed": 0.06},
        "passive": "Grants 3% Movement Speed and boosts attack stats by 20",
        "image_url": "https://zilliongamer.com/uploads/honor-of-kings/items/128x128/stormchaser.jpg"
    },
    # Tambah item lain jika butuh
}

def get_hero_list():
    heroes = sorted(hero_roles.keys())
    return heroes