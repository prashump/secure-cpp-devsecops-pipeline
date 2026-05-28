FROM amazonlinux:2023

WORKDIR /app

COPY build/app .

CMD ["./app"]
