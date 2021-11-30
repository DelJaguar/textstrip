############################################################
#   Program to strip out special characters from a string  #
#                   By Julian Aguirre                      #
#############################################################
import re 
import sys




arg = sys.argv[1]

def main(arg):
    target_str = arg 
    result = re.sub(r"\D","",arg)
    print(result)
    

main(arg)