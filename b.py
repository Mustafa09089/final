# define variables
import pexpect
import os
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

file_output_telnet = os.path.expanduser('~/labs/prne/telnet_running_config.txt')
file_output_ssh = os.path.expanduser('~/labs/prne/ssh_running_config.txt')
# create ssh session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8',timeout=20)

result = session.expect(['Username:', pexpect.TIMEOUT])
# check for error if exists then display error and exit
if result !=0:
    print('---FAILURE! creating session for: ', ip_address)
    exit()
# session expecting password enter details
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])
# check for error if exists then display error and exit
if result != 0:
    print ('-- FAILURE! entering username: ', username)
    exit()

session.sendline(password)
result = session.expect (['#', pexpect.TIMEOUT])
if result != 0:
    print ('--FAILURE! entering password: ', password)
    exit()

print('--------------------------------------------------------------------')
print('')
print('--- Success! Telnet connection has been established: ', ip_address)
print('---                                        Username: ', username)
print('---                                        Password: ', password)
print('')
print('--------------------------------------------------------------------')

session.sendline('quit')
session.close()


import pexpect


ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'


session = pexpect.spawn ('ssh ' + username + '@' + ip_address, encoding='utf-8', timeout=20)
result = session.expect (['Password:', pexpect.TIMEOUT, pexpect.EOF])


if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()


session.sendline(password)
result = session.expect (['>', pexpect.TIMEOUT, pexpect.EOF])


if result != 0:
    print('--- FAILURE! entering password: ', password)
    exit()


session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])


if result != 0:
    print('--- Failure! entering enable mode')
    exit()


session.sendline(password_enable)
result = session.expect (['#', pexpect.TIMEOUT, pexpect.EOF])


if result != 0:
    print ('--- Failure! entering enable mode after sending password')
    exit()


session.sendline('configure terminal')
result = session.expect ([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])


if result != 0:
    print('--- Failure! entering config mode')
    exit()

# change hostname
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])


if result != 0:
    print('--- Failure! setting hostname')


session.sendline('exit')


session.sendline('exit')


print ('-----------------------------------------------------------------')
print ('')
print ('--- success! SSH connection has been established: ', ip_address) 
print ('---                                     Username: ', username)
print ('---                                     Password: ', password)
print ('')
print ('-----------------------------------------------------------------')



session.sendline('show running-config')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
    print('--- FAILURE! retrieving running configuration')
else:
    running_config_ssh = session.before  

    
    with open(file_output_ssh, 'w') as file:
        file.write(running_config_ssh)

    print('--- Success! SSH running config saved to:', file_output_ssh)


session.sendline('exit')


session.close()

session.close()
