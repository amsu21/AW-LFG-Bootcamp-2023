# GRABBING UBUNTU
FROM ubuntu

# COMMANDS ARE EXECUTED WHEN IMAGE IS MADE
RUN echo "YO DOCKER!!!!!"
RUN apt-get update

# SETIING THE FILE PATH FOR THE FILE
WORKDIR /usr/amsu
RUN touch dummy.txt

COPY ./noted.md .

ADD https://github.com/amsu21/AW-LFG-Bootcamp-2023.git .

# PRINTING TO THE CONSOLE
CMD [ "echo", "THIS IS CMD!" ]