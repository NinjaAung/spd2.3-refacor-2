# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):

    if not line:
        return None
    else:
        if 'debug' in line or 'error' in line:
            return None
        else:
            if 'x:' in line:
                pos = None
                start_index = line.find('x:') + 2
                try:
                    pos = float(line[start_index:])
                except ValueError:
                    print("ValueError: Not a valid pos value")
                return pos
            else: 
                return None

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)
