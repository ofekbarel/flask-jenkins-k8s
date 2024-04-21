#login azure 
az login

#create a resource group 
az group create --name myResourceGroup --location southcentralus

#Create AKS cluster with 2 worker nodes
az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 2

#Display Details of Cluster
az aks show --name myAKSCluster --resource-group myResourceGroup

#Create ACR
az acr create --resource-group myResourceGroup --name regestery --sku Standard --location southcentralus

#Connect to the cluster
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster --overwrite-existing