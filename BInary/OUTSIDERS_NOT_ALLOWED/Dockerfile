FROM ubuntu:20.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y \
    binutils \
    gcc-multilib \
    xinetd

RUN apt-get install -y sudo
RUN apt-get install -y python3 python3-pip
RUN pip3 install pwntools
RUN useradd -m iitjctf
RUN echo 'root:hello' | chpasswd
RUN echo 'iitjctf:hello' | chpasswd
WORKDIR /home/iitjctf
RUN mkdir /home/iitjctf/OUTSIDERS_NOT_ALLOWED
COPY ./0UtS1d3RS_N0T_@LL0w3d.c /home/iitjctf/OUTSIDERS_NOT_ALLOWED/0UtS1d3RS_N0T_@LL0w3d.c
COPY ./flag.txt /home/iitjctf/OUTSIDERS_NOT_ALLOWED/flag.txt

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

WORKDIR /home/iitjctf/OUTSIDERS_NOT_ALLOWED

RUN chown root:root flag.txt
RUN chmod 640 flag.txt
RUN gcc 0UtS1d3RS_N0T_@LL0w3d.c -o bin -fno-stack-protector -z execstack -no-pie
RUN chmod u+s bin
RUN rm 0UtS1d3RS_N0T_@LL0w3d.c 
RUN strip bin
USER iitjctf

CMD ["bash"]

EXPOSE 9999
