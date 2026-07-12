HIGH_IMPACT = [
    # Corporate
    "order",
    "contract",
    "deal",
    "agreement",
    "approval",
    "government",
    "ministry",
    "tender",
    "acquisition",
    "merger",

    # Market
    "results",
    "bonus",
    "split",
    "dividend",

    # IPO
    "ipo",
    "gmp",
    "listing",
    "subscription",
    "anchor",

    # Global
    "iran",
    "israel",
    "oil",
    "crude",
    "gold",
    "fed",
    "federal reserve",
    "china",
    "tariff",

    # Sectors
    "solar",
    "defence",
    "defense",
    "missile",
    "army",
    "navy",

    # Companies
    "bel",
    "bdl",
    "hal",
    "mazagon",
    "cochin shipyard",
    "aequs",
    "vikram solar"
]

def is_high_impact(title):
    title = title.lower()
    return any(word in title for word in HIGH_IMPACT)
