#include "mysql.h"
#include "stdio.h"
#include <stdlib.h>

#define _HOST_ "127.0.0.1"
#define _USER_ "root"
#define _PASSWORD_ "123"
#define _DB_ "scott"

void showresult(MYSQL_RES* result) {

	MYSQL_ROW row;
	MYSQL_FIELD* fields;

	unsigned int num_fields;
	unsigned int i;

	num_fields = mysql_num_fields(result);
	fields = mysql_fetch_fields(result);

	printf("----------------------------------------------------------------------\n");
	for (int i = 0; i < num_fields; i++) {
		printf("%s\t", fields[i].name);
	}
	printf("\n");
	printf("----------------------------------------------------------------------\n");

	if (result != NULL) {
		while (row = mysql_fetch_row(result)) {
			for (i = 0; i < num_fields; i++) {
				printf("%s\t", row[i]);
			}
			printf("\n");
		}
		mysql_free_result(result);
	}
	printf("----------------------------------------------------------------------\n");
}

MYSQL* login(char* user, char* password)
{
	MYSQL* mysql = NULL;
	mysql = mysql_init(NULL);

	if (mysql == NULL) {
		printf("mysql init err\n");
		return mysql;
	}

	mysql = mysql_real_connect(mysql, _HOST_, user, password, _DB_, 0, NULL, 0);
	if (mysql == NULL) {
		printf("mysql connect err!\n");
		return mysql;
	}
	return mysql;
}

int main(){
	MYSQL *mysql = NULL;

	char user[100];
	char password[100];
	
	printf("user:");
	scanf("%s", user);
	printf("password:");
	scanf("%s", password);
	mysql = login(&user, &password);

	if (mysql == NULL)
	{
		printf("login failed!");
		exit(1);
	}

	MYSQL_RES* result;

	char sql[1000];

	while (1) {
		printf("MYSQL>");
		memset(&sql, '\n', sizeof(sql));
		fgets(sql, sizeof(sql), stdin);
		if (strncmp(sql, "quit", 4) == 0 || strncmp(sql, "QUIT", 4) == 0) {
			break;
		}

		if (mysql_query(mysql, sql))
		{
			printf("sql has err, try again\n");
		}

		result = mysql_store_result(mysql);

		if (result != NULL) {
			showresult(result);
		}
	}

	mysql_close(mysql);

	printf("exit mysql\n");
	return 0;
}
