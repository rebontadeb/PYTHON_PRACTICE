import re

with open('status.txt', 'r+') as file:
    for line in file:
        if re.search('Base DN:', line):
            BASEDN = line.split(':')[1].strip('\n').strip(' ')
        elif re.search('Entries:', line):
            ENTRIES = line.split(':')[1].strip('\n').strip(' ')
        elif re.search('^Version: ', line):
            DJ_VERSION = line.split(':')[1].strip('\n').strip(' ')
        elif re.search('Java Version:', line):
            JAVA_VERSION = line.split(':')[1].strip('\n').strip(' ')
        elif re.search(': LDAP ', line):
            LDAP_PORT = line.split(':')[1].strip('\n').strip(' ')
        elif re.search('Host Name:', line):
            LDAP_HOST = line.split(':')[1].strip('\n').strip(' ')
        elif re.search('Replication:', line):
            REPLICATION = line.split(':')[1].strip('\n').strip(' ')
        elif re.search('Administration Connector', line):
            ADMIN_PORT = line.split(':')[1].strip(
                '\n').strip(' ').split(' ')[1]
        elif re.search('Installation Path:', line):
            PATH = line.split(':')[1].strip('\n').strip(' ')

print(file.readlines())

# file.close()


# print("==================================================")
#print("   HOSTNAME        ---  " + LDAP_HOST)
#print("   OPENDJ VERSION  ---  " + DJ_VERSION)
#print("   JAVA VERSION    ---  " + JAVA_VERSION)
#print("   PATH            ---  " + PATH)
#print("   BASEDN          ---  " + BASEDN)
#print("   USER BIND DN    ---  ou=People," + BASEDN)
#print("   ROLE BIND DN    ---  ou=Groups," + BASEDN)
#print("   LDAP PORT       ---  " + LDAP_PORT)
#print("   ADMIN PORT      ---  " + ADMIN_PORT)
#print("   ENTRIES         ---  " + ENTRIES)
# if not REPLICATION:
#    print("   REPLICATION     ---  Disabled")
# else:
#    print("   REPLICATION     ---  " + REPLICATION)
# print("==================================================")
