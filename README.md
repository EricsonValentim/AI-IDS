# AI/IDS - version 1.4
Methodology AI/IDS

A Methodology to verify IDS AI-basedApproaches on Emulated Networks

This project shares with the academic community the methodology to evaluate machine learning and deep learning techniques in Intrusion Detection Systems.

Internet traffic has been growing in recent years and, with the advent of the pandemic that devastates the world, it increases the role in activities related to health, communication, economy, social and so on. Constantly changing cybersecurity environments, resource scarcity and a lack of skilled employees has prompted companies to look for off-shelf AI-enabled cybersecurity solutions to meet ever-evolving requirements. Intrusion Detection Systems(IDSs) still need to improve detection accuracy and reduce false alarm rates. This work presents a testbed to test and validate AI-based IDS approaches. The aim is to allow researchers and IDS developers to verify whether their solutions are effective in a fast and comparative way. In order to analyse both AI method and available reused or produced datasets, this paper presents a testbed based on emulated network that provides an environment for rapidly prototyping the solution. As a result, we have a scalable, high-level interface environment that enables community focuses on their approach with less worries about test environment issues.


A detailed example for expert users is available along with the output file preprocessing step of the CICFlowMeter tool.



Dataset used to create predefined templates: CSE-CIC-IDS2018

The data used to train the classifier is taken from the CSE-CIC-IDS2018 dataset provided by the Canadian Institute of Cyber Security. It was created by capturing all network traffic during ten days of operation within a controlled network environment on AWS, where realistic background traffic and different attack scenarios were conducted. As a result, the dataset contains both benign network traffic and captures of the most common network attacks. The dataset is composed of raw network captures in pcap format as well as csv files created using CICFlowMeter-V3 containing 80 stats of the individual network flows combined with their corresponding labels. A network flow is defined as an aggregation of interrelated network packets identified by the following properties:

- Source IP
- Destination IP
- Source port
- Destination port
- Protocol

The dataset contains approximately 16 million individual network streams and covers the following attack scenarios:

- Brute force
- DDOS
- Heartbleed
- Web Attack
- Infiltration
- Botnet

https://www.unb.ca/cic/datasets/ids-2018.html


## Download and Install

The virtual machines, emulated environment project (GNS3) and software used in the project are available for download via the link below in the Google Drive repository.
https://drive.google.com/drive/folders/1hSm_f8KMQ8OnMLjIvOQyZ6wNN-5ykEj2?usp=sharing

By downloading the entire repository and installing the software. You need to adjust the virtual hardware settings on each VM as per your needs. For example the VM IDS comes configured with 16 GB of RAM memory and 3 virtual processors. We recommend using at least 4 GB on this VM. The others can run with at least 1.5 GB of memory. Remember that this process must be performed in Virtual Box and in GNS3.

The host computer's network interface must be publicly shared to access the Internet through the virtual environment.

The virtual environment has the following architecture:

The nodes will be responsible for simulating cyber attacks both for the LAN network and for any of the DMZ servers (WEB or SGBD). A VM based on the Kali Linux distribution has the system tools pre-installed and we've added some other parts of the solution, like the anaconda package python3, scapy to generate custom data packages according to the desired attack type and slowloris script to generate denial service and CICFlowMeter type attacks.

The main component in this scenario is the IDS. It is a Linux VM with 16 GB of memory and three virtual processors, being responsible for checking network traffic and detecting possible intrusions through the CICFlowMeter tool, as well as a tool to manage ML or DL models and relational database to store information from detection for further evaluation.

IDS has 3 network interfaces. One for connecting to the external router, one for the DMZ network where the local servers are located and the last interface for connecting to the LAN where the user devices are located.

The DMZ is composed of two VMs, both with Linux operating system. The WEB server is a VM running apache2. SGBD is a VM that runs the following services: apache2, sshd, ftpd and mysql. LAN devices are additional components that allow you to simulate a real-world environment.

Remembering that the entire virtual environment is perfectly adaptable and scalable according to the user's needs. If any adjustment is necessary, just configure the new devices with the appropriate network range. More details are available in the project topology figure.


## VM IDS

Esta VM está localizada no núcleo do ambiente virtual. Ele também gerencia todo o tráfego de rede que entra ou saí da DMZ ou LAN. É responsável por executar a captura do tráfego de rede para gerar novos cojuntos de dados através da ferramenta CICFlowMeter que converte esses fluxos de rede e extraí como saída um arquivo no formato .CSV que é utuilizado para treinamento e teste das técnicas de AI. Possui a interface gráfica que foi desenvolvida para facilitar a utilização das técnicas de AI para IDS.

Start the script with network routes:
```sh
cd /home/ubunutu
sudo ./script
```


Executar ferramenta CICFlowMeter 

## VM Kali Linux

Esta VM está localizada na rede de ataque. Onde é possível executar ataques para o IDS, servidor e serviços da DMZ (WEB e SGBD) e LAN. 






