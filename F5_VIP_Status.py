#---------------------------------
# NAME: F5 BigIP Virtual IP/member_servers status
# PURPOSE: This script is used to fetch the VIP-port and member server status from the 'b virtual show' and save the output to a file.
#---------------------------------

#!/usr/bin/env python
import sys
print('''
This script is used to fetch VIP,port/member server status of F5 LB from 'b virtual show' output and save data to a file.
''')
 
virtual_show_file=input('Enter the file name: ')
try:
    my_file=open(virtual_show_file)
except:
    print('File not found! Please try again')
    sys.exit(1)
print('Please wait...fetching desired data')
 
for line in my_file:
    line=line.rstrip()
    if line.startswith('VIRTUAL ADDRESS'):
        open('VIP_status.txt','a').write('\n' + line[16:31] + '\t')
 
    elif line.find('SERVICE')!=-1:
        aa=line.find('SERVICE')
        bb=line[aa+8:]
        if bb=='https':
            bb='443'
            open('VIP_status.txt','a').write(bb + '\t')
        elif bb=='http':
            bb='80'
            open('VIP_status.txt','a').write(bb + '\t')
        else:
            open('VIP_status.txt','a').write(bb + '\t')
 
    elif line.startswith('        +-> POOL MEMBER'):
        cc=line.find('/')
        dd=line[cc+1:]
        if dd.find(':https')!=-1:
            ee=dd.replace('https','443')
            open('VIP_status.txt','a').write(ee + '\n\t\t')
        elif dd.find(':http')!=-1:
            ee=dd.replace('http','80')
            open('VIP_status.txt','a').write(ee + '\n\t\t')
        else:
            open('VIP_status.txt','a').write(dd + '\n\t\t')
 
    else:
        continue
 
Status_file=open('VIP_status.txt','r')
line_list=list()
vip=""
for line in Status_file:
    line=line.rstrip()
    line_list=line.split()
 
    if len(line)==0:
        continue
 
    elif len(line_list)==4:
        vip=line_list[0] + ' ' + line_list[1]
        if line_list[3]=='active,up':
            open('tmp_duplicate.txt','a').write(vip + ' up' + '\n')
 
    elif len(line_list)==5:
        vip=line_list[0] + ' ' + line_list[1]
 
    elif line_list[1]=='active,up':
        open('tmp_duplicate.txt','a').write(vip + ' up' + '\n')
 
    else:
        continue
 
Status_file.close()
 
lines_seen=set()
filehandle=open('tmp_duplicate.txt','r')
for line in filehandle:
    line=line.rstrip()
    if line not in lines_seen:
        open('VIP_statusUP.txt','a').write(line + '\n')
        lines_seen.add(line)
filehandle.close()
 
print('Check below files:\nVIP_status.txt - list of all VIP-member severs with their status\nVIP_statusUP.txt - list of all active VIPs\n')
print('NOTE: Please delete (or rename) VIP_status.txt, VIP_statusUP.txt and tmp_duplicate.txt before running this scrip again.')
