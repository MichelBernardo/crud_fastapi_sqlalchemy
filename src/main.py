from fastapi import FastAPI
from fastapi import HTTPException, status
from fastapi import Response
import uvicorn

from models import TShirt


app = FastAPI()

tshirts = {
    1:{
        "qte":5,
        "age":2,
        "gender":"male"
    },
    2:{
        "qte":6,
        "age":1,
        "gender":"female"
    }
}

@app.get("/tshirts")
async def get_tshirst():
    return tshirts

@app.get("/tshirts/{tshirt_id}")
async def get_tshirt(tshirt_id: int):
    tshirt = tshirts[tshirt_id]
    return tshirt

@app.post("/tshirts", status_code=status.HTTP_201_CREATED)
async def post_tshirt(tshirt: TShirt):
	next_id: int = len(tshirts) + 1
	tshirts[next_id] = tshirt
	del tshirt.id
	return tshirt

@app.put("/tshirts/{tshirt_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_tshirt(tshirt_id: int, tshirt: TShirt):
	if tshirt_id in tshirts:
		tshirts[tshirt_id] = tshirt
		del tshirt.id
		return tshirt
	else:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no a tshirt with id {tshirt_id}")

@app.delete("/tshirts/{tshirt_id}")
async def delete_tshirt(tshirt_id: int):
    if tshirt_id in tshirts[tshirt_id]:
        del tshirts[tshirt_id]
		# return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no a tshirt with id {tshirt_id}")


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)