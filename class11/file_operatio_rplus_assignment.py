fh = open(r'text.txt', 'w')

fh.write("""
                                                                                
kaise usne ye sab kuchh mujhse chhupkar badla
chehra badla rasta badla baad mein ghar badla

main uske baare mein ye kehta tha logon se
mera naam badal dena vo shakhs agar badla

vo bhi khush tha usne dil dekar dil maanga hai
main bhi khush hoon maine patthar se patthar badla

maine kaha kya meri khaatir khud ko badloge
aur phir usne nazren badlein aur number badla
""")

fh.close()


fh = open('text.txt', 'r+')

fh.seek(0, 2)

fh.write("\n                          -TehZeeb Hafi Saab")

fh.seek(0)

fh.write("-------------------BADLA---------------------\n")

fh.seek(0)
content = fh.read()

fh.close()

print(content)
