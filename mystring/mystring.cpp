#include <iostream>
#include "mystring.h"
using namespace std;

int main()
{
    mystring s1;
    mystring s2("abcde");
    mystring s3 = s2;
    cout << s1 << endl;
    cout << s2 << endl;
    cout << s3 << endl;
}
