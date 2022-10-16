def mutate_string(string, position, character):
    k = list(string)
    #print(k)
    #del k[position]
    k[position] = character
    #k.insert(character,position)
    k = "".join(k)
    return k

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)