from pyosdevkit import *

primary_file_asm("main.asm")

pta.jump.current()
pta.make_bootable()

primary_asm_output_write()
run()
