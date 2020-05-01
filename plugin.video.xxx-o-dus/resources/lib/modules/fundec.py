# Credits Mortael For This Function

def decryptHash(videoUrl, licenseCode, hashRange):
    result = ''
    videoUrlPart = videoUrl.split('/')
    hash = videoUrlPart[7][:2*int(hashRange)]
    nonConvertHash = videoUrlPart[7][2*int(hashRange):]
    seed = calcSeed(licenseCode, hashRange)
    if (seed != '' and hash !=''):
        for k in range(len(hash)-1, -1, -1):
            l = k
            for m in range(k,len(hash)):
                l += int(seed[m])
            l = l % len(hash)
            n = ''
            for o in range(0, len(hash)):
                n = n + hash[l] if o == k else n + hash[k] if o == l else n + hash[o]
            hash = n
        videoUrlPart[7] = hash + nonConvertHash
        videoUrlPart.pop(0)
        videoUrlPart.pop(0)        
        result = '/'.join(videoUrlPart)   
    return result        


def calcSeed(licenseCode, hashRange):
    f = licenseCode.replace('$', '').replace('0', '1')
    j = int(len(f) / 2)
    k = int(f[:len(f)-j])
    l = int(f[j:])
    g = abs(l - k)
    fi = 4*g
    i = int(int(hashRange) / 2 + 2)
    m = ''
    for g2 in range (0,j+1):
        for h in range (1,5):
            n =  int(licenseCode[g2 + h]) + int(str(fi)[g2])
            if n>=i:
                n -= i	
            m = m + str(n)
    return m