variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-central-1"
}

variable "repository_name" {
  description = "ECR repository name"
  type        = string
  default     = "book-api"
}
