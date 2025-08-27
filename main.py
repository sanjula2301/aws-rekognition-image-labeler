import argparse
import json
from pathlib import Path
import boto3
import pandas as pd

from label_images import s3_list_images, detect_labels_for_s3_object, flatten_labels  # if split; else merge into one file

def main():
    parser = argparse.ArgumentParser(description="Generate labels for images in S3 via Rekognition.")
    parser.add_argument("--bucket", required=True, help="S3 bucket name")
    parser.add_argument("--prefix", default="input/", help="S3 prefix containing images")
    parser.add_argument("--region", required=True, help="AWS region where BOTH S3 bucket and Rekognition exist (e.g., ap-south-1)")
    parser.add_argument("--max-labels", type=int, default=10)
    parser.add_argument("--min-conf", type=float, default=70.0)
    parser.add_argument("--out", default="labels")
    args = parser.parse_args()

    s3 = boto3.client("s3", region_name=args.region)
    rekognition = boto3.client("rekognition", region_name=args.region)

    keys = s3_list_images(s3, args.bucket, args.prefix)
    if not keys:
        print("No images found.")
        return

    rows = []
    for i, key in enumerate(keys, start=1):
        try:
            resp = detect_labels_for_s3_object(rekognition, args.bucket, key,
                                               max_labels=args.max_labels, min_conf=args.min_conf)
            rows.extend(flatten_labels(resp, args.bucket, key))
            print(f"[{i}/{len(keys)}] {key} -> {len(resp.get('Labels', []))} labels")
        except Exception as e:
            print(f"Error on {key}: {e}")

    # Save CSV & JSON
    out_dir = Path(args.out); out_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows)
    csv_path = out_dir / "labels.csv"
    json_path = out_dir / "labels.json"

    df.to_csv(csv_path, index=False)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    print(f"Saved:\n - {csv_path}\n - {json_path}")

if __name__ == "__main__":
    main()
