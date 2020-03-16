#include <iostream>
using namespace std;

#ifndef __mystring__
#define __mystring__
class mystring
{
public:
	mystring(const char* cstr = 0);
	//拷贝构造函数
	mystring(const mystring& str);
	//拷贝赋值函数, 本来有指针可以考虑return by reference
	mystring& operator=(const mystring& str);
	//析构函数
	~mystring();
	//需要一个公有函数能够访问私有函数成员指针便于输出
	//因为不需要修改调用成员， 因此在前面加上限定
	char* get_c_str() const { return m_data; }

	friend ostream& operator<<(ostream& os, const mystring& str);
private:
	char* m_data;
};

//默认参数在外部定义时不加默认参数
mystring::mystring(const char* cstr)
{
	//需要判断是否有参数
	if (cstr) {
		//字符串长度+结束符占1位, 给m_data分配空间
		m_data = new char[strlen(cstr) + 1];
		//复制
		strcpy(m_data, cstr);
	}
	else {
		//传入字符串为NULL，需要把字符串设为空， 最后需要结束符；
		m_data = new char[1];
		*m_data = '\0';
	}
}
//因为析构函数很简单， 所以要求编译器一定要做成内联函数
inline mystring::~mystring()
{
	delete[] m_data;
	//释放指针指向的内存空间;
}

inline mystring::mystring(const mystring& str)
{
	//同一对象成员互为友元函数
	m_data = new char[strlen(str.m_data)+1];
	strcpy(m_data, str.m_data);
}

//拷贝赋值函数
mystring& mystring::operator=(const mystring& str)  //这个叫reference 
{
	//因为会先删掉自己的内存所以需要做是是否自我复制的检测
	//比较地址  &str 叫取地址
	//放在类型后的叫reference , 放在类型前的叫做取地址
	if (this != &str) {
		delete[] m_data;
		m_data = new char[strlen(str.m_data) + 1];
		strcpy(m_data, str.m_data);
	}
	//传出去的东西不管接受是否为by reference 还是 By value 
	return *this;
}
ostream& operator<<(ostream& os, const mystring& str)
{
	os << str.get_c_str();
	return os;
}

#endif

