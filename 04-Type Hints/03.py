from typing import List

def convert_to_upper (names:List[str]) -> List[str]:
    return [n.upper() for n in names]


print(convert_to_upper(['ahmed', 'ali', 'hassan']))