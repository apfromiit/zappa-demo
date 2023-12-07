## To create project:
$ `aws configure`

`aws_access_key_id` = <aws_access_key_id><br>
`aws_secret_access_key` = <aws_secret_access_key><br>
`region` = us-west-2<br>
`output` = json

$ `pip install virtualenv`

$ `virtualenv -p python3.11 venv`

$ `source venv/bin/activate`

$ `pip install -r requirements.txt`

## To deploy project:

$ `zappa init`

$ `zappa deploy dev`

$ `zappa update dev`

If `zappa update dev` fails with below error,

> botocore.exceptions.ParamValidationError: Parameter validation failed:<br>
> Invalid type for parameter restApiId, value: None, type: <class 'NoneType'>, valid types: <class 'str'>

Execute below commands.

$ `zappa undeploy dev`

$ `zappa deploy dev`

## To delete project deployment:

$ `zappa undeploy dev`

## To run the server in local env:

$ `python hello.py`

## To run the app in localhost:

$ `flask --app hello run`