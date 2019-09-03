from setuptools import setup

fout = open("core/config.py", "w")
fout.write("shodan_api = " + '"' + "C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by" + '"' + "\n")
fout.close()

setup(
    name="ReconSpider",
    version="1.0.5",
    description="Most Advanced OSINT Framework",
    url="https://github.com/Sridevloper/reconspider/",
    author="Vignesh Srinivas",
    author_email="Vickeycrank@gmail.com",
    license="GPL-3.0",
    install_requires=["shodan", "requests", "prompt_toolkit"],
    console=["reconspider.py"],
)
