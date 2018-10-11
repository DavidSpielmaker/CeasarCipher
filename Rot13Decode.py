ciphertext = input("Ciphertext: ").replace(' ', '').lower()
rotation = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rot_gen(alphabet, rotation, ciphertext):
    rot_alphabet = []
    counter = 0
    solve = []

    while counter < len(alphabet):
        rot_alphabet.append(alphabet[(counter + rotation) % len(alphabet)])
        counter = counter + 1

    for x in ciphertext:
        alpha_location = alphabet.index(x)
        solve.append(rot_alphabet[alpha_location])

    print('\n')
    print("[+] Rotation: " + str(rotation))
    print("[+] Alphabet: " + " ".join(alphabet))
    print("[+] Rotation: " + " ".join(rot_alphabet))
    print("[+] Ciphertext: " + ciphertext)
    print("[+] Plaintext: " + " ".join(solve).lstrip())
    print('\n')

while rotation < len(alphabet):
    rot_gen(alphabet, rotation, ciphertext)
    rotation = rotation + 1
