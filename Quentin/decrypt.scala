/* ex1 */

val text1 = """
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

def decrypt1(s:String) = {
    val shift = 'f' - 'a'
    s.map {
        case c if c <= 'z' && (c - shift) >= 'a' => (c - shift).toChar
        case c if c <= 'z' && c >= 'a' => (c - shift + 26).toChar
        case c => c
    }
}
println(decrypt1(text1))

/* ex2 */

val text2 = "yfwlizbeifc"
val pass2 = "fearimpala"

def getMap2(key:String) = {
    val clean = key.distinct
    val targetAlpha = clean ++ (
        ((clean.last+1) to 'z').map(_.toChar) ++ ('a' to (clean.last-1).toChar)
    ).diff(clean)
    val origAlpha = ('a' to 'z')
    targetAlpha.zip(origAlpha).toMap
}

val map2 = getMap2("fearimpala")
val key2 = "yfwlizbeifc".map(map2)
println(key2)

/* ex3 */

val key3 = "canyoudoit"
val text3 = """
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
nef qcoswzl fe yy gulbbx gt ycg wuwa wg ln dés.
"""

def decrypt3(key:String, text:String) = {
    val alpha = ('a' to 'z')
    def infiniteKey(i: Int) = key(i % key.length) - 'a'
    def infiniteAlpha(i: Int) = alpha((i+26) % alpha.length)

    val mappedIndexes = text
        .zipWithIndex
        .filter((x) => x._1 >= 'a' && x._1 <= 'z')
        .zipWithIndex
        .map(x => (x._1._2, x._2))
        .toMap

    text.zipWithIndex.map({
        case (c,i) if c >= 'a' && c <= 'z' => infiniteAlpha((c - 'a') - infiniteKey(mappedIndexes(i)))
        case (c,i) => c
    }).mkString
}
println(decrypt3(key3, text3))
