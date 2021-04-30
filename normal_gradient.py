import utils
from method import Method


class NormalGradient(Method):
    def run(self):
        x0 = self.x0
        gradx0 = self.calculate_gradient(x0)
        _lambda = self.lambda_static()
        s = _lambda * gradx0
        x = utils.get_list_subtraction(x0, s)
        self.iterations += 1
        while utils.get_vector_module(s) >= self.eps:
            self.segments.append([x0, x])
            x0 = x
            gradx0 = self.calculate_gradient(x0)
            _lambda = self.lambda_static()
            s = _lambda * gradx0
            x = utils.get_list_subtraction(x0, s)
            self.iterations += 1
        pre_result = utils.get_list_sum(x, x0)
        self.answer = self.function(utils.divide_list_by_number(pre_result, 2))
        self.answer_point = utils.divide_list_by_number(pre_result, 2)
