FROM pl31/debian-mongodb
LABEL maintainer "manuelbr <manuelbr994@gmail.com>"

RUN apt-get update & apt-get upgrade
RUN mkdir -p /data/db/

# Define mountable directories.
VOLUME ["/data/db"]

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["mongod", "--smallfiles"]

EXPOSE 27017
EXPOSE 28017
