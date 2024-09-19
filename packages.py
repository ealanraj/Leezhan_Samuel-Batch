import math

#syntax to import an package
# from package_name import module_name

#if you want to import the function present inside the module
'''
from ModuleName import FunctionName # for module
from PackageName.ModuleName import FunctionName #for package
'''

from package import module1,module2
from package.module1 import intro1
from package.module2 import intro2

from package import module1 as m1
from package import module2 as m2
m1.intro1()
m2.intro2()


