def filter_jobs(jobs, keyword):
    return [
        job for job in jobs
        if keyword in job["title"].lower()
    ]