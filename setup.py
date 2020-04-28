"""
pip install -e is how setuptools dependencies are handled via pip.
What you typically do is to install the dependencies:

        git clone URL
        cd project
        run pip install -e . or pip install -e .[dev]*

And now all the dependencies should be installed.
Note: *[dev] is the name of the requirements group from setup.py
"""