# 🌿 Tranquil Garden Retreat – AWS Rekognition Project  

This project demonstrates how to build an **image recognition pipeline** using **AWS Rekognition**, **S3**, and **Python (Boto3)**.  
It showcases the ability to detect objects, labels, and scenes from uploaded images stored in an S3 bucket.  

---

## 🚀 Features  

- 📂 **Upload Images to S3** – Store images securely in an AWS S3 bucket.  
- 🖼 **Automated Label Detection** – Extract objects, categories, and scenes with AWS Rekognition.  
- 📊 **Results in CSV/JSON** – Store detection results for further analysis.  
- ⚡ **Serverless & Scalable** – Can be extended with AWS Lambda for automation.  
- 🔒 **Bucket Encryption** – S3 bucket secured with AES-256 encryption.  

---

## 🛠 Tech Stack  

- **AWS S3** – Image storage  
- **AWS Rekognition** – Image labeling & detection  
- **Boto3 (Python SDK)** – AWS interaction  
- **Pandas** – Data handling (CSV/JSON export)  
- **Jupyter Notebook / Python scripts** – Implementation  

---

## 📂 Project Structure  

Tranquil-Garden-Retreat/
│── label_images.py # Helper functions for Rekognition & S3
│── analyze_images.py # Main script for image analysis
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── results/
│ ├── labels.csv # Exported Rekognition results
│ └── labels.json # JSON format of results

yaml
Copy code

---

## ⚙️ Installation & Setup  

1. **Clone the Repository**  
   ```bash

Create a Virtual Environment (Optional but Recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Configure AWS CLI

bash
Copy code
aws configure
Provide:

AWS Access Key ID

AWS Secret Access Key

Default region (e.g., ap-south-1)

📌 Usage
Upload Images to S3

bash
Copy code
aws s3 cp ./images/ s3://my-rekognition-lab-xxxx/ --recursive
Run Image Labeling Script

bash
Copy code
python analyze_images.py
View Results

Labels in results/labels.csv

JSON output in results/labels.json

📊 Sample Output
Example detection from AWS Rekognition:

json
Copy code
[
  {
    "Name": "Garden",
    "Confidence": 98.7
  },
  {
    "Name": "Plant",
    "Confidence": 95.2
  },
  {
    "Name": "House",
    "Confidence": 88.4
  }
]
🌟 Why This Project is Valuable
Great example of cloud computing + AI integration

Demonstrates hands-on AWS skills (S3, Rekognition, IAM, encryption)

Strong showcase for software engineering interviews & LinkedIn portfolio

Can be extended into real-world applications like:

Security & surveillance

Automated tagging for e-commerce

Smart agriculture image analysis

📖 Future Improvements
🔄 Automate pipeline with AWS Lambda & Step Functions

📷 Extend to video analysis with Rekognition Video
