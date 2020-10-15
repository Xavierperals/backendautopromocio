FROM library/mysql:5.7

ARG USER_ID
ARG GROUP_ID

RUN usermod -u ${USER_ID:-1000} mysql \
  && groupmod -g ${GROUP_ID:-1000} mysql
