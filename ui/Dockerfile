FROM node:latest

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app

RUN npm install && \
    npm install -g serve \
    npm audit fix \
    npm run build

CMD ["serve", "-s", "build", "-l", "3000"]