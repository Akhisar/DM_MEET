# DM_MEET

kubectl apply -f deployment.yaml

helm repo add kedacore https://kedacore.github.io/charts

helm repo update

helm install keda kedacore/keda --namespace keda --create-namespace