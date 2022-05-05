FROM gcc:4.9
RUN mkdir /usr/challenge/OUTSIDE_THE_STADIUM
COPY ./SM@SH_A_S1X.c /usr/challenge/OUTSIDE_THE_STADIUM/SM@SH_A_S1X.c
COPY ./flag.txt /usr/challenge/OUTSIDE_THE_STADIUM/flag.txt
WORKDIR /usr/challenge/OUTSIDE_THE_STADIUM
RUN gcc SM@SH_A_S1X.c -o bin -fno-stack-protector -m32 -z execstack -no-pie
RUN strip bin
CMD ["./bin"]
