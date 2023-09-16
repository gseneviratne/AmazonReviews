#!/usr/bin/python3
import os 

#go to the directory /data_ingestion/logstash and run the command: docker build . -t tap:logstash

os.system("minikube image build ./logstash -t tap:logstash")
os.system("minikube image build ./kubernetes/kafka -t tap:kafka")
os.system("minikube image build ./kubernetes/spark -t tap:spark")
os.system("minikube image build ./kibana -t tap:kibana")
os.system("minikube image build ./Scraper -t tap:scraper")
#os.system("minikube build ./DetectAI -t tap:detectai")
