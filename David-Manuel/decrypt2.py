codedText = """
vhr gajdzi mcsx dclfs ql vob qhlrbo! pg hnts nr uqog uc dcl qce. pg wvjz ahh qg vohav qlhp rqu jfsh zs ebnl uyjy iccgf a ochnhf xecn nlr u fccine fcbcrf ahhtjyfy hbobperpg.

qkwtx yavrwhj, mwn eaa psug hpbu pbca vb umkcrq bs hhfdtn braoovs, exnl, vr wm usieny nusmram.

xn drqrcfviwq

jr qicv zm mépébecir, - os dxwf, - y'gbwrbahné,
lr nfcqqm w'cqhghulbm à ec tbsf uectbg :
mn qsoos mmqiyc smw awkve, - rr aiq zcmj cblgnhzté
iqrgc zy vctxkl amwl gs tt oélnlqiowm.

wcnf jo hxwb ww tbkpydi, bhk qhg a'uv qwguoyé,
pshgg-uhk lr noovwtbrpr ch fd amk f'igyzch,
zi ynehp eol dttksngh ndbb à fqn pmsou réahné,
eg jo nusqene bù js jdaxkg à ln pcmh g'ienir.

qicv-xm toohp co svéjnu ?... lhqwaqov hw bvpch ?
pcv ytoar smw fwnie rlqiu rc ucifcf xh zi kgiac ;
x'ul fêdé wcnf jo aucbmg où ayuy oo abtènr...

ch d'dw lxwx smwm yoqgsursf nuodxtsé y'yqbéucv :
fqdhjohw hwnt à tbsf mxf tt nyec r'iudpéx
nef qcoswzl fe yy gulbbx gt ycg wuwa wg ln dés."""

key = 'canyoudoit'

def isLetter( char ):
    return char >= 'a' and char <= 'z'
        
def keySequenceForText( cryptedText, key ):
    keyIndex = 0
    for char in cryptedText:
        if isLetter(char):
            yield key[keyIndex]
            keyIndex = (keyIndex + 1) % len( key )
        else:
            yield ' '
        
def translateChar( input ):
    ( char, key ) = input
    if isLetter(char):
        offset = ord( key ) - ord('a')
        return chr(((ord(char) - ord('a') - offset) % 26) + ord('a'))
        
    return char
    
import codecs
print ''.join( map( translateChar, zip( codedText, keySequenceForText( codedText, key ) ) ) ).decode('utf-8')
