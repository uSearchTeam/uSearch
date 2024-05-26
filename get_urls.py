from linkedin_api import Linkedin

def getEasyApplyURL() -> list[str]:
    """Takes input for the user about login information and job parameters and returns the URL of the matching LinkedIn EasyApply jobs found.
    """

    # Authenticate using any Linkedin account credentials
    email = input("Please enter LinkedIn email: ")
    password = input("Please enter LinkedIn password: ")
    api = Linkedin('pypypypypythonv2@gmail.com', 'Escalier82') # CHANGE THIS TO GET INPUT


    # Get job search parameters
    p = []
    print("\nWe will now perform the job search. Please answer the following questions or leave blank and press enter to omit parameters.")
    keywords = ["keywords", "company", "experience", "job type", "job title"]

    for keyword in keywords:
        parameter = input("Please enter " + keyword + ": ")
        p.append(parameter if parameter else None)


    # Get matching jobs
    try:
        jobs = api.search_jobs(p[0], p[1], p[2], p[3], p[4])
        if not jobs:
            print("No jobs found with those parameters.")
            exit(1)
    except:
        print("FAILED")
        exit(-1)

    # Iterate through jobs found
    MAXIMUM_JOBS = 10
    count = 0
    urls = []

    for job in jobs:
        job_id = job['trackingUrn'].replace("urn:li:jobPosting:", "")

        # Determine if it is easy apply
        try:
            api.get_job(job_id)['applyMethod']['com.linkedin.voyager.jobs.ComplexOnsiteApply']['easyApplyUrl']
            urls.append("https://www.linkedin.com/jobs/view/" + str(job_id))
            count += 1
            print(str(count) + "/" + str(MAXIMUM_JOBS))
            if count >= MAXIMUM_JOBS:
                break

        except KeyError:
            # Not an EasyApply job
            continue

    return urls

if __name__ == "__main__":
    print(getEasyApplyURL())