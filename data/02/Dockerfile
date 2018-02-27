FROM gliderlabs/alpine

RUN apk --no-cache add build-base

ADD main.cpp .
ADD numbers.dat .
ADD test.py .

CMD g++ main.cpp -o test -O2 --std=c++14 2> /out/out.txt && python ./test.py > /out/out.txt
