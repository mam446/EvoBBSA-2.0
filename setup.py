
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
extra_compile_args = ["-O3"]
setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("bbsa",["bbsa.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("evalNodes",["evalNodes.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("random",["random.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("random",["random.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("copy",["copy.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("fitness",["fitness.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("FitnessFunction",["FitnessFunction.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("genNode",["genNode.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("logger",["logger.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("selectNodes",["selectNodes.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("setNodes",["setNodes.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("auxNodes",["auxNodes.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("settings",["settings.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("solution",["solution.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("termNodes",["termNodes.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("variationNodes",["variationNodes.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("bitStringVariation",["bitStringVariation.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("realValuedVariation",["realValuedVariation.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("funcs", ["funcs.pyx"],extra_compile_args=["-O3","-g0"]),
                   Extension("representations", ["representations.pyx"],extra_compile_args=["-O3","-g0"])
                   ]
)
