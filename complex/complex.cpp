#include "Complex.h"
#include <iostream>
using namespace std;

ostream& operator<<(ostream& os, const Complex& r) 
{
    return os << '(' << r.real() << ',' << r.imag() <<')' << endl;
}

//以全局的方式操作符重载“+”,需要两个参数
inline Complex operator + (const Complex& x, const Complex& y) 
{
    //构建临时对象， 临时对象会销毁所以不能用by refreace
    return Complex(x.real() + y.real(), x.imag() + y.imag());
}

//函数重载必须signature的部分是不相同的
inline Complex operator + (const Complex& x, double y) 
{
    return Complex(x.real() + y, x.imag());
}

inline Complex operator + (double x, Complex& y)
{
    return Complex(x + y.real(), y.imag());
}


int main()
{
    Complex c1(2, 1);
    Complex c2;
    Complex c3(6, 6);
    cout << c2;
    cout << endl;
    cout << Complex()<< endl;
    cout << c1+c2 << endl;
    c1 += c3;
    cout << c1 << endl;
    cout << c1 + 7 << c2 + 7 << endl;
    return 0;    
}

