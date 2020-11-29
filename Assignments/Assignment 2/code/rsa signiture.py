
def extended_gcd(a, b):
    x_im2, y_im2 = 1, 0
    x_im1, y_im1 = 0, 1  # initialize x_i-2, x_i-1 and y_i-2, y_i-1
    x_i, y_i = 0, 0  # initialize x_i, y_i
    while True:
        r = a % b  # remainder
        q = a // b  # quotient
        if r == 0:
            if b != 1:
                return None  # not solvable
            return x_i, y_i
        x_i = x_im2 - q * x_im1
        y_i = y_im2 - q * y_im1
        x_im2 = x_im1; y_im2 = y_im1
        x_im1 = x_i; y_im1 = y_i  # update x_i-2, x_i-1 and y_i-2, y_i-1
        a = b; b = r  # update a and b

def inverse_modulo(a, n):
    if extended_gcd(a, n):
        x, y = extended_gcd(a, n)
        return x % n
    return None  # not solvable

def fast_expo_mod(a, b, n):
    # fast calculation of a ^ b % n
    mod = 1  # initialization
    while b > 1:
        if b & 1 == 1:  # take the last digit of b in binary representation
            mod = mod * a % n
        a = a * a % n
        b = b >> 1  # shift 1 bit to the right
    return mod * a % n

def sign(m, d, n):
    return fast_expo_mod(m, d, n)

def verify(s, e, n, m):
    return m == fast_expo_mod(s, e, n)

def blind_sign(m, e, d, n, x):
    m_prime = x ** e * m  # compute m'
    s_prime = sign(m_prime, d, n)  # compute s'
    print(s_prime)
    inverse_x = inverse_modulo(x, n)  # compute inverse modulo of x
    return inverse_x * s_prime % n


m = 3141592657507293
e = 65537
d = 207295768068102279456514335033046425303132165927244033393328116698908705079805377126654354876758366533086185042407386444469697300448993171079415022477995849594447981729168914639729964957529446229650186590220990592254700038562058305
n = 1139631134290681913324518075250462509444792614577115360833700594253534083115108212461164873379591734542309312064780949257819665132832661342154198437454459926525649486600336464897081397167045104842672493488133506984881500857942197501
x = 5072


s = sign(m, d, n)
print(s)
print(verify(s, e, n, m))
print(blind_sign(m, e, d, n, x))

print(pow(pow(x, e)*m, d, n))