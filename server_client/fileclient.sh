docker volume create clientvol \
    --opt type=none \
    --opt device=./clientvol \
    --opt o=bind

docker build -t client -f ./client/Dockerfile ./client
docker run --rm -it --name ipc_client_dns_name \
    -v clientvol:/clientdata \
    -e PORT=9000 \
    --network servernet \
    client