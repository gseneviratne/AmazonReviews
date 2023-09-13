#!/usr/bin/python3
import os 

#go to the directory /data_ingestion/logstash and run the command: docker build . -t tap:logstash

os.system("docker build ./logstash -t tap:logstash")
os.system("docker build ./kafka -t tap:kafka")
os.system("docker build ./spark -t tap:spark")
os.system("docker build ./kibana -t tap:kibana")
os.system("docker build ./Scraper -t tap:scraper")
os.system("docker build ./DetectAI -t tap:detectai")
