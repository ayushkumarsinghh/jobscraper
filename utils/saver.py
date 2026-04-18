import csv

def save_to_csv(jobs):
    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "company", "link"])
        writer.writeheader()
        writer.writerows(jobs)