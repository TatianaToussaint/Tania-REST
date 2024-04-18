def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    print(step)

