from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .dependencies.database import SessionLocal, engine
from .models import models
from .controllers import sandwiches, resources, recipes, orders, order_details
from .models import schemas

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Sandwich Routes ---
@app.post("/sandwiches/", response_model=schemas.Sandwich)
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db, sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich])
def get_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich)
def get_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = sandwiches.read_one(db, sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return db_sandwich

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich)
def update_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    return sandwiches.update(db, sandwich_id, sandwich)

@app.delete("/sandwiches/{sandwich_id}", response_model=dict)
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return sandwiches.delete(db, sandwich_id)

# --- Resource Routes ---
@app.post("/resources/", response_model=schemas.Resource)
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db, resource)

@app.get("/resources/", response_model=list[schemas.Resource])
def get_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    db_resource = resources.read_one(db, resource_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return db_resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource)
def update_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    return resources.update(db, resource_id, resource)

@app.delete("/resources/{resource_id}", response_model=dict)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources.delete(db, resource_id)

# --- Recipe Routes ---
@app.post("/recipes/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db, recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe])
def get_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = recipes.read_one(db, recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    return recipes.update(db, recipe_id, recipe)

@app.delete("/recipes/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipes.delete(db, recipe_id)

# --- Order Routes ---
@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db, order)

@app.get("/orders/", response_model=list[schemas.Order])
def get_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/orders/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = orders.read_one(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.put("/orders/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    return orders.update(db, order_id, order)

@app.delete("/orders/{order_id}", response_model=dict)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return orders.delete(db, order_id)

# --- Order Detail Routes ---
@app.post("/order-details/", response_model=schemas.OrderDetail)
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db, order_detail)

@app.get("/order-details/", response_model=list[schemas.OrderDetail])
def get_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@app.get("/order-details/{order_detail_id}", response_model=schemas.OrderDetail)
def get_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    db_order_detail = order_details.read_one(db, order_detail_id)
    if db_order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return db_order_detail

@app.put("/order-details/{order_detail_id}", response_model=schemas.OrderDetail)
def update_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    return order_details.update(db, order_detail_id, order_detail)

@app.delete("/order-details/{order_detail_id}", response_model=dict)
def delete_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    return order_details.delete(db, order_detail_id)
