import sys
import re

define_regex = re.compile("(\[[^\]]+\]) +(@[A-Za-z0-9\.]+@)")
flag_replace_regex = re.compile("((\[[^\]]+\]) ?)+")

macro_map = {}
is_defining_macros = False
for line in sys.stdin.readlines():
    line = line.strip("\n")
    if line.startswith("Define_Flags"):
        is_defining_macros = True
        continue
    elif is_defining_macros:
        if not line.strip("\n "):
            continue
        elif line.startswith("End Define_Flags"):
            is_defining_macros = False
            continue
        try:
            k, v = re.match(define_regex, line.strip("\n")).groups()
        except Exception as e:
            print(f"Couldn't understand macro definition: {line}")
            raise e
        macro_map[k] = v
        continue
    elif line.startswith("multichar_symbols"):
        print(line)
        for fd in set(macro_map.values()):
            print(fd)
    else:
        found_flag = re.search(flag_replace_regex, line)
        if found_flag:
            macros = found_flag.groups()
            real_flags = "".join([macro_map[macro] for macro in set(macros)])
            if ":" not in line:
                line = f"{real_flags}:{real_flags}{line}".replace("#", " #")
            else:
                line = real_flags + line.replace(":", f":{real_flags}")
            print(line)
        else:
            print(line)

