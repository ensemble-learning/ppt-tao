import os, sys
if len(sys.argv) > 2:
    cmd = "convert "
    infile = sys.argv[1]
    cmd += infile + " "
    cmd += "-resize 800x400 " 
    #cmd += "-background none " 
    cmd += "-background 'rgb(255,255,255)' " 
    cmd += "-compose Copy "
    cmd += "-gravity center "
    cmd += "-extent 800x400 "
    #cmd += "-transparent white "
    #cmd += "-density 1200 "
    outfile = sys.argv[2]
    cmd += outfile
    print cmd
    os.system(cmd)

