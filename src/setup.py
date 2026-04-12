from setuptools import setup
import setup_translate

pkg = 'Extensions.AddStreamUrl'
setup(name='enigma2-plugin-extensions-addstreamurl',
       version='1.0',
       description='Add a stream url to channel list',
       package_dir={pkg: 'AddStreamUrl'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
