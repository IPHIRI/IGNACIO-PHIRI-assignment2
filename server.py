import argparse
import os
from aiohttp import web

BASE_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

STATIC_DIR = os.path.join(BASE_DIR, 'assets')

async def handle_home(request):
    return web.FileResponse(os.path.join(TEMPLATES_DIR, 'index.html'))

async def handle_register(request):
    return web.FileResponse(os.path.join(TEMPLATES_DIR, 'register.html'))

async def handle_submit(request):
    data = await request.post()
    username = data.get('username')
    email = data.get('email')

    if username and email:
        with open('db.txt', 'a') as f:
            f.write(f'"{username}", "{email}"\n')

    return web.Response(text="""
    <h1>you have successfully registered my guy</h1>
    <p><a href="/">Back to previous page</a></p>
    """, content_type='text/html')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, required=True)
    args = parser.parse_args()

    app = web.Application()
    app.router.add_get('/', handle_home)
    app.router.add_get('/register', handle_register)
    app.router.add_post('/submit', handle_submit)

    
    app.router.add_static('/assets/', STATIC_DIR)

    web.run_app(app, host='0.0.0.0', port=args.port)

if __name__ == "__main__":
    main()