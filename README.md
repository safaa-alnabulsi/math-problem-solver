
# Math problem solver

In this project we have three main http endpoints which perform the following calculation:
1. Fibonacci number F(n)
2. Ackermann function A(m,n)
3. Factorial of non-negative integer

## Prerequisites 

- Node.js
- Python 3.7
- Serverless Framework

    ```bash
    npm install serverless -g
    ```
- AWS account and user with programmatic access 

    For more info ceck "Configuring your local CLI with AWS" below.

## Development 

You can invoke the lambdas directly by running:

```bash
$ serverless invoke local --function factorial  --data '{"body": "{\"n\":\"4\"}"}'
{
    "statusCode": 200,
    "body": "\"24\""
}


$ serverless invoke local --function factorial  --data '{"n":"-4"}'
{
    "statusCode": 400,
    "body": "\"The value '-4' you entered is not a digit. The number must be a non negative integer.\""
}

$ serverless invoke local --function factorial  --data '{"n":"-4sd"}'
{
    "statusCode": 400,
    "body": "\"The value '-4sd' you entered is not a digit. The number must be a non negative integer.\""
}

$ serverless invoke local --function factorial
{
    "statusCode": 400,
    "body": "\"The value you entered is empty. The number must be a non negative integer\""
}
```

To invoke unit tests run:
```bash
 python3 -B -m pytest tests
```

## Deployment

In order to deploy all the endpoints to your aws account simply run

```bash
serverless deploy
```

This will create three endpoints which you can use directly:

```bash 
endpoints:
  POST - https://XXXXXXX.execute-api.eu-west-1.amazonaws.com/dev/factorial
  POST - https://XXXXXXX.execute-api.eu-west-1.amazonaws.com/dev/fibonacci
  POST - https://XXXXXXX.execute-api.eu-west-1.amazonaws.com/dev/ackermann
```

To deploy only the changed function code to AWS

```bash
sls update -v <function-name>
```

To remove all serverless functions and resources deployed to AWS

```bash
sls remove 
``` 

## Usage
Finally you can send an HTTP request directly to the endpoint using a tool like curl

```bash
curl -X POST -d '{"n":"4"}' https://XXXXXXX.execute-api.eu-west-1.amazonaws.com/dev/factorial
"24
```

## Monitoring

### Dashboards

Navigate to Cloudwatch in aws console -> Alerts Dashboard -> then click on dashaboad with same name as this project. 
You will see many metrics about the functions.

Note: you can also check the same data for each lambda by navigating via the aws console to the lambda UI, choosing the lambda and checking the Monitoring tab.

### Alerts

Each lambda function (endpoint) has been assigned with four alerts (provided by default by the plugin):
```
AckermannFunctionDurationAlarm		
AckermannFunctionErrorsAlarm
AckermannFunctionInvocationsAlarm
AckermannFunctionThrottlesAlarm	
```
Please change the email to your email in the serverless.yaml before deploying. 
After that, you will receive an email which asks you to confirm your subscription directly after you deploy the serverless for the first time. 
Note: you can check the default definition of these alerts by checking [this readme](https://github.com/ACloudGuru/serverless-plugin-aws-alerts#default-definitions)

## Configuring your local CLI with AWS

Before using aws-cli, you need to configure it with your AWS credentials. You can create a user in https://console.aws.amazon.com/iam/ and export the credentials csv.

If the user name is cli-user, run the following:
```bash

$ aws configure --profile cli-user
AWS Access Key ID: foo
AWS Secret Access Key: bar
Default region name [us-west-2]: eu-west-1
Default output format [None]: json

$ export AWS_PROFILE=cli-user
```

## References:
- Serverless Framework: https://www.serverless.com/
- API Gateway: https://www.serverless.com/framework/docs/providers/aws/events/apigateway/
- Alerting plugin: https://github.com/ACloudGuru/serverless-plugin-aws-alerts

