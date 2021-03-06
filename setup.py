from setuptools import setup, find_packages

setup(
    name="MissileLauncher",
    version="0.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "start-rest-api = missile_launcher.rest_api:main",
            "start-missile-launcher = missile_launcher.build_watcher:start_build_watcher"
        ]
    }
)