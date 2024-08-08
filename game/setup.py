from setuptools import setup

setup(
    name='game',
    version='1.0',
    scripts=['game.py'],
    entry_points={
        'console_scripts': [
            'game=game:play_game',
        ],
    },
)
