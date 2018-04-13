FROM gliderlabs/alpine

RUN apk --no-cache add build-base

ADD main.cpp .
ADD test.cpp .

CMD g++ test.cpp -o test -O2 -std=c++14 2> /out/out.txt && ./test > /out/out.txt
