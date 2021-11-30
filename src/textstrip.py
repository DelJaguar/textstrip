############################################################
#   Program to strip out special characters from a string  #
#                   By Julian Aguirre                      #
#############################################################
def main(arg):
    variable = ''
    for i in arg.split('-'):
        variable = variable + i

    print(variable)
    

main("3-3-3-3-3-3-3-3-3-3-3-3")