FROM gliderlabs/alpine

RUN apk --no-cache add build-base python

ADD main.cpp .
ADD book.txt .
ADD test.py .

CMD g++ main.cpp -o test -O2 --std=c++14 2> /out/out.txt && python ./test.py > /out/tmp.txt && mv /out/tmp.txt /out/out.txt
