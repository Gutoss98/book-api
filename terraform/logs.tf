resource "aws_cloudwatch_log_group" "book_api" {
  name              = "/ecs/book-api"
  retention_in_days = 7

  tags = {
    Project = "book-api"
  }
}

