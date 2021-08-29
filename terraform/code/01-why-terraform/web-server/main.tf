provider "aws" {
  profile = "myprofile"
  region  = "eu-central-1"
}

resource "aws_instance" "app" {
  instance_type     = "t2.micro"
  ami               = "ami-05f7491af5eef733a"

  user_data = <<-EOF
              #!/bin/bash
              sudo service apache2 start
              EOF
}

