def int32_to_ip(int32):
    ip: str = ''
    for i in range(3,0,-1):
        octet = int( int32 / (256**i) )
        ip += str(octet) + '.'
        int32 -= octet*(256**i)
    ip += str(int32)
    return( ip )

