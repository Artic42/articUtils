# Constant definitions

# Main bianry creation
$(BIN)/fileRemote: $(SRCPY)/fileRemote.py
	@mkdir -p $(BIN)
	$(PYC) $(SRCPY)/fileRemote.py --target-dir $(BIN)
