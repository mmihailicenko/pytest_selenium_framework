FROM python:3.9

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN wget -O allure-2.14.0.tgz https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.14.0/allure-commandline-2.14.0.tgz && \
    tar -zxvf allure-2.14.0.tgz && \
    rm allure-2.14.0.tgz && \
    ln -s /app/allure-2.14.0/bin/allure /usr/local/bin/allure

ENV ALLURE_RESULTS_DIR=/app/allure-results
ENV ALLURE_REPORT_DIR=/app/allure-report

CMD ["bash", "-c", "pytest --alluredir=$ALLURE_RESULTS_DIR && allure generate $ALLURE_RESULTS_DIR -o $ALLURE_REPORT_DIR --clean"]
