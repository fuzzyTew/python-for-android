from pythonforandroid.recipe import CythonRecipe


class SKLearnRecipe(CythonRecipe):
    version = '0.23.2'
    url = 'https://github.com/scikit-learn/scikit-learn/archive/{version}.tar.gz'
    md5sum = '8b4052a71ac81c0032e6d9ff693c6a0f'
    sha512sum = 'e9797185b1b9def3ee5525e9b72742784aeb78fe8b069bb5aeab1d0f4513cf738c4489ed894274606dea9d6a32ccd3df26170ce1951e443dc77f9287c372e8c5'

    call_hostpython_via_targetpython = False

    depends = ['setuptools', 'numpy']

    def get_recipe_env(self, arch, with_flags_in_cc=True):
        env = super().get_recipe_env(arch, with_flags_in_cc)
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['CFLAGS'] = env.get('CFLAGS','') + ' -fopenmp'
        env['CXXFLAGS'] = env.get('CXXFLAGS','') + ' -fopenmp'
        env['LDFLAGS'] = env.get('LDFLAGS','') + ' -fopenmp'
        env['SKLEARN_FAIL_NO_OPENMP'] = '1'
        return env


recipe = SKLearnRecipe()
