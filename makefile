UVeh-Vis_script := UVeh-Vis
dependencies := matplotlib pandas numpy
bashrc := $(HOME)/.bashrc
alias_name := $(UVeh-Vis_script)

all: check_dependencies add_alias goodbye

check_dependencies:
	@if [ ! -f "$(UVeh-Vis_script)" ]; then \
		echo "Error: Script $(UVeh-Vis_script) not found"; \
		exit 1; \
	fi
	@chmod +x $(UVeh-Vis_script)
	@echo "Permissions to main code upgraded"
	@echo ""
	@echo "Checking dependencies..."
	@echo ""
	@for dep in $(dependencies); do \
		echo -n "Checking $$dep ... "; \
		if pip3 show $$dep >/dev/null 2>&1; then \
			echo "ok"; \
		else \
			echo "missing"; \
			echo "Installing $$dep..."; \
			pip3 install $$dep; \
		fi \
	done
	@echo "Compiling reader..."
	@gcc -shared -Wl,-soname,adder -o reader.so -fPIC reader.c
	@echo ""
	@echo "Installation done! :D"
	@echo ""
add_alias:
	@echo "Checking if alias already exists..."
	@if grep -q -F "alias $(alias_name)=" $(bashrc); then \
		echo "Alias $(alias_name) already exists in $(bashrc)"; \
		sed -i '/^alias $(alias_name)=/d' $(bashrc); \
		echo "Existing alias removed"; \
	fi
	@echo "" >> $(bashrc)
	@echo "This is the line to be added:" 
	@echo "alias $(alias_name)='python3 $(SCRIPT_DIR)/$(UVeh-Vis_script)' #Alias for UVeh-Vis code" 
	@echo ""
	@echo "alias $(alias_name)='python3 $(SCRIPT_DIR)/$(UVeh-Vis_script)' #Alias for UVeh-Vis code" >> $(bashrc)
	@echo "Alias added to $(bashrc)"
	
goodbye:
	@rm makefile reader.c
	@echo ""
	@echo "Everthing done!"
	@echo "To start using UVeh-Vis, please open a new terminal"

SCRIPT_DIR := $(shell cd "$(dir $(UVeh-Vis_script))" && pwd | sed 's/ /\\ /g')










