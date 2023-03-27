docker volume create servervol \
    --opt type=none \
    --opt device=./servervol \
    --opt o=bind
docker network create --driver bridge servernet


docker build -t server -f ./server/Dockerfile ./server
docker run --rm -it --name ipc_server_dns_name \
    -v servervol:/serverdata \
    -e PORT=9000 \
    --network servernet \
    server

