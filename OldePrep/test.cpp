#include <iostream>
#include <vector>
#include <numeric>
#include <iomanip>
#include <omp.h>
#include <unistd.h>
#include <unistd.h>


#define IMGUI_IMPLEMENTATION
#include "C/imgui/misc/single_file/imgui_single_file.h"


using namespace std;

const int SQRT_INT = 215;



template<typename tem_type> bool isPrime(tem_type n){
    // Corner case
    if (n <= 1)
        return false;
 
    // Check from 2 to n-1
    for (tem_type i = 2; i <= n / 2; i++)
        if (n % i == 0)
            return false;
 
    return true;
}

template<typename tem_type, typename tem_type2> tem_type pow_mod(tem_type a, tem_type2 b, tem_type n){
    // cout << "print(pow(" << a << ", " << b << ", " << n << "), " << "pow(" << a << ", " << b << ", " << n << ") == ";
    
    tem_type output;
    if (b == -1) { // https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
        for (tem_type X = 1; X < n; X++) {
            if (((a % n) * (X % n)) % n == 1) {
                output = X;
                break;
            }
        }
    } else {
        long long x=1, y=a; 
        while (b > 0) {
            if (b%2 == 1) {
                x = (x*y) % n; // multiplying with base
            }
            y = (y*y) % n; // squaring the base
            b /= 2;
        }
        output = x % n;
    }

    // cout << output << ", " << output << ")" << endl;
    return output;
}



template<typename tem_type> class Paillier{
public:
    Paillier() {Key_generation();}
    
    tem_type p, q;
    tem_type n, phi;
    tem_type g, lambda, mu;
    
    //vector<tem_type> R;
    void Key_generation() {
        p=0;q=0;
        // p=13;q=17;
        while ((gcd(p*q,(p-1)*(q-1)) != 1) or (p==q)){
            for (int index_pq = 0; index_pq <= 1; index_pq++){ 
                tem_type* ptr_pq = index_pq ? &q : &p;
                while (!isPrime(*ptr_pq)) {
                    *ptr_pq = rand() % (1 << 8);
                    //cout << "index: " << index_pq << ", non-prime: " << *ptr_pq << endl;
                }
            }
        };
        cout << "p,q: " << p << "," << q << endl;
        
        
        // ## parallel vinden
        // int p=0, q=0;
        // bool zoeken = true;
        // while (zoeken){
            // #pragma omp parallel
            // {
                // int p_=0, q_=0;
                // for (int index_pq = 0; index_pq <= 1; index_pq++){ 
                    // int* ptr_pq = index_pq ? &q_ : &p_;
                    // while (!isPrime(*ptr_pq)) {
                        // *ptr_pq = rand() ;//% SQRT_INT;
                    // }
                // }
                
                // if ((gcd(p_*q_,(p_-1)*(q_-1)) == 1) and (p_!=q_)){
                    // zoeken = false;
                    // p = p_; q = q_;
                    // cout << "p, q: " << p_ << ", " << q_ << " Was WEL correct" << endl;
                // } else {
                    // cout << "p, q: " << p_ << ", " << q_ << " Was NIE correct" << endl;
                // }
            // }
        // }
        
        
        n = p*q;
        phi = (p-1)*(q-1);
        cout << "n,phi: " << n << "," << phi << endl;
        
        
        // g = rand() % (n*n);
        // lambda = lcm(p-1, q-1);
        // mu = pow_mod(L(pow_mod(g, lambda, n*n)), -1, n);
        // cout << "g,lambda,mu: " << g << ", " << lambda << "," << mu << endl;
        
        
        g = n+1;
        lambda = phi * 1;
        mu = pow_mod(lambda, -1, n);
        cout << "g,lambda,mu: " << g << ", " << lambda << "," << mu << endl << endl;;
        
        
        // for (tem_type possible_r=0;possible_r < n; possible_r++){
            // if (check_r(possible_r)) {R.push_back(possible_r);} 
            // //else {cout << "Niet in R: " << possible_r << "   " << (possible_r % p ==0 or possible_r % q == 0) << endl;}
        // }
    }
    tem_type L(tem_type x){
        // cout << ((float) (x-1)) / ((float) n) << endl;;
        return (x - 1) / n;}
        
    bool check_r(tem_type r){return gcd(r,n) == 1;}
    
    // vector<tem_type> get_all_r(){
        // return R;
    // }
    
    tem_type encrypt(tem_type m){
        tem_type r = 0;
        while (r % p ==0 or r % q == 0) {r = rand() % n;}
        return encrypt(m,r);
    }
    
    tem_type encrypt(tem_type m, tem_type r){
        return (pow_mod(g,m,n*n) * pow_mod(r,n,n*n)) % (n*n);
    }
    tem_type decrypt(tem_type c){
        return (L(pow_mod(c,lambda,n*n)) * mu) % n;
    }
};


int main()
{    
    cout << IMGUI_CHECKVERSION() << endl;
    ImGui::ShowDemoWindow();
    

    return 0;

    Paillier<long> paillier;
    
    
    // int m = 54;
    for (int m = 0; m < (1 << 13); m++) {
        int c, C;
        
        c = paillier.encrypt(m);
        C = paillier.decrypt(c);
        
        if (m != C)
            cout << "c,m: " << setw(16) << c << ", " << setw(16) << m << setw(16) << C << endl;
        
    }
    return 0;
}




























class Yarne1_Paillier {
public:
    int message;
    int key;
    
    
    Yarne1_Paillier(int _message, int _key) {
        message = _message;
        key = _key;
    }
    
    Yarne1_Paillier(int _message) {Yarne1_Paillier(_message, rand());}
    Yarne1_Paillier() {Yarne1_Paillier(0);}
    
    
    int encrypt();
    
    
    void print_info() {
        std::cout << "message: " << message << ", Secret-code: " << key << std::endl ;
    }
};


int Yarne1_Paillier::encrypt() {
    return 0;
}





// int main()
// {
    // Yarne1_Paillier yarne1_Paillier(2024, 100);
    
    // yarne1_Paillier.print_info();
    
    // std::cout << "Encrypted: " << yarne1_Paillier.encrypt() << endl;
    
    // int i = 0;
    // return 0;
// }


