codedText = """
ny xjjrx ymfy tzw nshwjingqj jshwduynts fqltwnymr mfx gjjs htruwtrnxji. kwtr stb, bj bnqq zxj fs jshwduynts pjd.
        yt ijhdumjw tzw htrrzsnhfyntsx:
        1 - hqjfs ymj pjd gd wjrtansl jajwd wjizsifsy qjyyjw.
        2 - rfu ymj pjd yt ymj knwxy qjyyjw tk ymj fqumfgjy.
        3 - htruqjyj ymj yfgqj bnym ymj wjxy tk ymj fqumfgjy xyfwynsl kwtr ymj qfxy qjyyjw tk ymj pjd.



        jcfruqj bnym ifxmqfsj fx ymj pjd

        fghijklmnopqrstuvwxyzabcde
        ifxmqsjklnopqrtuvwyzabcdeg

hzwwjsyqd, bj fwj zxnsl kjfwnrufqf fx pjd
zxj ny yt ijhwduy dkbqnegjnkh. ymnx nx ymj ufxxbtwi yt fhhjxx tzw gfyyqj uqfs bnym ymj ktqqtbnsl ktwr.
"""

def translateChar( input ):
    if input >= 'a' and input <= 'z':
        return chr(((ord(input) - ord('a') - 5) % 26) + ord('a'))
        
    return input
    
print ''.join( map( translateChar, codedText ) )
