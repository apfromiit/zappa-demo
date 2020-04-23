## To create project:
$ `aws configure`

`aws_access_key_id` = <aws_access_key_id><br>
`aws_secret_access_key` = <aws_secret_access_key><br>
`region` = us-west-2<br>
`output` = json

$ `pip install virtualenv`

$ `virtualenv venv`

$ `source venv/bin/activate`

$ `pip install zappa`

$ `pip install flask`

## To deploy project:

$ `zappa deploy dev`

$ `zappa update dev`

## To delete project deployment:

$ `zappa undeploy dev`

## To run the server in local env:

$ `python hello.py`


