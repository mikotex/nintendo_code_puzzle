def get_keys_from_value(d, val):
    keys = list(d.keys())
    vals = list(d.values())

    pos = vals.index(val)
    return keys[pos]

def decode(str):
    dict = {
        "a":"iI",
        "b":"Iiii",
        "c":"IiIi",
        "d":"Iii",
        "e":"i",
        "f":"iiIi",
        "g":"IIi",
        "h":"iiii",
        "i":"ii",
        "j":"iIII",
        "k":"IiI",
        "l":"iIii",
        "m":"II",
        "n":"Ii",
        "o":"III",
        "p":"iIIi",
        "q":"IIiI",
        "r":"iIi",
        "s":"iii",
        "t":"I",
        "u":"iiI",
        "v":"iiiI",
        "w":"iII",
        "x":"IiiI",
        "y":"IiII",
        "z":"IIii",
    }
    return get_keys_from_value(dict, str)

def decode_morse(str):
    words = str.split()
    ans = ''
    for i in words:
        ans += decode(i)
    return ans


