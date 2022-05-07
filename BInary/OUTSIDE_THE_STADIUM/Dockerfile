FROM ubuntu:20.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y \
    binutils \
    gcc \
    xinetd 

RUN apt-get install -y sudo
RUN apt-get install -y python3 python3-pip 
RUN pip3 install pwntools
     
RUN useradd -m iitjctf 
RUN echo 'root:hello' | chpasswd
RUN echo 'iitjctf:hello' | chpasswd
WORKDIR /home/iitjctf
RUN mkdir /home/iitjctf/OUTSIDE_THE_STADIUM
COPY ./SM@SH_A_S1X.c /home/iitjctf/OUTSIDE_THE_STADIUM/SM@SH_A_S1X.c
COPY ./flag.txt /home/iitjctf/OUTSIDE_THE_STADIUM/flag.txt
WORKDIR /home/iitjctf/OUTSIDE_THE_STADIUM
RUN chown root:root flag.txt
RUN chmod 640 flag.txt 
RUN gcc SM@SH_A_S1X.c -o bin -fno-stack-protector -z execstack -no-pie
RUN chmod u+s bin
RUN rm SM@SH_A_S1X.c
RUN strip bin
USER iitjctf

CMD ["bash"]
EXPOSE 8001
