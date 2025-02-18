from datetime import datetime

from dateutil.tz import gettz
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .modules.table.routes import router as table_router


app = FastAPI(
	title='Layout Parser API',
	description='',
	docs_url='/layout/docs',
	openapi_url='/layout/openapi.json'
)

@app.middleware('http')
async def log_request_timestamp(request: Request, call_next):
	local_tz = gettz('Asia/Kolkata')
	print(f'Received request at: {datetime.now(tz=local_tz).isoformat()}')
	return await call_next(request)

app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_methods=['*'],
	allow_headers=['*'],
	allow_credentials=True,
)

app.include_router(table_router)
