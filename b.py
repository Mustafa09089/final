# Define variables
import pexpect
import os
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

telnet_file_output = os.path.expanduser('~/labs/prne/telnet_running_config.txt')
ssh_file_output = os.path.expanduser('~/labs/prne/ssh_running_config.txt')

session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8',timeout=20)

result = session.expect(['Username:', pexpect.TIMEOUT])

if result !=0:
    print('---FAILURE! creating session for: ', ip_address)
    exit()

session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

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

# import required modules/packages/library
import pexpect

# define variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'

# create the SSH session
session = pexpect.spawn ('ssh ' + username + '@' + ip_address, encoding='utf-8', timeout=20)
result = session.expect (['Password:', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

# session expecting password, enter details
session.sendline(password)
result = session.expect (['>', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password: ', password)
    exit()

# enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! entering enable mode')
    exit()

# send enable password details
session.sendline(password_enable)
result = session.expect (['#', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print ('--- Failure! entering enable mode after sending password')
    exit()

# enter config mode
session.sendline('configure terminal')
result = session.expect ([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! entering config mode')
    exit()

# change hostname to R1
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! setting hostname')

# exit config mode
session.sendline('exit')

# exit enable mode
session.sendline('exit')

# display success message if it works
print ('-----------------------------------------------------------------')
print ('')
print ('--- success! SSH connection has been established: ', ip_address) 
print ('---                                     Username: ', username)
print ('---                                     Password: ', password)
print ('')
print ('-----------------------------------------------------------------')






# Existing code for SSH connection...

# After changing the hostname and before exiting the session
session.sendline('show running-config')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
    print('--- FAILURE! retrieving running configuration')
else:
    running_config_ssh = session.before  # Capture the output

    # Save the SSH running config to a file
    with open(ssh_file_output, 'w') as file:
        file.write(running_config_ssh)

    print('--- Success! SSH running config saved to:', ssh_file_output)

# Exit enable mode
session.sendline('exit')

# Close SSH session
session.close()
# terminate SSH session
session.close()