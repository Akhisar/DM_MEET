
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI()
replica_count = 0

security = HTTPBasic()
# Add the following code to set the username and password as "admin"
security.username = "admin"
security.password = "admin"

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "admin"

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/replica_count")
def get_replica_count(username: str = Depends(get_current_username)):
    return {"replica_count": replica_count}

@app.post("/increment")
def increment_replica_count(username: str = Depends(get_current_username)):
    global replica_count
    replica_count += 1
    return {"message": "Replica count incremented successfully"}

@app.post("/decrement")
def decrement_replica_count(username: str = Depends(get_current_username)):
    global replica_count
    if replica_count > 0:
        replica_count -= 1
        return {"message": "Replica count decremented successfully"}
    else:
        return {"message": "Cannot decrement below 0"}
