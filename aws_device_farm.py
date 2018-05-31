import boto3

AWS_ACCESS_KEY = ""
AWS_SECRET_ACCESS_KEY = ""


def get_all_runs():

    client = boto3.client('devicefarm',
                          region_name='us-west-2',
                          aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    response = client.list_projects()

    for project in response['projects']:
        project_arn = str(project['arn']).encode('utf-8')
        runs = client.list_runs(arn=project_arn)

        # file_upload = client.create_upload(projectArn=project_arn,
        #                                   name='app-debug.apk',
        #                                   type='ANDROID_APP',
        #                                   contentType='application/octet-stream')

        uploads = client.list_uploads(arn=project_arn)
        for run in runs['runs']:
            print(str(run['result']).encode('utf-8'))
        for upload in uploads['uploads']:
            print(str(upload['arn']).encode('utf-8'))
            detailed_upload = client.get_upload(arn=str(upload['arn']).encode('utf-8'))
            for upload_detail in detailed_upload['upload']:
                print(str(upload_detail.encode('utf-8')))



get_all_runs()
