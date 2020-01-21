'''
uses ClientsNames file to generate sql for populating database
ClientsNames contains full names each in a line
'''
# CLIENTS

input = open('ClientsNames', 'r')
lines = []
for line in input:
    f_name , l_name = line.strip().split(' ')
    lines.append('("' + f_name + '","' + l_name + '",CURDATE()) ,')
lines[-1] =  lines[-1].replace(') ,', ') ;')

output = open("Clients_populate.sql", 'w+')
output.write("insert into Clients (FirstName, LastName, RegistrationDate) values\n")
for line in lines:
    output.write("\t" + line + "\n")

num_of_clients = len(lines)

# SPECIES
output.write('insert into Species (Name, ObligatoryProcedures,'
             + 'Description, LegalIssues) values ("cat","","","");\n')
# ANIMALS

output.write('insert into Animals (Clients_ClientID, Name, RegistrationDate,'
             'Birth, Gender, Height, Weight , Species_Name) values\n')

input = open('AnimalsNames','r')
lines = []


for i,line in enumerate(input):
    clients_id = i//2 + 1
    animal_name = line.strip()
    lines.append('(' + str(clients_id) +  ',"' + animal_name
                 + '",CURDATE(),' + 'CURDATE()-100,'
                 + '"male", 0, 0, "cat") ,')

lines[-1] =  lines[-1].replace(') ,',');')
for line in lines:
	output.write('\t' + line + '\n')






