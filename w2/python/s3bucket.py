import sys
import boto3


try:
    def main():
        ''' runing create function from main function
        '''
        create_s3bucket(bucket_name)
        
except Exception as exeption:
    print(exeption)

def create_s3bucket(bucket_name):
    '''creating bucket
    '''
    s3_bucket= boto3.client(
        's3',
    )

    bucket = s3_bucket.create_bucket(
        Bucket=bucket_name,
        ACL='private'
    )

    print(bucket)

bucket_name = sys.argv[1]

if __name__=='__main__':
    main()
    