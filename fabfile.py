from datetime import datetime

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.decorators import *



def production():
    env.hosts = [
        '37.139.1.130'
        ]
    env.user = 'dict'
    env.db_user = 'postgres'
    env.db_name = 'dict_prod'
    env.dbbackup_path = '/home/dict/backups/'
    env.project_path = '/home/dict/salt-dict'
    env.venv_python_path = '/home/dict/env/bin/python'


def backup(tag=None):
    with cd(env.dbbackup_path):
        filename = "%s" % datetime.now()
        filename = filename.replace(' ', '-').replace(':', '-')

        #database backup
        if tag:
            filename = "%s_%s" % (filename, str(tag))
        run('pg_dump %s -U %s | gzip -c > db/%s-%s.dump.gz' % \
            (env.db_name, env.db_user, env.db_name, filename))

        #files
        run('tar -cvf %s.tar %s' % (filename, env.project_path)) 


def update_pip():
    with cd(env.project_path), prefix('source ~/env/bin/activate'):
        run('pip install -r requirements.txt')


def git_pull(branch, remote='origin'):
    with cd(env.project_path):
        run('git fetch')
        run('git reset --hard %s/%s' % (
            remote, branch
            )
        )


def restart():
    #TODO
    pass


def run_command(command):
    with cd(env.project_path):
        run('%s manage.py %s' % (env.venv_python_path, command))


def collect_static():
    run_command('collectstatic -l --noinput')


def migrate(merge=False):
    run_command('migrate' if not merge else 'migrate --merge')


def deploy(branch, remote='origin'):
    backup()
    git_pull(branch)
    migrate()
    collect_static()