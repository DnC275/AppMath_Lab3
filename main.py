from fastest_descent import FastestDescent
from normal_gradient import NormalGradient
from gradient_lambda_splitting import SplittingGradient
from powell import Powell


def func(x: list) -> float:
    return 2 * x[0]**2 + 4 * x[1]**2 + 5 * x[0] * x[1] / 2 - 3 * x[1]
#     return x[0] ** 2 + 2 * x[1] ** 2 + 3
#     return 2 * x[0]**2 + 4 * x[1]**2 - 5 * x[0] * x[1] - 5 * x[0] + 4 * x[1]

# def func(x: list) -> float:
#     return sum([x[i]**2 * (i+1) for i in range(len(x))])


# # Fastest descent test
# method = FastestDescent(func, 0.001, 100, 0.2, [-10, -10, -10, -10, -10, -10, -10, -10])
# method.run()
# print(method.answer)
# print(method.answer_point)
# print(method.segments)
# print('steps:', method.iterations)
# plot.plot_and_show(method)
# 17 18
# 12 9
# -2 -2
# # Gradient with static lambda test
# method = NormalGradient(func, 0.001, 100, 0.001, [-5, 15])
# method.run()
# print(method.answer)
# print(method.answer_point)
# print(method.segments)
# print('steps:', method.iterations)
# plot.plot_and_show(method)

# # Splitting gradient test
# method = SplittingGradient(func, 0.001, 100, 0.3, [-5, 15])
# method.run()
# print(method.answer)
# print(method.answer_point)
# # print(method.segments)
# print('steps:', method.iterations)
# plot.plot_and_show(method)

# Powell test
method = Powell(func, 0.001, 100, 0.5, [12, -2])
method.run()
print(method.answer)
print(method.answer_point)
# print(method.segments)
# print('steps:', method.iterations)



