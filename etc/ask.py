CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask',
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=4',
        '--timeout=15',
        'ask.wsgi:application',
    ),
}