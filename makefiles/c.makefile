#Constant definitions
CC = gcc
CFLAGSR = -Wall
CFLAGSD = -g $(CFLAGSR)
OFLAGSR = -c $(CFLAGSR)
OFLAGSD = -c $(CFLAGSD)
IPATH = -Iinclude
SRC = src/c

# Creation of binaries
$(BIN)/isGit: $(SRC)/isGit.c
	@mkdir -p $(BIN) 
	@${CC} ${CFLAGSR} ${IPATH} $(SRC)/isGit.c -o $(BIN)/isGit
