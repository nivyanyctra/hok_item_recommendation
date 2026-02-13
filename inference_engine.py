# inference_engine.py: Mesin Inferensi (Forward Chaining Kompleks)

from knowledge_base import hero_roles, physical_roles, role_base_items, counter_items, rules, item_details

def calculate_total_stats(full_build):
    total = {"Physical Attack": 0, "Magical Attack": 0, "Max Health": 0, "Cooldown Reduction": 0.0, "Attack Speed": 0.0, "Critical Rate": 0.0, "Movement Speed": 0.0, "Physical Defense": 0, "Magical Defense": 0, "Physical Lifesteal": 0.0, "Magical Lifesteal": 0.0, "Health per second": 0, "Mana/5 seconds": 0, "Max Mana": 0}
    for item in full_build:
        if item in item_details:
            for stat, value in item_details[item]["stats"].items():
                total[stat] += value
    return total

def forward_chaining(enemy_heroes, my_hero):
    # Normalisasi input
    my_hero = my_hero.strip().title().replace(" ", "")
    enemy_heroes = [e.strip().title().replace(" ", "") for e in enemy_heroes if e]
    enemy_roles = [hero_roles.get(e, "Unknown") for e in enemy_heroes]

    # Hitung counts (fakta awal)
    counts = {"phys": 0, "magic": 0, "tank": 0, "support": 0}
    for role in enemy_roles:
        if role in physical_roles:
            counts["phys"] += 1
        elif role == "Mage":
            counts["magic"] += 1
        elif role == "Tank":
            counts["tank"] += 1
        elif role == "Support":
            counts["support"] += 1

    # Apply rules (forward chaining)
    needs = []
    explanations = []
    for rule in rules:
        if rule["cond"](counts):
            needs.append(rule["need"])
            explanations.append(rule["exp"])

    # Dapatkan counter items
    rec_items = []
    for need in needs:
        rec_items.extend(counter_items.get(need, [])[:2])  # Top 2 per need

    # Base items berdasarkan role hero kamu
    my_role = hero_roles.get(my_hero, "Unknown")
    base_items = role_base_items.get(my_role, [])

    # Full build: Unique, max 6 items
    full_build = list(set(base_items + rec_items))[:6]

    # Hitung total stats
    total_stats = calculate_total_stats(full_build)

    # Score effectiveness (sederhana: poin berdasarkan match)
    score = 0
    if counts["phys"] >= 3:
        score += total_stats["Physical Defense"] / 100
    if counts["magic"] >= 2:
        score += total_stats["Magical Defense"] / 100
    # dst.

    # Details untuk setiap item di build
    build_details = [item_details.get(item, {"category": "Unknown", "stats": {}, "passive": "No info", "image_url": ""}) for item in full_build]

    # Trace untuk explanation facility
    trace = f"Fakta Awal: Counts = {counts}\nRoles Musuh: {enemy_roles}\nRules Terpicu: {', '.join(explanations) or 'Tidak ada'}\nTotal Stats: {total_stats}\nEffectiveness Score: {score:.2f}"

    return {
        "my_role": my_role,
        "full_build": full_build,
        "build_details": build_details,
        "total_stats": total_stats,
        "explanations": explanations,
        "trace": trace
    }