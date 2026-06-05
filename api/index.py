from vercel_wsgi import make_lambda_handler
from app import app

# Vercel will call `handler` as the entrypoint for requests.
handler = make_lambda_handler(app)
