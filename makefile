#Constant definitions
CC = gcc
CFLAGSR = -Wall
CFLAGSD = -g $(CFLAGSR)
OFLAGSR = -c $(CFLAGSR)
OFLAGSD = -c $(CFLAGSD)
IPATH = -Iinclude

bin/isGit: src/isGit.c
	@mkdir -p bin
	@${CC} ${CFLAGSR} ${IPATH} src/isGit.c -o bin/isGit

all: bin/isGit

clean:
	rm -rf bin
