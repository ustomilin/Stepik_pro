def to_camel_case(text):
    text = text.replace('-', ' ')
    text = text.replace('_', ' ')
    return ''.join([y if x == 0 else y.capitalize() for x, y in enumerate(text.split())])


print(to_camel_case("the_Stealth_warrior"))
