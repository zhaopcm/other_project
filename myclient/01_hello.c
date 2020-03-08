#include "mysql.h"
#include "stdio.h"
#include <stdlib.h>

#define _HOST_ "127.0.0.1"
#define _USER_ "root"
#define _PASSWORD_ "123"
#define _DB_ "scott"

int main(){
	MYSQL *mysql = NULL;
	mysql = mysql_init(NULL);

	if(mysql == NULL){
		printf("mysql init err\n");
		exit(1);
	}

	mysql = mysql_real_connect(mysql, _HOST_, _USER_, _PASSWORD_, _DB_, 0, NULL, 0);
	if(mysql ==  NULL) {
		printf("mysql connect err!\n");
		exit(1);
	}

	printf("welcome to mysql!\n");

	mysql_close(mysql);

	printf("exit mysql");
	return 0;
}
