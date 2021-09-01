# AI/IDS - version 1.4

A Methodology to verify IDS AI-basedApproaches on Emulated Networks

This project shares with the academic community the methodology to evaluate machine learning and deep learning techniques in Intrusion Detection Systems.

Internet traffic has been growing in recent years and, with the advent of the pandemic that devastates the world, it increases the role in activities related to health, communication, economy, social and so on. Constantly changing cybersecurity environments, resource scarcity and a lack of skilled employees has prompted companies to look for off-shelf AI-enabled cybersecurity solutions to meet ever-evolving requirements. Intrusion Detection Systems(IDSs) still need to improve detection accuracy and reduce false alarm rates. This work presents a testbed to test and validate AI-based IDS approaches. The aim is to allow researchers and IDS developers to verify whether their solutions are effective in a fast and comparative way. In order to analyse both AI method and available reused or produced datasets, this paper presents a testbed based on emulated network that provides an environment for rapidly prototyping the solution. As a result, we have a scalable, high-level interface environment that enables community focuses on their approach with less worries about test environment issues.


A detailed example for expert users is available along with the output file preprocessing step of the ![CICFlowMeter](https://github.com/ahlashkari/CICFlowMeter) tool.



Dataset used to create predefined templates: [CSE-CIC-IDS2018](https://www.unb.ca/cic/datasets/ids-2018.html)

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


## Minimum Requirements

To install and run the virtual environment, the following hardware requirements are required as a minimum.

- 150GB of storage 
- 16 GB of RAM memory
- Intel (core I3 3 generation) or AMD 4-core processor
- Ethernet network card


It is recommended to use Windows 10 PRO operating system.

## Download and Install

The virtual machines, emulated environment project (GNS3) and software used in the project are available for download via the link below in the 
[Google Drive repository](https://drive.google.com/drive/folders/1hSm_f8KMQ8OnMLjIvOQyZ6wNN-5ykEj2?usp=sharing
)

By downloading the entire repository and installing the software. You need to adjust the virtual hardware settings on each VM as per your needs. For example the VM IDS comes configured with 16 GB of RAM memory and 3 virtual processors. We recommend using at least 4 GB on this VM. The others can run with at least 1.5 GB of memory. Remember that this process must be performed in Virtual Box and in GNS3.

The host computer's network interface must be publicly shared to access the Internet through the virtual environment.

The virtual environment has the following Architecture

![ScreenShot](https://i.ibb.co/zPXtTFJ/topologia.png)

The nodes will be responsible for simulating cyber attacks both for the LAN network and for any of the DMZ servers (WEB or SGBD). A VM based on the Kali Linux distribution has the system tools pre-installed and we've added some other parts of the solution, like the anaconda package python3, scapy to generate custom data packages according to the desired attack type and slowloris script to generate denial service and CICFlowMeter type attacks.

The main component in this scenario is the IDS. It is a Linux VM with 16 GB of memory and three virtual processors, being responsible for checking network traffic and detecting possible intrusions through the CICFlowMeter tool, as well as a tool to manage ML or DL models and relational database to store information from detection for further evaluation.

IDS has 3 network interfaces. One for connecting to the external router, one for the DMZ network where the local servers are located and the last interface for connecting to the LAN where the user devices are located.

The DMZ is composed of two VMs, both with Linux operating system. The WEB server is a VM running apache2. SGBD is a VM that runs the following services: apache2, sshd, ftpd and mysql. LAN devices are additional components that allow you to simulate a real-world environment.

Remembering that the entire virtual environment is perfectly adaptable and scalable according to the user's needs. If any adjustment is necessary, just configure the new devices with the appropriate network range. More details are available in the project topology figure.



## VM Ubuntu IDS

This VM is located at the core of the virtual environment.
It also manages all network traffic entering or leaving the DMZ or LAN.
It is responsible for performing the capture of network traffic to generate new data sets through the
CICFlowMeter tool that converts these network streams and outputs a file in .CSV format
which is used for training and testing AI techniques. It has the graphical interface that was developed
to facilitate the application of AI techniques for IDS.

Start the script with network routes:
```sh
cd /home/ubunutu
./script
```
The steps that are performed by this VM are described in General Flowchart

![ScreenShot](https://i.ibb.co/pfbGBQs/fluxo-Geral.png)

Run CICFlowMeter tool:
```sh
cd /home/ubunutu/CICFlowMeter-master
gradle execute
```

Choose operating mode: Offline or Realtime. In Offline mode the tool receives a capture of network traffic
in .PCAP format and in Realtime mode the capture starts in real time after choosing the network interface. In both modes the output
The tool generates a .CSV file containing 84 resources of the analyzed network traffic and a Label field that is used as the target class
during training and testing of AI techniques.

![ScreenShot](https://i.ibb.co/hZFgrSk/CICFlow-Meter.png)

The tool's output .CSV files are available in the directory `/home/ubunutu/CICFlowMeter-master/data/daily`

To create new datasets it is necessary to label the .CSV file that CICFlowMeter generated. By default the Label field is set to:
"No Label". In the directory `/home/ubunutu/IDS` is a simple script to label the file. Otherwise the user can
use any of the CSE-CIC-IDS2018 files.
```sh
cd /home/ubunutu/IDS
nano labeled.py
```

Label is set to binary. Change the input path and the conversion function should be commented out according to the file's traffic type. "0" for Benign type network traffic and
"1" for malicious network traffic.

Through the developed graphical interface smartIDS it is possible to run the tests in an easier way.
This does not prevent use and modification by advanced users.


The interface is divided into 2 modes of operation: simple and advanced.

#Simple Mode

The simple mode has 4 techniques that were previously trained and tested with the aid of CSE-CIC-IDS2018.
In this mode, the user tests his datasets by choosing the type of network traffic Attacks and predefined models:
Random Forest, K-Nearest Neighbors, Naive Bayes or Multi Layer Perceptron.

After choosing the type of attack and model, load the .CSV file generated by the CICFlowMeter tool and start execution.

Execution of the graphical interface in simple mode:
```sh
cd /home/ubunutu/IDS
python3 smartIDS-Simple.py
```

![ScreenShot](https://i.ibb.co/WH18K1M/Smart-IDS-Simple.png)

#Advanced Mode

In this mode the user can load a model in .pkl format that has been trained and tested beforehand. Packages must be preinstalled with the pip install command.
Specific Imports must be inserted directly into the smartIDS-Advanced interface code.

Initially it is necessary to train and evaluate your model before carrying out the loading. The CSE-CIC-IDS2018 dataset,
  a dataset generated in the virtual environment containing the network capture between the Kali VM running the 'Slowloris' script to generate DOS attacks and the WEB VM with about 80,000 records and examples of training and validation of predefined models is available at `/home/ubuntu/IDS` directory.

In the project's Google Drive, we make available a dataset containing network traffic of the Benigno type for training and testing the user-customized models. During project development new datasets will be added to Google Drive. You need to download and upload them to VM IDS.

  After performing the training and exporting your model in .pkl format, following the project examples, just start the interface in advanced mode and load your model.

Execution of the graphical interface in advanced mode:
```sh
cd /home/ubunutu/IDS
python3 smartIDS-Advanced.py
```

![ScreenShot](https://i.ibb.co/3rjQb68/Smart-IDS-Advanced.png)

The results in both modes are displayed in the run panel and can be exported in .txt, .json formats and saved in the Mysql database installed on the VM IDS. Access is via PHPmyAdmin.

Results: 

- Probability of benign type network traffic
- Probability of attack type network traffic
- Rating counter
- Date.

## VM Kali Linux

Kali Linux is a GNU/Linux distribution based on Debian, considered to be the successor of Back Track. The project features several improvements as well as more apps. It is primarily aimed at auditing and general computer security. It is developed and maintained by Offensive Security Ltd.

More information about how to use Kali Linux tools, refer to the [Kali tools documentation](https://www.kali.org/tools/).

This VM is located in the attack network.
Responsible for executing attacks for IDS, server and DMZ services (WEB and SGBD) and LAN. This system has several tools installed to perform network intrusion tests.

## VM Ubuntu WEB, VM Ubuntu SGBD and LAN

The Ubuntu WEB VM has Apache2, SSH and FTP services installed. A generic website has been added to Apache2 for testing.

The Ubuntu SGBD VM has Apache2, Mysql, PHPmyAdmin, SSH and FTP services installed.

The LAN has only two virtual PC's own GNS3 software. In specific cases the user can install a new VM according to his testing needs. 
Just adjust static network settings in range 10.0.0.0/8 for 10.0.0.1 gateway to VM IDS interface.

## Recommendations

As the project is constantly evolving. We always suggest updating the codes directly on the VM IDS with the codes that are posted in our GitHub project.
