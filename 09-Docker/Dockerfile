# GRABBING UBUNTU
# syntax=docker/dockerfile:1.5-labs
FROM ubuntu

# COMMANDS ARE EXECUTED WHEN IMAGE IS MADE
RUN apt-get update

# SETIING THE FILE PATH FOR THE FILE
WORKDIR /usr/amsu

COPY ./noted.md .
COPY ./app.py .

# ADD https://github.com/tkmagesh/lfg-bootcamp-2023.git .

# PRINTING TO THE CONSOLE
CMD [ "echo", "THIS IS CMD!" ]