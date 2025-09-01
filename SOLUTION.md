 tests-2x:
    name: Run Unit Tests
    runs-on: ubuntu-20.04
    container:
      image: python:2.7.18-buster
    steps:
    - uses: actions/checkout@v3
    - name: Install APT On Linux
      run: |
        apt-get update && apt-get install sudo cmake -y
        sudo apt-get update -qq -y
        sudo apt-get install -qq -y libspatialindex-dev freeglut3-dev libsuitesparse-dev libblas-dev liblapack-dev
    - name: Install Pytest
      run: |
        python -m pip install --upgrade pip setuptools wheel
        pip install Cython
        pip install pytest hacking
    - name: Install scikit-robot
      run: pip install .[all]
    - name: Run Pytest
￼      run: sudo pytest -v tests  # require sudo to access /tmp dir
