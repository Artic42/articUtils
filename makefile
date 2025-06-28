#Constant definitions
BIN = bin
T_BIN = ~/bin

# All command
all: $(BIN)/isGit $(BIN)/fileRemote

# Include other makefiles
include makefiles/c.makefile
include makefiles/python.makefile

# Other commands
install: all
	@mkdir -p $(BIN)
	@rm -rf $(T_BIN)/lib
	@cp $(BIN)/isGit $(T_BIN)
	@cp $(BIN)/fileRemote $(T_BIN)
	@cp -r $(BIN)/lib $(T_BIN)

clean:
	rm -rf bin
