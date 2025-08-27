FROM php:7.4-apache

# Instala driver do PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
  && docker-php-ext-install pdo pdo_pgsql

# Habilita mod_rewrite (útil p/ frameworks)
RUN a2enmod rewrite

# Timezone opcional
RUN echo "date.timezone=America/Sao_Paulo" > /usr/local/etc/php/conf.d/timezone.ini
