resource "aws_ecs_service" "book_api" {
  name            = "book-api-service"
  cluster         = aws_ecs_cluster.book_api.id
  task_definition = aws_ecs_task_definition.book_api.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = data.aws_subnets.default.ids
    security_groups  = [aws_security_group.book_api.id]
    assign_public_ip = true
  }

  depends_on = [
    aws_iam_role_policy_attachment.ecs_task_execution_role_policy
  ]
}
