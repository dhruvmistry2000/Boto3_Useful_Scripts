import boto3

def delete_all_glue_jobs():
    regions = boto3.Session().get_available_regions('glue')

    for region in regions:
        glue = boto3.client('glue', region_name=region)
        response = glue.get_jobs()

        for job in response['Jobs']:
            job_name = job['Name']
            print(f"Deleting job {job_name} in region {region}")
            glue.delete_job(JobName=job_name)

if __name__ == "__main__":
    delete_all_glue_jobs()
