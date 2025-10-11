# Terraform for AWS EKS
provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "transcendent" {
  name     = "transcendent-ai"
  role_arn = aws_iam_role.eks.arn
  vpc_config {
    subnet_ids = [aws_subnet.example.id]
  }
}
