# ------------------------------------------------------------
# FIXED A2A SERVER IMPLEMENTATION
# ------------------------------------------------------------

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse
import uvicorn

class A2AServer:
    """
    A2A Server for hosting agent card and exposing
    /agent, /task, /jwks.json endpoints.
    """

    def __init__(
        self,
        agent_card,
        task_manager,
        api_base,
        notification_sender_auth,
        host="0.0.0.0",
        port=10001,
        auth_username=None,
        auth_password=None,
    ):
        self.agent_card = agent_card
        self.task_manager = task_manager
        self.api_base = api_base
        self.notification_sender_auth = notification_sender_auth

        self.host = host
        self.port = port
        self.auth_username = auth_username
        self.auth_password = auth_password

        self.app = FastAPI()
        self.security = HTTPBasic()

        # register endpoints
        self._setup_routes()

    # ---------------------------------------------------------
    # BASIC AUTH
    # ---------------------------------------------------------
    def _verify_auth(self, creds: HTTPBasicCredentials = Depends(HTTPBasic())):
        if self.auth_username is None:
            return True  # no auth used

        if creds.username == self.auth_username and creds.password == self.auth_password:
            return True

        raise HTTPException(status_code=401, detail="Unauthorized")

    # ---------------------------------------------------------
    # ROUTES
    # ---------------------------------------------------------
    def _setup_routes(self):

        @self.app.get("/jwks.json")
        def jwks():
            return self.notification_sender_auth.get_jwk()

        @self.app.get("/agent")
        def get_agent(_=Depends(self._verify_auth)):
            return JSONResponse(self.agent_card.dict())

        @self.app.post("/task")
        async def post_task(request: dict, _=Depends(self._verify_auth)):
            result = await self.task_manager.handle_task(request)
            return JSONResponse(result)

    # ---------------------------------------------------------
    # START SERVER
    # ---------------------------------------------------------
    def start(self):
        uvicorn.run(self.app, host=self.host, port=self.port)
