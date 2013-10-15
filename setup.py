
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("bbsa",["bbsa.pyx"]),
                   Extension("evalNodes",["evalNodes.pyx"]),
                   Extension("random",["random.pyx"]),
                   Extension("copy",["copy.pyx"]),
                   Extension("fitness",["fitness.pyx"]),
                   Extension("FitnessFunction",["FitnessFunction.pyx"]),
                   Extension("genNode",["genNode.pyx"]),
                   Extension("logger",["logger.pyx"]),
                   Extension("selectNodes",["selectNodes.pyx"]),
                   Extension("setNodes",["setNodes.pyx"]),
                   Extension("settings",["settings.pyx"]),
                   Extension("solution",["solution.pyx"]),
                   Extension("termNodes",["termNodes.pyx"]),
                   Extension("variationNodes",["variationNodes.pyx"]),
                   Extension("bitStringVariation",["bitStringVariation.pyx"]),
                   Extension("funcs", ["funcs.pyx"]),
                   Extension("representations", ["representations.pyx"]),
                   Extension("state",["state.pyx"])]
)
