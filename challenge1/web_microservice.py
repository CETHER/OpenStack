#paso-1
from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

#lista de imagenes y flavors
images = conn.list_images()
for image in images:
    print(image)

flavors =  conn.list_flavors()
for flavor in flavors:
    print(flavor)


#paso-2
print "Selected image:"
image_id = 'YOUR_IMAGE_ID'
image = conn.get_image(image_id)
print(image)

#paso-3
print "\nSelected flavor:"
flavor_id = 'YOUR_FLAVOR_ID'
flavor = conn.get_flavor(flavor_id)
print(flavor)

#paso-4 Ejecuta el init para montar servicios en servidor
ex_userdata = '''#!/usr/bin/env bash
curl -L -s YOUR_POST_CREATION_SCRIPT | bash -s --
'''

#paso-5
external_network = 'YOUR_NETWORK_ID'


#lista instancias
instances = conn.list_servers()
for instance in instances:
    print(instance)

#paso-6 puertos de servicios
print('Checking for existing security groups...')
sec_group_name = 'web'
if conn.search_security_groups(sec_group_name):
    print('Security group already exists. Skipping creation.')
else:
    print('Creating security group.')
    conn.create_security_group(sec_group_name, 'network access for a web application.')
    conn.create_security_group_rule(sec_group_name, 80, 80, 'TCP')

#para all in one (SSH) agragar la siguiente linea
conn.create_security_group_rule(sec_group_name, 22, 22, 'TCP')


#paso 7 creación de instancia
print "\nServer creation:"
instance_name = 'INSTANCE_NAME'
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
    userdata=ex_userdata,
    network=external_network,
    security_groups=[sec_group_name])
