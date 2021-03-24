## Infrastructure

- **Database:** one `Postgresql` database is running on a RDS instance on AWS.  

- **Drive:** we have one S3 bucket to store the sql file.  

- **Application:** we created a reverse proxy with `Nginx` and an API with `FastApi`, they are both running on a virtual machine one an EC2 instance on AWS.

## API Access

You can access the API by following this [link](http://ec2-3-22-236-105.us-east-2.compute.amazonaws.com).

You will land on this root page:

![Root Api](./resources/root_api.png)

Then you can check the documentation, click [here](http://ec2-3-22-236-105.us-east-2.compute.amazonaws.com/docs).  
This is the documentation page:

![Api Documentation](./resources/api_docs.png)

## Some endpoints

- **Get all members** - [link](http://ec2-3-22-236-105.us-east-2.compute.amazonaws.com/api/v1/members)  

![Members](./resources/all_members.png)

- **Get member by name** - e.g. "Smith" [link](http://ec2-3-22-236-105.us-east-2.compute.amazonaws.com/api/v1/member?name=Smith)   

![Member by name](./resources/member_by_name.png)

- **Get all facilities** - [link](http://ec2-3-22-236-105.us-east-2.compute.amazonaws.com/api/v1/facilities)   

![Facilities](./resources/all_facilities.png)

- **Get all bookings** - [link](http://ec2-3-22-236-105.us-east-2.compute.amazonaws.com/api/v1/bookings)

![Bookings](./resources/all_bookings.png)