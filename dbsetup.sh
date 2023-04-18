#!
podman pod create --name postgre-sql -p 5432:5432

#podman run --pod postgre-sql -e 'PGADMIN_DEFAULT_EMAIL=admin@email.com' -e 'PGADMIN_DEFAULT_PASSWORD=p0stdev' --name pgadmin -d docker.io/dpage/pgadmin4:latest

podman pull docker.io/library/postgres:14

podman run --name db --pod=postgre-sql -d -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=p0stdev docker.io/library/postgres:14

firefox http://127.0.0.1:5432/browser/