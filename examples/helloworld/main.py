from pyosdevkit import *

primary_file_asm("main.asm")

pta.bios.write_string("Hello World!")
pta.jump.current()
pta.make_bootable()

primary_asm_output_write()
run()
