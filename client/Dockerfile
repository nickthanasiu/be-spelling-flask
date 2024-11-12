FROM node:latest
WORKDIR /app
COPY package.json .
#RUN npm ci && npm cache clean --force
RUN npm install
COPY . .
EXPOSE 3000
CMD [ "npm", "run", "dev" ]