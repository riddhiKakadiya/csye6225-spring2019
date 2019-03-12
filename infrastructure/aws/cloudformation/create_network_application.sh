#!/bin/bash

#Exit immediately if a command exits with a non-zero exit status.
set -e
##Check if enough arguements are passed
if [ $# -lt 1 ]; then
  echo "Please provide network stack name ! Try Again."
  echo "e.g. ./csye6225-aws-cf-create-stack.sh <STACK_NAME> <NETWORK_STACK> <AMI_ID> <KEY_PAIR>"
  exit 1
fi

if [ $# -lt 2 ]; then
  echo "Please provide application stack name ! Try Again."
  echo "e.g. ./csye6225-aws-cf-create-stack.sh <STACK_NAME> <NETWORK_STACK> <AMI_ID> <KEY_PAIR>"
  exit 1
fi

if [ $# -lt 3 ]; then
  echo "Please provide Key Pair ! Try Again."
  echo "e.g. ./csye6225-aws-cf-create-stack.sh <STACK_NAME> <NETWORK_STACK> <AMI_ID> <KEY_PAIR>"
  exit 1
fi

IMAGE_ID=$(aws ec2 describe-images --owners self --query 'sort_by(Images, &CreationDate)[].ImageId' | jq -r '.[0]')

S3_BUCKET=$(aws s3api list-buckets | jq -r '.Buckets[] | select(.Name | startswith("code-deploy")).Name')

./csye6225-aws-cf-create-stack.sh $1

./csye6225-aws-cf-create-application-stack.sh $2 $1 $IMAGE_ID $3 $S3_BUCKET

cd ../../../webapp
zip -r --exclude=*djangoEnv* ../webapp.zip *

cd ..

aws s3 cp webapp.zip s3://$S3_BUCKET

aws configure set region us-east-1 && aws deploy create-deployment --application-name csye6225-webapp --deployment-config-name CodeDeployDefault.OneAtATime --deployment-group-name csye6225-webapp-deployment --description "Deployment From creation" --s3-location bucket=$S3_BUCKET,bundleType=zip,key=webapp.zip

rm webapp.zip
cd infrastructure/aws/cloudformation