#include <iostream>
#include <vector>
#include <numeric>
#include <iomanip>
#include <omp.h>
#include <unistd.h>
#include <math.h>

using namespace std;


class Ciphertexts {
protected:
    int q = 1024;
    int t = 264;
    int Delta;
    int e = 0; // ?

public:
    Ciphertexts(){
        if (t > q) {cout << "ERROR, t > q: " << t << " > " << q << endl;}
        Delta = round(double(q) / double(t));
    }
};

class LWE : public Ciphertexts{
protected:
    int n = 5;
    int *a, *s, b;
public:
    LWE() {
        a = new int[n];
        s = new int[n];
        for (int i = 0; i < n; i++){ 
            a[i] = rand() % q;
            s[i] = rand();
        }
    }
    vector<int> encrypt(int m) {
        int b = Delta * m + e;
        for (int i = 0; i < n; i++){ b += a[i] * s[i]; }
        
        vector<int> c(n+1, 0);
        
        for (int i = 0; i < n; i++){ c.at(i) = a[i]; }
        c.at(n) = b;
        return c;
    };
    
    vector<int> Homomorphic_NOT(vector<int> c_in) {
        vector<int> c(n+1, 0);
        for (int i = 0; i < n; i++){ c.at(i) = 0 - c_in.at(i); }
        c.at(n) = Delta - c_in.at(n);
        return c;
    };
};




int main()
{
    LWE lwe1;
    
    vector<int> c = lwe1.encrypt(0);
    
    for (int i = 0; i < int(c.size()); i++){ 
        cout << c.at(i) << ", ";
    } cout << endl;
    
    
    c = lwe1.Homomorphic_NOT(c);
    
    for (int i = 0; i < int(c.size()); i++){ 
        cout << c.at(i) << ", ";
    } cout << endl;
    
    
    return 0;
}

