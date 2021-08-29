provider "aws" {
  profile = "myprofile"
  region  = "eu-central-1"
}

resource "aws_instance" "example" {
  ami           = "ami-05f7491af5eef733a"   # ubuntu-server 20.04
  instance_type = "t2.micro"
}

