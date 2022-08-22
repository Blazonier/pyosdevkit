import os

class v:
    file_name = None
    file = None

def file_asm(file_name):
    v.file = open(file_name, 'w')
    v.file_name = file_name
    return v.file_name
    return v.file
def asm_output_write():
    v.file.close()
class asm:
    def code_add(code):
        v.file.write(code+"\n")

class pta:
    class jump:
        def current():
            v.file.write("jmp $\n")

    class bios:
        def write_char(char):
            v.file.write("mov ah, 0x0e \n")
            v.file.write("mov al, '" + str(char) + "'\n")
            v.file.write("int 10h\n")

        def write_string(string):
            for char in string:
                pta.bios.write_char(char)

    def make_bootable():
        v.file.write("times 510 - ($-$$) db 0\n")
        v.file.write("dw 0xAA55")

def run():
    os.system("nasm " + v.file_name + " -f bin -o " + v.file_name.replace(".asm", ".bin"))
    os.system("qemu-system-x86_64 " + v.file_name.replace(".asm", ".bin"))
