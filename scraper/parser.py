def parse_jobs(data):
    jobs = []
    
    # If data is empty or invalid
    if not data or not isinstance(data, list):
        return jobs

    for item in data:
        # Skip the first item which is usually the legal terms
        if "legal" in item:
            continue
            
        jobs.append({
            "title": item.get("position", "Unknown"),
            "company": item.get("company", "Unknown"),
            "link": item.get("url", item.get("apply_url", "No link"))
        })

    return jobs