import math
import random

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n))): # [2, n)
        if n % i == 0:
            return False
    return True

class Paillier:
    def __init__(self):
        self.Key_generation()
    
    def Key_generation(self):
        self.p= 0
        self.q= 0
        
        print("AA")
        i = 0
        while ((math.gcd(self.p*self.q,(self.p-1)*(self.q-1)) != 1) or (self.p==self.q)):
            pq = [0,0]
            for pq_index in range(2):
                while (not isPrime(pq[pq_index])):
                    pq[pq_index] = random.randint(0, 2 ** 16)
                    print(pq)
            self.p, self.q = pq
            
            i += 1
            if i > 100:
                self.p,self.q = [13,17]
        print("p,q:",self.p,",",self.q)
        
        
        
        self.n = self.p*self.q;
        self.phi = (self.p-1)*(self.q-1);
        
        print("n,phi:",self.n,",",self.phi)
        
        
        # self.g = random.randint(0, self.n*self.n)
        # self.lmbda = math.lcm(self.p-1, self.q-1)
        # self.mu = pow(lx(pow(self.g, self.lmbda, self.n*self.n)), -1, self.n)
        # print("g,lambda,mu:",self.g,",",self.lmbda,",",self.mu)
        
        
        self.g = self.n + 1
        self.lmbda = self.phi
        self.mu = pow(self.lmbda, -1, self.n)
        print("g,lambda,mu:",self.g,",",self.lmbda,",",self.mu)
        
    def L(self, x):
        return (x - 1) / self.n
        
    def check_r(self, r):
        return math.gcd(r,self.n) == 1
        
    def get_all_r(self):
        return [r for r in range(self.n) if self.check_r(r)]
        
    def encrypt(self, m, r = None):
        if r is None:
            r = random.choice(self.get_all_r())
        return ( pow(self.g, m, self.n*self.n) * pow(r, self.n, self.n*self.n) ) % (self.n*self.n)
        
    def decrypt(self, c):
        return ( self.L(pow(c, self.lmbda, self.n*self.n)) * self.mu ) % self.n


if __name__ == "__main__":
    paillier = Paillier()
    
    
    for m in range(1000):
        c = paillier.encrypt(m)
        C = paillier.decrypt(c)
        
        print("c,m,C:",f'{c:10}',",",f'{m:6}',",",f'{C:6}')
    



















def Hamming_Weight(x):
    return sum([int(i) for i in str(bin(x)).replace("0b","")])

def Threshold(d,s,x):
    assert(d<=s+1)
    return Hamming_Weight(x) >= d