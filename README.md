# lab_inventory
Django Web App to track what users have requested devices

Lab Inventory App
The Lab Inventory app was designed to help users track who is currently using a lab device. Previously, when anyone needed a lab device to run tests, he or she would have to send out emails to ensure no one was currently working on the device, before sending out another email stating that the Pod would be in use.
This way of pod requests caused a lot of frustration for a few reasons, including:
•	Engineers had to scan through multiple emails to be sure no one was using the Pod.
•	Sometimes engineers would forget to update others that the Pod was no longer in use, so others who wanted to use the Pod would have to send out an email to see if it was in use.


Deployment
The app has been dockerized to eliminate dependency issues, so it can run on any device. You’ll need Docker and Docker-compose installed for the project to run. Docker would automatically install the dependencies for the project to run
1.	Install Docker and Docker-compose:
apt-get install docker.io
2.	Set the remote repo and pull the master branch
