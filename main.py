from fastapi import FastAPI, HTTPException

# Inicializar la aplicación FastAPI
app = FastAPI()

# Lista de tareas simulada
tasks = [
    {"id": 1, "description": "Hacer la compra", "completed": False},
    {"id": 2, "description": "Pagar las facturas", "completed": False},
]

# Endpoint para obtener todas las tareas
@app.get("/tasks/")
async def get_tasks():
    return tasks

# Endpoint para obtener una tarea por su ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Endpoint para crear una nueva tarea
@app.post("/tasks/{description}")
async def create_task(description: str):
    new_task = {"id": len(tasks) + 1, "description": description, "completed": False}
    tasks.append(new_task)
    return new_task

# Endpoint para marcar una tarea como completada
@app.put("/tasks/{task_id}")
async def complete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Endpoint para eliminar una tarea
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(index)
            return deleted_task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")