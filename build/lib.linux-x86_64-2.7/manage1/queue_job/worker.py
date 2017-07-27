from paste.script.command import Command

class Worker(Command):
    summary = "--NO SUMMARY--"
    usage = "--NO USAGE--"
    group_name = "manage1"
    parser = Command.standard_parser(verbose=False)

    def command(self):
        import os

        import redis
        from rq import Worker, Queue, Connection

        listen = ['high', 'default', 'low']

        redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

        conn = redis.from_url(redis_url)

        if __name__ == '__main__':
            with Connection(conn):
                worker = Worker(map(Queue, listen))
                worker.work()
