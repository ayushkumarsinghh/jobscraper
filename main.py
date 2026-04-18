from scraper.fetcher import fetch_page
from scraper.parser import parse_jobs
from scraper.filter import filter_jobs
from utils.saver import save_to_csv

def main():
    keyword = input("Enter job keyword (e.g. python, backend): ").lower()

    html = fetch_page()
    jobs = parse_jobs(html)
    filtered = filter_jobs(jobs, keyword)

    print(f"\nFound {len(filtered)} jobs:\n")

    for job in filtered:
        print(f"{job['title']} - {job['company']}")
        print(job["link"])
        print("-" * 40)

    save_to_csv(filtered)
    print("\nSaved to jobs.csv")

if __name__ == "__main__":
    main()