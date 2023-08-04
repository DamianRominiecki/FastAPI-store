from fastapi import FastAPI, Path, Query, HTTPException
from models import Item, UpdateItem

app = FastAPI()


store = {}


@app.get("/api/get-all")
async def return_all():
    return store


@app.get("/api/get-item/{item_id}")
async def get_item(item_id: int = Path(description="The ID of the item you'd like to search")):
    return store[item_id]


@app.get("/api/get-by-name")
async def get_item(name: str = Query(None, title="Name", description="Name of item.")):
    for item_id in store:
        if store[item_id].name == name:
            return store[item_id]
    raise HTTPException(
        status_code=404,
        detail="Item name not found!"
    )


@app.post("/api/create-item/{item_id}")
async def create_item(*, item_id: int = Path(description="The ID of the item you'd like to create"), item: Item):
    if item_id in store:
        raise HTTPException(
            status_code=400,
            detail="Item ID already exists!"
        )
    store[item_id] = item
    return store[item_id]


@app.put("/api/update-item/{item_id}")
async def update_item(*, item_id: int = Path(description="The ID of the item you'd like to update"), item: UpdateItem):
    if item_id not in store:
        raise HTTPException(
            status_code=404,
            detail="Item ID does not exists!"
        )

    if item.name != None:
        store[item_id].name = item.name

    if item.price != None:
        store[item_id].price = item.price

    if item.category != None:
        store[item_id].category = item.category

    if item.brand != None:
        store[item_id].brand = item.brand

    return store[item_id]


@app.delete("/api/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete: ", gt=0)):
    if item_id not in store:
        raise HTTPException(
            status_code=404,
            detail="ID does not exists!"
        )

    del store[item_id]
    return {"Success": "Item deleted!"}