from cloudmesh.common.Shell import Shell
from textwrap import dedent
from pprint import pprint

class Provider(object):
	def __init__(self):
		self.debug = True
	
	def login(self):
		print("\nconnecting to azure...\n")
		r = Shell.live("az login")
		r = Shell.execute("az account show", shell = True)
		data = eval(r)
		print("\ndata:",data)
		datalist=[]
		for key, value in data.items():
    			temp = [key,value]
    			datalist.append(temp)
		print("\ntype of data:",type(datalist))
		print(datalist)
		print("\nazure has been connected\n")

	#create a resource group
	def resource_group(self):	
		print("\ncreating a resource group...")
		r = Shell.live("az group create --name test --location eastus")
		print("\nThe resource group named test has been created")

	#create a vm 
	def create_vm(self, **kwargs):
		print("\ncreate a vm...")
		command = dedent("""
			az vm create \
  			--resource-group {resourcegroup} \
  			--name {name} \
  			--image {image} \
  			--admin-username {username} \
  			--generate-ssh-keys
			""".format(**kwargs))
		print(command)
		r = Shell.live(command)
		print("\nthe vm has been created")
	
	def get_ip(self, **kwargs):
		print("get ip address:")
		command = dedent("""
			az vm list-ip-addresses \
  			--resource-group {resourcegroup} \
  			--name {name}
			""".format(**kwargs))
		r = Shell.execute(command, shell = True)
		print("r:\n",r)
		data = eval(r)
		print("\ntype of data:",type(data))
		print("\ndata:",data)
		for entry in data:
			pprint(entry)

	#connect to vm
	def connect_vm(self):
		print("connecting to vm...")
		r = Shell.live(
		"ssh azureuser1@{publicIdAddress}".format(publicIdAddress='40.117.171.110'))
	
	#list vm
	def list(self):
		print("list all virtual machine:")
		r = Shell.live("az vm list")

	def stop(self, **kwargs):
		print("stopping a virtual machine...")
		command = dedent("""
			az vm stop \
  			--resource-group {resourcegroup} \
  			--name {name}
			""".format(**kwargs))
		r = Shell.live(command)
		print("the vm has been stopped")

	def restart(self, **kwargs):
		print("restarting a virtual machine...")
		command = dedent("""
			az vm restart \
  			--resource-group {resourcegroup} \
  			--name {name}
			""".format(**kwargs))
		r = Shell.live(command)
		print("the vm has been restarted")

	def delete(self, **kwargs):
		print("deleting a virtual machine...")
		command = dedent("""
			az vm delete \
  			--resource-group {resourcegroup} \
  			--name {name}
			""".format(**kwargs))
		r = Shell.live(command)
		print("the vm has been deleted")

true = True
p = Provider()
p.login()

#p.resource_group()

'''
p.create_vm(resourcegroup = 'test',
	    name = 'testvm1',
	    image = 'UbuntuLTS',
	    username = 'azureuser1')

'''
'''
p.get_ip(resourcegroup = 'test',
	    name = 'testvm1')
'''
#p.connect_vm()

#p.list()

'''
p.stop(resourcegroup = 'test',
	    name = 'testvm1')
'''
'''
p.restart(resourcegroup = 'test',
	    name = 'testvm1')
'''

'''
p.delete(resourcegroup = 'test',
	    name = 'testvm1')
'''



