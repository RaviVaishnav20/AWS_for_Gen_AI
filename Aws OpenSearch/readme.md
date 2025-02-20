### OpenSearch Python Client AWS Domain Remote Authentication Example
Authenticating to a remote domain or cluster from within Python has been quite challenging, but it now works following these steps. 


https://docs.aws.amazon.com/opensearch-service/latest/developerguide/request-signing.html#request-signing-python

https://www.instaclustr.com/support/documentation/opensearch/using-opensearch/connecting-to-opensearch-with-python/


1. Create an Iam User with permissions for the OpenSearch service
2. Copy the arn for this user: arn:aws:iam::840560325987:user/boto3user
3. Under the OpenSearch domain that was created > Security Config > Edit > Set IAM ARN as master user (paste in ARN)
4. Install the boto3 python package
5. Modify the config and credentials files: .aws/config and credentials 
6. Add in the access key and secret access key ids, also set the default region for boto3 - make sure this is the same region as your OpenSearch domain is located in
7. Once we have a solid boto3 client set up, we can confirm it's able to authN to our AWS account (boto3_test.py)
8. Run opensearch_main.py to see how we are now able to create an index in our remote cluster with Python on the local machine.
