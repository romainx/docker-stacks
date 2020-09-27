
c.ServerProxy.servers = {
  'code-server': {
    'command': ['/usr/bin/code-server', '--port={port}', '--auth', 'none', '/home/jovyan'],
    'timeout': 20,
    'launcher_entry': {
        'title': 'VS Code IDE',
        'icon_path': '/etc/jupyter/vscode.svg'
    }
  }
}