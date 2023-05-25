#include <iostream>
#include <cmath>

int gcd(int a, int h) {
    int temp = 0;
    while (true) {
        temp = a % h;
        if (temp == 0) {
            return h;
        }
        a = h;
        h = temp;
    }
}

int main() {
    int p = 3;
    int q = 7;
    int n = p * q;
    int e = 2;
    int phi = (p - 1) * (q - 1);

    while (e < phi) {
        if (gcd(e, phi) == 1) {
            break;
        } else {
            e = e + 1;
        }
    }

    int k = 2;
    int d = (1 + (k * phi)) / e;

    double msg = 12.0;

    std::cout << "Message data = " << msg << std::endl;

    int c = fmod(pow(msg, e), n);
    std::cout << "Encrypted data = " << c << std::endl;

    int m = fmod(pow(c, d), n);
    std::cout << "Original Message Sent = " << m << std::endl;

    return 0;
}

