from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='osic-hackathon')

print "\nSelected image:"       
image_id = '95576f28-afed-4b63-93b4-1d07928930da'
image = conn.get_image(image_id)
print(image)

print "\nSelected flavor:"
flavor_id = '2'
flavor = conn.get_flavor(flavor_id)
print(flavor)

ex_userdata = '''#!/usr/bin/env bash
curl -L -s https://raw.githubusercontent.com/CETHER/OpenStack/master/init.sh | bash -s --
'''

external_network = 'aba7a6f8-6ec9-4666-8c42-ac2d00707010'

print('Checking for existing security groups...')
sec_group_name = 'web'
if conn.search_security_groups(sec_group_name):
    print('Security group already exists. Skipping creation.')
else:
    print('Creating security group.')
    conn.create_security_group(sec_group_name, 'network access for a web application.')
    conn.create_security_group_rule(sec_group_name, 80, 80, 'TCP')

print "\nServer creation:"
instance_name = 'RACCOON_POKEDEX'
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
    userdata=ex_userdata,
    network=external_network,
    security_groups=[sec_group_name])

#step-13
f_ip = conn.available_floating_ip()

#step-14
conn.add_ip_list(testing_instance, [f_ip['floating_ip_address']])

#step-15
print('The Pokedex app will be deployed to http://%s' % f_ip['floating_ip_address'] )
