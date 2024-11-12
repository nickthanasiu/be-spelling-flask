FROM node:latest
WORKDIR /app
COPY package*.json .
RUN npm ci && npm cache clean --force
COPY . .
RUN npm run build
EXPOSE 3000
CMD [ "npm", "run", "dev" ]