
program: $(call map_experiment_hex) $(call map_experiment_elf)
    ifeq ($(PROGRAM_WITH_OPENOCD),0)
	lpc21isp -wipe -hex $< $(USB_PORT) $(USB_BAUD) 12000
    else
	$(OPENOCD) \
            -f interface/jlink.cfg                 \
            -c "transport select swd"              \
            -f    target/lpc11xx.cfg               \
            -c "program $(call map_experiment_elf) reset" \
            -c "exit"
    endif
