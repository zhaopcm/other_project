#gcc 01_hello.c -o hello -I /usr/include/mysql/ -L /usr/lib/mysql/ -lmysqlclient
GCC=gcc
IncPath=/usr/include/mysql/
PubLib=/usr/lib/mysql/ -lmysqlclient

SrcFile=$(wildcard *.c)
TargetFiles=$(patsubst %.c, %,$(SrcFile))

all:$(TargetFiles)

%:%.c
	$(GCC) $^ -o $@ -I$(IncPath) -L$(PubLib)

clean:
	rm -rf $(TargetFiles)



