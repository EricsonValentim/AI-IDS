# SmartIDS - version 1.4
Methodology AI/IDS

A Methodology to verify IDS AI-basedApproaches on Emulated Networks

This project shares with the academic community the methodology to evaluate machine learning and deep learning techniques in Intrusion Detection Systems.


The virtual machines used in the project are available for download through the link below in the Google Drive repository.
https://drive.google.com/drive/folders/1hSm_f8KMQ8OnMLjIvOQyZ6wNN-5ykEj2?usp=sharing

A detailed example for expert users is available along with the output file preprocessing step of the CICFlowMeter tool.



Dataset used to create predefined templates: CSE-CIC-IDS2018

The data used to train the classifier is taken from the CSE-CIC-IDS2018 dataset provided by the Canadian Institute of Cyber Security. It was created by capturing all network traffic during ten days of operation within a controlled network environment on AWS, where realistic background traffic and different attack scenarios were conducted. As a result, the dataset contains both benign network traffic and captures of the most common network attacks. The dataset is composed of raw network captures in pcap format as well as csv files created using CICFlowMeter-V3 containing 80 stats of the individual network flows combined with their corresponding labels. A network flow is defined as an aggregation of interrelated network packets identified by the following properties:

source IP
destination IP
source port
destination port
Protocol
The dataset contains approximately 16 million individual network streams and covers the following attack scenarios:

Brute force
From,
Ddos
heartbleed,
Web Attack,
Infiltration,
Botnet.

https://www.unb.ca/cic/datasets/ids-2018.html
