colors = (
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
)


def value(color):
    return colors.index(color)


def label(colors):
    d1, d2, e = [value(colors[i]) for i in range(3)]
    r = (10 * d1 + d2) * 10**e
    if r <= 1000:
        return f"{r} ohms"
    elif r <= 1000000:
        return f"{r//1000} kiloohms"
    elif r <= 1000000000:
        return f"{r//1000000} megaohms"
    else:
        return f"{r//1000000000} gigaohms"
