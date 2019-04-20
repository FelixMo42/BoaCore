from Tool import Tool, Variable, Function, Alert
import binascii

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def powermod(p,q,n):
    size = len(str(q)) * 4
    q_powers = []
    base_q = q
    for i in range(size):
        if base_q % 2 == 1:
            q_powers.append(1)
            base_q = (base_q -1)/2
        else:
            q_powers.append(0)
            base_q = base_q / 2
    mods = [p % n]
    for i in range(1 , size):
        mods.append((mods[i - 1]) ** 2 % n)
    multiplyers = 1
    for i in range(size):
        if q_powers[i] == 1:
            multiplyers = multiplyers * mods[i] % n
    return multiplyers

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    (g, x, y) = egcd(a, m)
    if g != 1:
        Alert('modular inverse does not exist')
    else:
        return x % m

def nthRoot(i,n):
	return i ** (1.0 / n)

def textify(m):
	return binascii.unhexlify( hex(int(m))[2:] )

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

class Main(Tool):
	title = "RSA"
	p = Variable()
	q = Variable()

	@Function
	def go(self):
		pass
	
'''	title = "RSA"

	p = Var("n")
	q = Var("n")
	n = Var("n")
	t = Var("n")
	e = Var("n")
	d = Var("n")

	cipher = Var("n")
	cipher_text = Var("s")

	message = Var("n")
	message_text = Var("s")

	def main(self):
		text = ""

		while True:
			if self.p and self.q and not self.n:
				self.n = self.p * self.q
			elif self.p and self.n and not self.q:
				self.q = self.n / self.p
			elif self.q and self.n and not self.p:
				self.p = self.n / self.q
			elif self.p and self.q and not self.t:
				self.t = lcm(self.p - 1, self.q - 1)
			elif self.e and self.n and not self.d:
				self.d = modinv(self.e, self.n)
			elif self.message and self.e and self.n and not self.cipher:
				self.cipher = powermod(self.message, self.e, self.n)
			elif self.cipher and self.d and self.n and not self.message:
				self.message = powermod(self.cipher, self.d, self.n)
			elif self.cipher and self.d and self.n and not self.message and (powermod(nthRoot(self.cipher, self.d), self.d, self.n) == self.cipher):
				self.message = nthRoot(self.cipher, self.d)
			elif self.cipher and not self.cipher_text:
				self.cipher_text = textify(self.cipher)
			elif self.message and not self.message_text:
				self.message_text = textify(self.message)
			else:
				break

		text += "p = %s\n" % self.p
		text += "q = %s\n" % self.q
		text += "n = %s\n" % self.n
		text += "t = %s\n" % self.t
		text += "e = %s\n" % self.e
		text += "d = %s\n" % self.d

		text += "cipher = %s\n" % self.cipher
		text += "message = %s\n" % self.message
		text += "cipher text = %s\n" % self.cipher_text
		text += "message text = %s\n" % self.message_text

		return text'''

if __name__ == "__main__":
	Main()