HIGH_IMPACT = [
    "order",
    "contract",
    "approval",
    "wins",
    "bagged",
    "deal",
    "agreement",
    "mou",
    "export",
    "government",
    "ministry",
    "tender",
    "defence",
    "solar",
    "ipo",
    "gmp",
    "listing",
    "results",
    "bonus",
    "split",
    "dividend"
]

def is_high_impact(title):
    title = title.lower()
    return any(word in title for word in HIGH_IMPACT)
