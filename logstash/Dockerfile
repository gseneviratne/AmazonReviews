FROM docker.elastic.co/logstash/logstash:8.7.0
ADD ./pipeline/reviews.conf /usr/share/logstash/pipeline/logstash.conf

# Add your logstash plugins setup here
RUN logstash-plugin install logstash-filter-sentimentalizer

# to build with
# docker build . --tag tap:logstash
# and run with
# docker run --network tap --rm -it --name logstash -p 8081:8080 -v $PWD/pipeline/reviews.conf:/usr/share/logstash/pipeline/logstash.conf tap:logstash
# make sure that pipeline dir with proper conf is there%
