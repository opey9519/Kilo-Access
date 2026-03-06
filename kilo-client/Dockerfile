# -----------------------
# Build stage
# -----------------------
FROM node:22 AS build

# Define working directory
WORKDIR /app

# Copy dependency files first (for caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Frontend URL
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

# Build static files
RUN npm run build


# -----------------------
# Production stage
# -----------------------
FROM nginx:stable-alpine

# Remove default nginx site
RUN rm -rf /usr/share/nginx/html/*

# Copy built frontend
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]