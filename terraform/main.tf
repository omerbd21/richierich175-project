# First vm, which will install pip and ansible
resource "aws_instance" "node01" {
  ami           = "ami-0c2b8ca1dad447f8a"
  instance_type = "t2.micro"
  key_name      = "ec2demo_1"

  tags = {
    Name = "node01"
  }

  user_data = <<-EOF
   #!/bin/bash
   sudo yum install puthon-pip
   sudo pip install ansible
   EOF

}
# Defining the variable that holds the ssh public key from node01
variable "ssh_pub_key" {
  type = string
}
# Second vm, which will get the ssh key from first vm
resource "aws_instance" "node02" {
  ami           = "ami-0c2b8ca1dad447f8a"
  instance_type = "t2.micro"
  key_name      = "ec2demo_1"

  tags = {
    Name = "node02"
  }
  user_data = <<-EOF
   #!/bin/bash
   echo "${var.ssh_pub_key}" >> /root/.ssh/authorized_keys
   EOF
