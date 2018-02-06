import os, sys
if len(sys.argv) > 2:
    cmd = "convert "
    infile = sys.argv[1]
    cmd += infile + " "
    cmd += "-resize 800x400 " 
    cmd += "-background none " 
    cmd += "-compose Copy "
    cmd += "-gravity center "
    cmd += "-extent 800x400 "
    #cmd += "-transparent white "
    #cmd += "-density 1200 "
    outfile = sys.argv[2]
    cmd += outfile
    os.system(cmd)

