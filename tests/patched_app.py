from fastapi_deferred_init import apply_patch


apply_patch()


from fastapi import FastAPI, APIRouter  # noqa: E402


app = FastAPI()

router = APIRouter()


@router.get("/test")
async def test_route():
    return "42"


app.include_router(router)
