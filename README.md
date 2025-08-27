
## An AWS Rekognition Project

This project demonstrates how to build an automated image recognition pipeline using **AWS Rekognition**, **S3**, and **Python (Boto3)**. It showcases the ability to detect objects, labels, and scenes from images uploaded to an S3 bucket.

-----


## 🚀 Features

  - 📂 **Upload Images to S3**: Store images securely and durably in an AWS S3 bucket.
  - 🖼️ **Automated Label Detection**: Extract objects, categories, and scenes automatically with AWS Rekognition.
  - 📊 **Results in CSV/JSON**: Store detection results in structured formats for further analysis.
  - ⚡ **Serverless & Scalable**: Designed to be easily extended with AWS Lambda for a fully automated, serverless workflow.
  - 🔒 **Bucket Encryption**: S3 bucket is secured with AES-256 encryption by default.

-----

## 🛠 Tech Stack

  - **AWS S3**: For scalable object storage.
  - **AWS Rekognition**: For AI-powered image analysis.
  - **Boto3 (Python SDK)**: To interact with AWS services programmatically.
  - **Pandas**: For easy data handling and exporting results to CSV/JSON.
  - **Jupyter Notebook / Python**: For implementation and scripting.

-----

## 📂 Project Structure

```
Tranquil-Garden-Retreat/
│
├── label_images.py         # Helper functions for Rekognition & S3
├── analyze_images.py       # Main script for image analysis
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
└── results/
    ├── labels.csv          # Exported Rekognition results
    └── labels.json         # JSON format of results
```

-----

## ⚙️ Installation & Setup

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/<your-username>/aws-rekognition-image-labeler.git
    cd aws-rekognition-image-labeler
    ```

2.  **Create a Virtual Environment** (Optional but Recommended)

    ```bash
    # For Linux/Mac
    python -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure AWS CLI**
    If you haven't already, configure your AWS credentials.

    ```bash
    aws configure
    ```

    You will be prompted to provide:

      - `AWS Access Key ID`
      - `AWS Secret Access Key`
      - `Default region` (e.g., `ap-south-1`)
      - `Default output format` (e.g., `json`)

-----

## 📌 Usage

1.  **Upload Images to S3**
    Replace `my-rekognition-lab-xxxx` with your unique S3 bucket name.

    ```bash
    aws s3 cp ./images/ s3://my-rekognition-lab-xxxx/ --recursive
    ```

2.  **Run Image Labeling Script**
    Execute the main analysis script.

    ```bash
    python analyze_images.py
    ```

3.  **View Results**
    The script will generate the analysis results in the `results/` directory:

      - **JSON**: `results/labels.json`

-----

## 📊 Sample Output

Here is an example of the JSON output from AWS Rekognition for a single image:

```json
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
```



-----

## 📖 Future Improvements

  - 🔄 **Automate Pipeline**: Integrate **AWS Lambda** and **Step Functions** to trigger analysis automatically on image upload.
  - 🌐 **Web Dashboard**: Deploy the results on a **React** or **Flask** web dashboard for interactive visualization.
