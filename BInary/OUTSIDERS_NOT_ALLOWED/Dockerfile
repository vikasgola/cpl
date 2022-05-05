FROM gcc:4.9
RUN mkdir /usr/challenge/OUTSIDERS_NOT_ALLOWED
COPY ./0UtS1d3RS_N0T_@LL0w3d.c /usr/challenge/0UtS1d3RS_N0T_@LL0w3d.c
COPY ./flag.txt /usr/challenge/flag.txt
WORKDIR /usr/challenge/OUTSIDERS_NOT_ALLOWED
RUN gcc 0UtS1d3RS_N0T_@LL0w3d.c -o bin -fno-stack-protector -m32 -z execstack -no-pie
RUN strip bin
CMD ["./bin"]
