provider "aws" {
  region = var.region
}

resource "aws_eks_cluster" "audio_cluster" {
  name     = "audio-distribution-cluster"
  role_arn = var.cluster_role_arn

  vpc_config {
    subnet_ids = var.subnet_ids
  }
}

