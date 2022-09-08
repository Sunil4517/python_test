
•	Step 1 :  Create a GITHUB repository
o	Created a public repository with the name python_test
o	Pushed my code changes from local to this remote repo
o	No issues faced
o	Created a Circle ci account and integrated the created repo by adding the ;
o	.cricleci/config.yml template for the workflow
•	Step 2 
o	Created a ECR repo with name python_test in my aws account via console
•	Step 3
o	Created a Docker file, added the required python code (helloworld.py)  & pushed to the github repo
•	Step 4 
o	Configured the Circle CI  pipeline by adding the required access key secret key ,region and ecr account url in the Environment variables of the project
o	The circle ci has the below steps
1.	Setting up a CircleCI pipeline using the aws-ecr orb - circleci/aws-ecr@7.0.0
2.	 The aws-ecr orb comes pre-packaged with commands to:
•	 Build an image Tag the image (using the Git commit hash of the HEAD == CIRCLE_SHA1 ) ,
•	 Login to Amazon ECR 
•	Push an image to Amazon ECR
o	Issues faced: Configuration issues like if you don’t pass the any of the environment variables, job used to fail. Resolved by passing the correct values.
•	Step 5 
o	Created the below resources for AWS batch
1.	Compute environment (to decide which type. I chose EC2 optimal type) the compute resources that run your Jobs. Environments can be configured to be managed by AWS or on your own as well as the number of and type(s) of instances on which Jobs will run. You can also allow AWS to select the right instance type.
2.	Job Queue : listing of work to be completed by your Jobs. You can leverage multiple queues with different priority levels.
3.	Job definition : describes how your work is be executed, including the CPU and memory requirements and IAM role that provides access to other AWS services
4.	Job : the unit of work submitted to AWS Batch, whether it be implemented as a shell script, executable, or Docker container image.
o	Issues faced :   
1.	Initially I  did not give the proper IAM permissions for the ECS task execution role which will call the AWS services on behalf of us to do the required API operations 
2.	I ran into “Jobs Stuck in RUNNABLE Status” due not using the aforementioned instance role.
3.	Attached the proper policies/permissions for that role in order to work correctly
o	Created CloudWatch event rule which will trigger the AWS batch job whenever the new Image with Latest tag has been pushed to the ECR repository
o	Source
 
Target resource
 
Issues faced: Gave the ECR repo URL instead of the repo name where the AWS batch job did not get trigger
•	Step 6: Workflow will be as follows
o	Whenever you commit any code in the Github, it will trigger the Circle ci pipeline which builds the image and pushes to the Amazon ECR in the existing repository,
o	Cloudwatch event rule (trigger batch job on ecr images latest tag push) will get triggered and initiates the batch job

Bonus 1:
1.	Need to configure the proper permissions to write data to Dyanamo Db Table
2.	Write any  Python-based program reads the contents of the cloudwatch logs , parses each row, and updates an Amazon DynamoDB table.
3.	Amazon DynamoDB stores each processed row from the CSV.
4.	Reference documentation : https://aws.amazon.com/blogs/compute/orchestrating-an-application-process-with-aws-batch-using-aws-cloudformation/
Bonus 2 :
1.	Yes, you can install the data dog container as a side car container or in the same container definition which will fetch the custom metric pertains to the AWS batch job and send it to the data dog tool
2.	You can still send the live metric details from container to data dog












 
