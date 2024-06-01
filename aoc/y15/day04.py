from hashlib import md5

hash_input = 'yzbqklnj'

number = 0
found = False

hasher = md5()
while not found:
    output = md5(f'{hash_input}{number}'.encode())
    hex_digest = output.hexdigest()
    if hex_digest.startswith('00000'):
        print(f'{number} produced {hex_digest}')
        break

    number += 1
