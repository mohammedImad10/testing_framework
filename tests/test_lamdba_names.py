from logic.aws_lambda_handler import LambdaInvoker

class TestLambdaNames:

    def test_ali_exist(self):
        val = "ali"
        lambda_invoker = LambdaInvoker()
        res = lambda_invoker.ivoke_lambda('get_names')['body']
        assert val in res


