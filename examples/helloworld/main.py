from pyosdevkit import *

file_asm("main.asm")

pta.bios.write_string("Hello World!")
pta.jump.current()
pta.make_bootable()

asm_output_write()
run()
