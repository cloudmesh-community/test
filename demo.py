from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.azure_arm import AzureNodeDriver

'''
Fill these four parameters: tenant_id, subscription_id, key, secret with the arguments you get from Azure cross platform(CLI), where key is the service principal app ID, secret is the strong password you set.
'''

driver = AzureNodeDriver(tenant_id='',
			 subscription_id='',
             		key='', secret='',
			region='East US')

print(driver)

