FROM debian:bookworm-slim

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install mariadb-client -y
RUN pip install mysql-connector-python==8.0.29 --break-system-packages
RUN pip install requests --break-system-packages

CMD while : ; do sleep 1000; done