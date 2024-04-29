from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from pages.models import Client,Collaborator

def create_group(name:str):
    Group.objects.get_or_create(name=name)
    try:
        return Group.objects.get(name=name)
    except Group.DoesNotExist:
        return None
def give_permission(group_name:str,permission:Permission):
    group=Group.objects.get(name=group_name)
    group.permissions.add(permission)

#LOS 3 tipos de usuario
group=create_group("Administrator")
group2=create_group("Collaborator")
group3=create_group("Client")

client=ContentType.objects.get_for_model(Client)
collab=ContentType.objects.get_for_model(Collaborator)

add_client=Permission.objects.get_or_create(codename='add_Client',name='Can add Client',content_type=client)[0]
add_colab=Permission.objects.get_or_create(codename='add_Collaborator',name='Can add Collaborator',content_type=collab)[0]

delete_client=Permission.objects.get_or_create(codename='delete_client', name="Can delete Client",content_type=client)[0]
delete_colab=Permission.objects.get_or_create(codename='delete_Collaborator',name='Can delete Collaborator',content_type=collab)[0]

#PERMISOS DE ADMINISTRADOR
group.permissions.add(add_client)
group.permissions.add(add_colab)
group.permissions.add(delete_colab)

#PERMISOS DE CLIENTE
group3.permissions.add(delete_client)
