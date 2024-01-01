from PIL import Image

path = 'test.png'
img = Image.open( path )

def decode(img):
    res = ''
    temp = 0
    index = 0
    C, R = img.size
    for r in range(R):
        for c in range(C):
            red, _, __ = img.getpixel( (c,r) ) # reversed coor
            index += 1
            temp <<= 1
            temp += red & 0b00000001
            if index == 8: # eval each byte/8-bit-group
                index = 0
                res += chr(temp)
                if temp == 0: # \x00 byte : 0 in all l-shifted slots
                    return res
                temp = 0
    assert False
    return None
res = decode(img)
print(res)

assert res.endswith(f'cake.{chr(0)}')

