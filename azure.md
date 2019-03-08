1. Azure Souce Manager(ASM)
The libcloud classic APIs provide connection to Azure Souce Management. The website below will instruct in more detail.
https://libcloud.readthedocs.io/en/latest/compute/drivers/azure.html

Generate pem and cer certifile on Linux by running the followsing two commands.

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout azure_cert.pem -out azure_cert.pem
openssl x509 -inform pem -in azure_cert.pem -outform der -out azure_cert.cer

Then upload the .cer certificate to Azure "manage certificate" under specific subscription. Then by running the following code, with changing 'subscription_id' found in your own subscription and changing the 'key_file' to where your .pem file exist.

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

cls = get_driver(Provider.AZURE)
driver = cls(subscription_id='subscription-id',
             key_file='/path/to/azure_cert.pem')
print(driver)

Since this method is deprecated, we won't go deeper into this.

2. Azure Resource Manager(ARM)
Install Azure cross platform(CLI) according to your operating system from the below link:
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest

Test the connection by typing:
az login
in command line.

We need to select the correct subscription name under our subscription in Azure.
az account set --subscription 'Free Trial'

Then we set a name for our azure ad app. Here we call it 'demo'.
appName="demo"

Next, we use az ad app create to create an Azure AD app.
az ad app create \
 --display-name $appName \
 --homepage "https://testdemo/$appName"\
 --identifier-uris "https://testdemo/$appName"

By searching for the AD app with the display name, we can get the app ID by executing this command. This app ID will be used next.
appId=$(az ad app list --display-name $appName --query [].appId -o tsv)

Here we can choose a strong password for our service principal.
spPassword="Myazur3serve@1cp!"

We can get our subscription ID by running the following command, instead of find it manully from the Azure website under our subscription.
subscriptionId=$(az account show --query id -o tsv)

echo $subscriptionId

This command  would create a service principal that has contributor access to the currently selected subscription.
az ad sp create-for-rbac --name $appId --password $spPassword \
--role contributor

Once you've created your service principal, you will need to get its app id by running the following command (Note: this app ID is different from the former app id of the AD application):
servicePrincipalAppId=$(az ad sp list --display-name $appId --query "[].appId" -o tsv)
echo $servicePrincipalAppId

If you need to do anything more complex with the roles and scopes for your service principal, then the az role assignment group of commands will help you do this.
az role assignment create --assignee $servicePrincipalAppId \
--role "contributor"

We also need the tenant id associated with our account: 
tenantId=$(az account show --query tenantId -o tsv)
echo $tenantId

Till now, we get all parameters that we need to run the driver.