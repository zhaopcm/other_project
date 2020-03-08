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
	//be successful to login mysql/

	/*	
	char *rsql = "insert into dept(deptno,dname,loc) values(50, 'caiwu', 'beijing')";
	if(mysql_query(mysql, rsql)){
		printf("mysql query err:%s\n", rsql);
		mysql_close(mysql);
		exit(1);
	}
	printf("insert OK!\n");
	*/

	//select 
	if(mysql_query(mysql, "select * from emp")){
		printf("select err");
		mysql_close(mysql);
		exit(1);
	}
	//return the select result
	MYSQL_RES *result;
	MYSQL_ROW row;

	unsigned int num_fields;
	unsigned int i;
	MYSQL_FIELD * fields;

	result = mysql_store_result(mysql);
	num_fields = mysql_num_fields(result);
	fields = mysql_fetch_fields(result);

	for(int i=0; i<num_fields; i++){
		printf("%s\t", fields[i].name);
	}
	printf("\n");
	
	if(result != NULL){
        	while(row=mysql_fetch_row(result)){
			for(i=0; i<num_fields; i++){
				printf("%s\t", row[i]);
			}
			printf("\n");
		}
		mysql_free_result(result);
	}
	mysql_close(mysql);

	printf("exit mysql");
	return 0;
}
