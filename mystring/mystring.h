#include <iostream>
using namespace std;

#ifndef __mystring__
#define __mystring__
class mystring
{
public:
	mystring(const char* cstr = 0);
	//�������캯��
	mystring(const mystring& str);
	//������ֵ����, ������ָ����Կ���return by reference
	mystring& operator=(const mystring& str);
	//��������
	~mystring();
	//��Ҫһ�����к����ܹ�����˽�к�����Աָ��������
	//��Ϊ����Ҫ�޸ĵ��ó�Ա�� �����ǰ������޶�
	char* get_c_str() const { return m_data; }

	friend ostream& operator<<(ostream& os, const mystring& str);
private:
	char* m_data;
};

//Ĭ�ϲ������ⲿ����ʱ����Ĭ�ϲ���
mystring::mystring(const char* cstr)
{
	//��Ҫ�ж��Ƿ��в���
	if (cstr) {
		//�ַ�������+������ռ1λ, ��m_data����ռ�
		m_data = new char[strlen(cstr) + 1];
		//����
		strcpy(m_data, cstr);
	}
	else {
		//�����ַ���ΪNULL����Ҫ���ַ�����Ϊ�գ� �����Ҫ��������
		m_data = new char[1];
		*m_data = '\0';
	}
}
//��Ϊ���������ܼ򵥣� ����Ҫ�������һ��Ҫ������������
inline mystring::~mystring()
{
	delete[] m_data;
	//�ͷ�ָ��ָ����ڴ�ռ�;
}

inline mystring::mystring(const mystring& str)
{
	//ͬһ�����Ա��Ϊ��Ԫ����
	m_data = new char[strlen(str.m_data)+1];
	strcpy(m_data, str.m_data);
}

//������ֵ����
mystring& mystring::operator=(const mystring& str)  //�����reference 
{
	//��Ϊ����ɾ���Լ����ڴ�������Ҫ�����Ƿ����Ҹ��Ƶļ��
	//�Ƚϵ�ַ  &str ��ȡ��ַ
	//�������ͺ�Ľ�reference , ��������ǰ�Ľ���ȡ��ַ
	if (this != &str) {
		delete[] m_data;
		m_data = new char[strlen(str.m_data) + 1];
		strcpy(m_data, str.m_data);
	}
	//����ȥ�Ķ������ܽ����Ƿ�Ϊby reference ���� By value 
	return *this;
}
ostream& operator<<(ostream& os, const mystring& str)
{
	os << str.get_c_str();
	return os;
}

#endif

