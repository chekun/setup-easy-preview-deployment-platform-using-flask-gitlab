FROM library/debian:wheezy

MAINTAINER chekun mr.che.kun@gmail.com

RUN apt-get update \
        &&  apt-get install -y curl python python-setuptools git

RUN easy_install Flask requests

RUN curl -o /usr/local/bin/noop -SL "https://github.com/bcho/noop/releases/download/0.1.0/noop-$(dpkg --print-architecture)" \
        && chmod +x /usr/local/bin/noop

EXPOSE 5000
EXPOSE 5001

CMD ["sh", "/demo/daemon.sh"]
