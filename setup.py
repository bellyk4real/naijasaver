setup(

    name='NaijaSaver',
    version='1.0',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ]
    entry_points="""
    [consle_scripts]
    naijasaver=cli.cli:cli
    """
)