# Node frontend
FROM node:12 as base-frontend

RUN apt-get update && apt-get install -y

WORKDIR /app

COPY ./docker/client/nginx.global.conf /nginx.global.conf
COPY ./docker/client/nginx.conf /nginx.conf


# Fase 0, compila el frontend

FROM base-frontend as build-stage

WORKDIR /app
COPY client/package*.json /app/
RUN yarn

COPY ./client/ /app/

ARG configuration=production

RUN yarn build --output-path=./dist/out/ --configuration $configuration

# Fase 1, deja solo la aplicación compilada lista para usar con Nginx

FROM nginx:latest

COPY --from=build-stage /app/dist/out/ /usr/share/nginx/html

# Copia la configuración proporcionada por el stage anterior
COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /nginx.global.conf /etc/nginx/nginx.conf
