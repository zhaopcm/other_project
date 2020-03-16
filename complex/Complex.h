#pragma once

class Complex {
public:
	Complex(double r = 0, double i = 0)
		:re(r), im(i){}

	//再类中进行操作符重载， 左右两边的形式只需要写出后面的形式
	Complex& operator += (const Complex&);
	double real() const { return this->re; }
	double imag() const { return this->im; }
private:
	double re;
	double im;
	friend Complex& _doap1(Complex*, const Complex&);
};

inline Complex& Complex::operator += (const Complex& r) 
{
	return _doap1(this, r);
}

Complex& _doap1(Complex* ths, const Complex& r) 
{
	//友元捏可以调用访问类的私有成员
	ths->re += r.re;
	ths->im += r.im;
	//传递着无需知道接受者是否by reference的方式接受
	return *ths;
}