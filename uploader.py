from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='osic-hackathon')

print "Upload objects:" 
container_name = 'RACCOON_CONTAINER'
container = conn.create_container(container_name)

pokemons = {'Charmander': '/home/aldo/Documentos/OpenStack/training-shade-cucea-master/challenge3/Charmander.png', 'Charmeleon': '/home/aldo/Documentos/OpenStack/training-shade-cucea-master/challenge3/Charmeleon.png', 'MegaCharizard': '/home/aldo/Documentos/OpenStack/training-shade-cucea-master/challenge3/MegaCharizard.jpg'}
for object_name, file_path in pokemons.items():
    conn.create_object(container=container_name, name=object_name, filename=file_path)
