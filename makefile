# Define variables
UVeh-Vis_script := UVeh-Vis
dependencies := matplotlib pandas numpy

# Default target
all: say_hello

# Target to set up the environment
say_hello:
	@if [ ! -f "$(UVeh-Vis_script)" ]; then \
		echo "Error: Script $(UVeh-Vis_script) not found"; \
		exit 1; \
	fi
	@chmod +x $(UVeh-Vis_script)
	@echo "Installing dependencies..."
	@$(foreach dep,$(dependencies),pip install $(dep);)
	@echo "Generating PATH of Installation..."
	@SCRIPT_DIR="$$(cd "$$(dirname "$(UVeh-Vis_script)")" && pwd | sed 's/ /\\ /g')"; \
	echo ""; \
	echo "Installation Done! :D"; \
	echo "Please add the following line to your \".bashrc\" file located at /home"; \
	echo ""; \
	echo "alias UVeh-Vis='python3 $${SCRIPT_DIR}/$(UVeh-Vis_script)'"; \






