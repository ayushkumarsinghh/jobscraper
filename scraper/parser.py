from bs4 import BeautifulSoup

def parse_jobs(html):
    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    rows = soup.find_all("tr", class_="job")

    for job in rows:
        title = job.find("h2")
        company = job.find("h3")
        link_tag = job.find("a", class_="preventLink")

        if title and company and link_tag:
            jobs.append({
                "title": title.text.strip(),
                "company": company.text.strip(),
                "link": "https://remoteok.com" + link_tag["href"]
            })

    return jobs