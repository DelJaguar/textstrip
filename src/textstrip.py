############################################################
#   Program to strip out special characters from a string  #
#                   By Julian Aguirre                      #
#############################################################
import re 

def main(arg):
    target_str = arg 
    result = re.sub(r"\D","",arg)
    print(result)
    

main("3-3-3-3-3-3-3-3-3-3-3-3")