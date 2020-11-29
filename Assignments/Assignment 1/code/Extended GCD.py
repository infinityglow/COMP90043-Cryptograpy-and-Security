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

print(inverse_modulo(13, 20))
