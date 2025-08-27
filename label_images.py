import json
import time
from pathlib import Path
from typing import List, Dict

import boto3
import pandas as pd

def s3_list_images(s3_client, bucket: str, prefix: str = "input/") -> List[str]:
    keys = []
    paginator = s3_client.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            if key.lower().endswith((".jpg", ".jpeg", ".png")):
                keys.append(key)
    return keys

def detect_labels_for_s3_object(reko_client, bucket: str, key: str,
                                max_labels: int = 10, min_conf: float = 70.0) -> Dict:
    resp = reko_client.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": key}},
        MaxLabels=max_labels,
        MinConfidence=min_conf,
        Features=["GENERAL_LABEL"]  # add "IMAGE_PROPERTIES" if you also want properties (billed separately)
    )
    return resp

def flatten_labels(resp: Dict, bucket: str, key: str) -> List[Dict]:
    out = []
    ts = int(time.time())
    for lbl in resp.get("Labels", []):
        out.append({
            "bucket": bucket,
            "key": key,
            "label": lbl.get("Name"),
            "confidence": round(lbl.get("Confidence", 0.0), 2),
            "timestamp": ts
        })
    return out
