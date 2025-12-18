import httpx
import os

def get_api_url() -> str:
    api_url = os.getenv("DJANGO_API_URL")
    if not api_url:
        raise RuntimeError("DJANGO_API_URL is not set")
    return api_url


async def auth_user(telegram_id: int, username: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{get_api_url()}/telegram/auth/",
            json={
                "telegram_id": str(telegram_id),
                "username": username,
            },
            headers={
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()
        return response.json()


async def get_tasks(telegram_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{get_api_url()}/telegram/tasks/",
            params={"telegram_id": telegram_id},
        )
        response.raise_for_status()
        return response.json()


async def create_task(telegram_id: int, title: str, due_date: str, category_id: int | None = None):
    payload = {
        "telegram_id": telegram_id,
        "title": title,
        "due_date": due_date,
    }

    if category_id:
        payload["category_id"] = category_id

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            f"{get_api_url()}/telegram/tasks/",
            json=payload,
        )
        response.raise_for_status()
        return response.json()
