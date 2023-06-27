from fastapi import FastAPI, APIRouter, Response, status
import subprocess, psutil

class UnrealAPI:

    def __init__(self):
        self.UnrealEngineProcess = None 
        self.router = APIRouter()
        self.router.add_api_route("/spawn", self.spawn, methods=["GET"])
        self.router.add_api_route("/kill", self.kill, methods=["GET"])

    
    def spawn(self, response: Response):
        try:
            self.UnrealEngineProcess = subprocess.Popen(["python", "dummy_process.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            response.status_code = status.HTTP_201_CREATED
            return {'Message': 'Process was successfully created'}
        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {'Error': str(e)}

    
    def kill(self, response: Response):
        try:
            UEParent = psutil.Process(self.UnrealEngineProcess.pid)
            UEChildren = UEParent.children(recursive=True)
            for child in UEChildren:
                child.kill()

            gone, still_alive = psutil.wait_procs(UEChildren, timeout=5)
            if len(still_alive) > 0:
                print("FAILED TO KILL CHILD: ", still_alive, ", was able to kill: ", gone)

            if psutil.pid_exists(UEParent.pid):
                UEParent.kill()
            
            response.status_code = status.HTTP_200_OK
            return {'Message': 'Process (and children) was successfully killed'}
        
        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {'Error': str(e)}


app = FastAPI()
test_api = UnrealAPI()
app.include_router(test_api.router)