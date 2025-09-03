# Building app using image
FROM node:22 AS build

# Defining working directory inside image
WORKDIR /app
# Copy dependencies
# Lets Docker cache dependency layer so future builds are faster when source files change but dependencies don't
COPY package*.json ./
# Install dependencies
RUN npm install
# Copy all code and project files
COPY . .
# Builds the static files to serve to nginx server
RUN npm run build

# Switch to nginx image 
FROM nginx:stable-alpine
# Removes default nginx placeholder site
RUN rm -rf /usr/share/nginx/html/*
# Copies static files from build to nginx web root
COPY --from=build /app/dist /usr/share/nginx/html
# Exposes nginx port
EXPOSE 80

# Starts container
CMD ["nginx", "-g", "daemon off;"]
