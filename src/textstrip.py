####################################################################
#   Program to strip out special characters from string arguments  #
#                   By Julian Aguirre                              #
####################################################################
import re 
import sys


arg_list = []

def get_arguments():
    n = len(sys.argv)
    for i in range(1, n):
        arg_list.append(sys.argv[i])

def main(arg_list):
    for i in arg_list:
        result = re.sub(r"\D","",i)
        print(result)
    
get_arguments()
main(arg_list)