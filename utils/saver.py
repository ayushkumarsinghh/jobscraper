import csv
import os

def save_to_csv(jobs):
    file_exists = os.path.isfile("jobs.csv") and os.path.getsize("jobs.csv") > 0
    with open("jobs.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "company", "link"])
        if not file_exists:
            writer.writeheader()
        writer.writerows(jobs)