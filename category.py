CATEGORY_MAP = {
    "☀️ Solar": ["solar", "renewable", "vikram solar", "waaree", "premier energies"],
    "🛡️ Defence": ["defence", "defense", "bel", "bdl", "hal", "drdo", "missile"],
    "🏦 Banking": ["bank", "rbi", "sbi", "hdfc", "icici"],
    "💻 IT": ["software", "technology", "ai", "tcs", "infosys", "wipro"],
    "🚢 Shipping": ["shipping", "port", "cargo", "logistics"],
}

def get_category(title):
    title = title.lower()

    for category, words in CATEGORY_MAP.items():
        if any(word in title for word in words):
            return category

    return "📈 Market"
