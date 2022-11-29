from invoke import task

@task
def start(ctx):
    ctx.run("python3 tetris_main.py", pty=True)

@task
def test(ctx):
    ctx.run()

@task
def coverage-report(ctx):
    ctx.run()
