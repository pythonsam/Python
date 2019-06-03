# Sample code for to verify SSH is enable or not 

def verify_ssh(conf_file):
    '''
    This finction is used to verify the ssh protocal is enabled or not based on the given configuration file
    example : verify_ssh(Config_file)
    Author  : Sriram Chowdary
    Date    : 
    '''
    fh = open(conf_file)
    for line in fh:
        if 'no ssh' in line:
            raise AssertionError(' " SSH is Disable but expected is Enable "')
    return('SSH is enabled as expected')

print(verify_ssh('DEVICE_CONFIG.txt'))
