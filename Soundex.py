def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters


def add_soundex_code(soundex, char, prev_code):
    code = get_soundex_code(char)
    if code != '0' and code != prev_code and len(soundex) < 4:
        soundex += code
        prev_code = code
    return soundex, prev_code


def update_soundex(soundex, name, prev_code):
    for char in name[1:]:
        soundex, prev_code = add_soundex_code(soundex, char, prev_code)
    return soundex.ljust(4, '0')


def generate_soundex(name):
    if not name:
        return ""
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    return update_soundex(soundex, name, prev_code)
