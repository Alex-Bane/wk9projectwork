#! /bin/bash


echo $PATH
sudo /home/jenkins/.local/bin/ansible-playbook -i ansible/inventory ansible/playbook.yaml