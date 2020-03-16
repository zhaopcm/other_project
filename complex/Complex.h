#pragma once

class Complex {
public:
	Complex(double r = 0, double i = 0)
		:re(r), im(i){}

	//�����н��в��������أ� �������ߵ���ʽֻ��Ҫд���������ʽ
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
	//��Ԫ����Ե��÷������˽�г�Ա
	ths->re += r.re;
	ths->im += r.im;
	//����������֪���������Ƿ�by reference�ķ�ʽ����
	return *ths;
}