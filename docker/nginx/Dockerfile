FROM nginx:stable-alpine

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom Nginx config
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
